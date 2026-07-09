# 项目：Modbus 流量分析器

## 1. 项目目标

开发一个 Python 工具，从 PCAP 中解析 Modbus TCP 流量，输出通信矩阵、功能码统计、异常响应和写操作列表。

## 2. 能证明的能力

- Python 工具开发。
- PCAP 解析。
- Modbus 字段理解。
- 工控安全检测思维。
- 报告自动化。

## 3. 功能设计

输入：

- PCAP 文件。

输出：

- 通信矩阵。
- 功能码统计。
- 写操作清单。
- 异常响应清单。
- Markdown 报告。

## 4. 核心字段

- 源 IP。
- 目的 IP。
- 事务 ID。
- 单元 ID。
- 功能码。
- 起始地址。
- 数量。
- 异常码。

## 5. 安全价值

该工具能帮助评估：

- 哪些主机访问 PLC。
- 是否存在写寄存器或写线圈。
- 是否存在异常响应。
- 是否有未知主机访问控制设备。

## 6. 面试表达

> 我做过 Modbus 流量分析器，用 PCAP 作为输入，解析通信双方、功能码、地址和异常响应，并把写操作单独标记出来。这个工具的价值是把抓包数据转成评估报告可用的通信矩阵和风险摘要，支撑白名单和异常行为分析。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[项目：OpenPLC + Modbus + PID 实验室](Project_OpenPLC_Modbus_PID_Lab.md)
- 本章目录：[12_Research_Projects](README.md)
- 下一篇：[项目：工控 CVE 复现与分析](Project_ICS_CVE_Reproduction.md)

