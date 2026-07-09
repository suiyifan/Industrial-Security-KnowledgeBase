# S7Comm 与西门子通信

## 1. 原理解释

S7Comm 是西门子 S7 系列 PLC 常见通信协议，通常运行在 ISO-on-TCP 之上，常见端口为 TCP 102。

与 Modbus 的寄存器模型不同，S7 更接近 PLC 内存区访问模型。它关注的是：

- I 区输入
- Q 区输出
- M 区中间标志
- DB 数据块
- 诊断和工程操作

## 2. 工程实现

典型链路：

```text
HMI / SCADA / 工程站
  -> TCP 102
  -> ISO-on-TCP / COTP
  -> S7Comm
  -> PLC 内存区 / DB / 诊断服务
```

工程站通过 S7 通信可以完成在线监控、读取变量、下载块、诊断 PLC 状态等操作。

## 3. 数据流

HMI 读取 DB 中的温度设定值：

```text
HMI 变量绑定 DB10.DBW4
  -> S7 Read Var 请求
  -> PLC 读取 DB10 偏移 4
  -> 返回字节
  -> HMI 按数据类型解析
  -> 画面显示设定值
```

如果是写操作：

```text
HMI 输入新 SP
  -> S7 Write Var
  -> DB 中 SP 改变
  -> PID 或控制逻辑使用新值
  -> 输出和物理过程改变
```

## 4. 安全风险

重点关注：

- 非工程站访问 TCP 102。
- 未授权读取 DB。
- 写 DB 中设定值、模式、报警阈值。
- 工程下载或块写入。
- PLC Start / Stop 操作。
- 诊断信息泄露 PLC 型号、固件、模块信息。

S7 风险不只是“102 端口开放”，而是攻击者可能理解和修改 PLC 内存区。

## 5. Wireshark 观察点

过滤：

```text
tcp.port == 102
s7comm
```

重点看：

- Read Var
- Write Var
- Setup Communication
- Job / Ack_Data
- DB Number
- Area
- Address
- Data Length

## 6. 工业案例

如果抓包发现未知主机对 PLC 执行 `Write Var`，目标是 `DB20.DBW10`，而点表显示它是某回路 SP，则风险应描述为：

```text
未知主机通过 S7Comm 写入 PLC DB20.DBW10，该变量对应控制回路设定值。若该操作未授权，可能改变控制目标，导致温度、压力或流量偏离预期范围。
```

## 7. 面试表达

### 60 分答案

> S7Comm 是西门子 PLC 常见协议，通常使用 TCP 102。它和 Modbus 不同，更偏 PLC 内存区访问，可以读写 I/Q/M/DB 等区域。

### 90 分答案

> 我分析 S7Comm 时会关注它访问的是哪个区域，特别是 DB 数据块，因为 HMI 设定值、模式、PID 参数、报警阈值经常在 DB 里。读 DB 可能泄露工艺状态，写 DB 可能改变控制目标。工程站相关操作如块下载、PLC Stop/Start 需要更高风险评级。

## 8. 实操建议

- 使用 PLCSIM 或 S7 模拟环境。
- 用 Wireshark 抓 TCP 102。
- 对比 HMI 读变量和写变量流量。
- 建立“DB 地址 -> 变量语义 -> 控制影响”表。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[Modbus 深挖：寄存器模型、抓包与安全分析](Modbus_Deep_Dive.md)
- 本章目录：[04_Industrial_Protocol](README.md)
- 下一篇：[OPC UA：工业互联与安全模型](OPC_UA_Deep_Dive.md)

