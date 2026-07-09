# Modbus 深挖：寄存器模型、抓包与安全分析

## 1. 原理解释：Modbus 为什么能长期存在

Modbus 的成功不是因为技术最先进，而是因为它简单、开放、资源占用低，并抽象出统一的寄存器访问模型。

它让不同厂家的 PLC、仪表、变频器、远程 I/O 能用一致方式通信。

## 2. 工程实现：RTU 与 TCP

Modbus RTU 通常运行在 RS485 上，采用 Master / Slave 模型。

Modbus TCP 运行在以太网上，默认端口 `502`。

对比：

| 类型 | 传输 | 特点 |
|---|---|---|
| Modbus RTU | RS485 串口 | CRC 校验，适合现场总线 |
| Modbus TCP | TCP/IP | MBAP Header，适合工业以太网 |

## 3. 数据区模型

| 类型 | 数据 | 权限 | 常见用途 |
|---|---|---|---|
| Coil 0xxxx | 1 bit | 可读写 | DO、线圈、启停命令 |
| Discrete Input 1xxxx | 1 bit | 只读 | DI、开关状态 |
| Input Register 3xxxx | 16 bit | 只读 | AI、过程值 |
| Holding Register 4xxxx | 16 bit | 可读写 | SP、参数、AO、配方 |

安全分析重点：

- `Input Register` 常是只读过程值。
- `Holding Register` 常包含可写参数和设定值。
- `Coil` 写操作可能对应设备启停。

## 4. 地址偏移

文档中的 `40001` 通常是人类可读地址，报文中的起始地址可能是 `0`。

例如：

```text
文档地址 40001 -> 报文地址 0x0000
文档地址 40010 -> 报文地址 0x0009
```

这点在抓包和写脚本时很容易出错。

## 5. 常见功能码

| 功能码 | 含义 | 安全关注 |
|---|---|---|
| 01 | 读 Coil | 读取输出状态 |
| 02 | 读 Discrete Input | 读取输入状态 |
| 03 | 读 Holding Register | 读取参数 / 设定值 |
| 04 | 读 Input Register | 读取过程值 |
| 05 | 写单个 Coil | 改输出 / 命令 |
| 06 | 写单个 Holding Register | 改参数 / SP |
| 0F | 写多个 Coil | 批量改输出 |
| 10 | 写多个 Holding Register | 批量改参数 / 配方 |

读操作不一定安全，写操作通常更敏感。

## 6. Modbus TCP 报文结构

Modbus TCP = MBAP Header + PDU。

读取 Holding Register 示例：

```text
00 01  00 00  00 06  01  03  00 00  00 02
```

字段：

| 字段 | 字节 | 含义 |
|---|---|---|
| Transaction ID | 00 01 | 请求 / 响应配对 |
| Protocol ID | 00 00 | 固定为 0 |
| Length | 00 06 | 后续字节长度 |
| Unit ID | 01 | 单元 ID |
| Function Code | 03 | 读 Holding Register |
| Start Address | 00 00 | 起始地址 |
| Quantity | 00 02 | 数量 |

## 7. Wireshark 分析步骤

过滤：

```text
tcp.port == 502
modbus
```

分析顺序：

1. 确认源 IP 和目的 IP。
2. 判断是否为正常 HMI / SCADA / 工程站。
3. 看功能码：读还是写。
4. 看地址和数量。
5. 看时间规律和频率。
6. 结合点表判断寄存器含义。
7. 结合 HMI 操作日志和趋势判断是否正常。

## 8. 安全视角

常见风险：

- 未授权读取过程数据。
- 未授权写 Coil，影响设备启停。
- 未授权写 Holding Register，修改 SP、参数、配方。
- 缺少认证和加密。
- 缺少访问源限制。
- 任意主机可访问 TCP 502。

## 9. 工业案例：写 Holding Register

抓包发现：

```text
Function Code: 0x06
Address: 0009
Value: 80
```

结合点表：

```text
40010 -> VALVE01_OPEN_SP -> 1 号阀开度设定
```

报告不能只写：

```text
发现 Modbus 写寄存器。
```

应该写：

```text
发现主机 A 对 PLC-01 执行 Modbus 写单寄存器操作，目标地址对应 1 号阀开度设定。若该操作未授权，可能改变阀门开度，影响流量和工艺稳定。
```

## 10. 面试表达

### 60 分答案

> Modbus 是典型寄存器模型协议，常见数据区包括 Coil、Discrete Input、Input Register 和 Holding Register。安全分析时我会重点区分读写功能码，尤其关注 05、06、0F、10 这类写操作。

### 90 分答案

> 分析 Modbus TCP 时，我会先看 TCP 502 通信双方，再解析 MBAP Header、功能码、地址和数量。03/04 多用于读取，06/10 等写操作风险更高。但判断风险不能只看功能码，还要结合来源 IP、时间、频率、点表和工艺语义。写 Holding Register 可能只是改普通参数，也可能是改 PID 设定值、阀门开度或配方。

### 常见追问

问：为什么 40001 在报文里是 0？

答：

> 40001 是文档中的人类地址，报文里通常使用从 0 开始的偏移地址，所以 40001 对应起始地址 0。

## 11. 实操建议

后续实践路线：

1. 使用 OpenPLC 或 Modbus 模拟器。
2. 用 Wireshark 抓读 Holding Register 报文。
3. 用 Python / pymodbus 发送读请求。
4. 再发送写请求到测试变量。
5. 记录功能码、地址、值、HMI 变化。
6. 写一篇“Modbus 写寄存器如何影响控制变量”的报告。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[Modbus TCP]()
- 本章目录：[04_Industrial_Protocol]()
- 下一篇：[S7Comm 与西门子通信]()

