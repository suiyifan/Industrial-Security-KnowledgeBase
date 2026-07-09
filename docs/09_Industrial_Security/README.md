# 09 Industrial Security：工控安全体系

本章从单点技术进入体系化工控安全。前面章节学的是 PLC、网络、协议、系统、漏洞和逆向；这一章要把它们组织成 “如何保护一个真实工业现场” 的安全框架。

## 本章能力目标

- 理解工控安全和传统 IT 安全的差异。
- 能够用 Purdue 模型、分区分域、纵深防御描述工业网络。
- 能够基于 IEC 62443 理解资产、区域、通道、安全等级和能力要求。
- 能够使用 MITRE ATT&CK for ICS 描述攻击阶段和技术。
- 能够把漏洞影响映射到控制回路、操作员、工程站、网关和 PLC。
- 能够写出一份基础工控安全评估方案。

## 学习顺序

1. [IEC 62443 与工控安全体系](./IEC62443_Overview.md)
2. [工控威胁建模](./ICS_Threat_Model.md)
3. [攻击控制回路](./Attack_Control_Loop.md)
4. [MITRE ATT&CK for ICS](./MITRE_ATTCK_ICS.md)
5. [Stuxnet 与 TRITON 案例](./Stuxnet_TRITON_Case_Study.md)
6. [纵深防御体系](./Defense_in_Depth.md)
7. [安全评估方法论](./Security_Assessment_Methodology.md)
8. [应急响应与恢复](./Incident_Response_and_Recovery.md)
9. [面试问答](./Interview_QA.md)
10. [术语表](./Glossary.md)

## 体系化思维

工控安全不只是 “发现漏洞”。更完整的问题是：

- 资产在哪里，承担什么控制职责。
- 网络如何分区，跨区通信是否必要和可控。
- 哪些路径能从办公网、远程维护、工程站到达控制器。
- 攻击者如果获得某个节点权限，下一步能影响什么。
- 安全措施是否会影响可用性、实时性和安全生产。
- 发生事件后如何隔离、取证、恢复和复盘。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[术语表](../08_Vulnerability_Research/Glossary.md)
- 本章目录：[09_Industrial_Security](README.md)
- 下一篇：[IEC 62443 与工控安全体系](IEC62443_Overview.md)

