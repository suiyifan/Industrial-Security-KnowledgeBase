import argparse
from pathlib import Path

KEYWORDS = ("原理","工程","数据流","控制流","状态流","安全风险","工控场景","攻击链","防护","实验","面试","总结")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("markdown_file",type=Path)
    source=p.parse_args().markdown_file
    if not source.is_file(): p.error(f"文件不存在：{source}")
    text=source.read_text(encoding="utf-8")
    chars=len(text)
    headings=sum(1 for x in text.splitlines() if x.lstrip().startswith("#"))
    missing=[x for x in KEYWORDS if x not in text]
    status=(["TOO_SHORT"] if chars<5000 else [])+(["MISSING_SECTION"] if missing else [])
    status=status or ["PASS"]
    rows=[f"- {x}: {'FOUND' if x in text else 'MISSING'}" for x in KEYWORDS]
    report="\n".join(["# Markdown 质量检查报告","",f"- 文件：{source.as_posix()}",f"- 字符数：{chars}",f"- 标题数量：{headings}",f"- 检查结果：{', '.join(status)}",f"- 缺失关键词：{'、'.join(missing) if missing else '无'}","","## 关键词检查","",*rows,""])
    out=Path("memory/reports")/f"{source.stem}_quality_report.md"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(report,encoding="utf-8")
    print(report,end="")
    print(f"报告已保存：{out.as_posix()}")

if __name__=="__main__": main()
