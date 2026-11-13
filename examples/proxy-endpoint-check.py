#!/usr/bin/env python3
"""Check whether a proxy endpoint accepts a TCP connection.

The proxy URL is requested with hidden terminal input so credentials are not
placed in shell history or printed. This is an endpoint reachability check:
it does not authenticate to the proxy, establish a tunnel, or verify egress.
"""
from __future__ import annotations

import argparse
import getpass
import socket
import ssl
import sys
from urllib.parse import urlsplit


ALLOWED_SCHEMES = {"http", "https", "socks5", "socks5h"}


def parse_endpoint(raw: str) -> tuple[str, str, int, bool]:
    try:
        parsed = urlsplit(raw.strip())
        scheme = parsed.scheme.lower()
        host = parsed.hostname
        port = parsed.port
    except ValueError as exc:
        raise ValueError("代理 URL 格式无效，请检查 IPv6 方括号和端口。") from exc

    if scheme not in ALLOWED_SCHEMES:
        raise ValueError("协议必须为 http、https、socks5 或 socks5h。")
    if not host:
        raise ValueError("代理 URL 缺少主机名或 IP 地址。")
    if port is None or not 1 <= port <= 65535:
        raise ValueError("请在代理 URL 中明确填写 1–65535 范围内的端口。")
    if parsed.path not in ("", "/") or parsed.query or parsed.fragment:
        raise ValueError("代理端点 URL 不应包含路径、查询参数或片段。")

    has_credentials = parsed.username is not None or parsed.password is not None
    normalized_host = host if ":" in host else host.encode("idna").decode("ascii")
    return scheme, normalized_host, port, has_credentials


def main() -> int:
    parser = argparse.ArgumentParser(
        description="检查代理主机端口是否可建立 TCP 连接；不会输出代理凭据。"
    )
    parser.add_argument("--timeout", type=float, default=8.0, help="连接超时秒数，默认 8")
    args = parser.parse_args()

    if args.timeout <= 0:
        parser.error("--timeout 必须大于 0")

    raw = getpass.getpass("请输入代理 URL（输入内容不回显）：").strip()
    try:
        scheme, host, port, has_credentials = parse_endpoint(raw)
    except (ValueError, UnicodeError) as exc:
        print(f"参数错误：{exc}", file=sys.stderr)
        return 2

    connection = None
    try:
        connection = socket.create_connection((host, port), timeout=args.timeout)
        if scheme == "https":
            context = ssl.create_default_context()
            connection = context.wrap_socket(connection, server_hostname=host)
            print("TLS 握手：成功（证书链和主机名已由系统信任库验证）")

        print(f"协议：{scheme}")
        print(f"端点：{host}:{port}")
        print("TCP 连通性：成功")
        print(f"URL 中包含认证信息：{'是' if has_credentials else '否'}")
        print("注意：本工具没有执行代理认证、CONNECT/SOCKS 握手或出口 IP 检查。")
        return 0
    except socket.timeout:
        print("连接超时：请检查网络、主机、端口及服务端状态。", file=sys.stderr)
    except ssl.SSLError:
        print("TLS 握手失败：请检查 HTTPS 代理证书和 TLS 配置。", file=sys.stderr)
    except OSError:
        print("无法连接代理端点：请检查主机名、端口、防火墙和网络路由。", file=sys.stderr)
    finally:
        if connection is not None:
            connection.close()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
