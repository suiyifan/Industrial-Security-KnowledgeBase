import argparse
from pathlib import Path

def read(path,label):
    if not path.is_file(): raise SystemExit(f"ERROR: 缺少{label}：{path}")
    return path.read_text(encoding="utf-8")

def block(title,text):
    return f"## {title}\n\n```markdown\n{text.rstrip()}\n```"

def main():
    p=argparse.ArgumentParser()
    p.add_argument("markdown_file",type=Path)
    target=p.parse_args().markdown_file
    seed_path=Path("codex/工控安全研究员知识点汇总_seed.md")
    if seed_path.is_file():
        note="已载入 seed 文件。"; seed=block("知识点 seed",read(seed_path,"seed"))
    else:
        note=f"提示：{seed_path.as_posix()} 不存在，已跳过。"; seed="## 知识点 seed\n\n未提供。"
    task="将目标章节扩写为不少于6000字的中文教材级内容。必须遵循仓库规范和章节模板，包含理论说明、工程场景、实际案例、工控安全影响、实验设计、面试60分回答、面试90分回答和追问；写清数据流、控制流、状态流及其对真实物理过程的影响。实验仅限隔离授权环境。保留正确原文，最终只输出完整 Markdown 正文，不修改其他文件。"
    prompt="\n\n".join(["# 教材级扩写提示词",f"目标文件：{target.as_posix()}",task,block("AGENTS.md",read(Path("AGENTS.md"),"AGENTS.md")),seed,block("章节模板",read(Path("codex/chapter_template.md"),"章节模板")),block("目标 Markdown 当前内容",read(target,"目标文件"))])+"\n"
    out=Path("memory/outlines")/f"{target.stem}_expand_prompt.md"
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(prompt,encoding="utf-8")
    print(note); print(f"扩写提示词已保存：{out.as_posix()}")

if __name__=="__main__": main()
