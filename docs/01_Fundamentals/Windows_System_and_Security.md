# Windows 系统管理与安全分析

Windows 是工程站、操作员站、SCADA 服务器、历史数据库、域管理和厂商维护工具的常见平台。成熟工控安全工程师不能只会图形界面或零散 PowerShell 命令，而要理解 Windows NT 的对象、访问令牌、服务、注册表、事件日志和网络管理机制，再把主机状态映射到工程操作与物理过程。

## 学习目标

- 理解 Windows 架构、用户态/内核态、对象与句柄；
- 调查进程、线程、服务、计划任务、驱动和启动项；
- 理解 SID、访问令牌、特权、ACL、UAC 与完整性级别；
- 管理 NTFS、注册表、事件日志、PowerShell 和网络状态；
- 识别 SMB、RDP、WinRM、WMI/RPC 与域环境风险；
- 完成工程站和 SCADA 主机的基线、加固与事件排查；
- 区分主机失陷、控制系统影响和物理后果。

## 1. Windows 架构与工作原理

Windows NT 采用用户态和内核态分层。用户态包含应用、服务进程和环境子系统，内核态包含执行体、内核、驱动、硬件抽象层和系统缓存等组件。

```text
工程软件 / HMI / SCADA / 历史服务 / PowerShell
              |
      Win32 API / 系统库
              |
NT 系统调用 -> 内核执行体、对象管理、I/O、内存、安全、网络
              |
          驱动与硬件
```

应用通过句柄引用进程、文件、注册表项、事件和 Socket 等内核对象。句柄只在特定进程上下文中有意义，访问能否成功取决于调用线程的安全上下文和对象访问控制。

```powershell
Get-ComputerInfo
Get-CimInstance Win32_OperatingSystem |
  Select-Object Caption, Version, BuildNumber, LastBootUpTime
```

构建号只是补丁判断的一部分，还应查看累计更新、产品生命周期和厂商兼容性。工控主机不能因为“补丁重要”就绕过测试和维护流程直接更新。

## 2. 启动链、会话与登录

简化启动过程包括固件、Windows Boot Manager、内核、Session Manager、服务控制管理器和登录组件。安全启动可验证启动链签名，但不能替代磁盘加密、补丁和应用控制。

Windows 同时存在服务会话、控制台会话和远程桌面会话。调查“谁登录过”不能只看当前桌面用户：

```powershell
Get-CimInstance Win32_LoggedOnUser
query user
Get-LocalUser
Get-LocalGroupMember Administrators
```

域账户、服务账户、计划任务账户和远程网络登录可能没有交互桌面。事件日志中的登录类型、来源地址和认证包比简单用户名更重要。

## 3. 进程、线程、模块与句柄

```powershell
Get-Process | Sort-Object CPU -Descending |
  Select-Object -First 20 Name, Id, CPU, WorkingSet, StartTime

Get-CimInstance Win32_Process |
  Select-Object ProcessId, ParentProcessId, Name, ExecutablePath, CommandLine
```

进程调查重点包括：PID/PPID、用户、启动时间、命令行、可执行路径、签名、哈希、加载模块、句柄和网络连接。父进程只是来源线索，服务管理、WMI、任务计划和应用更新都会形成不同进程树。

```powershell
Get-AuthenticodeSignature 'C:\Program Files\Vendor\app.exe'
Get-FileHash 'C:\Program Files\Vendor\app.exe' -Algorithm SHA256
```

签名有效证明文件由对应证书签名且内容未在签名后改变，不证明软件没有漏洞或业务用途安全。哈希必须与可信版本、发布介质或基线比较。

### 3.1 进程资源与等待

任务管理器适合快速观察，性能监视器和资源监视器适合长期指标。高 CPU、高提交内存、句柄持续增长、磁盘队列和线程阻塞可能造成 SCADA 卡顿或历史数据缺口。

```powershell
Get-Counter '\Processor(_Total)\% Processor Time'
Get-Counter '\Memory\Available MBytes'
Get-Counter '\PhysicalDisk(_Total)\Avg. Disk Queue Length'
```

计数器名称受系统语言和版本影响。单次采样不足以定性，应结合基线、持续时间和应用日志。

## 4. 服务、驱动与恢复策略

服务由 Service Control Manager 管理，可在系统启动或按需启动，并以指定账户运行。

```powershell
Get-Service | Sort-Object Status, Name
Get-CimInstance Win32_Service |
  Select-Object Name, State, StartMode, StartName, PathName
sc.exe qc VendorService
```

安全检查包括：

- 服务账户是否权限过高；
- 可执行路径是否带引号、目录是否可被低权限用户写入；
- 参数、环境和依赖是否可信；
- 恢复动作是否造成无限重启；
- 服务二进制、DLL 和配置是否有版本基线；
- 驱动是否签名、必要且仍受支持。

不要直接停止未知服务验证影响。工程软件授权、通信驱动、加密狗、历史归档和冗余管理可能依赖它。

```powershell
Get-CimInstance Win32_SystemDriver |
  Select-Object Name, State, StartMode, PathName
driverquery.exe /v
```

驱动在高特权环境运行，缺陷或不兼容可能导致系统崩溃。工控设备驱动更新必须验证厂商矩阵与回滚。

## 5. SID、访问令牌与权限

Windows 用 SID 标识用户、组和安全主体。用户登录后形成访问令牌，其中包含用户 SID、组、特权、完整性级别和限制信息。线程可以模拟其他身份，因此仅查看进程所有者有时不足。

```powershell
whoami /user
whoami /groups
whoami /priv
whoami /all
```

对象的安全描述符包含所有者、DACL 和可选 SACL。DACL 决定允许/拒绝，SACL 用于审计。权限计算还受继承、显式拒绝、组成员和特权影响。

### 5.1 NTFS ACL

```powershell
Get-Acl 'C:\ProgramData\Vendor\Config' | Format-List
icacls.exe 'C:\ProgramData\Vendor\Config'
```

调查配置篡改风险时要逐级检查目录和文件权限，区分读取、写入、修改、删除和更改权限。共享权限与 NTFS 权限同时存在时，网络访问受到两者共同约束。

### 5.2 UAC 与完整性级别

UAC 帮助管理员账户以受限令牌日常运行，在需要时提升。它不是强安全边界，也不能替代独立低权限账户。完整性级别限制低完整性主体写入更高完整性对象，但具体访问仍结合 ACL。

### 5.3 特权与服务账户

调试、备份、恢复、加载驱动和模拟等特权非常敏感。服务账户应采用最小权限、禁止交互登录、受控凭据和明确轮换。采集、查询和配置发布服务不应共享一个高权限账户。

## 6. 文件系统、卷与数据保护

```powershell
Get-Volume
Get-Partition
Get-PSDrive -PSProvider FileSystem
fsutil.exe volume diskfree C:
```

NTFS 支持 ACL、备用数据流、重解析点、压缩、加密和变更日志。路径显示相同不代表对象相同，符号链接、挂载点和 Junction 会改变解析目标。

```powershell
Get-Item 'C:\ProgramData\Vendor\Config' -Force |
  Format-List FullName, Attributes, LinkType, Target
Get-ChildItem 'C:\ProgramData\Vendor' -Force
```

工业项目文件、配方、证书、报警数据库和备份需分别定义保密性、完整性和恢复要求。历史数据盘空间耗尽可能不影响 PLC 闭环，却会造成趋势与审计缺失。

### 6.1 VSS、备份与恢复

卷影复制可支持一致性快照和恢复，但不是离线备份，也可能被攻击者删除。应建立独立备份、访问隔离、完整性验证和恢复演练。

```powershell
vssadmin.exe list shadows
wbadmin.exe get versions
```

读取状态通常安全，创建、删除或恢复操作必须按正式流程执行。

## 7. 注册表与配置状态

注册表是分层配置数据库，常见根包括 HKLM、HKCU、HKCR、HKU 和 HKCC。其内容来自磁盘 hive 与运行时映射。

```powershell
Get-ItemProperty 'HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion'
Get-ChildItem 'HKLM:\SYSTEM\CurrentControlSet\Services'
```

注册表用于服务、驱动、网络、COM、登录和应用配置，是重要持久化与取证来源。读取时要区分 32/64 位视图、当前控制集和具体用户 hive。修改注册表前必须导出备份并确认厂商支持。

## 8. 计划任务与自动执行

```powershell
Get-ScheduledTask |
  Select-Object TaskPath, TaskName, State
Get-ScheduledTaskInfo -TaskName 'TaskName'
schtasks.exe /query /fo LIST /v
```

任务调查关注触发器、动作、运行账户、最高权限、工作目录和脚本路径权限。合法的备份、报表和厂商更新任务可能行为类似持久化，需要与基线和变更记录比对。

常见自动执行位置还包括服务、Run 键、启动目录、WMI 永久事件订阅、登录脚本和 Office/工程软件插件。不能只检查一个注册表路径便声称不存在持久化。

## 9. 网络配置、Socket 与防火墙

### 9.1 地址、路由、邻居和 DNS

```powershell
Get-NetAdapter
Get-NetIPConfiguration
Get-NetIPAddress
Get-NetRoute
Get-NetNeighbor
Get-DnsClientServerAddress
Resolve-DnsName hostname
Test-NetConnection 192.168.10.20 -Port 502
```

多网卡工程站要重点检查默认路由、接口跃点、网络共享、IP 转发和桥接，防止意外连接办公网与控制网。`Test-NetConnection` 是主动连接测试，生产设备必须在授权范围内使用。

### 9.2 端口与进程

```powershell
Get-NetTCPConnection -State Listen |
  Select-Object LocalAddress, LocalPort, OwningProcess
Get-NetUDPEndpoint
netstat.exe -ano
```

将 `OwningProcess` 与进程路径、账户和服务对应。`0.0.0.0` 或 `::` 表示所有相应接口监听，不等于跨区必然可达，还受 Windows 防火墙、路由和上游 ACL 影响。

### 9.3 Windows Defender Firewall

```powershell
Get-NetFirewallProfile
Get-NetFirewallRule -Enabled True |
  Select-Object DisplayName, Direction, Action, Profile
```

有效规则还涉及端口、地址、程序、服务和策略来源。域策略可能覆盖本地设置。修改规则必须保留管理通道、导出当前策略并准备回滚。

## 10. SMB、RPC、WMI、RDP 与 WinRM

Windows 管理与文件共享高度依赖这些协议：

| 技术 | 用途 | 主要风险 |
| --- | --- | --- |
| SMB | 文件、命名管道、管理共享 | 凭据、横向移动、共享权限、旧协议 |
| RPC/DCOM | 服务与远程组件调用 | 动态端口、复杂权限、远程管理面 |
| WMI/CIM | 系统查询和管理 | 高权限远程执行、日志与审计 |
| RDP | 交互式远程桌面 | 暴露、弱认证、会话与剪贴板 |
| WinRM | PowerShell 远程管理 | 身份、HTTPS/Kerberos、端点权限 |

```powershell
Get-SmbServerConfiguration
Get-SmbShare
Get-SmbSession
Get-CimInstance Win32_QuickFixEngineering
Get-Service WinRM, TermService
```

不要因为运维方便便允许任意跨区 SMB/RDP。供应商远程访问应通过堡垒机、强认证、审批、限时授权和会话审计。

## 11. PowerShell 的对象管道

PowerShell 管道传递对象而非纯文本：

```powershell
Get-CimInstance Win32_Service |
  Where-Object State -eq 'Running' |
  Select-Object Name, StartName, PathName |
  Export-Csv services.csv -NoTypeInformation -Encoding UTF8
```

这比解析本地化文本可靠。安全脚本应：

- 使用明确参数类型和验证；
- 避免把不可信输入交给 `Invoke-Expression`；
- 使用 `-LiteralPath` 处理外部路径；
- 设置 `$ErrorActionPreference` 或逐命令错误策略；
- 保留结构化输出、错误和退出状态；
- 区分只读采集与状态修改。

```powershell
param(
    [Parameter(Mandatory)]
    [ValidateScript({ Test-Path -LiteralPath $_ -PathType Container })]
    [string]$EvidenceDirectory
)
```

执行策略不是安全边界，不能阻止有能力的攻击者执行代码。应用控制、权限、签名、日志和受控管理路径需共同使用。

## 12. 事件日志与审计

Windows Event Log 按通道组织事件，常见包括 System、Application、Security 和产品专用通道。

```powershell
Get-WinEvent -ListLog * |
  Where-Object RecordCount -gt 0 |
  Select-Object LogName, RecordCount, IsEnabled

Get-WinEvent -FilterHashtable @{
    LogName='System'
    StartTime=(Get-Date).AddHours(-2)
} | Select-Object TimeCreated, Id, ProviderName, LevelDisplayName, Message
```

事件 ID 的含义依赖日志通道、提供程序和版本，不能脱离上下文建立“万能 ID 表”。调查应记录 Provider、Event ID、时间、计算机、用户、活动 ID 和原始 XML。

### 12.1 登录与权限事件

安全日志可记录登录、账户、特权和策略变化，但前提是审计策略已启用且日志未被覆盖。登录事件要关注登录类型、认证包、来源地址、目标用户和关联注销/会话事件。

```powershell
auditpol.exe /get /category:*
wevtutil.exe gli Security
```

### 12.2 PowerShell 日志

在兼容性验证后，可启用模块日志、脚本块日志和转录。日志可能包含敏感参数，必须限制访问并转发到独立平台。日志缺失可能来自未启用、版本差异、绕过或清理。

### 12.3 Sysmon 与扩展遥测

Sysmon 可记录进程创建、网络连接、文件与注册表等事件，但质量取决于配置，部署也需评估性能和数据量。它补充而不是替代原生日志、EDR 和应用审计。

## 13. Windows Defender、应用控制与防护

```powershell
Get-MpComputerStatus
Get-MpPreference
Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct
```

产品状态查询要结合实际企业管理平台。工业主机可能因兼容性设置排除目录或进程，排除范围过大会形成盲区。任何调整都需与厂商、生产和安全团队共同验证。

应用控制可使用 AppLocker 或 Windows Defender Application Control 等机制限制可执行文件、脚本和库。白名单必须覆盖更新、应急和厂商维护流程，并先在审计模式评估。

## 14. Active Directory 与域基础

域为用户、计算机、组和策略提供集中管理。域成员通过 Kerberos/NTLM 等协议认证，并接受组策略。工程站加入企业域、独立工控域或工作组，对攻击路径影响很大。

```powershell
whoami /fqdn
nltest.exe /dsgetdc:example.local
gpresult.exe /r
Get-CimInstance Win32_ComputerSystem |
  Select-Object Domain, PartOfDomain
```

工控域应有明确边界、管理跳板、分层账户和受控信任。办公域管理员不应自动拥有控制系统管理权限。服务账户、共享本地管理员密码和长期不轮换凭据是常见放大因素。

## 15. 软件、补丁与供应链

```powershell
Get-HotFix | Sort-Object InstalledOn -Descending
Get-AppxPackage
Get-ChildItem 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\*' |
  Get-ItemProperty |
  Select-Object DisplayName, DisplayVersion, Publisher
```

安装清单可能不完整：便携程序、驱动、厂商组件和 32/64 位注册表视图需额外检查。补丁评估应同时考虑漏洞、可利用性、资产关键性、兼容性、冗余、维护窗口和补偿控制。

生产主机不直接使用面向互联网环境的“自动升级优先”策略。正确流程是测试、备份、变更、验证和回滚，但也不能以兼容性为由无限期不治理高风险漏洞。

## 16. 持久化与异常调查

授权排查应建立基线后检查：

- 新增或变化的服务和驱动；
- 计划任务及运行账户；
- Run/RunOnce 和启动目录；
- WMI 永久事件订阅；
- 登录脚本、PowerShell 配置和应用插件；
- 新增本地/域管理员、远程桌面用户；
- 可写程序目录、DLL 搜索路径和未签名模块。

```powershell
Get-CimInstance -Namespace root/subscription -Class __EventFilter
Get-CimInstance -Namespace root/subscription -Class CommandLineEventConsumer
Get-CimInstance -Namespace root/subscription -Class __FilterToConsumerBinding
```

这些对象也可能由合法管理工具创建。必须结合创建时间、所有者、命令、签名、变更记录和网络行为判断。

## 17. 工业 Windows 主机加固

### 17.1 角色和服务最小化

- 明确工程站、操作员站、历史服务器和域控制器角色；
- 禁止混用日常办公、邮件、浏览和控制工程任务；
- 禁用不必要 SMB、RDP、WinRM、打印与旧协议；
- 服务使用独立低权限账户，限制交互登录；
- 管理员使用独立管理账户和受控跳板；
- 维护主机、应用、服务、端口、共享和任务基线。

### 17.2 凭据与远程访问

使用强认证、凭据保护、LAPS 类本地管理员密码管理、网络级身份验证和限时访问。禁止在脚本、工程项目或共享目录保存明文密码。剪贴板、磁盘映射和文件传输按业务最小开放。

### 17.3 数据、日志与恢复

工程项目和配方使用版本、审批和离线备份；日志转发到独立位置；关键服务器测试系统状态与应用数据恢复。恢复验证必须包含服务依赖、许可证、通信驱动和现场连接，而不只是 Windows 能启动。

## 18. 事件响应与证据采集

### 18.1 安全生产优先

发现异常时先确认过程状态、冗余、操作权限和安全屏障。立即关机、断网或杀进程可能导致失去操作画面、触发主备切换或丢失易失证据。隔离方案要由生产、安全和厂商共同决策。

### 18.2 只读优先的快速采集

在授权环境中可采集：

```powershell
Get-Date -Format o
Get-ComputerInfo
Get-CimInstance Win32_Process
Get-CimInstance Win32_Service
Get-NetTCPConnection
Get-NetIPConfiguration
Get-ScheduledTask
Get-LocalUser
Get-LocalGroupMember Administrators
Get-WinEvent -FilterHashtable @{LogName='System'; StartTime=(Get-Date).AddHours(-1)}
```

输出保存到受控目录并计算哈希。PowerShell 查询也会产生进程、文件访问和日志，报告应披露采集行为。

### 18.3 时间线关联

将进程创建、登录、服务、任务、文件修改、网络连接、应用日志、数据库审计、SCADA 事件和 PLC/SOE 对齐。先确认时区和时钟偏差，再区分事件发生时间、记录时间和采集时间。

## 19. 数据流、控制流与状态流

### 数据流

```text
网卡/文件/注册表 -> Windows 内核对象 -> SCADA/工程服务
                 -> 数据库/项目配置 -> 工业协议 -> PLC
```

ACL、服务身份、缓存和转换配置决定数据能否读取、修改和传播。

### 控制流

服务控制管理器、计划任务、WMI/RPC 或交互用户启动程序；程序处理输入并通过驱动、数据库或网络调用下游组件。权限提升会改变能触发的控制路径。

### 状态流

进程运行、服务 Running、端口 Listen、应用会话成功、PLC 变量变化和现场反馈各自独立。主机调查结论必须限定到已有证据层级。

## 20. 工控场景案例：工程站项目异常变更

某工程站的 PLC 项目在非维护时段发生版本变化。Windows 调查显示一个供应商远程账户通过 RDP 登录，随后工程软件进程启动并写入项目目录；安全日志与 RDP 日志可对应登录，文件哈希和 Git/项目版本记录确认差异。PLC 事件日志未发现下载操作。

结论是工程项目文件被未授权修改，但没有证据证明变更已下装控制器。响应包括吊销远程会话与凭据、隔离项目副本、比对可信版本、检查工程软件最近项目和通信日志、核对 PLC 在线程序，并收紧远程审批和项目目录权限。

## 21. 安全风险与攻击链

```text
远程凭据失陷 -> RDP/SMB/WinRM 进入工程站
-> 利用管理员组或服务配置获得高权限
-> 修改工程项目/驱动/发布配置 -> 工程软件加载
-> 下装或数据发布到 PLC/SCADA -> 控制逻辑与联锁决定过程后果
```

每一步都需要独立证据。工程站管理员权限代表严重主机失陷，但不能自动证明 PLC 程序已被修改。必须核对工程操作、协议流量、PLC 审计、程序校验和现场状态。

## 22. 隔离实验

### 实验一：令牌与 ACL

在 Windows 虚拟机创建标准用户和测试目录，使用 `whoami /all`、`Get-Acl` 和 `icacls` 分析访问允许/拒绝、继承和组成员影响。

### 实验二：服务、进程与端口

启动本地测试服务，用 `Get-CimInstance`、`Get-Service`、`Get-NetTCPConnection` 和事件日志将服务账户、PID、路径与端口对应。停止服务前创建快照，并只操作实验对象。

### 实验三：事件时间线

执行已记录的登录、文件修改、任务运行和服务启动，导出相关事件 XML，与文件时间和 PowerShell 转录建立时间线。

### 实验四：工程站基线

采集本地管理员、服务、驱动、任务、共享、监听端口、软件、关键文件哈希和日志策略。改变一个测试项后验证差异检测。不得连接真实工程站或 PLC。

## 23. 面试表达

### 60 分回答

Windows 安全排查要围绕进程令牌、服务、文件与注册表 ACL、网络连接和事件日志建立关联。我会用 CIM/PowerShell 查询进程路径和命令行，将端口映射到 PID 和服务，再检查账户、任务、签名、哈希及日志。工程站操作前必须评估生产影响，不能直接停止服务或删除文件。

### 90 分回答

我会把 Windows 工程站看成一条受权限控制的发布链：登录会话形成访问令牌，服务和工程软件以特定身份访问项目、注册表、驱动与网络，再通过工业协议接触 PLC。调查时对齐登录类型、进程树、服务、任务、文件哈希、Socket、PowerShell/应用日志和 PLC 审计。例如项目文件变化只证明主机数据完整性受损，只有发现下装会话、PLC 程序版本变化和在线校验差异，才能确认控制逻辑受影响；最终物理风险还取决于 PLC 模式、联锁和 SIS。

### 常见追问

**UAC 是否等于安全边界？** 不是。它主要帮助管理员以受限令牌工作，仍需独立账户、最小权限和应用控制。

**签名有效是否说明文件安全？** 不说明。签名证明来源和签名后完整性，合法软件也可能有漏洞或被滥用。

**服务显示 Running 是否代表业务正常？** 不代表。还要验证线程、端口、协议、依赖、数据库和业务状态。

**为什么不能看到 RDP 登录就认定攻击成功？** 登录可能合法，必须结合账户、来源、审批、后续进程和变更；即使主机失陷，也要继续验证控制系统操作。

## 本章总结

Windows 安全分析的核心不是工具数量，而是对象与身份关系：账户形成令牌，令牌访问进程、服务、文件、注册表和网络对象，日志记录其中部分状态变化。成熟工控安全工程师要把主机证据继续映射到工程项目、工业协议、PLC 状态和现场反馈，并在任何处置前优先保证生产安全与证据完整。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[Linux 系统管理与安全分析](Linux_Basics.md)
- 本章目录：[01_Fundamentals](README.md)
- 下一篇：[Git、GitHub 与研究证据管理](Git_and_GitHub.md)
