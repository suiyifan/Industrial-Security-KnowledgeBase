# OPC UA：工业互联与安全模型

## 1. 原理解释

OPC UA 是工业数据互联协议，目标是让不同厂商设备、SCADA、MES、历史库和上层系统以统一方式交换数据。

与 Modbus 的寄存器、S7 的内存区不同，OPC UA 使用节点模型。

## 2. 工程实现

典型架构：

```text
PLC / DCS / 设备
  -> OPC UA Server
  -> OPC UA Client
  -> SCADA / MES / Historian / 数据平台
```

OPC UA Server 暴露地址空间，Client 读取或写入节点。

## 3. 数据流

```text
Client 连接 Server
  -> 建立 Secure Channel
  -> 创建 Session
  -> Browse 节点
  -> Read / Write / Subscribe
  -> 数据进入 HMI、历史库或上层系统
```

订阅机制允许 Client 持续接收变量变化，而不是不停轮询。

## 4. 安全模型

OPC UA 相比早期协议更重视安全：

- 应用证书
- 安全策略
- 消息签名
- 消息加密
- 用户认证
- 会话管理

但实际部署中常见问题：

- 使用 None 安全策略。
- 证书管理混乱。
- 匿名访问开启。
- 账号弱口令。
- 节点权限过宽。
- Server 暴露给不该访问的网络。

## 5. 安全风险

读风险：

- 泄露工艺变量。
- 泄露设备结构。
- 泄露点表和命名习惯。

写风险：

- 修改设定值。
- 修改模式。
- 影响控制命令。

配置风险：

- 匿名 Browse 使攻击者快速理解地址空间。
- 不加密导致敏感数据明文。

## 6. 工业案例

如果 OPC UA Server 允许匿名 Browse 和 Read，攻击者可以枚举节点：

```text
Plant1.Reactor101.TempPV
Plant1.Reactor101.TempSP
Plant1.Pump02.StartCmd
```

这会直接泄露工艺结构和关键变量。

## 7. 面试表达

### 60 分答案

> OPC UA 是工业互联协议，采用节点模型，支持读写、订阅和安全机制，常用于 PLC、SCADA、MES、历史库之间的数据交换。

### 90 分答案

> OPC UA 的优势是安全模型比传统协议完整，包括证书、加密、签名和用户认证。但实际风险常来自配置不当，例如匿名访问、None 安全策略、节点权限过宽。分析时我会看地址空间是否泄露关键变量，写权限是否能修改 SP、模式或命令。

## 8. 实操建议

- 搭建 OPC UA Demo Server。
- 使用 UaExpert 浏览节点。
- 对比匿名访问和认证访问。
- 抓包观察加密与非加密差异。
- 记录节点权限如何影响风险。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[S7Comm 与西门子通信](S7Comm_Deep_Dive.md)
- 本章目录：[04_Industrial_Protocol](README.md)
- 下一篇：[IEC 60870-5-104：电力远动协议](IEC104_Deep_Dive.md)

