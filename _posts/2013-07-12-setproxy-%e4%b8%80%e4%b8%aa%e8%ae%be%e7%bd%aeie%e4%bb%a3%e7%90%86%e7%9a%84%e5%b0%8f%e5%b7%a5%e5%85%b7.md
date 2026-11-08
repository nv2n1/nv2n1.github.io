---
title: "Managing Proxy Settings on Windows via Command Line"
date: 2013-07-12 16:47:43 +0000
layout: post
canonical: https://www.systutorials.com/setproxy-%e4%b8%80%e4%b8%aa%e8%ae%be%e7%bd%aeie%e4%bb%a3%e7%90%86%e7%9a%84%e5%b0%8f%e5%b7%a5%e5%85%b7/
---

Managing proxy settings through the GUI is tedious, especially when you need to switch between multiple proxy servers frequently. Rather than hunting through settings menus each time, command-line tools eliminate friction and enable scripted deployments across your infrastructure.

The original SetProxy tool is outdated and incompatible with modern Windows versions. Use `netsh` or PowerShell instead—both are built-in with no compilation or installation required.

## Setting WinHTTP Proxy with netsh

WinHTTP is the system-wide proxy layer used by most applications, including Edge, curl, and many CLI tools:

``` bash
netsh winhttp set proxy proxy-server="http=192.168.1.100:8080;https=192.168.1.100:8080" bypass-list="localhost;127.0.0.1;<local>"
```

Breaking this down:

- `proxy-server` accepts separate entries for HTTP and HTTPS
- `bypass-list` specifies hosts that bypass the proxy
- `<local>` is a built-in token that matches any single-label hostname

View current settings:

``` bash
netsh winhttp show proxy
```

Clear the proxy entirely:

``` bash
netsh winhttp reset proxy
```

## Per-User Registry Proxy (Legacy Applications)

Some older applications read proxy settings from the Registry instead of WinHTTP. This affects Internet Explorer and similar legacy tools:

``` powershell
$regPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
Set-ItemProperty -Path $regPath -Name ProxyServer -Value "192.168.1.100:8080"
Set-ItemProperty -Path $regPath -Name ProxyEnable -Value 1
```

Disable it:

``` powershell
Set-ItemProperty -Path $regPath -Name ProxyEnable -Value 0
```

If you need separate HTTP and HTTPS proxies, format them as a single value:

``` powershell
$regPath = "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
Set-ItemProperty -Path $regPath -Name ProxyServer -Value "http=192.168.1.100:8080;https=192.168.1.100:8443"
Set-ItemProperty -Path $regPath -Name ProxyEnable -Value 1
```

## Batch File Wrappers for Quick Access

Create reusable batch files to toggle proxies without opening a terminal.

**proxy-enable.bat:**

```batch
@echo off
netsh winhttp set proxy proxy-server="http=192.168.1.100:8080;https=192.168.1.100:8080" bypass-list="localhost;127.0.0.1;<local>"
echo Proxy enabled: 192.168.1.100:8080
pause
```

**proxy-disable.bat:**

```batch
@echo off
netsh winhttp reset proxy
echo Proxy disabled
pause
```

Save these to a folder on your PATH or create desktop shortcuts by right-clicking the batch file and selecting “Send to \> Desktop (create shortcut)”. Double-click to apply settings instantly.

## Automated Proxy Rotation

For environments requiring frequent proxy switches, rotate through a list randomly:

``` powershell
$proxies = @(
    "proxy1.internal:8080",
    "proxy2.internal:8080",
    "proxy3.internal:8080"
)

$currentIndex = Get-Random -Minimum 0 -Maximum $proxies.Length
$proxy = $proxies[$currentIndex]

netsh winhttp set proxy proxy-server="http=$proxy;https=$proxy"
Write-Host "Proxy set to: $proxy"
```

For sequential rotation with state persistence, use a configuration file:

``` powershell
$configFile = "$env:TEMP\proxy-index.txt"
$lastIndex = if (Test-Path $configFile) { [int](Get-Content $configFile) } else { 0 }

$proxies = @(
    "proxy1.internal:8080",
    "proxy2.internal:8080",
    "proxy3.internal:8080"
)

$nextIndex = ($lastIndex + 1) % $proxies.Length
$proxy = $proxies[$nextIndex]

netsh winhttp set proxy proxy-server="http=$proxy;https=$proxy"
$nextIndex | Set-Content $configFile
Write-Host "Proxy set to: $proxy (index $nextIndex)"
```

## Applying Proxy to Scheduled Tasks

When running applications or scripts as a service account, WinHTTP proxy settings are tied to the user context. If your task runs as SYSTEM, configure WinHTTP for that account:

``` powershell
# Run as Administrator
# For SYSTEM context tasks, hardcode proxy in application config instead
$regPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Internet Settings"
Set-ItemProperty -Path $regPath -Name ProxyServer -Value "192.168.1.100:8080"
Set-ItemProperty -Path $regPath -Name ProxyEnable -Value 1
```

Alternatively, hardcode the proxy in application configuration files or environment variables rather than relying on system-wide settings:

``` powershell
[Environment]::SetEnvironmentVariable("HTTP_PROXY", "http://192.168.1.100:8080", "Machine")
[Environment]::SetEnvironmentVariable("HTTPS_PROXY", "http://192.168.1.100:8080", "Machine")
```

## Verifying Proxy Configuration

Check what your system sees across different layers:

``` powershell
# WinHTTP proxy (system-wide)
netsh winhttp show proxy

# PowerShell's built-in proxy
$env:HTTP_PROXY

# Internet Explorer / Legacy apps (Registry)
Get-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings"

# Machine-level environment variables
[Environment]::GetEnvironmentVariable("HTTP_PROXY", "Machine")
```

Note that different components may use different proxy configurations. Applications that use WinHTTP see `netsh winhttp` settings, while older apps may only respect Registry settings. Language runtimes (Python, Node.js) typically respect `HTTP_PROXY` and `HTTPS_PROXY` environment variables.

## SOCKS Proxy Support

WinHTTP does not natively support SOCKS proxies. If you need SOCKS, use one of these approaches:

- Configure applications individually (`curl` via `--socks5`, `ssh` via `ProxyCommand`)
- Use a local HTTP-to-SOCKS converter like Privoxy or Tinyproxy
- Set environment variables for language-specific tools (Python, Node.js, Go, Rust) that understand SOCKS natively

Example with Python:

``` bash
set HTTPS_PROXY=socks5://localhost:1080
python script.py
```

For persistent SOCKS support on Windows, consider running a local HTTP proxy that translates to SOCKS:

``` bash
# Install Privoxy, configure with SOCKS parent
# Edit privoxy config to forward to SOCKS5
listen-address 127.0.0.1:8118
forward-socks5 / localhost:1080 .
```

Then configure WinHTTP to use the local proxy:

``` bash
netsh winhttp set proxy proxy-server="http=127.0.0.1:8118;https=127.0.0.1:8118"
```
