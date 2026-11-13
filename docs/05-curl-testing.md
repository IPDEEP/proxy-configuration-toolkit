# 05｜如何使用 curl 测试代理连接？

curl 可以帮助判断代理端点是否可连接、认证是否成功，以及一次基础 HTTP 请求是否完成。但它不能证明所有应用都会采用相同网络路径。

## 1. HTTP Proxy 测试

```bash
curl --proxy "http://proxy.example.net:10000" \
  --connect-timeout 10 \
  --max-time 30 \
  --verbose \
  https://example.com/
```

如果需要认证，优先使用环境变量或客户端支持的安全凭据方式，避免把密码直接写进 Shell 历史。

## 2. SOCKS5 测试

本地解析目标域名（客户端支持时）：

```bash
curl --proxy "socks5://proxy.example.net:10000" https://example.com/
```

代理侧解析目标域名（客户端支持时）：

```bash
curl --proxy "socks5h://proxy.example.net:10000" https://example.com/
```

## 3. 常用参数

| 参数 | 用途 |
|---|---|
| `--proxy` | 指定代理地址 |
| `--connect-timeout 10` | 限制建立连接的时间 |
| `--max-time 30` | 限制整个请求的总时间 |
| `--verbose` | 输出连接过程细节 |
| `--fail-with-body` | HTTP 错误状态时返回失败并保留响应体（需确认 curl 版本支持） |

`--verbose` 可能输出主机名、请求头或其他诊断信息，分享日志前应先脱敏。

## 4. 常见结果如何理解？

| 现象 | 可能原因 | 下一步检查 |
|---|---|---|
| Connection timed out | 网络不可达、路由问题、服务端无响应或超时设置 | 主机、端口、网络和服务状态 |
| Connection refused | 端口未监听或端点配置错误 | 端口和服务端配置 |
| HTTP 407 | 代理要求认证或认证未通过 | 用户名、密码、认证方式 |
| DNS resolution failed | 本地或代理侧 DNS 解析问题 | DNS 模式和客户端支持情况 |
| TLS certificate error | 证书链、系统时间或 TLS 配置异常 | 证书和系统信任配置 |
| 目标网站返回 403 | 目标服务拒绝请求 | 目标服务策略及请求授权 |

以上为排查线索，不是对具体故障的唯一判断。

## 5. 不要把关闭证书验证当作常规解决办法

`--insecure` 或 `-k` 会关闭 TLS 证书验证，可能掩盖中间人攻击或证书配置问题。应先排查证书链、系统时间和客户端配置。

## 相关文档

- [代理协议基础](01-proxy-protocols.md)
- [代理连接故障排查](07-connection-troubleshooting.md)
