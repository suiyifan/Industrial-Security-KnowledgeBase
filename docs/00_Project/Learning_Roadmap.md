# 学习路线：11 个 Sprint

每个 Sprint 建议 1 周。如果时间紧，可以把 Sprint 2、3、4、6 作为面试优先路线，把 Sprint 7、8、9、10 作为能力拔高路线。

## Sprint 1：开发环境 + 知识库框架

目标：

- 搭建 GitHub 知识库。
- 建立学习笔记、实验报告、漏洞分析报告模板。
- 配置 Python、Git、VS Code、Markdown、Wireshark、IDA Free / Ghidra 等工具。

实践：

- 初始化本仓库。
- 写第一篇 `memory/Self_Assessment.md`。
- 建立 `labs/README.md`，记录后续实验。

产出：

- 可展示的知识库项目。
- 一张个人能力矩阵。

## Sprint 2：Python + Git + Linux + 网络基础

理论：

- Python 基础语法、文件处理、网络编程、异常处理、日志。
- Git 分支、提交、README、Issue、项目结构。
- Linux 常用命令、进程、端口、权限、日志。
- TCP/IP、HTTP、DNS、ARP、ICMP、路由、端口。

实践：

- 写端口扫描器。
- 写 TCP echo client/server。
- 用 Wireshark 抓 HTTP、DNS、TCP 三次握手。

产出：

- `scripts/tcp_echo_server.py`
- `scripts/simple_port_scanner.py`
- 一篇抓包分析笔记。

## Sprint 3：PLC + PID + DCS + SCADA

理论：

- PLC 输入输出、扫描周期、梯形图概念。
- PID 控制的 P / I / D 含义。
- DCS、SCADA、HMI、工程站、操作员站、历史数据库。
- 工业现场网络分层。

实践：

- 画一张“工厂控制系统拓扑图”。
- 用仿真资料理解 PLC 控制水箱 / 电机 / 阀门。

产出：

- `docs/02_Automation/Industrial_Automation_Overview.md`
- `assets/industrial-network-topology.png` 或 Mermaid 图。

## Sprint 4：TCP/IP + Wireshark + 工业协议

理论：

- TCP/UDP 差异。
- Wireshark 过滤器。
- Modbus TCP 报文结构。
- S7comm、OPC UA、IEC 104 的使用场景。

实践：

- 抓取并分析 Modbus TCP 样例包。
- 手写 Modbus TCP 读保持寄存器请求。

产出：

- `docs/04_Industrial_Protocol/Modbus_TCP.md`
- `scripts/modbus_read_holding_registers.py`

## Sprint 5：Python 协议开发 + Socket + Scapy

理论：

- Socket 编程。
- Scapy 构包、发包、解析。
- 协议字段、状态机、超时重试。

实践：

- 写 Modbus TCP 探测脚本。
- 写 PCAP 解析脚本，提取 IP、端口、功能码。

产出：

- `scripts/modbus_probe.py`
- `scripts/pcap_summary.py`

## Sprint 6：Web 安全

理论：

- SQL 注入、文件上传、越权、RCE、SSRF、XSS、认证绕过。
- 漏扫器、Web 漏扫器、基线核查、IDS / IPS 原理。

实践：

- 用本地靶场复现 3 个基础漏洞。
- 写一篇“Web 漏洞如何映射到工控平台风险”的笔记。

产出：

- `docs/06_Web_Security/Web_Vulnerability_Basics.md`
- `labs/web-security-basic/`

## Sprint 7：汇编 + PE + Windows + IDA

理论：

- x86/x64 基础寄存器、栈、调用约定。
- PE 文件结构。
- Windows API。
- IDA / Ghidra / WinDbg / OD 基本流程。

实践：

- 分析一个简单 crackme。
- 识别字符串、函数、导入表、关键分支。

产出：

- `docs/07_Reverse_Engineering/Reverse_Engineering_Basics.md`
- `labs/reverse-crackme-01/`

## Sprint 8：漏洞分析 + CVE + 工控漏洞

理论：

- CVE、CWE、CVSS。
- 漏洞复现、PoC、影响范围、修复建议。
- 工控漏洞常见类型：未授权访问、弱口令、命令注入、缓冲区溢出、路径穿越、明文协议。

实践：

- 选 2 个公开工控 CVE 做复现或静态分析。
- 写标准漏洞分析报告。

产出：

- `docs/08_Vulnerability_Research/CVE_Analysis_Method.md`
- `docs/12_Research_Projects/Project_CVE_Reproduction.md`

## Sprint 9：ICS 安全体系 + IEC 62443

理论：

- 工控安全分区分域。
- 纵深防御。
- IEC 62443 核心概念。
- 等保、关基、风险评估、资产识别。

实践：

- 对一个模拟工控网络做资产、威胁、风险、控制措施分析。

产出：

- `docs/09_Industrial_Security/IEC62443_Overview.md`
- `templates/Security_Assessment_Report_Template.md`

## Sprint 10：AI 辅助漏洞研究 + AgentSecLab

理论：

- AI 辅助代码审计。
- AI 辅助协议字段理解。
- AI 辅助报告生成。
- Agent 工作流的边界：不能替代验证，必须复现实证。

实践：

- 用 AI 辅助分析一个协议解析脚本或开源漏洞。
- 建立自己的安全研究 Prompt 库。

产出：

- `prompts/Vulnerability_Research_Prompts.md`
- `docs/11_AI_for_Security/AI_Assisted_Vulnerability_Research.md`

## Sprint 11：项目实战 + GitHub 作品集 + 杭州面试

理论：

- 简历项目表达。
- 面试 STAR 表达。
- “自动化背景如何转工控安全”的叙事。

实践：

- 完成 3 个作品集项目：
  - 工控协议解析器
  - 工控 CVE 分析报告
  - 工控安全评估样例报告

产出：

- GitHub README 优化。
- `docs/13_Interview/Interview_QA.md`
- `docs/13_Interview/Self_Introduction.md`

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[岗位画像：工控安全分析](Job_Profile.md)
- 本章目录：[00_Project](README.md)
- 下一篇：[能力矩阵](Capability_Matrix.md)

