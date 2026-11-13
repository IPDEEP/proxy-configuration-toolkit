# 03｜macOS 如何配置代理？

本指南介绍 macOS 终端中的 Shell 环境变量，以及它们与系统网络代理设置之间的区别。

## 1. 在当前终端设置 HTTP Proxy

适用于 zsh 或 bash：

```bash
export HTTP_PROXY="http://proxy.example.net:10000"
export HTTPS_PROXY="$HTTP_PROXY"
export NO_PROXY="localhost,127.0.0.1,::1"
```

请确认服务端确实支持 HTTP Proxy。若服务提供 SOCKS5，应使用客户端支持的 SOCKS5 配置方式，不要直接套用 HTTP 示例。

## 2. 安全检查变量状态

```bash
[ -n "$HTTP_PROXY" ] && echo "HTTP_PROXY 已设置" || echo "HTTP_PROXY 未设置"
[ -n "$HTTPS_PROXY" ] && echo "HTTPS_PROXY 已设置" || echo "HTTPS_PROXY 未设置"
```

避免在共享终端或录屏中输出包含用户名、密码的完整代理 URL。

## 3. 使用 curl 测试

```bash
curl --proxy "$HTTP_PROXY" \
  --connect-timeout 10 \
  --max-time 30 \
  --verbose \
  https://example.com/
```

## 4. 清除当前终端设置

```bash
unset HTTP_PROXY HTTPS_PROXY ALL_PROXY NO_PROXY
```

## 5. Shell 变量与 macOS 系统代理的区别

Shell 环境变量通常只影响当前终端进程及其子进程。macOS 的系统网络代理设置则由网络服务管理，部分图形界面应用可能读取系统设置，而不读取终端环境变量。

可以在 macOS“系统设置”的“网络”中查看当前网络服务的代理选项。具体名称可能因系统版本而异。

## 6. 是否应该写入 .zshrc？

可以将不含敏感信息的常规配置写入 Shell 启动文件，但不建议直接保存明文密码。启动文件可能被备份、同步或被其他本地进程读取。

## 相关文档

- [代理环境变量参考](10-environment-variables.md)
- [代理配置安全规范](09-proxy-security.md)
