# Industrial Security KnowledgeBase

面向“工控安全分析 / 工控漏洞研究 / 安全评估”岗位的个人学习与作品集知识库。

目标岗位来自招聘 JD 与 HR 沟通内容，核心方向包括：

- 工控系统软件、协议、设备的信息安全研究
- 数据挖掘、软件逆向、协议逆向、脆弱性挖掘、工具开发
- 新漏洞、利用工具、攻击手段、防护产品的跟踪研究
- 安全测试、评估、审计与安全分析报告撰写
- 工控协议、工业场景、产品安全问题发现与 CVE 挖掘

## How to Use

1. 从 `docs/00_Project/Job_Profile.md` 了解目标岗位画像。
2. 从 [全书总目录与章节大纲](./docs/00_Project/Book_Outline.md) 选择当前建设章节。
3. 由 GPT 按章节大纲编写技术正文，Codex 负责整理入库、链接校验和 Git 更新。
4. 每学一个主题，用 `templates/Study_Note_Template.md` 记录。
5. 每做一个实验，用 `templates/Lab_Report_Template.md` 固化过程和截图。
6. 每次面试、复盘、提问后，把新增结论写入 `memory/` 或对应章节。

## Writing Standard

后续新增知识点默认遵循 seed 文件规范：

```text
控制理论 -> 工程实现 -> 协议/数据流 -> 安全风险 -> 面试表达 -> 实操验证
```

如果主题不直接涉及控制理论，则使用：

```text
原理解释 -> 工程实现 -> 数据流/控制流/状态流 -> 安全风险 -> 面试表达 -> 实操建议
```

详细规范见：

- [AGENTS.md](./AGENTS.md)
- [Seed 知识点归类与整合计划](./docs/00_Project/Seed_Knowledge_Classification.md)
- [工控安全研究员知识点汇总_seed.md](./工控安全研究员知识点汇总_seed.md)

## Navigation

`docs/` 下的知识点文档底部都带有导航索引：

- 上一篇
- 本章目录
- 下一篇

这样可以按阅读顺序连续学习，不需要每次回到首页重新点击。

## Directory Map

- `docs/00_Project`: 岗位画像、学习路线、能力矩阵、更新规则
- `docs/01_Fundamentals`: Python、Git、Linux、网络、计算机基础
- `docs/02_Automation`: PLC、PID、DCS、SCADA、工业控制基础
- `docs/03_Industrial_Network`: TCP/IP、抓包、工业网络拓扑与边界
- `docs/04_Industrial_Protocol`: Modbus、S7、OPC UA、IEC 104 等协议
- `docs/05_Industrial_System`: 工控设备、组态软件、工程站、历史数据库
- `docs/06_Web_Security`: Web 漏洞、系统漏洞、业务逻辑漏洞
- `docs/07_Reverse_Engineering`: 汇编、PE、Windows、IDA、WinDbg、OD
- `docs/08_Vulnerability_Research`: 漏洞分析、PoC、CVE、工控漏洞复现
- `docs/09_Industrial_Security`: IEC 62443、工控安全体系、安全评估
- `docs/10_Tool_Development`: Python 工具、Socket、Scapy、协议解析器
- `docs/11_AI_for_Security`: AI 辅助漏洞研究、AgentSecLab 工作流
- `docs/12_Research_Projects`: GitHub 作品集项目
- `docs/13_Interview`: 杭州面试准备、简历、问答库

## Update Rule

当你向 Codex 提问时，可以使用下面格式：

```text
请根据今天的问题更新知识库：
主题：
我目前理解：
卡点：
希望沉淀到哪个章节：
```

如果没有指定章节，默认先写入 `memory/Inbox.md`，再定期归档。
