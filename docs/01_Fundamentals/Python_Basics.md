# Python 基础

## 1. Python 在安全岗位中的作用

Python 是安全研究中非常常用的语言。它适合快速写脚本、处理数据、构造网络请求、解析协议、自动化重复任务。

在目标岗位中，Python 可以用于：

- 写端口扫描器。
- 写协议探测工具。
- 解析 PCAP 或日志。
- 批量处理漏洞信息。
- 写 PoC 或辅助复现脚本。
- 自动生成报告中的数据表。

## 2. 初学者要先掌握什么

不用一开始就学复杂框架。先掌握这些：

1. 变量和数据类型
2. 条件判断
3. 循环
4. 函数
5. 文件读写
6. 异常处理
7. 列表、字典、集合
8. 模块和包
9. 命令行参数
10. Socket 网络编程

## 3. 变量与数据类型

变量是给数据起名字。

```python
host = "127.0.0.1"
port = 502
is_open = True
```

常见类型：

| 类型 | 示例 | 说明 |
|---|---|---|
| `str` | `"Modbus"` | 字符串 |
| `int` | `502` | 整数 |
| `float` | `1.5` | 小数 |
| `bool` | `True` | 布尔值 |
| `list` | `[80, 443, 502]` | 列表 |
| `dict` | `{"port": 502}` | 字典 |

## 4. 条件判断

```python
port = 502

if port == 502:
    print("可能是 Modbus TCP")
else:
    print("其他服务")
```

安全工具里经常用条件判断来区分端口、协议、响应状态。

## 5. 循环

```python
ports = [80, 443, 502]

for port in ports:
    print(port)
```

端口扫描器的核心就是循环测试端口。

## 6. 函数

函数用于把重复逻辑封装起来。

```python
def is_modbus_port(port: int) -> bool:
    return port == 502
```

好的函数应该：

- 名字清楚。
- 只做一件事。
- 输入和输出明确。
- 出错时能处理异常。

## 7. 文件读写

读取文件：

```python
with open("targets.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

写入文件：

```python
with open("result.txt", "w", encoding="utf-8") as f:
    f.write("scan finished\n")
```

安全场景：

- 读取目标 IP 列表。
- 写入扫描结果。
- 解析日志文件。
- 生成报告数据。

## 8. 异常处理

网络连接、文件读取都可能失败。异常处理能让程序不至于直接崩溃。

```python
try:
    value = int("abc")
except ValueError:
    print("转换失败")
```

网络工具中常见异常：

- 连接超时
- 目标拒绝连接
- DNS 解析失败
- 权限不足

## 9. 命令行参数

安全工具通常需要从命令行传入目标。

```python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("host")
parser.add_argument("--port", type=int, default=502)
args = parser.parse_args()

print(args.host, args.port)
```

运行方式：

```bash
python tool.py 127.0.0.1 --port 502
```

## 10. Socket 基础

Socket 是程序访问网络的接口。你可以把它理解成“程序里的网线插口”。

最简单的 TCP 连接：

```python
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.settimeout(2)
    result = sock.connect_ex(("127.0.0.1", 80))
    if result == 0:
        print("open")
    else:
        print("closed")
```

关键点：

- `AF_INET`: IPv4
- `SOCK_STREAM`: TCP
- `settimeout`: 设置超时时间
- `connect_ex`: 连接目标，返回状态码

## 11. 与工业协议的关系

Modbus TCP 运行在 TCP 之上，默认端口 502。后续你用 Python 构造 Modbus 请求时，本质上就是：

1. 建立 TCP 连接。
2. 按协议格式拼接 bytes。
3. 发送 bytes。
4. 接收响应 bytes。
5. 按协议字段解析响应。

所以 Python、Socket、bytes 是工业协议开发的基础。

## 12. 本章实践

### 练习 1：端口判断

写一个函数，输入端口号，输出它是否是常见端口。

常见端口：

- 22 SSH
- 80 HTTP
- 443 HTTPS
- 502 Modbus TCP

### 练习 2：读取目标文件

创建 `targets.txt`：

```text
127.0.0.1
192.168.1.1
```

写 Python 逐行读取并打印。

### 练习 3：连接端口

使用 `socket.connect_ex` 测试某个端口是否开放。

## 13. 面试表达

可以这样说：

> 我用 Python 作为安全工具开发的主要语言，重点掌握文件处理、命令行参数、异常处理和 Socket 编程。后续做工控协议研究时，可以用 Python 构造协议报文、探测资产、解析响应，并把结果整理成报告。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[Linux 基础]()
- 本章目录：[01_Fundamentals]()
- 下一篇：[网络基础]()

