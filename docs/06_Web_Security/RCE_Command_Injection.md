# 远程命令执行与系统接管

RCE 指攻击者可以让服务器执行任意代码或系统命令。命令注入通常来自后端把用户输入拼接进系统命令。

工控 Web 系统中危险功能：

- 网络诊断 ping/traceroute
- 日志打包下载
- 固件升级
- 备份恢复
- 脚本任务
- 远程运维命令

RCE 发生在不同资产上影响不同：

- 普通 Web 服务器：入口和跳板。
- 工业网关：可能接触 PLC 或协议转换配置。
- 工程站 Web 服务：可能接触工程文件。
- SCADA Server：可能影响采集和监控。

> 面试表达：我不会只说 RCE 可以拿服务器权限，而会先判断服务器角色。如果 RCE 在工业网关或 SCADA Server 上，攻击者可能读取 PLC 地址、点表、通信配置，甚至进一步访问控制网资产。

<!-- NAVIGATION_INDEX -->

---

## 导航索引

- 上一篇：[越权、认证绕过与权限模型](Access_Control_Auth_Bypass.md)
- 本章目录：[06_Web_Security](README.md)
- 下一篇：[SSRF、内网探测与工控边界](SSRF_Internal_Pivot.md)

