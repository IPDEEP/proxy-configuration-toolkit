# 仅对当前 PowerShell 进程及其子进程生效。
# 请在本地替换占位符，不要提交真实凭据。

$env:HTTP_PROXY = "http://proxy.example.net:10000"
$env:HTTPS_PROXY = $env:HTTP_PROXY
$env:NO_PROXY = "localhost,127.0.0.1,::1"

Write-Output "当前 PowerShell 的代理环境变量示例已设置。"
