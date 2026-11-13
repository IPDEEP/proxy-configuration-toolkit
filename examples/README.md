# 示例文件说明

本目录包含代理配置、连接测试和环境变量示例：

- `curl-http-proxy.sh`：通过 HTTP Proxy 发起请求；
- `curl-socks5-proxy.sh`：通过 SOCKS5 发起请求；
- `proxy-check.py`：使用 Python Requests 进行请求级连接测试；
- `proxy-endpoint-check.py`：检查代理主机端口 TCP 连通性；HTTPS proxy 额外检查 TLS 握手；
- `proxy-environment.sh`：bash / zsh 环境变量示例；
- `proxy-environment.ps1`：PowerShell 环境变量示例。

## 代理端点检查工具

要求 Python 3.10 或更高版本，无需安装第三方依赖：

```bash
python examples/proxy-endpoint-check.py
```

工具会通过隐藏输入提示读取代理 URL，支持：

- `http://host:port`
- `https://host:port`
- `socks5://host:port`
- `socks5h://host:port`

可调整超时：

```bash
python examples/proxy-endpoint-check.py --timeout 12
```

注意：TCP 连通不等于代理认证、协议握手、隧道建立或目标网站访问成功。该工具不会验证出口 IP。不要在录屏、共享终端或不可信设备中输入真实凭据。

详细说明见 [代理端点连通性检查工具](../docs/11-proxy-endpoint-checker.md)。

## 运行前准备

1. 确认服务端支持的代理协议；
2. 在本地设置正确的代理地址和认证参数；
3. 安装 curl；Python Requests 示例需要 Python 3 和 Requests；
4. 先使用非敏感目标测试；
5. 不要将真实账号密码写入代码或提交到仓库。

安装 Python Requests 依赖：

```bash
python -m pip install requests
```

现有 `proxy-check.py` 默认使用 `https://example.com/` 作为普通请求测试目标，不会自动评估 IP 风险、纯净度或特定平台的接受情况。
