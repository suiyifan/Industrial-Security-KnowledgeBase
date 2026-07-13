# Linux 系统管理与安全分析

Linux 广泛运行于工业网关、边缘计算节点、历史数据平台、安全设备、容器主机和研究工具环境。成熟工程师掌握的不是一张命令速查表，而是 Linux 的对象模型：启动单元、用户身份、文件与挂载、进程线程、Socket、命名空间、日志和审计之间如何关联。命令只是观察和改变这些对象的接口。

## 学习目标

- 理解 Linux 启动、内核、用户空间、systemd 与服务依赖；
- 管理文件、挂载、用户、权限、ACL、Capabilities 与 sudo；
- 调查进程、线程、资源、文件描述符和持久化位置；
- 使用 `ip`、`ss`、`tcpdump`、`nft` 等分析网络状态；
- 使用 journal、传统日志与 audit 建立事件时间线；
- 使用 Shell 管道安全处理文本并自动化证据采集；
- 完成工业 Linux 主机的基线、故障诊断和入侵排查；
- 说明系统异常如何影响协议服务、监控数据和物理过程。

## 1. Linux 系统模型与工作原理

Linux 严格说是内核；发行版还包含启动系统、运行库、Shell、包管理器和应用。用户程序通过系统调用访问内核管理的进程、内存、文件、网络和设备。

```text
应用/服务/容器
  -> glibc 与系统调用
  -> Linux 内核：调度、内存、VFS、网络、驱动、安全模块
  -> CPU、RAM、磁盘、网卡、串口与工业 I/O
```

不同发行版的包管理、默认路径和安全策略不同，嵌入式设备还可能使用 BusyBox、只读根文件系统和厂商定制内核。执行命令前要确认发行版、内核、架构和运行环境。

```bash
uname -a
cat /etc/os-release
uname -m
hostnamectl
```

`uname -r` 显示运行内核版本，不能单独证明发行版补丁状态；厂商可能回移安全补丁而不改变上游版本号。漏洞判断必须结合发行版公告、包版本和厂商固件信息。

## 2. 启动链与 systemd

典型启动链为：

```text
固件/UEFI -> 引导程序 -> Linux 内核 + initramfs
          -> 根文件系统 -> PID 1 -> 系统服务 -> 业务服务
```

内核日志可提供驱动、设备、文件系统和网络初始化线索：

```bash
dmesg --human
journalctl -k -b
```

生产主机上读取 `dmesg` 可能受权限限制。内核日志出现设备 reset、I/O error 或 OOM 时，应继续关联硬件、进程和业务影响。

### 2.1 systemd 单元

systemd 不只管理服务，还管理 socket、timer、mount、path 和 target 等单元。

```bash
systemctl --failed
systemctl status historian.service
systemctl cat historian.service
systemctl show historian.service
systemctl list-dependencies historian.service
journalctl -u historian.service -b
```

`status` 适合快速观察，`show` 提供机器可读属性，`cat` 显示实际单元及覆盖配置。调查服务要关注：

- `ExecStart` 与实际可执行路径；
- `User`、`Group` 与补充组；
- 环境文件和工作目录；
- 依赖、启动顺序和失败恢复；
- 文件系统、Capabilities、命名空间等沙箱选项；
- Drop-in 覆盖是否改变厂商默认配置。

不要在生产系统直接 `restart` 验证。先确认冗余、维护窗口、依赖、当前连接和安全状态。

## 3. 文件系统、路径与挂载

Linux 将多种文件系统统一挂载到一棵目录树。常见位置：

| 路径 | 典型用途 | 安全关注 |
| --- | --- | --- |
| `/etc` | 系统与服务配置 | 权限、版本、秘密、非授权修改 |
| `/var` | 日志、缓存、数据库、队列 | 容量、写入权限、完整性 |
| `/usr` | 程序与共享资源 | 软件来源、只读保护 |
| `/opt` | 第三方/厂商软件 | 自带库、更新和服务权限 |
| `/run` | 本次启动运行状态 | PID、Socket、临时凭据 |
| `/proc` | 进程与内核视图 | 运行时证据，不是普通磁盘文件 |
| `/sys` | 设备和内核对象视图 | 写入可能改变设备行为 |
| `/dev` | 设备节点 | 串口、磁盘和专用设备权限 |

```bash
findmnt
findmnt -T /var/lib/historian
df -hT
df -i
lsblk -f
du -xhd1 /var
```

`df` 查看文件系统容量，`du` 统计可见文件占用；两者差异可能来自已删除但仍被进程打开的文件、挂载遮蔽或保留空间。inode 耗尽也会导致“磁盘还有空间却无法创建文件”。

### 3.1 链接与路径安全

硬链接指向同一 inode，符号链接保存另一条路径。脚本或高权限服务若在检查路径后再打开，可能遭遇符号链接替换或竞态。外部文件名必须限制在授权根目录，临时文件应使用安全 API 创建。

```bash
ls -li path
readlink -f path
stat path
namei -l /opt/vendor/config/app.conf
```

`namei -l` 可逐级显示路径权限，适合定位某一级目录缺少执行权限的问题。

## 4. 用户、组与身份来源

Linux 使用 UID/GID 作为内核身份，用户名只是映射。账户可能来自本地文件、LDAP、SSSD 或其他 NSS 来源。

```bash
id
id service_account
getent passwd service_account
getent group operators
who
w
last
lastlog
```

`/etc/passwd` 中出现账户不代表能使用密码登录；Shell、密码状态、PAM、SSH 和集中身份策略共同决定认证。`last` 依赖本地记录，日志缺失不能证明没有登录。

### 4.1 文件权限与 ACL

传统模式位分为所有者、组和其他用户的读、写、执行：

```bash
ls -la
stat /opt/vendor/bin/gateway
getfacl /opt/vendor/config
```

目录的读权限允许列出名称，执行权限允许遍历和访问已知名称，写权限允许创建/删除目录项。不能用文件权限语义机械解释目录。

ACL 可提供更细权限。排查时如果模式位看似拒绝但访问仍成功，应检查 ACL、组、Capabilities、挂载选项和进程实际身份。

### 4.2 SUID、SGID 与粘滞位

SUID 可让可执行文件以文件所有者有效 UID 运行；SGID 对程序或目录有不同作用；粘滞位常用于共享目录限制删除他人文件。

```bash
find / -xdev -perm -4000 -type f 2>/dev/null
find / -xdev -perm -2000 -type f 2>/dev/null
```

这些命令用于授权基线和排查，不应把所有 SUID 文件判为恶意。重点是与批准基线比较、确认来源、版本和是否可被低权限输入影响。

### 4.3 sudo 与最小权限

```bash
sudo -l
visudo -c
```

sudo 规则中的通配符、可编辑脚本、环境变量、解释器和允许调用外部命令的程序可能扩大权限。服务运维应授予具体动作，而不是方便地开放完整 Shell。

### 4.4 Linux Capabilities

Capabilities 把 root 权限拆分为细粒度能力：

```bash
getcap -r / 2>/dev/null
capsh --print
getpcaps <pid>
```

例如绑定低端口、管理网络和读取受限文件对应不同能力。能力配置错误仍可能接近完整 root 风险，需结合程序功能分析。

## 5. 进程、线程与运行环境

```bash
ps -eo pid,ppid,user,lstart,stat,comm,args --forest
pstree -ap
top
pidstat -p <pid> 1
```

关键字段包括 PID、父 PID、用户、启动时间、状态、命令名和完整命令行。`ps aux` 是快照；CPU 瞬时为 0 不代表进程长期空闲。

常见进程状态：运行/可运行、可中断睡眠、不可中断睡眠、停止和僵尸。大量 `D` 状态进程常指向 I/O 等待；僵尸表示父进程尚未回收退出状态，不等于进程仍在执行。

### 5.1 `/proc` 进程视图

```bash
readlink -f /proc/<pid>/exe
tr '\0' ' ' < /proc/<pid>/cmdline
cat /proc/<pid>/status
cat /proc/<pid>/limits
ls -l /proc/<pid>/fd
cat /proc/<pid>/maps
```

可执行文件被替换或删除后，`/proc/<pid>/exe` 仍指向进程实际映像并可能显示 `(deleted)`。调查应保留哈希、路径、映射和启动来源。

### 5.2 打开文件与库

```bash
lsof -p <pid>
lsof +L1
ldd /opt/vendor/bin/gateway
cat /proc/<pid>/maps
```

`lsof +L1` 可寻找已删除但仍打开的文件，常用于解释磁盘空间差异。不要对不可信可执行文件直接运行可能触发其代码的分析命令；`ldd` 对未知样本需谨慎，优先使用静态解析工具。

### 5.3 资源与性能

```bash
free -h
vmstat 1
iostat -xz 1
pidstat -rud -p <pid> 1
ulimit -a
```

Linux 会把空闲内存用于缓存，`free` 中不能只看 `free` 列，应结合 `available`、交换、缺页和业务指标。高 load average 不只来自 CPU，也可能来自不可中断 I/O 等待。

## 6. 信号、作业与进程控制

信号用于通知进程发生事件。`SIGTERM` 请求优雅终止，`SIGKILL` 无法被捕获，可能跳过清理和数据落盘。

```bash
kill -TERM <pid>
kill -HUP <pid>
systemctl kill --signal=SIGTERM service
```

信号语义由应用决定，`SIGHUP` 不一定都表示重载。生产服务优先使用受支持的服务管理命令和厂商流程，避免直接强杀导致历史库、工程项目或配方损坏。

## 7. 软件包、程序与供应链

根据发行版使用包管理器查询安装来源和文件归属：

```bash
# Debian/Ubuntu
dpkg -l
dpkg -S /usr/bin/ssh
apt-cache policy openssh-server

# RHEL 系
rpm -qa
rpm -qf /usr/bin/ssh
rpm -V <package>
```

包数据库验证是线索，不覆盖 `/opt` 中的厂商软件、运行时生成文件或被攻击者同时修改的数据库。固件设备还可能没有标准包管理器。

```bash
file /opt/vendor/bin/gateway
sha256sum /opt/vendor/bin/gateway
readelf -h /opt/vendor/bin/gateway
strings -a /opt/vendor/bin/gateway
```

哈希用于同版本比对，不能单独判断善恶。应结合可信发布物、签名、版本、构建来源和运行行为。

## 8. 网络配置与路由

### 8.1 地址、链路、路由和邻居

```bash
ip -br link
ip -br address
ip route show table all
ip rule
ip neigh
ip route get 192.168.20.15
```

`ip route get` 显示内核对具体目标的选路结果，包括出口接口和源地址。多网卡工程站要特别检查策略路由、错误默认网关和转发状态，避免形成办公网到控制网的非预期通道。

### 8.2 Socket 与端口

```bash
ss -lntup
ss -tanp
ss -s
lsof -nP -i
```

监听项应同时看本地地址、端口、协议、进程和网络命名空间：`0.0.0.0:502` 表示所有 IPv4 接口监听，不等于互联网必然可达；仍受路由、防火墙和上游边界控制。

连接状态要结合应用理解。大量 `SYN-RECV` 可能是扫描、丢包或负载问题；大量 `CLOSE-WAIT` 常说明应用没有及时关闭已被对端终止的连接。

### 8.3 DNS 与名称解析

```bash
getent hosts hostname
resolvectl status
dig hostname
cat /etc/nsswitch.conf
```

应用的名称解析结果未必与直接 `dig` 相同，因为 NSS 还可能查询 `/etc/hosts`、mDNS 或目录服务。排查应使用与应用一致的解析路径。

### 8.4 防火墙与转发

```bash
nft list ruleset
sysctl net.ipv4.ip_forward
```

现代系统优先使用 nftables，也可能存在 iptables 兼容层或厂商管理程序。读取规则前确认后端，避免看到一套空规则便认定没有防火墙。

规则分析要考虑 hook、表、链、优先级、接口、连接状态、NAT 和默认策略。生产修改必须保留带外管理、回滚方案和变更审批。

## 9. 抓包与网络诊断

```bash
ping -c 4 192.168.10.20
tracepath 192.168.10.20
tcpdump -D
tcpdump -ni any 'host 192.168.10.20 and tcp port 502'
ethtool <interface>
ip -s link show <interface>
```

`ping` 失败不证明设备不存在；`tcpdump -i any` 便于看本机所有接口，但链路层信息和重复观测需注意。长期采集应设置滚动文件、容量和权限：

```bash
tcpdump -ni <interface> -s 0 -C 100 -W 10 -w capture.pcap
```

主动扫描生产控制网可能影响老旧设备。优先使用现有流量、交换机镜像、日志与明确的单目标诊断。

## 10. 日志、journal 与时间

### 10.1 systemd journal

```bash
journalctl -b
journalctl -b -1
journalctl -u gateway.service --since '2026-07-14 08:00:00'
journalctl -p warning..alert
journalctl -o json
```

日志查询要记录时区、启动编号和时间范围。`journalctl -b -1` 是否可用取决于持久化配置。日志没有记录可能是服务未写、级别过滤、轮转、存储损坏或攻击者清理。

### 10.2 传统日志与轮转

常见日志位于 `/var/log`，具体文件随发行版和服务变化。使用 `logrotate` 管理轮转。调查时同时检查当前文件、压缩历史、journal、远程日志和应用自有目录。

```bash
find /var/log -maxdepth 2 -type f -printf '%TY-%Tm-%Td %TT %p\n' | sort
zgrep -i 'failed' /var/log/auth.log*
```

### 10.3 时间同步

```bash
timedatectl
chronyc tracking
chronyc sources -v
```

跨设备取证必须确认时区、NTP 源和偏差。墙上时间跳变可能造成日志乱序，持续时间分析应优先使用单调时钟或应用指标。

## 11. Linux Audit 与安全事件

audit 子系统可记录特定系统调用和对象访问：

```bash
auditctl -s
ausearch -m USER_LOGIN --start today
ausearch -f /opt/vendor/config/app.conf
aureport --auth
```

审计规则应围绕关键配置、身份与高风险操作设计。全量审计会制造巨大数据和性能负担。audit 日志证明内核记录了事件，不自动证明业务操作成功；还需结合应用与过程状态。

## 12. Shell、管道与文本处理

Shell 将命令、参数、重定向和管道组织成流程。管道把前一程序标准输出连接到后一程序标准输入：

```bash
journalctl -u gateway.service --since today |
  grep -F 'connection failed' |
  sort |
  uniq -c
```

常用文本工具：

| 工具 | 典型用途 | 注意点 |
| --- | --- | --- |
| `grep` | 按模式筛选 | 固定字符串用 `-F`；正则需正确转义 |
| `awk` | 字段处理与统计 | 不要假设含空格字段永远固定列 |
| `sed` | 流式替换 | 修改文件前保留证据副本 |
| `cut` | 简单定界字段 | 不适合复杂 CSV 引号规则 |
| `sort/uniq` | 排序去重统计 | `uniq` 只处理相邻重复项 |
| `xargs` | 将输入转为参数 | 文件名和空格需使用 NUL 分隔 |
| `jq` | JSON 查询 | 先验证输入结构和缺失字段 |

### 12.1 引号、展开与命令注入

变量展开必须使用双引号：

```bash
printf '%s\n' "$value"
```

不要把不可信输入拼接后交给 `eval` 或 `sh -c`。文件遍历使用 NUL 分隔：

```bash
find evidence -type f -print0 | xargs -0 sha256sum
```

脚本建议使用 `set -o errexit -o nounset -o pipefail`，但要理解每项对条件判断和管道的影响，不能机械加入后认为错误处理已完成。

## 13. 计划任务与持久化位置

```bash
systemctl list-timers --all
crontab -l
ls -la /etc/cron.* /var/spool/cron 2>/dev/null
systemctl list-unit-files --state=enabled
```

持久化调查还包括 systemd 单元与 Drop-in、Shell 初始化文件、动态链接器配置、内核模块、容器编排和厂商启动脚本。发现新条目后需确认创建时间、所有者、来源包、签名/哈希和业务变更记录。

## 14. 容器、命名空间与 cgroups

容器共享宿主机内核，通过 namespaces 隔离进程、网络、挂载和身份视图，通过 cgroups 限制资源。容器不是虚拟机，也不是天然安全边界。

```bash
lsns
cat /proc/<pid>/cgroup
nsenter -t <pid> -n ip address
systemd-cgls
```

主机上的端口可能由容器发布，进程看到的 PID 和网络接口也可能不同。调查必须确认对象属于宿主机还是哪个命名空间，避免把容器内部 `127.0.0.1` 当作宿主回环服务。

## 15. MAC、SELinux 与 AppArmor

传统 DAC 根据所有者和模式位授权，强制访问控制（MAC）可进一步限制即使 UID 允许的操作。

```bash
getenforce
sestatus
ls -Z /opt/vendor
aa-status
```

SELinux 拒绝通常记录 AVC，AppArmor 按配置文件限制路径与能力。排障不应直接永久关闭强制访问控制，而应确认策略、标签、期望行为和最小例外。

## 16. 工业 Linux 主机加固与防护

### 16.1 资产与服务最小化

- 记录硬件、内核、发行版、厂商软件、服务、端口与依赖；
- 禁用非必要服务、编译器和远程管理入口；
- 管理面绑定专用接口，通过堡垒机与受控路径访问；
- 查询、采集、发布和维护使用不同服务身份；
- 对 `/opt` 厂商程序、配置和证书建立哈希与版本基线。

### 16.2 SSH 安全

```bash
sshd -T
ssh-keygen -lf /etc/ssh/ssh_host_ed25519_key.pub
```

使用 `sshd -T` 查看有效配置，而不是只读单个配置文件。关键项包括允许用户/组、认证方式、root 登录、转发、空闲超时和日志。修改前保留当前会话与回滚路径，避免远程锁死。

### 16.3 文件系统和内核策略

按业务评估只读挂载、`nodev`、`nosuid`、`noexec`，但 `noexec` 不是完整执行阻断。使用 sysctl 加固前确认厂商支持和网络需求：

```bash
sysctl --system
sysctl -a
```

不要直接套用互联网服务器基线到实时或嵌入式设备；每项控制都需验证兼容性和安全生产影响。

### 16.4 补丁、备份与恢复

补丁前确认固件/软件矩阵、冗余、停机窗口、快照或备份、回滚和功能测试。备份必须包含配置、证书、服务单元、应用数据和恢复文档，并实际演练恢复。

## 17. 事件排查方法

### 17.1 先保全现场

生产事件首先确认人员与过程安全，再决定隔离。不要立即关机、删除文件或杀进程，因为这会丢失内存、连接和时间线证据。所有采集动作都要记录执行时间、人员、命令和输出位置。

### 17.2 快速状态采集

在授权情况下，可围绕以下对象采集：

```bash
date --iso-8601=seconds
uptime
who
ps -eo pid,ppid,user,lstart,stat,comm,args --forest
ss -tanup
ip address
ip route
findmnt
df -hT
systemctl --failed
journalctl --since '1 hour ago'
```

输出应写入受控证据目录并计算哈希。命令本身会改变访问时间、缓存和日志，因此报告必须披露采集影响。

### 17.3 分析顺序

1. 校准系统时间与事件时间；
2. 识别新增用户、登录、sudo 与 SSH 活动；
3. 建立进程树、服务、命令行和可执行来源；
4. 将监听端口和连接映射到进程；
5. 检查定时任务、服务、启动脚本等持久化；
6. 比对关键配置、程序哈希和包完整性；
7. 关联应用日志、数据库、PCAP、PLC 事件与现场趋势；
8. 区分已验证事实、推断和待补证事项。

## 18. 数据流、控制流与状态流

### 数据流

```text
网卡 -> 内核协议栈 -> Socket -> 协议服务 -> 数据库/配置
     -> SCADA/网关 -> PLC 通信 -> 控制变量
```

文件权限、缓冲区、队列、编码和日志都可能改变数据的可用性与可信度。

### 控制流

systemd 启动服务，内核调度线程，网络事件触发协议处理，业务逻辑再读写数据库或下发配置。异常启动项、权限提升或服务账户滥用会改变谁能够触发这条路径。

### 状态流

Linux 服务 `active`、端口 `LISTEN`、协议会话成功、PLC 变量改变和执行器反馈是不同状态。排查必须逐层验证，不能把主机层证据夸大为物理动作。

## 19. 工控场景案例：边缘网关异常外联

被动监测发现某 Linux 边缘网关在非维护时间访问新外部地址。主机调查显示一个由 systemd timer 触发的脚本，以高权限账户执行并从可写目录加载配置。脚本是供应商新增的遥测功能，但未经过现场变更审批，且配置允许普通运维组修改目标地址。

结论不是直接判定恶意软件，而是存在未经批准的跨区外联与权限设计缺陷。整改包括暂停外联、确认供应商用途、限制出站通信、收紧配置权限、以低权限身份运行、记录 timer 与网络基线，并评估网关若被利用是否能接触下游 PLC。

## 20. 安全风险与攻击链

```text
远程管理凭据失陷 -> 登录 Linux 网关 -> 利用 sudo/可写服务配置
-> 获取高权限 -> 修改协议代理或采集配置 -> 重启/等待自动加载
-> 数据或命令跨区传播 -> PLC/SCADA 接收 -> 联锁与反馈决定后果
```

验证攻击链时要收集认证日志、sudo、进程、文件变更、systemd、网络连接、应用日志和过程数据。获得 root 说明主机边界失陷，但最终物理影响仍取决于网关角色、协议权限、PLC 模式和安全屏障。

## 21. 隔离实验

### 实验一：服务与权限

在虚拟机创建低权限服务账户和测试 systemd 服务，限制配置目录读写。使用 `systemctl cat/show`、`id`、`namei -l`、`getfacl` 和 journal 解释一次权限拒绝。

### 实验二：进程、Socket 与抓包

启动本地 TCP 服务，用 `ps`、`/proc`、`ss`、`lsof` 和 `tcpdump` 将 PID、监听端口、连接和报文对应起来。分别模拟端口未监听、应用不响应和主动复位。

### 实验三：日志时间线

执行一组有记录的登录、sudo、文件修改和服务重启操作，使用 journal 与 audit 建立时间线，标注时区、来源和证据局限。

### 实验四：安全基线

采集账户、SUID/SGID、Capabilities、服务、监听端口、timer、软件包和关键文件哈希，形成只读基线。变更一个测试项后验证差异检测。实验不连接生产系统。

## 22. 面试表达

### 60 分回答

我理解 Linux 排查要围绕内核对象，而不是背命令。用户和组决定进程身份，权限、ACL、sudo 和 Capabilities 决定对象访问；systemd 管理服务依赖，`ps`、`/proc` 和 `lsof` 查看进程资源，`ip`、`ss` 和 `tcpdump` 对应网络状态，journal 与 audit 用于事件关联。生产工控主机操作前要评估冗余、实时性和变更影响。

### 90 分回答

遇到工业 Linux 主机异常时，我先确认过程安全和系统时间，再从启动服务、进程身份、可执行来源、文件权限、Socket、路由、防火墙、日志与持久化建立时间线。比如看到 `0.0.0.0:502` 只说明某网络命名空间内所有 IPv4 接口监听，还要确认进程、nftables、上游边界和应用认证。看到 TCP 零窗口也会关联线程、内存和磁盘，避免误判为纯网络故障。若主机被提权，我会继续验证服务是否能修改协议代理或配置、数据是否进入 PLC、联锁与反馈是否阻断，分层描述主机、系统和物理影响。

### 常见追问

**`chmod 777` 能否解决权限问题？** 它只是扩大传统模式位权限，可能制造篡改风险，且不能解决 ACL、SELinux、只读挂载或服务身份问题。应定位具体拒绝路径并授予最小权限。

**端口监听是否代表外部可访问？** 不代表。还要考虑绑定地址、命名空间、路由、本机防火墙、上游 ACL 和应用协议。

**Linux 内存 `free` 很少是否异常？** 不一定。内核会用内存做缓存，应看 available、交换、缺页、OOM 和业务延迟。

**为什么不直接杀掉可疑进程？** 生产安全、依赖与证据都可能受影响。应先确认过程风险，采集必要状态，再按响应计划隔离和处置。

## 本章总结

Linux 安全能力建立在系统模型上：身份运行进程，进程持有文件与 Socket，systemd 管理服务，内核管理资源和网络，日志记录部分状态变化。命令的价值是观察这些关系。成熟工控安全工程师既能从输出定位主机根因，也能沿数据流、控制流和状态流判断异常是否传播到控制系统与物理过程。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[C 语言、程序内存与内存安全](C_and_Memory_Safety.md)
- 本章目录：[01_Fundamentals](README.md)
- 下一篇：[Windows 系统管理与安全分析](Windows_System_and_Security.md)
