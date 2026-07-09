# 仿真与工具路线：把理论变成可验证经验

## 1. 目标

本路线用于把控制理论、PLC、协议分析和安全风险串起来。

目标不是“装很多工具”，而是形成一条可展示的验证链：

```text
控制对象仿真
  -> PLC / Runtime
  -> 工业协议变量映射
  -> Python 发包 / 写变量
  -> Wireshark 抓包
  -> PV / MV 变化观察
  -> 安全报告
```

## 2. 推荐工具

| 工具 | 用途 |
|---|---|
| Scilab + Xcos | 免费控制系统仿真 |
| MATLAB + Simulink | 控制理论和 PID 仿真 |
| OpenPLC | 开源 PLC Runtime |
| CODESYS | PLC 编程与仿真 |
| Factory I/O | 工业现场仿真 |
| PLCSIM | 西门子 PLC 仿真 |
| Wireshark | 抓包分析 |
| Python socket | 自定义协议交互 |
| pymodbus | Modbus 读写 |
| Scapy | 报文构造与解析 |

## 3. PID 仿真实验

建议实验：

1. 只调 `Kp`，观察上升时间、稳态误差、超调。
2. 只调 `Ki`，观察稳态误差消除和积分饱和。
3. 只调 `Kd`，观察阻尼增加和噪声放大。
4. PI 控制一阶液位对象。
5. PID 控制二阶欠阻尼对象。
6. 大时滞对象 PID 整定，观察振荡。

## 4. OpenPLC + Modbus 实验

目标：

```text
把 SP / Kp / Ki / Kd / PV / MV 映射到 Modbus Holding Register
```

实验链路：

```text
Python 修改 SP
  -> Modbus TCP 写 Holding Register
  -> OpenPLC 中 SP 改变
  -> 控制输出变化
  -> Wireshark 记录写寄存器报文
```

## 5. 反馈欺骗实验

目标：

模拟 PLC 或 HMI 看到假的 PV。

观察：

- 控制器是否继续输出错误动作。
- HMI 是否显示正常。
- 报警是否触发。
- 趋势是否能发现异常。

## 6. Python 工具路线

最低工具：

- TCP 端口扫描器
- Modbus 读寄存器
- Modbus 写寄存器
- PCAP 摘要分析
- 通信矩阵生成脚本

进阶工具：

- 自动识别工业端口
- 提取 Modbus 功能码统计
- 标记写操作
- 输出 Markdown 报告

## 7. 面试表达

### 60 分答案

> 我计划用 OpenPLC、CODESYS、Wireshark 和 Python 把控制变量、协议报文和安全风险串起来，重点验证写寄存器如何影响 SP、PID 参数或设备状态。

### 90 分答案

> 我的实验路线不是孤立学工具，而是先建立控制对象和 PLC 变量，再把 SP、PV、PID 参数映射到工业协议，通过 Python 发起读写，用 Wireshark 抓包，最后观察控制输出和过程变量变化。这样可以从控制理论、工程实现、协议行为和安全影响四个层面解释工控漏洞。

## 8. 作品集建议

可以形成三个项目：

1. `openplc-modbus-pid-lab`
2. `modbus-traffic-analyzer`
3. `industrial-communication-matrix-generator`

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[10 Tool Development](README.md)
- 本章目录：[10_Tool_Development](README.md)
- 下一篇：[11 AI for Security：AI 辅助安全研究](../11_AI_for_Security/README.md)

