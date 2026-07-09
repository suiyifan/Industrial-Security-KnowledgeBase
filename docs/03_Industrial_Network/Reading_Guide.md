# 03 章阅读路线

你现在可以先不做抓包和实践，按“架构 -> 边界 -> 路径 -> 项目表达”的顺序读。

## 第一轮：建立工业网络全局图

阅读：

1. `Industrial_Network_Overview.md`
2. `Purdue_Model_and_Zones.md`
3. `Typical_Topologies.md`

目标：

- 理解工业网络不是一张扁平网。
- 能说清楚办公网、生产管理网、工业 DMZ、监控层、控制层、现场层。
- 能看懂常见单产线、多站点 SCADA、DCS、工业 DMZ 拓扑。

复习问题：

- Purdue 模型 Level 0 到 Level 4 分别是什么？
- 工业 DMZ 为什么不是普通互联网 DMZ？
- 双网卡工程站为什么危险？

## 第二轮：理解分区和边界

阅读：

1. `Zones_and_Conduits.md`
2. `Industrial_DMZ.md`
3. `Industrial_Firewall_ACL.md`
4. `Network_Security_Devices.md`

目标：

- 理解 Zone 和 Conduit。
- 理解防火墙、网闸、堡垒机、单向传输、数据交换的区别。
- 知道访问控制要基于通信矩阵和最小权限。

复习问题：

- VLAN 为什么不等于安全隔离？
- 什么情况下需要工业 DMZ？
- 防火墙白名单策略至少要写清楚哪些字段？

## 第三轮：理解通信与攻击路径

阅读：

1. `Communication_Matrix.md`
2. `Attack_Path_Modeling.md`
3. `Remote_Access_and_Vendor_Maintenance.md`
4. `Gateway_Protocol_Conversion.md`

目标：

- 能把拓扑图转成通信矩阵。
- 能从通信矩阵中找异常路径。
- 能把远程运维、工业网关、协议转换写成攻击路径。

复习问题：

- 通信矩阵为什么要记录读写权限？
- 厂商 VPN 长期开启有什么风险？
- 工业网关为什么是高价值边界资产？

## 第四轮：理解监测和抓包

阅读：

1. `Passive_Monitoring_and_IDS.md`
2. `Packet_Capture_Methodology.md`
3. `Switch_Router_VLAN.md`
4. `Wireless_Serial_Fieldbus.md`

目标：

- 理解为什么工控网络优先被动监测。
- 知道镜像口、TAP、工业 IDS 的价值。
- 知道抓包要输出通信矩阵，而不只是截图。
- 记住工业网络不只有以太网，还有串口、现场总线、无线和 4G/5G。

复习问题：

- 工业 IDS 重点监测哪些行为？
- 抓包点不同会影响看到哪些流量吗？
- 串口转以太网为什么会扩大攻击面？

## 第五轮：准备项目化表达

阅读：

1. `Network_Assessment_Checklist.md`
2. `Network_Risk_Case_Studies.md`
3. `Project_Style_Interview_Stories.md`
4. `Interview_QA.md`
5. `Glossary.md`

目标：

- 能讲出工业网络评估检查框架。
- 能把网络问题讲成攻击路径。
- 能用项目化语言回答面试官。

面试前背熟五条：

1. 工业网络安全核心是分区、边界、通信矩阵和攻击路径。
2. 工业 DMZ 用于承载跨域数据和运维，不应变成全通跳板。
3. 远程运维要按需开通、MFA、堡垒机、审计、回收账号。
4. 防火墙策略要基于通信矩阵，限制工业协议写操作和工程操作。
5. 抓包分析要沉淀资产、协议、通信方向、写操作和异常跨区通信。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[03 章术语表](Glossary.md)
- 本章目录：[03_Industrial_Network](README.md)
- 下一篇：[04 Industrial Protocol](../04_Industrial_Protocol/README.md)

