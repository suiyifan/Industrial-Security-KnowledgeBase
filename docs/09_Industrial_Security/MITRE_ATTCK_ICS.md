# MITRE ATT&CK for ICS

## 1. ATT&CK for ICS 的作用

MITRE ATT&CK for ICS 是描述工控攻击行为的知识库。它的价值是把零散事件和技术动作统一成可沟通语言。

用途：

- 描述攻击阶段。
- 映射检测能力。
- 复盘安全事件。
- 建设攻防演练场景。
- 形成面试表达。

## 2. 常见攻击阶段

工控攻击常见阶段包括：

- Initial Access：初始访问。
- Execution：执行代码或命令。
- Persistence：持久化。
- Privilege Escalation：权限提升。
- Evasion：规避检测。
- Discovery：发现资产和网络。
- Lateral Movement：横向移动。
- Collection：收集项目、配置和数据。
- Command and Control：命令控制。
- Inhibit Response Function：抑制响应功能。
- Impair Process Control：损害过程控制。
- Impact：造成影响。

## 3. 工控特色技术

| 技术方向 | 示例 |
| --- | --- |
| 工程软件滥用 | 使用合法工程软件上传/下载程序 |
| 控制命令下发 | 写寄存器、启停、强制输出 |
| 过程数据伪造 | 修改 HMI 或 Historian 数据 |
| 安全功能抑制 | 禁用报警、旁路联锁 |
| 项目文件收集 | 窃取 PLC 程序、变量表、网络配置 |
| 网络发现 | 扫描 PLC、HMI、网关、OPC 服务器 |

## 4. 防御映射

使用 ATT&CK 时，不要只列技术，还要映射检测：

- 网络检测：异常协议命令、异常功能码、扫描。
- 主机检测：工程软件异常启动、项目文件批量访问。
- 身份检测：非工作时间登录、异常远程维护。
- 设备检测：PLC 模式切换、程序下载、固件升级。
- 操作检测：报警旁路、强制输出、设定值异常变化。

## 5. 面试表达模板

> 我会用 MITRE ATT&CK for ICS 把工控攻击行为结构化。比如攻击者先通过远程维护入口初始访问，再发现生产网资产，收集工程项目，使用合法工程软件连接 PLC，最后下载逻辑或修改设定值。对应防御上，我会映射网络检测、主机审计、身份审计和 PLC 操作审计，而不是只停留在单个漏洞。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[攻击控制回路](Attack_Control_Loop.md)
- 本章目录：[09_Industrial_Security](README.md)
- 下一篇：[Stuxnet 与 TRITON 案例](Stuxnet_TRITON_Case_Study.md)

