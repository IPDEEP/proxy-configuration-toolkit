# Proxy Endpoint Checker：代理端点连通性检查

## 工具用途

`proxy-endpoint-check.py` 检查指定代理主机和端口是否可以建立 TCP 连接：

- HTTP proxy；
- HTTPS proxy；
- SOCKS5；
- SOCKS5h。

HTTPS proxy 会额外进行 TLS 握手，并验证证书链和主机名。

**重要边界：** TCP 连接成功不代表代理认证成功、代理隧道建立成功、目标网站可访问或出口 IP 符合预期。本工具不执行代理认证，也不检测住宅属性、IP 信誉或平台接受情况。

## 环境要求

- Python 3.10 或更高版本；
- 无需安装第三方依赖；
- 本地终端可交互输入代理 URL。

## 运行方式

```bash
python examples/proxy-endpoint-check.py
```

输入格式示例（请替换为自己的授权端点）：

```text
http://proxy.example.net:10000
https://proxy.example.net:10443
socks5://proxy.example.net:1080
socks5h://proxy.example.net:1080
```

需要认证时，可以输入包含用户名和密码的 URL。终端输入不会回显，程序不会打印完整 URL 或凭据。但仍应避免在录屏、共享终端或不可信设备上输入真实认证信息。

指定连接超时：

```bash
python examples/proxy-endpoint-check.py --timeout 12
```

## 输出含义

- TCP 连通性成功：目标主机端口接受了 TCP 连接。
- HTTPS TLS 握手成功：与 HTTPS 代理端点完成 TLS 握手，且系统信任库验证通过。
- 连接超时或失败：检查主机名、端口、网络路由、防火墙和服务端监听状态。

对于 HTTP、SOCKS5 和 SOCKS5h，本工具只测试 TCP 端点，不代表协议协商已经成功。

## 下一步验证

如需验证代理认证、请求转发和目标站点访问，应继续使用本项目中的 `proxy-check.py` 或 curl 示例，并选择自己有权访问的测试 URL。不要把代理密码写入命令历史或公开日志。

## 相关资源

- [代理配置教程与资源](https://www.ipdeep.cn/integrations)
- [代理协议基础](../docs/01-proxy-protocols.md)
- [连接故障排查](../docs/07-connection-troubleshooting.md)
