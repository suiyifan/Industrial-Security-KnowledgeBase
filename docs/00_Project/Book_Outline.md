# 《工控安全研究员知识库》总目录与章节大纲

本文档是项目后续内容建设的唯一总目录。项目改为以“章节”为最小交付单位：GPT 负责技术正文初稿，Codex 负责内容整理、目录归档、Markdown 规范、内部链接、质量检查与 Git 更新。

## 一、章节生产规则

### 1. 章节状态

| 状态 | 含义 |
| --- | --- |
| `待编写` | 已确定大纲与目标文件，等待 GPT 生成完整正文 |
| `待整理` | 已收到 GPT 正文，等待 Codex 合并、排版与归档 |
| `已入库` | 正文已经写入目标文件，链接与导航已经更新 |
| `已校验` | 已完成结构、格式、链接和 Git diff 检查 |

现有文档只作为旧稿和素材，不因文件已经存在而自动标记为完成。是否完成以本目录的状态为准。

### 2. 单章最低结构

每章原则上采用以下结构，具体主题可适当调整：

```text
学习目标
-> 为什么存在 / 原理解释
-> 工业现场与工程实现
-> 数据流 / 控制流 / 状态流
-> 安全风险与物理过程影响
-> 防护、检测与应急
-> 隔离实验或实操建议
-> 面试 60 分回答 / 90 分回答 / 常见追问
-> 本章总结
```

### 3. 单章交付约定

向 Codex 交付正文时使用：

```text
章节编号：
章节名称：
目标文件：（不知道可留空）
GPT 生成正文：
处理方式：覆盖旧稿 / 合并旧稿 / 仅整理格式
是否提交 Git：是 / 否
是否推送远端：是 / 否
```

Codex 默认执行：确认目标文件、保留有效技术内容、统一 Markdown、检查术语与链接、更新章节状态、运行质量检查、展示 Git diff。未经明确要求，不自动提交或推送。

## 二、全书结构

```text
导论：岗位与研究方法
├─ 第一篇 计算机与安全基础
├─ 第二篇 自动化、控制理论与工业现场
├─ 第三篇 工业网络与安全边界
├─ 第四篇 工业协议分析
├─ 第五篇 工业系统与关键资产
├─ 第六篇 工控 Web 与应用安全
├─ 第七篇 逆向工程与固件分析
├─ 第八篇 漏洞研究与 CVE 实践
├─ 第九篇 工控安全体系与安全评估
├─ 第十篇 安全工具开发
├─ 第十一篇 AI 辅助安全研究
├─ 第十二篇 研究项目与作品集
└─ 第十三篇 面试表达与求职准备
```

建议按照“导论 → 第一至第十篇 → 研究项目 → 面试”的顺序建设。第十一篇 AI 辅助研究可以与各技术篇并行维护。

## 三、导论：岗位与研究方法

| 编号 | 章节 | 目标文件 | 核心范围 | 状态 |
| --- | --- | --- | --- | --- |
| 0.1 | 工控安全研究员岗位画像 | `docs/00_Project/Job_Profile.md` | 岗位职责、能力边界、典型任务、成长路径 | 待编写 |
| 0.2 | 全书学习路线与知识依赖 | `docs/00_Project/Learning_Roadmap.md` | 学习阶段、前置知识、章节依赖、产出物 | 待编写 |
| 0.3 | 工控安全研究方法论 | `docs/00_Project/Research_Methodology.md` | 从现场、系统、协议到漏洞与物理影响的分析方法 | 待编写 |
| 0.4 | 实验安全、授权与证据规范 | `docs/00_Project/Lab_Safety_and_Evidence.md` | 隔离实验、授权边界、证据保全、负责任披露 | 待编写 |

## 四、第一篇：计算机与安全基础

目标：建立后续自动化系统理解、网络与协议分析、逆向工程、漏洞研究、安全评估和工具开发共同依赖的计算机科学与安全工程底座。“基础”表示底层且通用，不表示内容简单；每个单元必须达到能够解释原理、完成诊断、支撑实验并迁移到工控场景的程度。

| 编号 | 章节 | 目标文件 | 核心范围 | 状态 |
| --- | --- | --- | --- | --- |
| 1.1 | 计算机组成与数据表示 | `docs/01_Fundamentals/Computer_Architecture_and_Data.md` | CPU、内存、总线、I/O、二进制、编码、字节序、整数与浮点 | 已校验 |
| 1.2 | 操作系统原理与运行时模型 | `docs/01_Fundamentals/Operating_System_Fundamentals.md` | 内核、进程、线程、虚拟内存、文件系统、系统调用、权限与并发 | 已校验 |
| 1.3 | Python 安全研究基础 | `docs/01_Fundamentals/Python_Basics.md` | 语言、数据结构、字节流、文件、异常、日志、测试、CLI 与工程化 | 已校验 |
| 1.4 | C 语言、程序内存与内存安全 | `docs/01_Fundamentals/C_and_Memory_Safety.md` | 指针、栈、堆、结构体、编译链接、未定义行为和常见内存缺陷 | 已校验 |
| 1.5 | Linux 系统管理与安全分析 | `docs/01_Fundamentals/Linux_Basics.md` | 启动、文件、权限、进程、systemd、网络、日志、Shell、加固与排查 | 已校验 |
| 1.6 | Windows 系统管理与安全分析 | `docs/01_Fundamentals/Windows_System_and_Security.md` | NT 内核、进程、服务、注册表、权限、事件日志、PowerShell 与排查 | 已校验 |
| 1.7 | Git、GitHub 与研究证据管理 | `docs/01_Fundamentals/Git_and_GitHub.md` | 对象模型、分支、协作、提交、版本、证据、敏感信息与供应链 | 已校验 |
| 1.8 | TCP/IP 与网络通信基础 | `docs/01_Fundamentals/Networking_Basics.md` | Ethernet、VLAN、ARP、IP、路由、TCP/UDP、DNS、HTTP 与诊断 | 已校验 |
| 1.9 | 网络服务、Web 与远程管理基础 | `docs/01_Fundamentals/Network_Services_and_Web.md` | DNS、DHCP、NTP、HTTP/TLS、SSH、SMB、RDP、代理和认证会话 | 已校验 |
| 1.10 | 数据库与工业数据基础 | `docs/01_Fundamentals/Database_and_Data_Fundamentals.md` | 关系模型、SQL、事务、索引、权限、备份、时序数据与历史库 | 已校验 |
| 1.11 | 密码学、PKI 与身份基础 | `docs/01_Fundamentals/Cryptography_PKI_and_Identity.md` | 哈希、MAC、对称/非对称加密、证书、密钥、认证与授权 | 已校验 |
| 1.12 | 网络安全工程基础 | `docs/01_Fundamentals/Cybersecurity_Engineering_Fundamentals.md` | CIA、资产、威胁、漏洞、风险、信任边界、最小权限和纵深防御 | 已校验 |
| 1.13 | 虚拟化、容器与隔离实验环境 | `docs/01_Fundamentals/Virtualization_Containers_and_Labs.md` | Hypervisor、虚拟网络、快照、容器、镜像、隔离与可复现实验 | 已校验 |
| 1.14 | Wireshark 与工业流量分析 | `docs/01_Fundamentals/Wireshark_Basics.md` | 抓包位置、证据边界、过滤、会话重组、协议时序与过程映射 | 已校验 |
| 1.15 | 日志、可观测性与数字取证基础 | `docs/01_Fundamentals/Logging_Observability_and_Forensics.md` | 时间、日志、指标、事件关联、证据保全、时间线和应急采集 | 已校验 |

## 五、第二篇：自动化、控制理论与工业现场

目标：建立从物理过程、测量与执行、控制算法、控制器运行时、监控操作到安全保护的完整工程模型，能够把网络与软件行为映射为控制状态变化、生产连续性影响和真实物理后果。本篇不是自动化名词速查，而是后续工业网络、协议分析、漏洞研究、事件调查和风险评估共同依赖的 OT 语义基础。

| 编号 | 章节 | 目标文件 | 核心范围 | 状态 |
| --- | --- | --- | --- | --- |
| 2.1 | 工业自动化系统全景 | `docs/02_Automation/Industrial_Automation_Overview.md` | 现场层、控制层、监控层、生产管理层及角色 | 已校验 |
| 2.2 | 物理过程、传感器与执行器 | `docs/02_Automation/Physical_Process_and_Field_Devices.md` | 温度、压力、流量、液位、电机、阀门及故障模式 | 已校验 |
| 2.3 | 模拟量、数字量与 I/O 链路 | `docs/02_Automation/Analog_Signal_and_IO_Deep_Dive.md` | 4–20 mA、开关量、量程转换、I/O 映像与诊断 | 已校验 |
| 2.4 | 控制理论与反馈控制基础 | `docs/02_Automation/Control_Theory_Basics.md` | 开环、闭环、稳定性、动态响应、扰动与反馈 | 已校验 |
| 2.5 | PID 控制与工程整定 | `docs/02_Automation/Control_Theory_Deep_Dive.md` | P/I/D、整定、饱和、积分抗饱和、异常操纵影响 | 已校验 |
| 2.6 | 顺序控制、状态机与批次过程 | `docs/02_Automation/Sequential_Batch_and_State_Control.md` | 步序、状态迁移、配方、模式、许可条件、异常恢复与竞态 | 已校验 |
| 2.7 | PLC 原理、扫描周期与程序组织 | `docs/02_Automation/PLC_Basics.md` | CPU、I/O、扫描周期、周期/事件任务、程序块与运行模式 | 已校验 |
| 2.8 | PLC 运行时与内存模型 | `docs/02_Automation/PLC_Runtime_Memory_Model.md` | 过程映像、变量区、数据块、保持区、通信变量与状态变化 | 已校验 |
| 2.9 | PLC 工程组态、程序下装与变更 | `docs/02_Automation/PLC_Engineering_Workflow.md` | 建项、硬件组态、编译、下载、在线监控、强制与版本治理 | 已校验 |
| 2.10 | 控制逻辑阅读与危险动作识别 | `docs/02_Automation/Control_Logic_Reading.md` | LD/FBD/ST/SFC、启停、模式、联锁、报警、通信与写点追踪 | 已校验 |
| 2.11 | DCS 架构、运行、冗余与工程变更 | `docs/02_Automation/DCS_Operations_Deep_Dive.md` | 控制站、操作站、工程站、服务器、控制回路、冗余切换与变更 | 已校验 |
| 2.12 | SCADA、HMI 与组态工程 | `docs/02_Automation/SCADA_HMI_and_Configuration.md` | 遥测遥控、画面、变量、脚本、配方、通信驱动与权限 | 已校验 |
| 2.13 | 操作员站、报警、趋势与历史数据 | `docs/02_Automation/Engineering_Operator_Historian.md` | 操作语义、报警生命周期、趋势、历史库、时间与证据关联 | 已校验 |
| 2.14 | 点表、标签与过程数据语义 | `docs/02_Automation/Point_Table_and_Tags_Deep_Dive.md` | 点名、地址、量程、质量码、报警、单位与跨层映射 | 已校验 |
| 2.15 | 电机、电气控制与变频驱动 | `docs/02_Automation/Motor_Drives_and_Electrical_Control.md` | 接触器、继电器、MCC、VFD、启停、保护、转速与安全影响 | 已校验 |
| 2.16 | SIS、安全联锁与失效安全 | `docs/02_Automation/Safety_SIS_and_Interlock.md` | BPCS/SIS 边界、联锁、旁路、SIL、独立保护层与验证 | 已校验 |
| 2.17 | 典型工业过程与行业控制场景 | `docs/02_Automation/Industrial_Scenarios.md` | 水处理、石化、电力、冶金、离散制造的过程变量与关键约束 | 已校验 |
| 2.18 | 自动化系统攻击面与物理影响 | `docs/02_Automation/Automation_Attack_Surface.md` | 工程站、控制器、现场设备、闭环攻击、恢复与后果分级 | 已校验 |

## 六、第三篇：工业网络与安全边界

| 编号 | 章节 | 目标文件 | 核心范围 | 状态 |
| --- | --- | --- | --- | --- |
| 3.1 | 工业网络架构、数据流与典型拓扑 | `docs/03_Industrial_Network/Industrial_Network_Overview.md` | 控制闭环、网络角色、流量类型、拓扑、性能与安全目标 | 已校验 |
| 3.2 | Purdue 模型、区域与通道 | `docs/03_Industrial_Network/Purdue_Model_and_Zones.md` | 层级、Zone/Conduit、信任边界、模型局限与资产归域 | 已校验 |
| 3.3 | 工业以太网交换、VLAN 与二层安全 | `docs/03_Industrial_Network/Switch_Router_VLAN.md` | 以太网、ARP、MAC 学习、802.1Q、环路、组播与二层攻击 | 已校验 |
| 3.4 | IP 寻址、路由与工业网络基础服务 | `docs/03_Industrial_Network/IP_Routing_and_Network_Services.md` | IPv4/CIDR、路由、ACL、NAT、DHCP、DNS、NTP、组播与 QoS | 已校验 |
| 3.5 | 工业网络冗余、收敛与时间同步 | `docs/03_Industrial_Network/Network_Redundancy_and_Time_Synchronization.md` | 环网、冗余网关、PRP/HSR、收敛、PTP/NTP 与故障验证 | 已校验 |
| 3.6 | 工业 DMZ 与跨区数据交换 | `docs/03_Industrial_Network/Industrial_DMZ.md` | 跳板、代理、历史镜像、文件交换、单向传输与双边界 | 已校验 |
| 3.7 | 工业防火墙与通信矩阵 | `docs/03_Industrial_Network/Industrial_Firewall_ACL.md` | 白名单、方向、状态、协议命令、规则验证与变更治理 | 已校验 |
| 3.8 | 远程运维与供应商接入 | `docs/03_Industrial_Network/Remote_Access_and_Vendor_Maintenance.md` | VPN、堡垒机、临时授权、审计、第三方风险与退出检查 | 已校验 |
| 3.9 | 工业网络抓包与证据方法论 | `docs/03_Industrial_Network/Packet_Capture_Methodology.md` | TAP、镜像口、抓包点、丢包、时间同步、会话重组与证据链 | 已校验 |
| 3.10 | 被动监测、资产识别与工业 IDS | `docs/03_Industrial_Network/Passive_Monitoring_and_IDS.md` | 被动发现、基线、语义规则、异常检测、部署与响应边界 | 已校验 |
| 3.11 | 网关、协议转换与边界风险 | `docs/03_Industrial_Network/Gateway_Protocol_Conversion.md` | 串口/以太网、协议代理、地址映射、状态与质量语义失真 | 已校验 |
| 3.12 | 无线、串口与现场总线接入 | `docs/03_Industrial_Network/Wireless_Serial_Fieldbus.md` | 工业无线、串口参数、总线仲裁、远程站点与介质安全 | 已校验 |
| 3.13 | 工业攻击路径与屏障建模 | `docs/03_Industrial_Network/Attack_Path_Modeling.md` | 初始入口、身份与信任、横向移动、控制能力、物理后果和屏障 | 已校验 |
| 3.14 | 工业网络评估、变更、恢复与验收 | `docs/03_Industrial_Network/Network_Assessment_and_Recovery.md` | 现场调研、配置审阅、非侵入验证、故障恢复、测试与交付 | 已校验 |

## 七、第四篇：工业协议分析

| 编号 | 章节 | 目标文件 | 核心范围 | 状态 |
| --- | --- | --- | --- | --- |
| 4.1 | 工业协议设计思想与分析框架 | `docs/04_Industrial_Protocol/Industrial_Protocol_Design_Philosophy.md` | 实时性、确定性、可用性、信任模型、状态机 | 待编写 |
| 4.2 | Modbus TCP 深入分析 | `docs/04_Industrial_Protocol/Modbus_Deep_Dive.md` | MBAP、功能码、地址模型、异常响应、过程映射 | 待编写 |
| 4.3 | Siemens S7comm 深入分析 | `docs/04_Industrial_Protocol/S7Comm_Deep_Dive.md` | 通信栈、作业/应答、变量访问、工程操作 | 待编写 |
| 4.4 | OPC UA 深入分析 | `docs/04_Industrial_Protocol/OPC_UA_Deep_Dive.md` | 信息模型、会话、订阅、安全策略与证书 | 待编写 |
| 4.5 | IEC 60870-5-104 深入分析 | `docs/04_Industrial_Protocol/IEC104_Deep_Dive.md` | APCI/ASDU、遥信遥测遥控、时序与状态 | 待编写 |
| 4.6 | EtherNet/IP 与 CIP | `docs/04_Industrial_Protocol/EtherNetIP_CIP_Overview.md` | 对象模型、显式/隐式消息、I/O 连接 | 待编写 |
| 4.7 | PROFINET 通信与实时机制 | `docs/04_Industrial_Protocol/Profinet_Overview.md` | DCP、RT/IRT、设备发现、周期数据 | 待编写 |
| 4.8 | EtherCAT 通信与分布式时钟 | `docs/04_Industrial_Protocol/EtherCAT_Overview.md` | 帧处理、逻辑寻址、状态机、同步机制 | 待编写 |
| 4.9 | 未知工业协议分析方法 | `docs/04_Industrial_Protocol/Protocol_Analysis_Methodology.md` | 流量分组、字段假设、状态机、差分实验 | 待编写 |
| 4.10 | 工业协议风险案例 | `docs/04_Industrial_Protocol/Protocol_Risk_Case_Studies.md` | 未授权命令、重放、篡改、拒绝服务与过程后果 | 待编写 |

## 八、第五篇：工业系统与关键资产

| 编号 | 章节 | 目标文件 | 核心范围 | 状态 |
| --- | --- | --- | --- | --- |
| 5.1 | 工业资产分类与关键性 | `docs/05_Industrial_System/Industrial_Asset_Taxonomy.md` | 控制器、服务器、工作站、网络与现场资产 | 待编写 |
| 5.2 | 工程师站的功能与安全 | `docs/05_Industrial_System/Engineering_Workstation_Security.md` | 工程软件、项目文件、下装、在线调试与权限 | 待编写 |
| 5.3 | 操作员站、HMI 与 SCADA 安全 | `docs/05_Industrial_System/Operator_HMI_SCADA_Security.md` | 监控操作、报警确认、画面脚本与会话安全 | 待编写 |
| 5.4 | 历史数据库与工业数据平台 | `docs/05_Industrial_System/Historian_and_Data_Platform.md` | 采集、压缩、归档、查询、同步与数据完整性 | 待编写 |
| 5.5 | RTU、IED 与远程站 | `docs/05_Industrial_System/RTU_IED_Remote_Station.md` | 电力/管线远程控制、遥测遥控、通信环境 | 待编写 |
| 5.6 | 工业网关与安全设备 | `docs/05_Industrial_System/Industrial_Gateway_and_Security_Appliance.md` | 协议网关、防火墙、网闸、审计与管理面 | 待编写 |
| 5.7 | 补丁、固件与生命周期管理 | `docs/05_Industrial_System/Patch_Firmware_Lifecycle.md` | 兼容性、停机窗口、签名、回滚、EOL | 待编写 |
| 5.8 | 工业主机安全加固基线 | `docs/05_Industrial_System/System_Hardening_Baseline.md` | 账户、服务、应用白名单、日志、备份与恢复 | 待编写 |

## 九、第六篇：工控 Web 与应用安全

| 编号 | 章节 | 目标文件 | 核心范围 | 状态 |
| --- | --- | --- | --- | --- |
| 6.1 | Web 安全基础与工控映射 | `docs/06_Web_Security/Web_Vulnerability_Basics.md` | HTTP、会话、输入、权限、数据层与工控场景 | 待编写 |
| 6.2 | SQL 注入与数据层风险 | `docs/06_Web_Security/SQL_Injection.md` | 注入根因、历史库/点表/配方、下游影响 | 待编写 |
| 6.3 | 文件上传、WebShell 与工程文件 | `docs/06_Web_Security/File_Upload_WebShell.md` | 上传链路、执行条件、项目文件和主机边界 | 待编写 |
| 6.4 | 命令注入与远程代码执行 | `docs/06_Web_Security/RCE_Command_Injection.md` | 系统调用、服务权限、设备管理命令与后果 | 待编写 |
| 6.5 | 身份认证、越权与访问控制 | `docs/06_Web_Security/Access_Control_Auth_Bypass.md` | 会话、角色、对象授权、站点隔离与审计 | 待编写 |
| 6.6 | SSRF 与内部网络访问 | `docs/06_Web_Security/SSRF_Internal_Pivot.md` | 服务端请求、内网资源、云/设备管理接口 | 待编写 |
| 6.7 | 工业设备 Web 管理面风险 | `docs/06_Web_Security/ICS_Web_Management_Risks.md` | 网关、HMI、安全设备、遗留组件与默认配置 | 待编写 |
| 6.8 | 从 Web 漏洞到物理过程影响 | `docs/06_Web_Security/Web_To_ICS_Impact.md` | 条件链、配置发布、控制路径、联锁与证据 | 待编写 |

## 十、第七篇：逆向工程与固件分析

| 编号 | 章节 | 目标文件 | 核心范围 | 状态 |
| --- | --- | --- | --- | --- |
| 7.1 | 逆向工程基础与工作流 | `docs/07_Reverse_Engineering/Reverse_Engineering_Basics.md` | 静态/动态分析、样本管理、证据与工具链 | 待编写 |
| 7.2 | 汇编、调用约定与调试基础 | `docs/07_Reverse_Engineering/Assembly_Debugging_Basics.md` | 寄存器、栈、函数、分支、调试与崩溃定位 | 待编写 |
| 7.3 | Windows PE 与系统接口 | `docs/07_Reverse_Engineering/Windows_PE_Basics.md` | PE 结构、导入导出、加载、API 与保护机制 | 待编写 |
| 7.4 | IDA 与 Ghidra 分析方法 | `docs/07_Reverse_Engineering/IDA_Ghidra_Workflow.md` | 函数识别、交叉引用、类型恢复、注释与验证 | 待编写 |
| 7.5 | 工业固件提取与分析 | `docs/07_Reverse_Engineering/Firmware_Analysis.md` | 固件来源、文件系统、服务、配置、签名与更新 | 待编写 |
| 7.6 | 工业协议逆向 | `docs/07_Reverse_Engineering/Protocol_Reverse_Engineering.md` | 客户端/服务端、抓包、差分、状态机和字段验证 | 待编写 |
| 7.7 | PLC 程序与工程文件逆向 | `docs/07_Reverse_Engineering/PLC_Program_Reverse_Engineering.md` | 工程格式、程序块、变量、保护与过程语义 | 待编写 |

## 十一、第八篇：漏洞研究与 CVE 实践

| 编号 | 章节 | 目标文件 | 核心范围 | 状态 |
| --- | --- | --- | --- | --- |
| 8.1 | 漏洞研究完整工作流 | `docs/08_Vulnerability_Research/Vulnerability_Research_Workflow.md` | 目标选择、攻击面、验证、根因、影响与披露 | 待编写 |
| 8.2 | CVE、CWE 与 CVSS 分析 | `docs/08_Vulnerability_Research/CVE_Analysis_Method.md` | 编号体系、弱点分类、评分、公告与适用范围 | 待编写 |
| 8.3 | PoC 复现方法与安全边界 | `docs/08_Vulnerability_Research/PoC_Reproduction_Methodology.md` | 环境、版本、触发、证据、清理与失败分析 | 待编写 |
| 8.4 | 模糊测试与接口测试基础 | `docs/08_Vulnerability_Research/Fuzzing_and_Testing_Basics.md` | 输入模型、语料、监控、崩溃去重与风险控制 | 待编写 |
| 8.5 | 补丁对比与根因分析 | `docs/08_Vulnerability_Research/Patch_Diffing_and_Root_Cause.md` | 版本差异、代码路径、修复机制与旁路验证 | 待编写 |
| 8.6 | 工控 CVE 的物理影响分析 | `docs/08_Vulnerability_Research/ICS_CVE_Impact_Analysis.md` | 资产角色、利用条件、控制链与安全屏障 | 待编写 |
| 8.7 | 漏洞报告与负责任披露 | `docs/08_Vulnerability_Research/Vulnerability_Report_Writing.md` | 证据、影响、复现、修复、厂商沟通与公开边界 | 待编写 |

## 十二、第九篇：工控安全体系与安全评估

| 编号 | 章节 | 目标文件 | 核心范围 | 状态 |
| --- | --- | --- | --- | --- |
| 9.1 | 工控威胁模型 | `docs/09_Industrial_Security/ICS_Threat_Model.md` | 资产、对手、入口、信任边界、后果与假设 | 待编写 |
| 9.2 | 控制闭环攻击分析 | `docs/09_Industrial_Security/Attack_Control_Loop.md` | 感知、控制、执行、反馈、隐蔽与物理后果 | 待编写 |
| 9.3 | 纵深防御体系 | `docs/09_Industrial_Security/Defense_in_Depth.md` | 架构、身份、主机、网络、监测、恢复与安全屏障 | 待编写 |
| 9.4 | IEC 62443 核心框架 | `docs/09_Industrial_Security/IEC62443_Overview.md` | 角色、生命周期、区域通道、安全等级与要求 | 待编写 |
| 9.5 | MITRE ATT&CK for ICS | `docs/09_Industrial_Security/MITRE_ATTCK_ICS.md` | 战术技术、检测映射、场景建模与模型局限 | 待编写 |
| 9.6 | Stuxnet 与 TRITON 案例 | `docs/09_Industrial_Security/Stuxnet_TRITON_Case_Study.md` | 攻击链、控制/安全系统、隐蔽、后果与启示 | 待编写 |
| 9.7 | 工控安全评估方法 | `docs/09_Industrial_Security/Security_Assessment_Methodology.md` | 范围、资产、访谈、配置、流量、风险与报告 | 待编写 |
| 9.8 | 工控事件响应与恢复 | `docs/09_Industrial_Security/Incident_Response_and_Recovery.md` | 安全生产优先、隔离、取证、恢复与复盘 | 待编写 |

## 十三、第十篇：安全工具开发

| 编号 | 章节 | 目标文件 | 核心范围 | 状态 |
| --- | --- | --- | --- | --- |
| 10.1 | Python Socket 工具开发 | `docs/10_Tool_Development/Python_Socket_Tooling.md` | TCP/UDP、超时、重试、并发、日志与安全默认值 | 待编写 |
| 10.2 | pymodbus 与协议验证工具 | `docs/10_Tool_Development/Pymodbus_Tooling.md` | 客户端、模拟服务、读写验证与隔离实验 | 待编写 |
| 10.3 | Scapy 构包与协议实验 | `docs/10_Tool_Development/Scapy_Packet_Crafting.md` | 分层构包、解析、校验、发送边界与复现 | 待编写 |
| 10.4 | PCAP 解析与工业流量摘要 | `docs/10_Tool_Development/PCAP_Parsing.md` | 会话、字段、统计、状态与过程变量映射 | 待编写 |
| 10.5 | 通信矩阵自动生成 | `docs/10_Tool_Development/Communication_Matrix_Generator.md` | 资产、方向、端口、协议、频率与白名单建议 | 待编写 |
| 10.6 | 报告自动化与证据引用 | `docs/10_Tool_Development/Report_Automation.md` | 数据模型、模板、截图、哈希、结果复核 | 待编写 |
| 10.7 | 工具项目工程化 | `docs/10_Tool_Development/Tool_Project_Portfolio.md` | CLI、配置、测试、文档、发布与作品集表达 | 待编写 |

## 十四、第十一篇：AI 辅助安全研究

| 编号 | 章节 | 目标文件 | 核心范围 | 状态 |
| --- | --- | --- | --- | --- |
| 11.1 | AI 辅助工控研究工作流 | `docs/11_AI_for_Security/AI_Workflow_for_ICS_Research.md` | 任务拆分、资料整理、验证闭环与人工决策 | 待编写 |
| 11.2 | AI 辅助代码审计 | `docs/11_AI_for_Security/AI_Code_Audit.md` | 数据流、危险函数、误报、验证与修复建议 | 待编写 |
| 11.3 | AI 辅助协议分析 | `docs/11_AI_for_Security/AI_Protocol_Analysis.md` | 字段假设、流量对照、状态机与实验验证 | 待编写 |
| 11.4 | AI 辅助漏洞研究 | `docs/11_AI_for_Security/AI_Assisted_Vulnerability_Research.md` | 情报、根因、PoC 理解、证据与安全边界 | 待编写 |
| 11.5 | AI 辅助报告生成 | `docs/11_AI_for_Security/AI_Report_Generation.md` | 结构化输入、事实引用、一致性与人工复核 | 待编写 |
| 11.6 | AI 能力边界与验证原则 | `docs/11_AI_for_Security/Limitations_and_Verification.md` | 幻觉、时效、隐私、授权、复现与审计 | 待编写 |

## 十五、第十二篇：研究项目与作品集

项目篇不追求继续增加知识点，而是把前面章节转化为可展示证据。

| 编号 | 项目 | 目标文件 | 核心产出 | 状态 |
| --- | --- | --- | --- | --- |
| 12.1 | OpenPLC + Modbus + PID 隔离实验 | `docs/12_Research_Projects/Project_OpenPLC_Modbus_PID_Lab.md` | 拓扑、控制逻辑、流量、异常实验、物理影响 | 待编写 |
| 12.2 | Modbus 流量分析器 | `docs/12_Research_Projects/Project_Modbus_Traffic_Analyzer.md` | 解析器、PCAP、功能码、异常检测、报告 | 待编写 |
| 12.3 | 工控 CVE 复现项目 | `docs/12_Research_Projects/Project_ICS_CVE_Reproduction.md` | 环境、根因、复现、影响、修复与披露边界 | 待编写 |
| 12.4 | 工控安全评估样例 | `docs/12_Research_Projects/Project_Security_Assessment_Report.md` | 资产、拓扑、风险、证据、整改和复测 | 待编写 |
| 12.5 | GitHub 作品集组织与展示 | `docs/12_Research_Projects/Project_Portfolio_Readme_Guide.md` | README、截图、演示、证据与面试表达 | 待编写 |

## 十六、第十三篇：面试表达与求职准备

| 编号 | 章节 | 目标文件 | 核心范围 | 状态 |
| --- | --- | --- | --- | --- |
| 13.1 | 自我介绍与转型叙事 | `docs/13_Interview/Self_Introduction.md` | 自动化背景、工控安全动机、能力证据与版本 | 待编写 |
| 13.2 | 项目经历故事库 | `docs/13_Interview/Project_Experience_StoryBank.md` | STAR、问题、动作、证据、结果与反思 | 待编写 |
| 13.3 | 技术面试核心问答 | `docs/13_Interview/Technical_QA_100.md` | 自动化、网络、协议、漏洞、评估和工具 | 待编写 |
| 13.4 | HR 与行为面试 | `docs/13_Interview/HR_QA.md` | 动机、优缺点、冲突、薪资、稳定性与规划 | 待编写 |
| 13.5 | 简历项目描述 | `docs/13_Interview/Resume_Bullets.md` | 动词、技术路径、量化结果与真实性边界 | 待编写 |
| 13.6 | 模拟面试与复盘 | `docs/13_Interview/Mock_Interview_Checklist.md` | 题目抽取、计时、追问、评分与补强闭环 | 待编写 |

## 十七、附录与辅助内容

以下文件不作为核心章节单独排期，在对应篇章完成后由 Codex 汇总维护：

- 各目录的 `README.md`：篇章简介、阅读顺序与导航；
- 各目录的 `Glossary.md`：术语、缩写与易混淆概念；
- 各目录的 `Interview_QA.md`：从正文抽取的专项问答；
- `Learning_Map.md`、`Reading_Guide.md`：学习依赖与阅读路径；
- `Practice_Checklist.md`、`Asset_Interview_Checklist.md`：实操和现场访谈检查表；
- `Risk_Case_Studies.md`：跨章节案例汇总；
- `Project_Style_Interview_Stories.md`：把技术内容转化为项目表达。

## 十八、推荐建设批次

为了让后续章节互相引用且避免返工，建议按以下批次推进：

### 批次 A：控制与现场基础

`2.1 → 2.2 → 2.3 → 2.4 → 2.5 → 2.6 → 2.7 → 2.9 → 2.11 → 2.12 → 2.13`

### 批次 B：网络与协议

`1.4 → 1.5 → 3.1 → 3.2 → 3.3 → 3.5 → 3.7 → 4.1 → 4.2 → 4.3 → 4.4 → 4.5`

### 批次 C：资产与应用攻击面

`5.1 → 5.2 → 5.3 → 5.4 → 5.6 → 6.1 → 6.2 → 6.3 → 6.4 → 6.5 → 6.6 → 6.8`

### 批次 D：逆向与漏洞研究

`7.1 → 7.2 → 7.3 → 7.4 → 7.5 → 7.6 → 8.1 → 8.2 → 8.3 → 8.5 → 8.6 → 8.7`

### 批次 E：体系、工具与作品集

`9.1 → 9.2 → 9.3 → 9.4 → 9.7 → 9.8 → 10.1 → 10.4 → 10.5 → 12.1 → 12.2 → 12.3 → 12.4`

### 批次 F：面试收口

在核心技术篇和至少三个项目完成后，再集中建设第十三篇，并从已校验正文抽取问答，避免先写空泛面试答案。

## 十九、下一章

建议从 **2.1 工业自动化系统全景** 开始。它将定义后续章节反复使用的系统层级、设备角色、数据流、控制流和状态流，也是协议、安全风险和物理影响分析的共同起点。
