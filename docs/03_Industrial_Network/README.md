# 03 Industrial Network：工业网络与边界安全

工业网络是工控安全的“路径层”。02 章让你知道工业现场有什么设备、谁控制谁；03 章要解决的是：这些资产如何连接，数据如何流动，攻击者可能从哪里进来，又可能如何横向移动到控制层。

本章重点不是重复普通网络基础，而是建立工控安全项目中真正会用到的网络分析能力：

- 看懂工业网络分层。
- 能画出生产网络、控制网络、现场网络、工业 DMZ 的关系。
- 能识别工程站、操作员站、SCADA Server、历史库、PLC、DCS 控制站之间的通信路径。
- 能理解防火墙、交换机、工业网关、VPN、堡垒机、单向网闸、数据采集服务器的安全价值。
- 能从通信矩阵、抓包和设备配置判断风险。
- 能把“网络连通”翻译成“工控攻击路径”。

## 学习顺序

1. [学习地图](./Learning_Map.md)
2. [工业网络总体架构](./Industrial_Network_Overview.md)
3. [Purdue 模型与工控分层](./Purdue_Model_and_Zones.md)
4. [分区分域与安全域设计](./Zones_and_Conduits.md)
5. [工业 DMZ 深入理解](./Industrial_DMZ.md)
6. [典型工业网络拓扑](./Typical_Topologies.md)
7. [通信矩阵与数据流分析](./Communication_Matrix.md)
8. [工业交换机、路由与 VLAN](./Switch_Router_VLAN.md)
9. [工业防火墙与访问控制](./Industrial_Firewall_ACL.md)
10. [远程运维与第三方接入](./Remote_Access_and_Vendor_Maintenance.md)
11. [工业网关、协议转换与边界设备](./Gateway_Protocol_Conversion.md)
12. [无线、串口与现场总线风险](./Wireless_Serial_Fieldbus.md)
13. [被动监测、流量镜像与工业 IDS](./Passive_Monitoring_and_IDS.md)
14. [工控网络安全设备与边界能力](./Network_Security_Devices.md)
15. [工业网络抓包分析方法](./Packet_Capture_Methodology.md)
16. [工业网络攻击路径建模](./Attack_Path_Modeling.md)
17. [网络评估检查清单](./Network_Assessment_Checklist.md)
18. [风险案例化表达](./Network_Risk_Case_Studies.md)
19. [面试项目表达素材](./Project_Style_Interview_Stories.md)
20. [面试问答](./Interview_QA.md)
21. [术语表](./Glossary.md)

## 本章完成标准

完成本章后，你应该能做到：

- 解释 Purdue 模型中 Level 0 到 Level 5 的作用。
- 说明控制网、生产管理网、办公网、工业 DMZ 为什么要隔离。
- 根据资产清单画出基本网络拓扑。
- 根据通信矩阵判断不合理访问路径。
- 解释远程运维为什么是工控网络高风险入口。
- 说明工业防火墙白名单策略应该如何围绕资产和协议设计。
- 用抓包结果判断谁在和 PLC / HMI / SCADA 通信。
- 把“办公网能访问工程站”“PLC 暴露 502 端口”写成具体工控风险。

## 面向岗位的重点

| 岗位要求 | 03 章对应能力 |
|---|---|
| 工控系统协议、设备安全研究 | 理解协议流量在网络中的路径 |
| 安全测试、评估、审计 | 能评估边界、访问控制、远程运维 |
| 跟踪攻击手段和防护产品 | 理解工业 IDS、防火墙、网闸、堡垒机 |
| 报告撰写 | 能把网络连通性写成攻击路径和整改建议 |
| 电力、石化、水处理等场景 | 理解多站点、远程监控、调度网络风险 |
