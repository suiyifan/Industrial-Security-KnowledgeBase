# 逆向工程基础

JD 要求熟悉 WinDbg、OD、IDA 等逆向、反汇编工具与手段。

## 学习顺序

1. 进制、内存、寄存器、栈
2. x86 / x64 基础指令
3. 函数调用约定
4. PE 文件结构
5. Windows API
6. IDA 静态分析
7. WinDbg / OD 动态调试

## 工控安全中的用途

- 分析工控软件的认证逻辑
- 分析协议处理函数
- 查找硬编码密码、后门、危险接口
- 分析崩溃点和漏洞触发路径
- 辅助 CVE 复现与影响判断

## 第一阶段目标

能打开一个程序，找到字符串、导入函数、关键分支，并写出“这个程序大概做什么、风险点在哪里”。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[07 Reverse Engineering：逆向工程](README.md)
- 本章目录：[07_Reverse_Engineering](README.md)
- 下一篇：[逆向工程方法论](Reverse_Engineering_Methodology.md)

