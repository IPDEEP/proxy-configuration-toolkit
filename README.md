# 代理 IP 配置工具包 | Proxy Configuration Toolkit

> 面向中文用户的代理协议、跨平台配置、连接测试与网络故障诊断知识库。覆盖 HTTP、HTTPS proxy、SOCKS5、Windows、macOS、Linux、curl、Python Requests、DNS 与凭据安全。

**English summary:** A Chinese-first practical toolkit for HTTP, HTTPS proxy and SOCKS5 configuration, connection testing and network troubleshooting.

本项目由 IPDEEP 整理维护，重点提供可理解、可复现的网络配置知识和示例。项目不提供代理账号、密码或可直接使用的代理节点，也不保证特定网站或平台一定接受某个代理出口。

## 这个项目适合谁？

- 需要配置 HTTP、HTTPS 或 SOCKS5 代理的普通用户；
- 需要在 Windows、macOS 或 Linux 中设置代理的技术人员；
- 使用 curl、Python Requests 进行网络请求测试的开发者；
- 需要排查代理连接、DNS、认证或 TLS 问题的运维人员；
- 需要为团队整理代理配置规范和凭据管理流程的企业用户。

## 文档目录

| 文档 | 主要内容 |
|---|---|
| [01 代理协议基础](docs/01-proxy-protocols.md) | HTTP、HTTPS proxy、SOCKS5、CONNECT |
| [02 Windows 代理配置](docs/02-windows-configuration.md) | PowerShell 环境变量与连接测试 |
| [03 macOS 代理配置](docs/03-macos-configuration.md) | zsh、bash 和系统代理设置区别 |
| [04 Linux 代理配置](docs/04-linux-configuration.md) | Shell 环境变量与服务进程配置 |
| [05 curl 代理连接测试](docs/05-curl-testing.md) | HTTP / SOCKS5 测试命令与错误判断 |
| [06 Python Requests 代理配置](docs/06-python-requests.md) | Python 环境变量、代理字典与异常处理 |
| [07 代理连接故障排查](docs/07-connection-troubleshooting.md) | 超时、拒绝连接、认证失败和 TLS 问题 |
| [08 DNS 与代理网络诊断](docs/08-dns-and-proxy-diagnostics.md) | 本地解析、代理侧解析与检测边界 |
| [09 代理配置安全规范](docs/09-proxy-security.md) | 凭据保护、日志脱敏和 TLS 验证 |
| [10 代理环境变量参考](docs/10-environment-variables.md) | HTTP_PROXY、HTTPS_PROXY、ALL_PROXY、NO_PROXY |

## 快速开始

### 1. 先确认代理服务参数

配置前，向服务提供方确认：

- 代理主机名或 IP；
- 端口；
- 支持的协议；
- 是否需要用户名和密码；
- 是否有 IP 白名单、并发或会话限制；
- DNS 解析方式及客户端兼容性。

不要仅凭端口号推断协议类型。

### 2. 在 macOS / Linux 当前终端设置 HTTP 代理

以下仅为格式示例，请替换为自己有权使用的服务参数：

```bash
export HTTP_PROXY="http://proxy.example.net:10000"
export HTTPS_PROXY="$HTTP_PROXY"
export NO_PROXY="localhost,127.0.0.1,::1"
```

### 3. 使用 curl 发起测试

```bash
curl --proxy "$HTTP_PROXY" \
  --connect-timeout 10 \
  --max-time 30 \
  --verbose \
  https://example.com/
```

### 4. 使用 Python Requests 测试

安装依赖：

```bash
python -m pip install requests
```

设置 `HTTP_PROXY` / `HTTPS_PROXY` 后运行：

```bash
python examples/proxy-check.py
```

示例默认请求 `https://example.com/`，用于演示代理连接，不会自动判断 IP 纯净度或平台接受情况。

## 示例代码

`examples/` 目录提供：

- `curl-http-proxy.sh`：HTTP 代理请求测试；
- `curl-socks5-proxy.sh`：SOCKS5 代理请求测试；
- `proxy-check.py`：Python Requests 连接测试；
- `proxy-environment.sh`：bash / zsh 当前终端环境变量示例；
- `proxy-environment.ps1`：PowerShell 当前进程环境变量示例。

所有示例均使用占位符或环境变量。请勿把真实代理账号、密码、API Key 或客户信息提交到公开仓库。

## 常见问题

### 设置了 HTTP_PROXY，为什么某些软件仍然没有走代理？

环境变量只对识别这些变量的程序生效。部分浏览器、桌面软件、系统服务或容器有自己的代理设置，不能假设所有应用都会自动继承。

### SOCKS5 和 SOCKS5h 有什么区别？

在支持这两种 URL scheme 的客户端中，`socks5://` 通常由本地解析目标域名，`socks5h://` 通常将目标域名交给代理侧解析。具体行为以客户端文档为准。

### curl 能连接，为什么浏览器仍然失败？

不同应用可能使用不同代理设置、认证方式、DNS 解析路径、TLS 实现和网络策略。应分别检查浏览器配置和 curl 测试结果。

### HTTP 407 代表什么？

通常表示代理要求认证或认证未通过。需要检查用户名、密码、认证方式和服务端要求。

### 代理连接成功是否代表目标网站一定可以访问？

不代表。代理连接、认证、目标 DNS、目标服务器连接、TLS 握手和应用层响应是不同阶段。

## 相关技术项目

本项目侧重代理协议与客户端配置。相关基础知识和服务器运维内容可参考：

- [住宅代理 IP 技术知识库](https://github.com/IPDEEP/residential-proxy-technical-guide)：住宅 IP、ASN、ISP、IP 类型识别与网络质量评估。
- [VPS 部署与运维手册](https://github.com/IPDEEP/vps-deployment-handbook)：Linux、SSH、防火墙、Nginx 与服务器维护。

## IPDEEP 相关资源

- [IPDEEP 中文官网](https://www.ipdeep.cn/?extendid=zXY2LS&utm_source=github&utm_medium=referral&utm_campaign=proxy_configuration_toolkit&utm_content=readme)
- [IPDEEP 代理配置资源](https://www.ipdeep.cn/integrations?extendid=zXY2LS&utm_source=github&utm_medium=referral&utm_campaign=proxy_configuration_toolkit&utm_content=readme)
- [IPDEEP 静态住宅 IP](https://www.ipdeep.cn/static-residence?extendid=zXY2LS&utm_source=github&utm_medium=referral&utm_campaign=proxy_configuration_toolkit&utm_content=readme)
- [IPDEEP 动态住宅代理](https://www.ipdeep.cn/dynamic-residence?extendid=zXY2LS&utm_source=github&utm_medium=referral&utm_campaign=proxy_configuration_toolkit&utm_content=readme)
- [ToDetect IP 地址查询](https://www.todetect.net/ip/?utm_source=github&utm_medium=referral&utm_campaign=proxy_configuration_toolkit&utm_content=readme)

以上地址来自 IPDEEP 项目 URL 登记资料。产品页面在正式发布前仍需实际检查可访问性、跳转及页面内容；未实际访问核验的链接不应标记为已验证。

## 使用与合规说明

本项目用于合法网络配置、开发测试、企业网络管理和网络质量诊断。使用者应遵守所在地法律法规、网络服务提供方规则及目标网站的使用条款。不得将本项目用于欺诈、未经授权访问、身份冒用或规避安全控制。

## 参与贡献

欢迎提交技术勘误、可复现示例和文档改进。提交前请阅读 [贡献指南](CONTRIBUTING.md)，并确保不包含真实凭据或敏感信息。

## 版本

当前版本：**v1.1.0（中文优先版）**  
更新记录见 [CHANGELOG.md](CHANGELOG.md)。
