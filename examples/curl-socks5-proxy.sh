#!/usr/bin/env bash
set -euo pipefail

: "${SOCKS_PROXY:?请先设置 SOCKS_PROXY 环境变量}"

# 若客户端与服务端支持 socks5h，可将目标域名交由代理侧解析。
curl \
  --proxy "$SOCKS_PROXY" \
  --connect-timeout 10 \
  --max-time 30 \
  --verbose \
  https://example.com/
