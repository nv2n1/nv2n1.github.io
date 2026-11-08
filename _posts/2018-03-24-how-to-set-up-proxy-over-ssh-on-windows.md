---
title: "Setting Up SSH Tunneling as a Proxy on Windows"
date: 2018-03-24 08:14:48 +0000
layout: post
canonical: https://www.systutorials.com/how-to-set-up-proxy-over-ssh-on-windows/
---

SSH tunneling is one of the most reliable ways to create a secure proxy on Windows. You can route traffic through a remote SSH server, encrypting your connection and bypassing local network restrictions.

## Prerequisites

You’ll need:

- An SSH server with valid credentials
- An SSH client (Windows 10/11 includes OpenSSH, or use PuTTY, Git Bash, or WSL)
- The remote server’s hostname/IP and SSH port
- A local port that isn’t already in use

## Using OpenSSH (Built-in on Windows 10+)

Windows 10 and later include OpenSSH by default. Open PowerShell or Command Prompt and create a SOCKS5 proxy:

``` bash
ssh -D 1080 username@remote-host.com
```

This binds a SOCKS5 proxy to `localhost:1080`. The `-D` flag specifies dynamic port forwarding.

If your SSH server uses a non-standard port:

``` bash
ssh -D 1080 -p 2222 username@remote-host.com
```

Keep this terminal window open while using the proxy. To run it in the background on Windows, use:

``` powershell
Start-Process ssh -ArgumentList "-D 1080 username@remote-host.com" -WindowStyle Hidden
```

## Using WSL (Windows Subsystem for Linux)

For more advanced scenarios, use WSL:

``` bash
wsl ssh -D 1080 username@remote-host.com
```

This gives you full Linux SSH capabilities with better process management.

## Configuring Applications to Use the Proxy

### Browser Configuration

For Firefox:

1.  Open Preferences → Network Settings
2.  Scroll to “Proxy”
3.  Select “Manual proxy configuration”
4.  Enter `127.0.0.1` for SOCKS Host and `1080` for Port
5.  Select SOCKS v5

For Chromium-based browsers, use command-line arguments:

``` powershell
chrome --proxy-server="socks5://127.0.0.1:1080"
```

### System-wide Proxy (Windows Settings)

Windows doesn’t natively support SOCKS proxies at the system level. Use third-party tools like:

- **Proxifier** — GUI application that routes any Windows traffic through a SOCKS proxy
- **ProxyCap** — Similar functionality with detailed filtering rules

## Setting Up with Authentication Key

If you use SSH keys instead of passwords:

``` bash
ssh -D 1080 -i C:\Users\YourName\.ssh\id_rsa username@remote-host.com
```

## Persistent SSH Tunnel with Automatic Reconnection

Create a batch script that reconnects if the tunnel drops:

```batch
@echo off
:loop
ssh -D 1080 username@remote-host.com
echo SSH tunnel disconnected, reconnecting...
timeout /t 5
goto loop
```

Save as `ssh-tunnel.bat` and run it. For production use, consider using a service wrapper or Task Scheduler.

## Using PuTTY for GUI Management

If you prefer a graphical interface:

1.  Open PuTTY
2.  Enter your remote host under “Session”
3.  Navigate to Connection → SSH → Tunnels
4.  Select “Dynamic” and enter local port `1080`
5.  Click “Add”
6.  Open the connection
7.  Configure your browser to use `127.0.0.1:1080` as SOCKS5 proxy

## Performance and Security Considerations

- **Compression**: Add `-C` flag to reduce bandwidth: `ssh -D 1080 -C username@remote-host.com`
- **Keep-alive**: Add `-o ServerAliveInterval=60` to prevent timeout during idle periods
- **Only use SOCKS5**: SOCKS4 lacks authentication; always use SOCKS5
- **Verify host keys**: Always verify the remote server’s SSH fingerprint before first connection
- **Firewall rules**: Ensure your firewall allows outbound SSH (port 22 or custom) to the remote server

## Troubleshooting

**Connection refused on localhost:1080**: Ensure the SSH tunnel is running and the port isn’t blocked by Windows Firewall.

**SSH_AUTH_FAIL**: Verify your username and password/key are correct. Test with `ssh -v username@remote-host.com` for verbose output.

**Slow performance**: Enable compression (`-C`) and check remote server load with `ssh username@remote-host.com 'top'`.

**Port already in use**: Check with `netstat -ano | findstr :1080` and use a different port if needed.
