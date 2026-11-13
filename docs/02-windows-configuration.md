# 02｜Windows 如何配置代理环境变量？

本指南使用 PowerShell 设置环境变量。环境变量通常影响当前 PowerShell 进程及其启动的子进程，但并非所有 Windows 软件都会读取这些变量。

## 1. 设置当前 PowerShell 会话

以下示例假设代理服务支持 HTTP Proxy：

```powershell
$env:PROXY_HOST = "proxy.example.net"
$env:PROXY_PORT = "10000"

$proxy = "http://$($env:PROXY_HOST):$($env:PROXY_PORT)"
$env:HTTP_PROXY = $proxy
$env:HTTPS_PROXY = $proxy
$env:NO_PROXY = "localhost,127.0.0.1,::1"
```

如果服务需要认证，应使用安全方式提供凭据。不要将真实用户名和密码写入公开脚本、仓库或共享命令记录。

## 2. 检查变量是否设置

不要直接打印可能包含凭据的完整代理 URL。可以只检查变量是否存在：

```powershell
"HTTP_PROXY set: " + [bool]$env:HTTP_PROXY
"HTTPS_PROXY set: " + [bool]$env:HTTPS_PROXY
```

## 3. 使用 curl 测试

```powershell
curl.exe --proxy $env:HTTP_PROXY `
  --connect-timeout 10 `
  --max-time 30 `
  --verbose `
  https://example.com/
```

使用 `curl.exe` 可以避免部分 PowerShell 环境中的命令别名干扰。

## 4. 清除当前会话设置

```powershell
Remove-Item Env:HTTP_PROXY -ErrorAction SilentlyContinue
Remove-Item Env:HTTPS_PROXY -ErrorAction SilentlyContinue
Remove-Item Env:NO_PROXY -ErrorAction SilentlyContinue
```

## 5. 为什么有些软件没有使用代理？

常见原因：

- 软件不读取 `HTTP_PROXY` / `HTTPS_PROXY`；
- 软件使用 Windows 系统代理设置；
- 软件有独立的代理配置；
- 软件启动时没有继承当前终端环境变量；
- 软件只支持特定代理协议或认证方式。

## 6. 持久化配置注意事项

不要为了方便就把含密码的代理 URL 写入全局环境变量、注册表或共享脚本。持久化前应评估本机账户权限、日志、备份和同步风险，并遵循组织的凭据管理规范。

## 相关文档

- [代理环境变量参考](10-environment-variables.md)
- [curl 代理连接测试](05-curl-testing.md)
- [代理配置安全规范](09-proxy-security.md)
