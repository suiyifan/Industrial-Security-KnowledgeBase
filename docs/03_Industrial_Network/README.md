# 03 Industrial Network：工业网络、通信边界与运行韧性

02 篇解释控制系统如何感知、决策并作用于物理过程；03 篇进一步研究这些控制资产为什么互联、工业数据如何穿越交换与路由设备、通信状态怎样影响控制状态，以及攻击者能否利用身份、路径和协议能力改变生产过程。

本篇不重复“OSI 七层、TCP 可靠、VLAN 隔离”等入门结论，而是在这些基础上继续回答：

- 一个 PLC 报文经过哪些二层、三层和边界设备，转发状态由谁维护；
- 周期 I/O、请求/响应、事件上送、工程下载、历史采集和时间同步对网络有什么不同要求；
- 广播、未知单播、组播、重传、队列、收敛与时钟漂移怎样影响控制质量；
- VLAN、防火墙、DMZ、网闸、VPN 和堡垒机分别控制什么，不能证明什么；
- 抓包点能看到哪一段事实，丢包、镜像过载、非对称路由和时间偏差如何误导分析；
- 网络访问怎样转化为观察、操作、工程、维护或保护系统能力，并最终影响物理过程；
- 如何在不扰动生产的前提下验证配置、边界、冗余、监测与恢复流程。

根目录的 `chat学习路径.pdf` 用作网络基础覆盖基线。本篇会校正其中的简化表述，并在报文字段约束、协议状态、异常路径、抓包证据和工业工程边界上继续深入。

## 一条贯穿全篇的分析链

```text
业务与控制目的
  ↓
源资产 / 进程 / 身份
  ↓  生成周期数据、请求、事件或工程操作
终端协议栈
  ↓  ARP / Ethernet / VLAN / IP / TCP-UDP / 应用协议
交换、路由、冗余与安全边界
  ↓  转发表、路由表、会话表、白名单、代理状态
目标资产 / 服务 / 控制器
  ↓  观察、操作、维护或工程能力
控制逻辑 / 执行器 / 物理过程
  ↓
反馈、报警、保护动作与业务后果
```

分析时同时跟踪五类状态：端点连接状态、交换与路由状态、安全设备会话状态、工业应用会话状态、设备与过程状态。只看到端口开放，不能证明应用命令可执行；只看到 TCP ACK，也不能证明 PLC 已接受变量写入；只看到 HMI 数值变化，也不能证明现场执行器真的动作。

## 核心章节顺序

1. [03 篇学习地图](Learning_Map.md)
2. [工业网络架构、数据流与典型拓扑](Industrial_Network_Overview.md)
3. [Purdue 模型、区域与通道](Purdue_Model_and_Zones.md)
4. [工业以太网交换、VLAN 与二层安全](Switch_Router_VLAN.md)
5. [IP 寻址、路由与工业网络基础服务](IP_Routing_and_Network_Services.md)
6. [工业网络冗余、收敛与时间同步](Network_Redundancy_and_Time_Synchronization.md)
7. [工业 DMZ 与跨区数据交换](Industrial_DMZ.md)
8. [工业防火墙与通信矩阵](Industrial_Firewall_ACL.md)
9. [远程运维与供应商接入](Remote_Access_and_Vendor_Maintenance.md)
10. [工业网络抓包与证据方法论](Packet_Capture_Methodology.md)
11. [被动监测、资产识别与工业 IDS](Passive_Monitoring_and_IDS.md)
12. [网关、协议转换与边界风险](Gateway_Protocol_Conversion.md)
13. [无线、串口与现场总线接入](Wireless_Serial_Fieldbus.md)
14. [工业攻击路径与屏障建模](Attack_Path_Modeling.md)
15. [工业网络评估、变更、恢复与验收](Network_Assessment_and_Recovery.md)

## 工程辅助材料

- [分区分域设计方法](Zones_and_Conduits.md)
- [典型工业网络拓扑图集](Typical_Topologies.md)
- [通信矩阵与数据流分析](Communication_Matrix.md)
- [工控网络安全设备与能力边界](Network_Security_Devices.md)
- [网络评估现场检查清单](Network_Assessment_Checklist.md)
- [网络风险案例](Network_Risk_Case_Studies.md)
- [项目式面试表达](Project_Style_Interview_Stories.md)
- [面试问答](Interview_QA.md)
- [阅读、复习与验收指南](Reading_Guide.md)
- [术语表](Glossary.md)

## 完成标准

完成本篇后，应能够：

- 从 P&ID、资产清单和交换机配置还原控制通信拓扑；
- 解释 MAC 学习、ARP、VLAN、路由、NAT、TCP/UDP 和工业应用的嵌套关系及状态边界；
- 分析环路、广播、组播、队列、重传、链路切换和时钟异常对控制过程的影响；
- 以业务流和最小能力建立通信矩阵及防火墙白名单；
- 设计工业 DMZ、远程维护和跨区数据交换路径，并说明单点和共因风险；
- 选择 TAP、SPAN、主机或边界日志重建数据流、控制流与事件时间线；
- 将网络可达性逐步证明到具体工业能力、控制动作、保护响应和物理后果；
- 在隔离环境完成抓包、故障注入、规则验证和恢复演练，并明确生产测试禁区。

## 安全实验边界

- 生产网默认只做经批准的被动观察和配置审阅；
- 不对未知工业资产主动扫描、泛洪、欺骗 ARP、注入控制报文或测试冗余切换；
- 镜像口、TAP、笔记本和临时账户均纳入变更、接入和退出检查；
- 主动实验只在仿真器、实验交换机或明确授权的隔离环境完成；
- 所有结论区分“配置推断、流量观察、日志佐证、实验验证和现场确认”。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[02 篇术语表](../02_Automation/Glossary.md)
- 本篇目录：[03_Industrial_Network](README.md)
- 下一篇：[03 篇学习地图](Learning_Map.md)
