# 01｜代理协议基础：HTTP、HTTPS Proxy 与 SOCKS5

代理协议决定客户端如何连接代理端点、传递请求以及完成认证。配置前应确认代理服务端和客户端支持的协议。

## 1. HTTP 代理

HTTP 代理能够理解 HTTP 请求。访问普通 HTTP 目标时，客户端通常通过代理发送请求；访问 HTTPS 目标时，常见方式是使用 HTTP `CONNECT` 方法建立隧道。

常见 URL 形式：

```text
http://proxy.example.net:10000
```

这里的 `http://` 描述客户端到代理端点的连接方式，不代表目标网站只能使用 HTTP。

## 2. HTTPS Proxy

部分代理端点支持客户端先与代理建立 TLS 连接。客户端可能使用 `https://` 形式表示这种代理端点，但是否支持取决于具体客户端和服务端。

不要默认一个 HTTP 代理端点也支持 TLS 到代理端的连接。应查看服务提供方说明和客户端文档。

## 3. SOCKS5

SOCKS5 是通用代理协议，常用于转发 TCP 连接。它本身不解析 HTTP 请求内容。

常见 URL 形式：

```text
socks5://proxy.example.net:10000
socks5h://proxy.example.net:10000
```

在支持这两种形式的客户端中，通常：

- `socks5://`：目标域名由本地客户端解析；
- `socks5h://`：目标域名交由代理侧解析。

不同客户端实现可能存在差异，不能把上述行为视为所有软件的统一规则。

## 4. HTTP CONNECT 是什么？

`CONNECT` 是 HTTP 方法之一，常用于请求代理建立到目标主机和端口的隧道。建立隧道后，客户端可以在该连接上进行 TLS 握手，从而访问 HTTPS 网站。

这并不意味着 HTTP 代理自动解密 HTTPS 内容。

## 5. 协议对比

| 维度 | HTTP Proxy | HTTPS Proxy | SOCKS5 |
|---|---|---|---|
| 理解 HTTP 请求 | 是 | 是 | 否 |
| 转发 HTTPS 目标 | 常见方式为 CONNECT | 常见方式为 CONNECT | 可转发 TCP |
| 客户端到代理的 TLS | 不代表支持 | 支持时可建立 | SOCKS5 本身不提供 |
| DNS 行为 | 取决于客户端实现 | 取决于客户端实现 | 取决于客户端模式 |
| 应用兼容性 | 视软件而定 | 视软件而定 | 视软件而定 |

## 6. 如何选择？

1. 确认服务端实际支持的协议；
2. 确认目标软件支持该协议；
3. 核对认证方式；
4. 明确 DNS 解析位置；
5. 使用非敏感请求进行测试；
6. 记录客户端版本和错误信息。

## 相关文档

- [curl 代理连接测试](05-curl-testing.md)
- [Python Requests 代理配置](06-python-requests.md)
- [DNS 与代理网络诊断](08-dns-and-proxy-diagnostics.md)
