# 04｜Linux 如何配置代理？

Linux 中的代理设置可能涉及当前 Shell、桌面环境、系统服务、容器和具体应用。不同程序的配置方式并不完全一致。

## 1. 当前 Shell 设置

以下以 bash 为例：

```bash
export HTTP_PROXY="http://proxy.example.net:10000"
export HTTPS_PROXY="$HTTP_PROXY"
export NO_PROXY="localhost,127.0.0.1,::1"
```

应根据服务提供方实际支持的协议选择 URL scheme。

## 2. 检查变量是否存在

```bash
test -n "$HTTP_PROXY" && echo "HTTP_PROXY 已设置"
test -n "$HTTPS_PROXY" && echo "HTTPS_PROXY 已设置"
```

不要把含有认证信息的变量直接输出到终端日志。

## 3. 使用 curl 测试

```bash
curl --proxy "$HTTP_PROXY" \
  --connect-timeout 10 \
  --max-time 30 \
  --verbose \
  https://example.com/
```

## 4. 清除变量

```bash
unset HTTP_PROXY HTTPS_PROXY ALL_PROXY NO_PROXY
```

## 5. systemd 服务为什么可能不读取终端变量？

systemd 管理的服务通常不会自动继承某个用户交互式 Shell 中临时设置的环境变量。服务需要按自身运行环境配置变量。

如确实需要为服务配置代理，应遵循组织的密钥管理规范，避免把明文凭据写入其他用户可读取的 unit 文件或日志。

## 6. 容器和应用程序

Docker 容器、包管理器、浏览器和其他应用可能需要单独配置代理。应查阅具体软件的官方文档，并分别验证请求是否通过预期代理发送。

## 相关文档

- [Windows 代理配置](02-windows-configuration.md)
- [macOS 代理配置](03-macos-configuration.md)
- [代理环境变量参考](10-environment-variables.md)
