# Modbus TCP

## 为什么先学 Modbus TCP

Modbus TCP 简单、公开、字段清晰，适合作为工业协议分析入门。

## 基础概念

- 默认端口：502
- 通信模式：Client / Server
- 常见功能码：
  - `0x01`: Read Coils
  - `0x02`: Read Discrete Inputs
  - `0x03`: Read Holding Registers
  - `0x04`: Read Input Registers
  - `0x05`: Write Single Coil
  - `0x06`: Write Single Register
  - `0x0F`: Write Multiple Coils
  - `0x10`: Write Multiple Registers

## 报文结构

Modbus TCP = MBAP Header + PDU。

MBAP Header：

- Transaction ID：事务 ID
- Protocol ID：协议 ID，通常为 0
- Length：后续长度
- Unit ID：单元 ID

PDU：

- Function Code：功能码
- Data：功能码对应的数据

## 安全关注点

- 明文传输
- 缺少认证
- 可被未授权读取寄存器
- 可被未授权写线圈 / 写寄存器
- 资产暴露后容易被探测

## 实践任务

1. 用 Wireshark 观察 Modbus TCP 报文。
2. 用 Python 构造读取保持寄存器请求。
3. 分析功能码与工业操作之间的关系。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[工业协议设计思想](Industrial_Protocol_Design_Philosophy.md)
- 本章目录：[04_Industrial_Protocol](README.md)
- 下一篇：[Modbus 深挖：寄存器模型、抓包与安全分析](Modbus_Deep_Dive.md)

