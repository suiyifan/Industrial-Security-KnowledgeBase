# Windows PE 基础

## 1. PE 文件是什么

PE 是 Windows 可执行文件格式，常见扩展包括 `.exe`、`.dll`、`.sys`、`.ocx`。在工控场景中，上位机、工程软件插件、驱动、协议库、授权组件、网关服务都可能是 PE 文件。

理解 PE 的目的不是背格式，而是知道安全分析时应该从哪里找线索：

- 程序入口在哪里。
- 依赖哪些 DLL。
- 调用了哪些系统 API。
- 包含哪些字符串、资源、配置和版本信息。
- 是否导出函数给其他程序调用。
- 是否被加壳、压缩或混淆。

## 2. PE 结构速览

| 区域 | 作用 | 逆向关注点 |
| --- | --- | --- |
| DOS Header | 兼容历史格式 | `MZ` 魔数，指向 PE Header |
| PE Header | 文件总体描述 | 机器架构、节数量、时间戳 |
| Optional Header | 加载参数 | 入口点、镜像基址、子系统 |
| Section Table | 节区表 | `.text`、`.data`、`.rdata`、`.rsrc` 等 |
| Import Table | 导入表 | 程序调用了哪些外部 API |
| Export Table | 导出表 | DLL 对外提供哪些函数 |
| Resource | 资源 | 图标、对话框、版本、字符串、内嵌配置 |
| Relocation | 重定位 | 地址修正信息 |

## 3. 节区如何读

常见节区：

- `.text`：代码区，反汇编主要看这里。
- `.rdata`：只读数据，常见字符串、常量、虚表、导入名称。
- `.data`：全局变量、可写数据。
- `.rsrc`：资源，可能包含界面文本、版本信息、嵌入文件。
- `.pdata`：异常处理和函数边界信息，x64 程序中对恢复函数很有帮助。

异常节区名可能意味着加壳或自定义打包。例如 `.UPX0`、`.UPX1` 常见于 UPX；高熵节区可能包含压缩或加密数据。

## 4. 导入表能告诉你什么

导入表是逆向的第一批高价值线索。

### 4.1 网络通信相关

- `socket`
- `connect`
- `bind`
- `listen`
- `accept`
- `send`
- `recv`
- `WSAStartup`
- `InternetOpen`
- `WinHttpSendRequest`

如果一个工程软件导入了 socket API，又包含 `Modbus`、`PLC`、`Download` 等字符串，可以优先找网络协议发送和接收路径。

### 4.2 文件与配置相关

- `CreateFile`
- `ReadFile`
- `WriteFile`
- `GetPrivateProfileString`
- `RegOpenKey`
- `RegSetValue`

这些函数常用于工程文件解析、配置读取、日志写入、授权文件读取。

### 4.3 进程与命令执行相关

- `CreateProcess`
- `ShellExecute`
- `WinExec`
- `LoadLibrary`
- `GetProcAddress`

这些函数对漏洞分析很敏感。如果外部输入能影响命令参数、DLL 路径或插件路径，可能产生命令执行、DLL 劫持或插件加载风险。

### 4.4 内存危险函数

- `strcpy`
- `strcat`
- `sprintf`
- `memcpy`
- `gets`
- `lstrcpy`

危险函数不是漏洞本身。要继续确认参数是否外部可控、长度是否受限、目标缓冲区是否足够。

## 5. PE 中的工程线索

工控软件常在 PE 中暴露很多业务线索：

- 设备型号：`PLC-xxx`、`RTU-xxx`。
- 协议名：`Modbus`、`S7`、`OPCUA`、`IEC104`。
- 功能动作：`Start`、`Stop`、`Download`、`Upload`、`Force`。
- 变量和对象：`Tag`、`Point`、`Register`、`Coil`。
- 错误信息：`Invalid password`、`CRC error`、`Session expired`。
- 调试日志：`send packet`、`parse response`、`login success`。

这些字符串可以作为交叉引用入口，向上找到调用函数，向下找到数据结构和状态机。

## 6. PE 分析流程

1. 用 `Detect It Easy` 或类似工具识别架构、编译器、壳。
2. 用 PE 查看工具看导入表、节区、资源、版本信息。
3. 用 strings 提取字符串并按协议、认证、文件、命令、错误分类。
4. 用 IDA/Ghidra 打开，先从导入函数和字符串交叉引用开始。
5. 给关键函数重命名，例如 `parse_modbus_request`、`check_license`、`download_project`。
6. 对关键路径做动态调试，验证参数和分支。

## 7. 面试表达模板

> 我分析 Windows 工控软件时会先看 PE 元信息和导入表。导入表能快速判断程序是否涉及网络通信、文件解析、插件加载、命令执行或危险内存操作。然后我会结合字符串和资源信息找协议名、设备型号、登录、下载、强制输出等业务入口，再用交叉引用恢复调用链。真正判断漏洞时，我会动态验证外部输入是否能到达危险函数或越权逻辑，而不是只凭一个危险 API 下结论。

## 8. 实操验证

可以找一个开源 Windows 网络工具或简单 Modbus 客户端，完成：

- 记录样本哈希、架构、编译器、是否加壳。
- 截图导入表中网络 API。
- 找到一个协议关键字符串及其交叉引用。
- 给 5 个函数重命名。
- 写出输入进入程序后的调用链。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[逆向工程方法论](Reverse_Engineering_Methodology.md)
- 本章目录：[07_Reverse_Engineering](README.md)
- 下一篇：[汇编与调试基础](Assembly_Debugging_Basics.md)

