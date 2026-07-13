# 02 篇术语表

本术语表用于快速复习。具体工程语义和厂商实现仍以正文、项目资料与设备文档为准。

## 1. 过程与控制

| 术语 | 含义 |
| --- | --- |
| Process | 被控制的物理或生产过程 |
| Controlled Variable | 需要维持的过程变量 |
| SP | Setpoint，设定值，控制目标 |
| PV | Process Variable，过程测量值 |
| MV/CV | Manipulated/Controller Output，控制器操纵输出 |
| Disturbance | 扰动，影响过程但非主要操纵量的输入 |
| Open Loop | 开环控制，不依据结果自动纠偏 |
| Closed Loop | 闭环控制，利用反馈修正偏差 |
| Process Gain | 操纵量变化引起稳态过程值变化的比例 |
| Time Constant | 表示对象响应速度的动态参数 |
| Dead Time | 输入变化到输出开始可见变化的延迟 |
| Integral Process | 输入不平衡会使输出持续累积变化的过程 |
| Stability | 扰动后状态是否保持有限并趋向平衡 |
| Overshoot | 响应超过目标的最大程度 |
| Settling Time | 响应进入并保持允许误差带所需时间 |

## 2. PID 与高级控制结构

| 术语 | 含义 |
| --- | --- |
| PID | 比例、积分、微分控制器 |
| Proportional Band | 比例带，某些平台用于表示比例作用 |
| Integral Windup | 执行器饱和时积分继续累积 |
| Anti-windup | 抑制或回算积分饱和的机制 |
| Bumpless Transfer | 模式或主备切换时避免输出突跳 |
| Cascade Control | 主回路输出作为副回路设定值 |
| Feedforward | 根据可测扰动提前补偿 |
| Ratio Control | 维持两个变量间比例 |
| Split Range | 一个输出分段驱动多个执行器 |
| Override/Selector | 按约束选择高值或低值控制需求 |

## 3. 仪表与 I/O

| 术语 | 含义 |
| --- | --- |
| Sensor | 感知物理量的传感元件 |
| Transmitter | 将测量转换为标准信号的变送器 |
| Final Element | 最终改变过程的元件，如切断阀 |
| DI/DO | 数字输入/数字输出 |
| AI/AO | 模拟输入/模拟输出 |
| Pulse I/O | 脉冲计数或脉冲输出 |
| Live Zero | 活零点，如 4 mA 表示量程下限 |
| Raw Value | A/D 或协议中的原始数值 |
| Scaling | 原始值与工程量之间的换算 |
| Range | 测量或输出的上下限范围 |
| Resolution | 能区分的最小变化 |
| Drift | 相同输入下输出随时间偏移 |
| Hysteresis | 上升和下降方向下同一输入对应不同输出 |
| Quality Code | 表示值好、坏、不确定或替代的状态 |
| Process Image | PLC 在任务周期使用的 I/O 映像 |
| Remote I/O | 通过网络或现场总线连接的分布式 I/O |

## 4. PLC 运行时与程序

| 术语 | 含义 |
| --- | --- |
| PLC | 可编程逻辑控制器 |
| PAC | 可编程自动化控制器，强调综合控制能力 |
| Scan Cycle | 输入、逻辑、输出及系统服务的周期模型 |
| Cyclic Task | 按固定周期触发的任务 |
| Event Task | 由事件或中断触发的任务 |
| Watchdog | 监测任务或扫描超时的机制 |
| RUN/STOP | 执行或停止用户程序的运行模式 |
| LD | Ladder Diagram，梯形图 |
| FBD | Function Block Diagram，功能块图 |
| ST | Structured Text，结构化文本 |
| SFC | Sequential Function Chart，顺序功能图 |
| Function Block | 具有实例状态的可复用程序单元 |
| Instance Data | 功能块跨扫描保存的内部状态 |
| Retentive Data | 特定重启或掉电后保留的数据 |
| Force | 强制变量或 I/O 为指定值 |
| Online Change | 控制器运行时修改部分工程 |
| Cross Reference | 变量读写与调用位置索引 |

## 5. 顺控、设备与批次

| 术语 | 含义 |
| --- | --- |
| State Machine | 由状态和转移条件描述行为的模型 |
| Step/Transition | 顺控中的步骤与转移条件 |
| Permissive | 启动或进入状态前必须满足的许可 |
| Interlock | 运行中阻止危险动作的约束 |
| Trip | 达到条件后自动停止或进入安全状态 |
| Reset | 原因消除后清除锁存故障，不代表自动启动 |
| Bypass | 经授权临时忽略某项条件或功能 |
| Recipe | 批次或产品的步骤与参数集合 |
| Batch | 按配方处理有限物料的生产批次 |
| Command Arbitration | 多个命令来源之间的优先级选择 |

## 6. DCS、SCADA 与操作监控

| 术语 | 含义 |
| --- | --- |
| DCS | 分散控制系统，集成控制、操作和工程管理 |
| SCADA | 监控与数据采集系统 |
| HMI | 人机界面 |
| RTU | 远程终端单元 |
| IED | 智能电子设备，电力等领域常见 |
| Engineering Station | 工程师站，用于组态、编程和下载 |
| Operator Station | 操作员站，用于监视与控制过程 |
| Historian | 面向过程数据的历史数据库 |
| Real-time Database | 保存当前标签、质量与状态的实时数据库 |
| SOE | Sequence of Events，顺序事件记录 |
| Select Before Operate | 先选择目标再执行的遥控流程 |
| Alarm Flood | 短时间产生大量报警 |
| Shelving | 操作员按规则临时搁置报警 |
| Suppression | 根据状态自动抑制无意义报警 |
| Stale Value | 因失联或停更形成的陈旧值 |

## 7. 电气与驱动

| 术语 | 含义 |
| --- | --- |
| MCC | Motor Control Center，电机控制中心 |
| Contactor | 接触器，用于接通或断开动力回路 |
| Overload Relay | 过载保护继电器 |
| Soft Starter | 降低电机启动冲击的软启动器 |
| VFD | Variable Frequency Drive，变频器 |
| Speed Reference | 速度或频率给定 |
| Local/Remote | 就地或远程控制权状态 |
| Auto Restart | 故障或掉电恢复后的自动重启功能 |
| STO | Safe Torque Off，安全转矩关闭 |
| LOTO | Lockout/Tagout，锁定挂牌与能量隔离 |

## 8. 功能安全

| 术语 | 含义 |
| --- | --- |
| BPCS | 基本过程控制系统 |
| SIS | 安全仪表系统 |
| SIF | 安全仪表功能，包含检测、逻辑和最终元件 |
| ESD | 紧急停车系统 |
| SRS | 安全需求规格 |
| SIL | 安全完整性等级，表示所需风险降低能力 |
| PFDavg | 低需求模式下平均要求时失效概率 |
| PFH | 高需求或连续模式下危险失效频率指标 |
| 1oo2/2oo3 | 一取二、二取三表决架构 |
| Proof Test | 发现潜在危险失效的证明测试 |
| Common Cause Failure | 同一原因同时导致多通道失效 |
| Independent Protection Layer | 足够独立、有效且可审计的保护层 |
| Fail-safe | 故障时趋向具体过程所定义的安全状态 |

## 9. 安全与项目证据

| 术语 | 含义 |
| --- | --- |
| Control Flow | 决定任务、逻辑和动作执行的路径 |
| Data Flow | 数值、质量和时间在系统间的传播 |
| State Flow | 设备、程序和过程状态的迁移 |
| Energy Flow | 电、热、压力、动能等物理能量传递 |
| Command-Feedback-Response | 命令、设备反馈和过程响应的一致性链 |
| Engineering Baseline | 经批准的工程、参数和配置基准 |
| Offline-Online Compare | 离线工程与在线控制器的差异比较 |
| Low-impact Validation | 优先使用离线、被动和隔离方法的验证策略 |
| Evidence Confidence | 理论可能、工程可信、实验验证或现场证实等级 |
| Recovery Validation | 同时验证数字状态与真实过程状态的恢复验收 |

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[阅读、复习与验收指南](Reading_Guide.md)
- 本篇目录：[02_Automation](README.md)
- 下一篇：[03 Industrial Network：工业网络与安全边界](../03_Industrial_Network/README.md)
