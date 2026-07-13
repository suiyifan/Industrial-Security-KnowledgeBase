# 自动化教材扩写流水线

工具只读取目标正文，不覆盖 docs，也不调用外部 API。请在仓库根目录执行。

## 质量检查

```powershell
python scripts/check_doc_quality.py docs/06_Web_Security/SQL_Injection.md
```

输出字符数、标题数量、关键词结果，并保存到 memory/reports/<文件名>_quality_report.md。少于 5000 字符输出 TOO_SHORT，缺关键词输出 MISSING_SECTION。

## 生成扩写提示词

```powershell
python scripts/generate_prompt.py docs/06_Web_Security/SQL_Injection.md
```

读取 AGENTS.md、可选 seed、章节模板和目标正文，输出到 memory/outlines/<文件名>_expand_prompt.md；seed 不存在时提示并跳过。
