# Linux 基础

## 1. Linux 是什么

Linux 是一种操作系统。服务器、安全工具、靶场环境、工业网关、嵌入式设备中都经常能看到 Linux。

对安全学习来说，Linux 不是“可选项”，而是基本工作环境。

## 2. 为什么工控安全岗位需要 Linux

工控安全研究中经常会遇到：

- 在 Linux 上运行安全工具。
- 查看服务端口是否开放。
- 分析日志。
- 部署本地靶场。
- 分析嵌入式固件。
- 连接远程服务器。

如果不会 Linux，很多实验会卡在环境配置阶段。

## 3. 文件系统基础

Linux 文件路径用 `/` 分隔。

常见目录：

| 目录 | 含义 |
|---|---|
| `/home` | 普通用户目录 |
| `/root` | root 用户目录 |
| `/etc` | 配置文件 |
| `/var/log` | 日志文件 |
| `/tmp` | 临时文件 |
| `/usr/bin` | 常见程序 |
| `/opt` | 第三方软件 |

## 4. 常用命令

### 4.1 查看当前位置

```bash
pwd
```

`pwd` 会显示你当前所在目录。

### 4.2 查看文件

```bash
ls
ls -l
ls -la
```

- `ls`: 查看当前目录文件。
- `ls -l`: 显示详细信息。
- `ls -la`: 显示隐藏文件。

### 4.3 切换目录

```bash
cd /etc
cd ~
cd ..
```

- `~` 表示当前用户家目录。
- `..` 表示上一级目录。

### 4.4 查看文件内容

```bash
cat file.txt
less file.txt
head file.txt
tail file.txt
tail -f app.log
```

安全分析中常用 `tail -f` 实时看日志。

### 4.5 创建文件和目录

```bash
mkdir notes
touch notes/today.md
```

### 4.6 复制、移动、删除

```bash
cp a.txt b.txt
mv old.txt new.txt
rm old.txt
```

删除命令要谨慎，尤其是 `rm -rf`。

## 5. 权限基础

Linux 文件权限常见形式：

```text
-rw-r--r--
```

可以拆成三组：

- 所有者权限
- 所属组权限
- 其他用户权限

每组权限：

- `r`: read，读
- `w`: write，写
- `x`: execute，执行

示例：

```bash
chmod +x script.sh
```

含义：给脚本增加执行权限。

## 6. 用户与权限

查看当前用户：

```bash
whoami
```

以管理员权限执行：

```bash
sudo command
```

安全学习中要理解：很多漏洞最终影响的是权限。如果一个 Web 漏洞让攻击者拿到 root 权限，风险远高于普通用户权限。

## 7. 进程与端口

查看进程：

```bash
ps aux
top
```

查看端口：

```bash
ss -tulnp
netstat -tulnp
```

其中：

- `t`: TCP
- `u`: UDP
- `l`: listening，监听中
- `n`: 不做域名解析，直接显示数字
- `p`: 显示进程

## 8. 网络排查命令

查看 IP：

```bash
ip addr
```

查看路由：

```bash
ip route
```

测试连通性：

```bash
ping 8.8.8.8
```

查看 DNS 解析：

```bash
nslookup example.com
dig example.com
```

请求 HTTP：

```bash
curl http://example.com
```

## 9. 日志基础

常见日志位置：

```bash
/var/log/
```

查看认证日志：

```bash
sudo tail -f /var/log/auth.log
```

不同发行版日志文件名可能不同。

## 10. 本章实践

### 练习 1：找出本机 IP

执行：

```bash
ip addr
```

记录：

- 网卡名
- IPv4 地址
- 是否有回环地址 `127.0.0.1`

### 练习 2：找出监听端口

执行：

```bash
ss -tulnp
```

记录：

- 哪些端口正在监听
- 对应哪个进程

### 练习 3：理解权限

创建脚本：

```bash
touch hello.sh
chmod +x hello.sh
ls -l hello.sh
```

观察权限变化。

## 11. 面试表达

可以这样说：

> 我掌握 Linux 的文件、权限、进程、端口和日志基础，能够在安全测试或漏洞复现时完成环境排查。例如我会用 `ss -tulnp` 查看服务监听，用 `tail -f` 跟踪日志，用 `chmod` 和 `sudo` 理解权限变化。
