# 01 Fundamentals：计算机与安全基础

本篇建立工控安全研究所需的计算机科学与安全工程底座。“基础”不是简单知识，而是后续所有高级能力反复依赖的底层模型：数据如何表示、程序如何运行、系统如何管理资源、网络如何传输、身份如何建立、证据如何形成。学习重点不是背命令，而是能够从原理解释现象、从输出定位问题、从系统行为追踪到工业过程。

## 本篇目标

学完本篇后，你应该能做到：

- 解释 CPU、内存、I/O、数据编码和操作系统运行机制。
- 使用 Python 与 C 理解和实现数据处理、协议解析及程序行为分析。
- 在 Linux、Windows 中完成系统管理、安全加固和事件排查。
- 理解网络、Web、数据库、密码学、身份与通用安全工程原理。
- 构建隔离、可恢复、可复现的漏洞与协议实验环境。
- 使用 Wireshark、系统日志和多源证据还原跨层行为。
- 将计算机行为映射到 PLC、SCADA、工程站和真实物理过程。

## 建议学习顺序

1. [学习地图](./Learning_Map.md)
2. [计算机组成与数据表示](./Computer_Architecture_and_Data.md)
3. [操作系统原理与运行时模型](./Operating_System_Fundamentals.md)
4. [Python 安全研究基础](./Python_Basics.md)
5. [C 语言、程序内存与内存安全](./C_and_Memory_Safety.md)
6. [Linux 系统管理与安全分析](./Linux_Basics.md)
7. [Windows 系统管理与安全分析](./Windows_System_and_Security.md)
8. [Git、GitHub 与研究证据管理](./Git_and_GitHub.md)
9. [TCP/IP 与网络通信基础](./Networking_Basics.md)
10. [网络服务、Web 与远程管理基础](./Network_Services_and_Web.md)
11. [数据库与工业数据基础](./Database_and_Data_Fundamentals.md)
12. [密码学、PKI 与身份基础](./Cryptography_PKI_and_Identity.md)
13. [网络安全工程基础](./Cybersecurity_Engineering_Fundamentals.md)
14. [虚拟化、容器与隔离实验环境](./Virtualization_Containers_and_Labs.md)
15. [Wireshark 与工业流量分析](./Wireshark_Basics.md)
16. [日志、可观测性与数字取证基础](./Logging_Observability_and_Forensics.md)
17. [实践任务清单](./Practice_Checklist.md)
18. [术语表](./Glossary.md)

## 面向岗位的学习重点

| 方向 | 为什么重要 | 本篇对应内容 |
|---|---|---|
| 工具开发 | 可靠处理字节、协议、日志和错误 | Python、C、数据表示、测试 |
| 协议分析 | 理解承载、编码、状态与时序 | 网络、Wireshark、密码学 |
| 漏洞研究 | 理解程序、内存、系统与权限边界 | C、操作系统、Linux、Windows |
| 工控系统安全 | 把 IT 行为映射到控制与物理后果 | 系统、网络、数据库、证据链 |
| 安全评估 | 建立资产、威胁、漏洞和风险模型 | 安全工程、身份、日志、取证 |
| 研究工程化 | 保证实验可复现、结果可审计 | Git、虚拟化、容器、证据管理 |

## 初学者学习方法

不要把“看懂”当成“掌握”。每学一个重要概念，都按五层标准检验自己：

1. **原理层**：能否用自己的话解释它为什么存在、解决什么问题？
2. **实现层**：能否指出它在操作系统、程序、协议或设备中的真实实现位置？
3. **流动层**：能否画出相关的数据流、控制流、状态流和信任边界？
4. **安全层**：能否说明错误配置或攻击如何沿链路传播，并最终影响工业过程？
5. **证据层**：能否用命令、脚本、抓包或日志证明判断，并保留可复现记录？

能够完成“解释—观察—验证—复盘—表达”的闭环，这个知识点才真正进入你的能力体系。每节学习后应同步完成对应实验，并把关键命令、输入条件、输出证据、异常现象和结论记录到研究日志中。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[Seed 知识点归类与整合计划](../00_Project/Seed_Knowledge_Classification.md)
- 本篇目录：[01_Fundamentals](README.md)
- 下一篇：[01 篇学习地图：计算机科学与安全工程基础](Learning_Map.md)
