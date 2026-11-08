---
title: "Setting Up a SOCKS Proxy Over SSH Tunnels"
date: 2013-07-12 16:31:56 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/proxy-using-ssh-tunnel/
---

A SOCKS5 proxy tunneled through SSH provides encrypted communication between your client and a remote server. This is useful for bypassing network restrictions, securing connections on untrusted networks, or routing traffic through a trusted server.

## Basic Setup

The simplest approach uses SSH’s dynamic port forwarding with the `-D` flag:

``` bash
ssh -D 8080 username@sshd_server
```

This creates a SOCKS5 proxy listening on `127.0.0.1:8080`. Configure your application (browser, curl, etc.) to use this proxy:

- Firefox: Preferences → Network Settings → Manual proxy configuration → SOCKS Host: `127.0.0.1`, Port: `8080`
- curl: `curl --socks5 127.0.0.1:8080 https://example.com`
- Environment variable: `export SOCKS_SERVER=127.0.0.1:8080`

To allow other machines on your network to use the proxy, bind to all interfaces:

``` bash
ssh -D "*:8080" username@sshd_server
```

Or bind to a specific IP address:

``` bash
ssh -D 192.168.1.10:8080 username@sshd_server
```

## How It Works

SSH’s dynamic port forwarding allocates a local socket that listens on the specified port. When a connection arrives, SSH forwards it through the encrypted tunnel. The SOCKS protocol running over the tunnel determines the destination from the client application’s request, then establishes a connection from the remote server to that destination.

## Practical Command Combinations

Combine `-D` with other SSH flags for different scenarios:

- `-N`: Don’t execute a remote command (useful for port forwarding only)
- `-f`: Background the SSH process after connection
- `-C`: Enable gzip compression
- `-T`: Disable pseudo-TTY allocation
- `-q`: Suppress warnings and diagnostics

Run a persistent proxy in the background:

``` bash
ssh -CnfND 8080 username@sshd_server
```

This backgrounds the process, compresses data, and disables TTY allocation. To kill it:

``` bash
pkill -f "ssh.*-D.*8080"
```

Or find the PID and kill it manually:

``` bash
ps aux | grep "ssh.*-D"
kill <PID>
```

For an interactive proxy that stays in the foreground:

``` bash
ssh -CTND 8080 username@sshd_server
```

Press Ctrl+C to disconnect.

## Port Forwarding to Other Proxy Servers

If you have a traditional proxy server (like squid) behind the SSH server, use local port forwarding instead:

``` bash
ssh -L 8080:proxy.internal:3128 username@sshd_server
```

This forwards local port 8080 to `proxy.internal:3128` on the remote network, accessible at `127.0.0.1:8080`.

## Using with curl and wget

Test the proxy with curl:

``` bash
curl --socks5 127.0.0.1:8080 https://example.com
```

For wget, configure `~/.wgetrc`:

    socks_server = 127.0.0.1
    socks_version = 5

## Integration with systemd

For persistent proxy tunnels, create a systemd service:

``` ini
[Unit]
Description=SSH SOCKS Proxy
After=network-online.target

[Service]
Type=simple
User=your_user
ExecStart=/usr/bin/ssh -NT -D 8080 username@sshd_server
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Save as `~/.config/systemd/user/ssh-socks-proxy.service`, then:

``` bash
systemctl --user enable ssh-socks-proxy
systemctl --user start ssh-socks-proxy
systemctl --user status ssh-socks-proxy
```

## SSH Configuration File

Define proxies in `~/.ssh/config` for convenience:

    Host socks-proxy
        HostName sshd_server
        User username
        DynamicForward 8080
        Compression yes
        ControlMaster auto
        ControlPath ~/.ssh/control-%C

Then simply run:

``` bash
ssh -N socks-proxy
```

## Security Considerations

- Only trust SSH servers you control or fully trust
- Use SSH key authentication instead of passwords
- Consider adding `-o StrictHostKeyChecking=accept-new` with care
- Monitor connection logs with `journalctl -f` if using systemd
- The proxy only encrypts traffic between client and SSH server; destination servers see the remote server’s IP

## Troubleshooting

Check connectivity:

``` bash
ssh -vvv -D 8080 username@sshd_server
```

Verify the proxy is listening:

``` bash
netstat -tuln | grep 8080
ss -tuln | grep 8080
```

Test with a simple HTTP request:

``` bash
curl -v --socks5 127.0.0.1:8080 http://example.com
```
