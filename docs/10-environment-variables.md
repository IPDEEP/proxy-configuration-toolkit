# 10｜代理环境变量参考

不少命令行工具和开发库支持通过环境变量读取代理配置，但支持范围和优先级因软件而异。

## 1. 常见变量

| 变量 | 常见用途 |
|---|---|
| `HTTP_PROXY` | HTTP 请求使用的代理 |
| `HTTPS_PROXY` | HTTPS 目标请求使用的代理 |
| `ALL_PROXY` | 某些客户端支持的通用代理回退变量 |
| `NO_PROXY` | 指定不通过代理访问的主机或地址 |

部分工具也识别小写形式。不同客户端对变量优先级、匹配语法和协议支持可能不同。

## 2. bash / zsh 示例

```bash
export HTTP_PROXY="http://proxy.example.net:10000"
export HTTPS_PROXY="$HTTP_PROXY"
export NO_PROXY="localhost,127.0.0.1,::1"
```

## 3. PowerShell 示例

```powershell
$env:HTTP_PROXY = "http://proxy.example.net:10000"
$env:HTTPS_PROXY = $env:HTTP_PROXY
$env:NO_PROXY = "localhost,127.0.0.1,::1"
```

## 4. 环境变量的作用范围

- 通常影响当前进程及其子进程；
- 独立启动的图形界面应用不一定继承终端变量；
- systemd 服务、容器和包管理器可能有独立设置；
- `NO_PROXY` 的匹配规则因客户端而异。

## 5. 不泄露凭据地检查变量

bash / zsh：

```bash
test -n "$HTTPS_PROXY" && echo "HTTPS_PROXY 已设置"
```

PowerShell：

```powershell
"HTTPS_PROXY set: " + [bool]$env:HTTPS_PROXY
```

## 6. 清除变量

bash / zsh：

```bash
unset HTTP_PROXY HTTPS_PROXY ALL_PROXY NO_PROXY
```

PowerShell：

```powershell
Remove-Item Env:HTTP_PROXY, Env:HTTPS_PROXY, Env:ALL_PROXY, Env:NO_PROXY -ErrorAction SilentlyContinue
```

## 相关文档

- [Windows 代理配置](02-windows-configuration.md)
- [macOS 代理配置](03-macos-configuration.md)
- [Linux 代理配置](04-linux-configuration.md)
