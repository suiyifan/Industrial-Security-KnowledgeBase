# Wireshark 抓包基础

## 1. Wireshark 是什么

Wireshark 是网络抓包和协议分析工具。它可以把网络通信变成一条条可查看的数据包。

对安全学习来说，Wireshark 的意义是：让抽象协议变成证据。

## 2. 为什么工控安全岗位需要 Wireshark

工控安全研究经常需要：

- 分析工业协议报文。
- 判断设备之间是否有异常通信。
- 查看是否存在明文传输。
- 验证 PoC 是否真的发出了预期报文。
- 从流量中发现资产、端口、功能码。

如果你能熟练抓包，面试时讲协议分析会更可信。

## 3. 抓包前要知道什么

### 3.1 网卡

抓包前要选择正确网卡。

常见网卡：

- Wi-Fi 网卡
- 有线网卡
- 虚拟机网卡
- Loopback 回环网卡

如果抓不到包，第一件事就是检查网卡选错了没有。

### 3.2 抓包过滤器和显示过滤器

Wireshark 有两类过滤器：

- Capture Filter：抓包前过滤。
- Display Filter：抓包后显示过滤。

初学阶段建议多用 Display Filter，因为抓包后还能反复调整。

## 4. 常用显示过滤器

### 4.1 按 IP 过滤

```text
ip.addr == 192.168.1.10
```

只显示和这个 IP 相关的流量。

### 4.2 按源 IP 过滤

```text
ip.src == 192.168.1.10
```

### 4.3 按目的 IP 过滤

```text
ip.dst == 192.168.1.10
```

### 4.4 按 TCP 端口过滤

```text
tcp.port == 502
```

### 4.5 按 HTTP 过滤

```text
http
```

### 4.6 按 DNS 过滤

```text
dns
```

### 4.7 按 TCP 握手过滤

```text
tcp.flags.syn == 1
```

只看 SYN 包。

## 5. 如何观察 TCP 三次握手

过滤：

```text
tcp
```

找到连续三条：

```text
SYN
SYN, ACK
ACK
```

观察字段：

- Source
- Destination
- Source Port
- Destination Port
- Flags
- Sequence Number
- Acknowledgment Number

## 6. 如何观察 DNS

过滤：

```text
dns
```

重点看：

- Query Name：查询的域名
- Query Type：A、AAAA、CNAME 等
- Response：返回的 IP

## 7. 如何观察 HTTP

过滤：

```text
http
```

重点看：

- Request Method
- Host
- URI
- Status Code
- User-Agent
- Cookie

如果是 HTTPS，内容会被加密，通常看不到具体请求路径和参数，只能看到连接信息、域名线索和证书相关信息。

## 8. 如何观察 Modbus TCP

过滤：

```text
tcp.port == 502
```

如果 Wireshark 识别出 Modbus，可以直接看到 Modbus 字段。

重点看：

- Transaction ID
- Unit ID
- Function Code
- Register Address
- Quantity

安全分析要关注：

- 是否存在写寄存器操作。
- 是否有异常频繁请求。
- 是否有未知主机访问 PLC。
- 是否存在未授权读取。

## 9. Follow TCP Stream

右键某个 TCP 包，选择：

```text
Follow -> TCP Stream
```

用途：

- 查看一次 TCP 会话完整内容。
- 分析 HTTP 请求和响应。
- 看明文协议交互。

工控协议是二进制时，Follow TCP Stream 也能帮助观察原始字节。

## 10. 导出证据

实验报告中可以保存：

- 关键截图
- 过滤器
- 数据包编号
- 请求与响应摘要
- PCAP 文件

注意：公开作品集中不要上传包含真实敏感信息的 PCAP。

## 11. 本章实践

### 练习 1：抓 ping

1. 打开 Wireshark。
2. 开始抓包。
3. 执行 `ping 8.8.8.8`。
4. 使用过滤器 `icmp`。
5. 找到 Echo Request 和 Echo Reply。

### 练习 2：抓 DNS

1. 清空浏览器缓存或换一个新域名。
2. 打开网页。
3. 使用过滤器 `dns`。
4. 找到域名查询和解析结果。

### 练习 3：抓 HTTP

访问一个 HTTP 测试站点，使用过滤器：

```text
http
```

记录：

- 请求方法
- Host
- URI
- 状态码

### 练习 4：抓 TCP 三次握手

使用过滤器：

```text
tcp.flags.syn == 1
```

观察 SYN 和 SYN, ACK。

## 12. 面试表达

可以这样说：

> 我会用 Wireshark 辅助协议分析。通常先根据 IP 和端口过滤流量，再确认 TCP 连接过程，最后查看应用层字段。比如分析 Modbus TCP 时，我会过滤 `tcp.port == 502`，观察功能码、Unit ID 和寄存器读写行为。
