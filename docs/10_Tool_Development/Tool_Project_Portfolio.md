# 工具项目作品集

## 1. 为什么要做作品集

对求职来说，工具项目能证明：

- 你会写代码。
- 你理解协议。
- 你知道安全边界。
- 你能把工具和报告结合。
- 你有持续学习能力。

## 2. 推荐项目结构

```text
tool-name/
├── README.md
├── requirements.txt
├── examples/
├── tests/
├── docs/
└── src/
```

README 应包括：

- 工具用途。
- 安装方法。
- 参数说明。
- 示例输入输出。
- 安全限制。
- 适用场景。
- 后续计划。

## 3. 适合展示的项目

### 3.1 Modbus Traffic Analyzer

能力点：

- PCAP 解析。
- Modbus 功能码识别。
- 写操作标记。
- 通信矩阵生成。
- Markdown 报告输出。

### 3.2 ICS CVE Reporter

能力点：

- CVE 信息结构化。
- 厂商公告整理。
- 工控影响模板。
- 报告自动生成。

### 3.3 Protocol Mini Lab

能力点：

- Socket 客户端。
- 仿真服务。
- 正常请求和异常请求。
- 抓包验证。

## 4. 面试表达模板

> 我的工具项目不是为了攻击生产设备，而是辅助工控安全分析。例如 Modbus 流量分析器可以从 PCAP 中提取通信矩阵、功能码和异常写操作，帮助评估通信关系和风险。项目 README 里我会写明授权使用、只读分析、输入输出和限制，这能体现工程化和安全边界意识。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[报告自动化](Report_Automation.md)
- 本章目录：[10_Tool_Development](README.md)
- 下一篇：[面试问答](Interview_QA.md)

