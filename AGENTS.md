# Codex Writing Guide

本仓库面向“工控安全研究员 / 工业互联网安全研究员 / 工控漏洞分析工程师”岗位。

## Default Writing Chain

后续新增或扩展知识点时，默认按以下链路展开：

```text
控制理论 -> 工程实现 -> 协议/数据流 -> 安全风险 -> 面试表达 -> 实操验证
```

如果某个主题不涉及控制理论，也要尽量按等价结构写：

```text
原理解释 -> 工程实现 -> 数据流/控制流/状态流 -> 安全风险 -> 面试表达 -> 实操建议
```

## Required Section Pattern

每个重要知识点尽量包含：

- 原理解释：为什么存在这个机制。
- 工程实现：真实 PLC / DCS / SCADA / 现场中怎么实现。
- 数据流：变量、内存、协议、信号如何流动。
- 安全视角：攻击点、后果、防护。
- 面试表达：60 分答案、90 分答案、常见追问。
- 实操建议：可用软件、仿真步骤、抓包点。

## Style Rules

- 不只写定义，要解释为什么这样设计。
- 不只写设备，要写数据流、控制流、状态流。
- 不只写漏洞，要说明漏洞如何影响真实物理过程。
- 不只写工具，要说明工具输出如何映射到控制行为。
- 每个小节尽量给出工业案例。
- 语言保持中文、工程化、教材化，避免空泛套话。
- 代码块和图示使用 Markdown 代码块，便于 GitHub 显示。

## Current Directory Mapping

本仓库已经采用英文目录名，不强制改成 seed 文件建议的中文目录。后续按现有目录归类：

- `docs/02_Automation`: 自动化、控制理论、PLC、DCS、SCADA、I/O、现场过程。
- `docs/03_Industrial_Network`: 工业网络、分区分域、DMZ、远程运维、抓包位置、监测。
- `docs/04_Industrial_Protocol`: 工业协议、Modbus、S7、OPC UA、Profinet、EtherNet/IP、EtherCAT。
- `docs/10_Tool_Development`: Python、Socket、Scapy、pymodbus、pcap 解析、报告自动化。
- `docs/07_Reverse_Engineering`: 逆向、固件、PLC 程序与协议逆向。
- `docs/09_Industrial_Security`: 威胁模型、闭环攻击、Stuxnet / TRITON、IEC 62443、纵深防御。
- `docs/13_Interview`: 面试问答、HR 回答、项目表达。
