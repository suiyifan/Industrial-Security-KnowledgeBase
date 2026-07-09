# 04 Industrial Protocol

# 04 Industrial Protocol：工业协议研究

工业协议是工控安全研究的核心入口。协议报文不是普通数据包，它承载的是过程值、设定值、设备状态、控制命令、工程下载和诊断操作。

## 学习顺序

1. [工业协议设计思想](./Industrial_Protocol_Design_Philosophy.md)
2. [Modbus TCP](./Modbus_TCP.md)
3. [Modbus 深挖：寄存器模型、抓包与安全分析](./Modbus_Deep_Dive.md)
4. [S7Comm 与西门子通信](./S7Comm_Deep_Dive.md)
5. [OPC UA：工业互联与安全模型](./OPC_UA_Deep_Dive.md)
6. [IEC 60870-5-104：电力远动协议](./IEC104_Deep_Dive.md)
7. [Profinet：工业以太网实时通信](./Profinet_Overview.md)
8. [EtherNet/IP 与 CIP 对象模型](./EtherNetIP_CIP_Overview.md)
9. [EtherCAT：高实时现场总线](./EtherCAT_Overview.md)
10. [工业协议分析方法论](./Protocol_Analysis_Methodology.md)
11. [工业协议风险案例](./Protocol_Risk_Case_Studies.md)
12. [面试问答](./Interview_QA.md)
13. [术语表](./Glossary.md)

每个协议都按“使用场景、端口、报文结构、常见操作、安全风险、抓包过滤器、Python 实践”整理。

后续新增协议文档时，默认按 seed 规范展开：

```text
原理解释 -> 工程实现 -> 协议/数据流 -> 安全风险 -> 面试表达 -> 实操验证
```

## 本章完成标准

- 能解释不同工业协议为什么存在。
- 能区分寄存器模型、内存区模型、节点模型、对象模型和周期实时模型。
- 能用 Wireshark 判断读操作、写操作、工程操作、诊断操作。
- 能把协议操作映射到变量、控制逻辑和物理过程。
- 能写出协议风险报告，而不只是说“端口开放”。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[03 章阅读路线](../03_Industrial_Network/Reading_Guide.md)
- 本章目录：[04_Industrial_Protocol](README.md)
- 下一篇：[工业协议设计思想](Industrial_Protocol_Design_Philosophy.md)

