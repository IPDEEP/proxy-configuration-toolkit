# 08｜DNS 与代理网络诊断

DNS 解析和代理转发是相关但不同的网络阶段。实际行为取决于代理协议、客户端实现和应用配置。

## 1. 本地 DNS 与代理侧 DNS

在支持相关模式的 SOCKS 客户端中：

- `socks5://` 通常由本地客户端解析目标域名；
- `socks5h://` 通常将目标域名交给代理侧解析。

并非所有应用都支持这两种模式，其他代理协议也可能有不同实现。

## 2. 查看本机 DNS 解析结果

Windows PowerShell：

```powershell
Resolve-DnsName example.com
```

macOS / Linux：

```bash
nslookup example.com
```

或：

```bash
dig example.com
```

这些命令查看本机当前解析器的查询结果，不能单独证明某个应用的代理请求采用了哪种 DNS 路径。

## 3. 为什么不同检测结果可能不同？

常见原因包括：

- DNS 服务商不同；
- 缓存和 TTL 不同；
- CDN 调度策略不同；
- 地区网络不同；
- 分流 DNS 或企业内网 DNS；
- 查询时间不同；
- 应用实际没有使用预期代理。

## 4. DNS 泄露测试的边界

DNS 测试结果反映特定设备、浏览器、网络和测试时刻的观测情况，不代表所有软件、所有协议和未来连接都具有相同表现。

不要使用敏感内部域名或私人网络地址进行公开测试。

## 5. 相关检测资源

- [ToDetect IP 地址查询](https://www.todetect.net/ip/)
- [IPDEEP DNS 泄露检测专题](https://www.todetect.cn/dns-leak/)

第二个链接来自项目资料中的专题栏目记录；发布前应确认当前页面 URL 是否仍有效。检测工具只能提供辅助信息，不能替代对具体客户端网络路径的检查。
