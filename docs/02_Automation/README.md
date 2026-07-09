# 02 Automation：工业自动化与控制系统

本章开始进入工控安全的核心地带。01 章解决“计算机和网络怎么工作”，02 章要解决“工业现场到底在控制什么、谁在控制、怎么控制、出问题会造成什么后果”。

工控安全研究不能只盯漏洞编号。你要能把漏洞放回工业场景里理解：

- 它影响的是工程站、操作员站、HMI、PLC、DCS、SCADA，还是历史数据库？
- 它可能导致信息泄露、误操作、控制逻辑篡改、设备停机，还是安全联锁失效？
- 它发生在离散制造、电力、石油石化、冶金、水处理，还是轨道交通场景？
- 它是 IT 风险，还是会转化为 OT 侧生产风险和安全风险？

## 学习顺序

1. [学习地图](./Learning_Map.md)
2. [工业自动化概览](./Industrial_Automation_Overview.md)
3. [工业现场与物理过程](./Physical_Process_and_Field_Devices.md)
4. [控制理论入门：开环、闭环、PID](./Control_Theory_Basics.md)
5. [控制理论深挖：从闭环稳定到攻击影响](./Control_Theory_Deep_Dive.md)
6. [4~20mA、I/O 与真实世界连接](./Analog_Signal_and_IO_Deep_Dive.md)
7. [PLC 系统](./PLC_Basics.md)
8. [PLC Runtime、扫描周期与内存模型深挖](./PLC_Runtime_Memory_Model.md)
9. [DCS 系统](./DCS_Basics.md)
10. [DCS 冗余与无扰切换](./DCS_Redundancy_and_Bumpless_Transfer.md)
11. [SCADA、HMI 与组态软件](./SCADA_HMI_and_Configuration.md)
12. [工程站、操作员站与历史数据库](./Engineering_Operator_Historian.md)
13. [工业行业场景](./Industrial_Scenarios.md)
14. [功能安全、SIS 与安全联锁](./Safety_SIS_and_Interlock.md)
15. [自动化系统攻击面](./Automation_Attack_Surface.md)
16. [自动化知识如何服务工控安全](./Automation_for_ICS_Security.md)
17. [现场项目视角：一次工控安全评估怎么展开](./Field_Project_View.md)
18. [点表、变量与工程资料深挖](./Point_Table_and_Tags_Deep_Dive.md)
19. [PLC 工程工作流深挖](./PLC_Engineering_Workflow.md)
20. [控制逻辑阅读方法](./Control_Logic_Reading.md)
21. [SCADA 项目资料与配置深挖](./SCADA_Project_Artifacts.md)
22. [DCS 运行维护与安全关注点](./DCS_Operations_Deep_Dive.md)
23. [资产访谈与现场调研问题清单](./Asset_Interview_Checklist.md)
24. [工控风险案例化表达](./Risk_Case_Studies.md)
25. [面试项目表达素材](./Project_Style_Interview_Stories.md)
26. [面试问答](./Interview_QA.md)
27. [术语表](./Glossary.md)

## 本章完成标准

完成本章后，你应该能做到：

- 画出一个典型工业控制系统的分层架构。
- 解释 PLC、DCS、SCADA、HMI、工程站、操作员站的区别。
- 解释传感器、执行器、控制器、控制逻辑之间的关系。
- 说清楚 PID 控制的基本思想。
- 理解工程下载、变量点表、报警、趋势、历史数据库等概念。
- 从安全角度分析工程站、HMI、PLC、工业网关的攻击面。
- 把一个漏洞的影响翻译成工业生产影响。
- 能说出一次工控安全评估会看哪些资料、问哪些问题、检查哪些配置。
- 能用点表、控制逻辑、报警、趋势、工程下载等细节解释漏洞影响。
- 面试时能把“我学过概念”升级成“我知道项目现场怎么分析”。

## 面向岗位的重点

| 岗位要求 | 02 章对应能力 |
|---|---|
| 工控系统软件、协议、设备安全研究 | 理解工业控制系统组成和控制链路 |
| 协议逆向、脆弱性挖掘 | 理解协议背后的真实工业操作 |
| 安全测试、评估、审计 | 能识别关键资产、关键链路、关键风险 |
| 安全分析报告、调研报告 | 能把技术漏洞写成工业风险 |
| 面向电力、石油、石化、冶金、水处理等客户 | 理解典型行业场景差异 |

## 深入学习建议

如果目标是面试，不要只背 PLC、DCS、SCADA 的定义。更像项目经历的表达来自这些细节：

- 你知道工程站里可能有什么工程文件、点表、通信配置和下载记录。
- 你知道 HMI 画面背后绑定变量点，按钮可能对应写变量或脚本动作。
- 你知道 PLC 的 Force、Run/Stop、上传/下载、在线监控都是高风险动作。
- 你知道报警、趋势、历史库不是装饰，而是事故追溯和异常判断证据。
- 你知道评估时要先问清楚资产、网络区域、远程运维、工程变更、备份恢复。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[01 章术语表]()
- 本章目录：[02_Automation]()
- 下一篇：[02 章学习地图]()

