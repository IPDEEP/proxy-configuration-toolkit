#!/usr/bin/env bash
# 仅对当前 Shell 及其子进程生效。不要将真实凭据提交到 Git。

export HTTP_PROXY="http://proxy.example.net:10000"
export HTTPS_PROXY="$HTTP_PROXY"
export NO_PROXY="localhost,127.0.0.1,::1"

echo "当前 Shell 的代理环境变量示例已设置。"
