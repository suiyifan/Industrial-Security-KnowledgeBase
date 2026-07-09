# 10 Tool Development：安全工具开发

岗位 JD 明确提到 “工具开发”。这里的工具开发不一定一开始就写大型平台，更适合从小而完整的工具开始：输入清晰、输出可读、边界明确、能辅助协议分析、资产识别、漏洞复现、报告整理。

## 本章能力目标

- 能用 Python 编写 Socket、协议请求、PCAP 解析和报告自动化脚本。
- 能理解工具的安全边界：授权、速率、只读优先、避免破坏性动作。
- 能把工具做成 GitHub 作品：README、参数、示例、限制、测试样例。
- 能从工控安全场景出发设计工具，而不是为了写代码而写代码。

## 学习顺序

1. [仿真与工具路线](./Simulation_and_Tooling_Roadmap.md)
2. [Python Socket 工具开发](./Python_Socket_Tooling.md)
3. [pymodbus 工具开发](./Pymodbus_Tooling.md)
4. [Scapy 数据包构造](./Scapy_Packet_Crafting.md)
5. [PCAP 解析与流量摘要](./PCAP_Parsing.md)
6. [通信矩阵生成器](./Communication_Matrix_Generator.md)
7. [报告自动化](./Report_Automation.md)
8. [工具项目作品集](./Tool_Project_Portfolio.md)
9. [面试问答](./Interview_QA.md)
10. [术语表](./Glossary.md)

## 推荐工具项目

| 项目 | 能力 |
| --- | --- |
| TCP echo client/server | Socket、异常处理、日志 |
| Modbus TCP 请求解析器 | 协议字段理解 |
| Modbus 只读资产探测器 | 授权扫描、速率控制 |
| PCAP 摘要分析器 | 流量统计、协议识别 |
| 通信矩阵生成器 | 工控评估报告支撑 |
| CVE 信息整理脚本 | 漏洞情报结构化 |
| 报告模板生成器 | Markdown 自动化 |

## 工具开发原则

- 默认只读。
- 默认低速率。
- 明确授权提示。
- 参数和输出清晰。
- 失败原因可解释。
- 不隐藏风险。
- README 写清用途、输入、输出、限制和示例。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[术语表](../09_Industrial_Security/Glossary.md)
- 本章目录：[10_Tool_Development](README.md)
- 下一篇：[仿真与工具路线：把理论变成可验证经验](Simulation_and_Tooling_Roadmap.md)

