# 示例文件说明

本目录包含以下基础示例：

- `curl-http-proxy.sh`：通过 HTTP Proxy 发起请求；
- `curl-socks5-proxy.sh`：通过 SOCKS5 发起请求；
- `proxy-check.py`：使用 Python Requests 进行连接测试；
- `proxy-environment.sh`：bash / zsh 环境变量示例；
- `proxy-environment.ps1`：PowerShell 环境变量示例。

## 运行前准备

1. 确认服务端支持的代理协议；
2. 在本地设置正确的代理地址和认证参数；
3. 安装 curl；Python 示例需要 Python 3 和 Requests；
4. 先使用非敏感目标测试；
5. 不要将真实账号密码写入代码或提交到仓库。

安装 Python 依赖：

```bash
python -m pip install requests
```

示例默认使用 `https://example.com/` 作为普通连通性测试目标，不会自动评估 IP 风险、纯净度或特定平台的接受情况。
