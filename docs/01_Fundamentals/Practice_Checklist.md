# 01 章实践任务清单

这一章的练习要服务于两个目标：

1. 让你真的掌握基础知识。
2. 让你产生可放进 GitHub 的学习证据。

## A. Git 实践

- [ ] 初始化一个 Git 仓库。
- [ ] 新建一篇学习笔记。
- [ ] 使用 `git status` 查看状态。
- [ ] 使用 `git add .` 暂存文件。
- [ ] 使用 `git commit -m "Add first note"` 提交。
- [ ] 使用 `git log --oneline` 查看历史。

交付物：

- 至少 3 次有意义的 commit。
- 提交信息能看出你学了什么。

## B. Linux 实践

- [ ] 使用 `pwd` 查看当前路径。
- [ ] 使用 `ls -la` 查看隐藏文件。
- [ ] 使用 `mkdir` 创建目录。
- [ ] 使用 `touch` 创建文件。
- [ ] 使用 `chmod +x` 修改脚本权限。
- [ ] 使用 `whoami` 查看当前用户。
- [ ] 使用 `ip addr` 查看 IP。
- [ ] 使用 `ss -tulnp` 查看监听端口。
- [ ] 使用 `tail -f` 查看日志。

交付物：

- 一篇 `Linux_Command_Notes.md`。
- 记录每个命令的用途和示例输出。

## C. Python 实践

- [ ] 写一个端口号识别脚本。
- [ ] 写一个读取 `targets.txt` 的脚本。
- [ ] 写一个 TCP 端口连接测试脚本。
- [ ] 给脚本加 `argparse` 命令行参数。
- [ ] 给网络连接加异常处理。

交付物：

- `scripts/simple_port_scanner.py`
- 一篇脚本说明文档。

## D. 网络基础实践

- [ ] 解释 IP 地址和端口。
- [ ] 解释 TCP 和 UDP 区别。
- [ ] 画出 TCP 三次握手。
- [ ] 解释 DNS 查询过程。
- [ ] 列出常见工业协议端口。

交付物：

- 一张工业协议端口表。
- 一篇“访问网页时发生了什么”的笔记。

## E. Wireshark 实践

- [ ] 抓 ICMP ping 包。
- [ ] 抓 DNS 查询包。
- [ ] 抓 HTTP 请求包。
- [ ] 找到 TCP 三次握手。
- [ ] 使用 `ip.addr == x.x.x.x` 过滤。
- [ ] 使用 `tcp.port == 502` 过滤。

交付物：

- 一篇抓包实验报告。
- 至少 3 张关键截图。
- 记录每次使用的过滤器。

## F. 本章综合项目

项目名称：

```text
Mini Network Analyzer
```

目标：

写一个 Python 小工具，读取目标 IP 和端口，测试端口是否开放，并把结果保存成文本文件。

最低功能：

- 支持命令行传参。
- 支持超时时间。
- 能输出开放端口。
- 能保存结果。

进阶功能：

- 识别常见服务名。
- 支持从文件读取目标。
- 输出 CSV。
- 给 502、102、4840、2404 等工业端口打标签。

## G. 完成标准

本章完成时，你应该能回答：

- Git 的工作区、暂存区、提交分别是什么？
- Linux 中如何查看端口和进程？
- Python 中如何建立 TCP 连接？
- TCP 三次握手是什么？
- DNS 是做什么的？
- Wireshark 如何过滤某个 IP 或端口？
- 为什么 Modbus TCP 默认端口是安全分析线索？

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[Wireshark 抓包基础](Wireshark_Basics.md)
- 本章目录：[01_Fundamentals](README.md)
- 下一篇：[01 章术语表](Glossary.md)

