# Seed 知识点归类与整合计划

来源文件：[工控安全研究员知识点汇总_seed.md](../../工控安全研究员知识点汇总_seed.md)

## 1. 写作规范归纳

seed 文件要求本知识库不是普通 PLC 教程，也不是普通网络安全教程，而是面向“工控安全研究员”的综合教材。

后续知识点默认采用以下链路：

```text
控制理论 -> 工程实现 -> 协议/数据流 -> 安全风险 -> 面试表达 -> 实操验证
```

每个重要主题至少回答六个问题：

1. 为什么存在这个机制？
2. 真实工业系统中如何实现？
3. 数据、控制、状态如何流动？
4. 攻击点在哪里？
5. 攻击如何影响物理过程？
6. 面试时如何讲成项目化能力？

## 2. 与现有目录的对应关系

| Seed 主题 | 现有归类目录 | 说明 |
|---|---|---|
| 控制、反馈、扰动、动态系统、稳定性、PID | `docs/02_Automation` | 属于自动化与工业控制基础 |
| 4~20mA、I/O、传感器、执行器 | `docs/02_Automation` | 连接物理过程与数字变量 |
| PLC 扫描周期、梯形图、内存模型、OB/FB/FC、Runtime | `docs/02_Automation` | PLC 深度工程实现 |
| DCS、控制站、工程师站、历史站、冗余、无扰切换 | `docs/02_Automation` | DCS 深度工程实现 |
| 工业网络、分层、DMZ、分区分域、冗余网络 | `docs/03_Industrial_Network` | 工业网络与边界 |
| RS232/RS485、Modbus、S7、OPC UA、Profinet、EtherCAT | `docs/04_Industrial_Protocol` | 工业协议专题 |
| Wireshark 抓包、Modbus TCP 抓包、异常通信分析 | `docs/03_Industrial_Network` 与 `docs/04_Industrial_Protocol` | 网络层与协议层共同覆盖 |
| Python socket、Scapy、pymodbus、pcap 解析 | `docs/10_Tool_Development` | 工具开发能力 |
| OpenPLC、CODESYS、Factory I/O、PLCSIM 实验 | `labs/` 与对应 docs 章节 | 未来实践模块 |
| 逆向、固件、PLC 程序与协议逆向 | `docs/07_Reverse_Engineering` | 逆向能力 |
| Stuxnet、TRITON、闭环攻击、MITRE ATT&CK for ICS | `docs/09_Industrial_Security` | 工控安全体系与案例 |
| 面试 100 问、HR 回答、项目经验表达 | `docs/13_Interview` | 面试表达 |

## 3. 本次已纳入的重点

本次先把 seed 中最核心的知识点分流到现有章节：

- `docs/02_Automation/Control_Theory_Deep_Dive.md`
- `docs/02_Automation/Analog_Signal_and_IO_Deep_Dive.md`
- `docs/02_Automation/PLC_Runtime_Memory_Model.md`
- `docs/02_Automation/DCS_Redundancy_and_Bumpless_Transfer.md`
- `docs/04_Industrial_Protocol/Industrial_Protocol_Design_Philosophy.md`
- `docs/04_Industrial_Protocol/Modbus_Deep_Dive.md`
- `docs/10_Tool_Development/Simulation_and_Tooling_Roadmap.md`
- `docs/13_Interview/Seed_Based_Interview_Answers.md`

## 4. 后续扩展优先级

下一轮建议优先扩展：

1. `04_Industrial_Protocol`: S7Comm、OPC UA、Profinet、EtherNet/IP、EtherCAT。
2. `10_Tool_Development`: Python socket、pymodbus、Scapy、pcap 解析。
3. `09_Industrial_Security`: 控制闭环攻击、Stuxnet、TRITON、MITRE ATT&CK for ICS。
4. `07_Reverse_Engineering`: 固件分析、PLC 程序逆向、协议逆向。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[知识库更新工作流](Update_Workflow.md)
- 本章目录：[00_Project](README.md)
- 下一篇：[01 Fundamentals：计算机与安全基础](../01_Fundamentals/README.md)

