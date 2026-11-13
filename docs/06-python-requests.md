# 06｜Python Requests 如何配置代理？

Python Requests 可以通过环境变量或 `proxies` 参数使用代理。实际支持情况与 Requests 版本、底层依赖和代理协议有关。

## 1. 安装依赖

```bash
python -m pip install requests
```

## 2. 通过环境变量配置

先在当前 Shell 设置 `HTTP_PROXY` 和 `HTTPS_PROXY`，再运行：

```python
import requests

response = requests.get(
    "https://example.com/",
    timeout=(10, 30),
)

print("HTTP 状态码：", response.status_code)
print("最终 URL：", response.url)
```

不要在公开日志中打印代理 URL 或认证信息。

## 3. 通过 proxies 参数配置

```python
import os
import requests

http_proxy = os.environ.get("HTTP_PROXY")
https_proxy = os.environ.get("HTTPS_PROXY")

if not http_proxy and not https_proxy:
    raise RuntimeError("请先设置 HTTP_PROXY 或 HTTPS_PROXY")

proxies = {}
if http_proxy:
    proxies["http"] = http_proxy
if https_proxy:
    proxies["https"] = https_proxy

response = requests.get(
    "https://example.com/",
    proxies=proxies,
    timeout=(10, 30),
)

print("HTTP 状态码：", response.status_code)
```

代理 URL 必须匹配服务端支持的协议和认证格式。

## 4. SOCKS 代理支持

Requests 使用 SOCKS 代理需要安装可选依赖：

```bash
python -m pip install "requests[socks]"
```

示例：

```python
proxies = {
    "http": "socks5h://proxy.example.net:10000",
    "https": "socks5h://proxy.example.net:10000",
}
```

是否支持特定认证方式和 URL scheme，应以当前 Requests 及底层依赖文档为准。

## 5. 设置超时并处理异常

```python
import requests

try:
    response = requests.get(
        "https://example.com/",
        timeout=(10, 30),
    )
    response.raise_for_status()
except requests.exceptions.ProxyError:
    print("代理连接或协议协商失败")
except requests.exceptions.ConnectTimeout:
    print("建立连接超时")
except requests.exceptions.ReadTimeout:
    print("读取响应超时")
except requests.exceptions.RequestException:
    print("请求失败，请在本地安全环境中检查诊断信息")
```

分享异常日志前，应检查是否包含敏感 URL、凭据或内部主机信息。

## 相关示例

- [proxy-check.py](../examples/proxy-check.py)
- [curl 代理连接测试](05-curl-testing.md)
