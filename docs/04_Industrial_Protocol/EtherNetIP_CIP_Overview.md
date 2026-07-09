# EtherNet/IP 与 CIP 对象模型

## 1. 原理解释

EtherNet/IP 是基于 CIP 的工业以太网协议，常见于罗克韦尔等自动化生态。

CIP 使用对象模型表达设备能力，访问的是对象、实例、属性和服务。

## 2. 工程实现

典型通信：

```text
PLC / Scanner
  -> EtherNet/IP
  -> Adapter / Drive / Remote IO
```

常见端口：

- TCP 44818
- UDP 2222

## 3. 数据流

EtherNet/IP 包含：

- 显式消息：配置、诊断、参数读写。
- 隐式消息：周期 I/O 实时数据。

安全分析要区分：

- 是普通诊断读取？
- 是参数写入？
- 是周期控制数据？

## 4. 安全风险

- 未授权读取设备对象。
- 修改驱动参数。
- 干扰周期 I/O。
- 设备身份和模块信息泄露。
- 工程工具访问未受限。

## 5. 面试表达

### 60 分答案

> EtherNet/IP 基于 CIP 对象模型，常用于 PLC、远程 I/O、驱动之间通信，常见端口 TCP 44818 和 UDP 2222。

### 90 分答案

> 分析 EtherNet/IP 时，我会区分显式消息和隐式 I/O。显式消息更多用于参数、诊断和配置，隐式消息更贴近周期控制数据。安全风险要结合对象和服务判断，例如修改驱动参数与读取设备信息的影响完全不同。

## 6. 实操建议

- 学习 CIP 对象、实例、属性、服务概念。
- 用 Wireshark 观察 TCP 44818 和 UDP 2222。
- 建立“对象访问 -> 工程含义 -> 安全影响”笔记。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[Profinet：工业以太网实时通信](Profinet_Overview.md)
- 本章目录：[04_Industrial_Protocol](README.md)
- 下一篇：[EtherCAT：高实时现场总线](EtherCAT_Overview.md)

