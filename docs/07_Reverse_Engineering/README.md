# 07 Reverse Engineering：逆向工程

本章把 JD 中的 “熟悉 WinDbg、OD、IDA 等逆向、反汇编工具手段” 展开为可学习、可复盘、可在面试中表达的能力链。工控安全研究中的逆向不是为了炫技，而是为了回答三个工程问题：

1. 目标软件、固件、驱动或协议到底如何工作。
2. 外部输入如何进入解析逻辑、状态机、控制逻辑或危险函数。
3. 是否存在可复现、可评估、可修复的安全风险。

## 本章能力目标

学完本章后，你应该能够：

- 读懂 Windows PE 文件的基本结构，知道导入表、导出表、节区、资源、重定位和入口点分别用于什么。
- 使用 IDA/Ghidra 识别函数、字符串、交叉引用、控制流、状态机和危险 API。
- 使用 x64dbg/WinDbg 做断点、单步、栈回溯、内存观察、异常定位和简单动态分析。
- 对工控上位机、网关程序、协议组件、固件镜像做初步逆向，能从样本中提取协议字段、命令码、校验逻辑和认证逻辑。
- 把逆向结论转化成安全分析报告：输入点、触发条件、影响范围、利用限制、缓解建议。

## 学习顺序

1. [逆向工程基础](./Reverse_Engineering_Basics.md)
2. [逆向工程方法论](./Reverse_Engineering_Methodology.md)
3. [Windows PE 基础](./Windows_PE_Basics.md)
4. [汇编与调试基础](./Assembly_Debugging_Basics.md)
5. [IDA/Ghidra 工作流](./IDA_Ghidra_Workflow.md)
6. [固件分析](./Firmware_Analysis.md)
7. [协议逆向](./Protocol_Reverse_Engineering.md)
8. [PLC 程序逆向](./PLC_Program_Reverse_Engineering.md)
9. [逆向风险案例](./Reverse_Risk_Case_Studies.md)
10. [面试问答](./Interview_QA.md)
11. [术语表](./Glossary.md)

## 与工控安全的关系

逆向工程在工控安全中常见于以下场景：

- 研究 HMI/SCADA 客户端如何与 PLC、RTU、网关通信。
- 分析工程软件项目文件、授权机制、下载逻辑和在线调试逻辑。
- 分析设备固件中的 Web 服务、协议服务、后门账号、硬编码密钥。
- 对公开 CVE 做补丁对比和根因分析。
- 将未知私有协议还原成字段结构、命令语义和状态机。
- 判断漏洞是否会影响真实生产：是否需要登录、是否需要工程模式、是否只在特定固件版本触发。

## 学习提醒

逆向学习容易陷入工具按钮和汇编细节。建议始终围绕工程问题推进：

- 我现在要找入口点、输入点、危险函数还是状态机。
- 我观察到的字符串、函数名、导入表、网络包能否互相印证。
- 静态分析结论是否能用调试、日志、抓包或最小样例验证。
- 面试表达时能否说清 “我怎么定位、怎么验证、风险是什么、限制是什么”。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[06 章术语表](../06_Web_Security/Glossary.md)
- 本章目录：[07_Reverse_Engineering](README.md)
- 下一篇：[逆向工程基础](Reverse_Engineering_Basics.md)

