# 简历 Bullet

## 个人总结

- 系统学习工控安全研究方向，覆盖 Python/Linux/网络基础、PLC/DCS/SCADA、工业协议、Web 安全、逆向分析、漏洞研究、IEC 62443 与工具开发。
- 具备基于仿真环境开展工控协议分析、抓包验证、漏洞复现和安全报告整理的能力。
- 关注工控安全测试边界，理解生产连续性、低风险验证、授权测试和现场缓解的重要性。

## 项目：Modbus 流量分析器

- 使用 Python 解析 PCAP 中的 Modbus TCP 流量，提取通信双方、功能码、寄存器地址、异常响应和写操作。
- 生成通信矩阵和 Markdown 摘要报告，用于辅助工业网络访问关系分析和异常写操作识别。
- 在工具设计中加入只读分析、异常处理和结果可解释输出，避免对真实设备产生影响。

## 项目：OpenPLC + Modbus 实验室

- 搭建 OpenPLC 仿真环境，编写基础控制逻辑并配置 Modbus 地址映射。
- 使用 Wireshark 抓取 Modbus TCP 流量，分析功能码、地址和值与控制变量之间的关系。
- 输出实验报告，说明写寄存器、设定值变化和控制输出之间的工控安全影响。

## 项目：工控 CVE 分析报告

- 对工控相关 CVE 进行公告整理、影响版本确认、PoC 安全审计和复现记录。
- 提取最小触发样本，分析漏洞入口、攻击条件、根因和工控场景影响。
- 编写漏洞分析报告，包含修复建议、现场缓解措施和限制条件。

## 技能关键词

- Python、Git、Linux、Wireshark、Socket
- PLC、SCADA、HMI、DCS、PID、Historian
- Modbus TCP、S7Comm、OPC UA、IEC 104
- Web 安全、逆向分析、固件分析、CVE 复现
- IEC 62443、分区分域、纵深防御、工控安全评估

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[杭州面试准备](Hangzhou_Interview_Prep.md)
- 本章目录：[13_Interview](README.md)
- 下一篇：[模拟面试检查清单](Mock_Interview_Checklist.md)

