---
title: "SSH Port Forwarding: Local, Remote, and Dynamic Tunnels"
date: 2013-09-29 12:56:21 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/port-forwarding-using-ssh-tunnel/
---

SSH port forwarding lets you tunnel network traffic through an encrypted connection, making it essential for accessing services on restricted networks, exposing local services safely, or routing traffic through a jump host. This guide covers the three main types and production-ready practices.

## Local Forwarding

Local forwarding listens on your local machine and relays connections through the SSH tunnel to a remote service. The SSH server acts as a relay—the destination service can be any machine reachable from the SSH server’s network.

``` bash
ssh -L 8080:remote-server:3306 user@ssh-server
```

This listens on your localhost port 8080 and forwards to `remote-server:3306` through the tunnel. Connect locally with:

``` bash
mysql -h 127.0.0.1 -P 8080
```

For non-standard SSH ports:

``` bash
ssh -L 8080:remote-server:3306 -p 2222 user@ssh-server
```

By default, local forwards bind only to loopback. To allow other processes on your machine to use the tunnel:

``` bash
ssh -L 0.0.0.0:8080:remote-server:3306 user@ssh-server
```

**Warning:** This exposes the tunnel to any local process. Only bind to `0.0.0.0` when necessary. A safer approach is to allow specific local services to connect through a loopback-bound tunnel using application configuration or local proxies.

Forward multiple ports in one session:

``` bash
ssh -L 3306:db-server:3306 -L 5432:db-server:5432 -L 8080:app-server:80 user@ssh-server
```

This reduces connection overhead compared to multiple SSH sessions.

## Remote Forwarding

Remote forwarding works in reverse: the SSH server listens on a remote port and forwards connections back to your local machine. This is essential when you’re behind a firewall and need to expose local services to remote machines.

``` bash
ssh -R 9000:localhost:8080 user@ssh-server
```

This causes `ssh-server` to listen on port 9000 and relay connections back to your local port 8080. Example: exposing a development server to a production team:

``` bash
ssh -R 8888:localhost:3000 deploy@prod-server
```

Now anyone accessing `prod-server:8888` reaches your local port 3000.

By default, remote forwards only bind to loopback on the SSH server (accessible locally as `localhost:9000`). To allow remote machines to connect, configure the SSH server’s `/etc/ssh/sshd_config`:

    GatewayPorts yes

Available options:

- `no` (default): Bind only to loopback
- `yes`: Bind to wildcard address (`0.0.0.0`)
- `clientspecified`: Client specifies the bind address using `ssh -R [bind_address:]port:host:port`

After editing, reload sshd:

``` bash
sudo systemctl reload ssh
```

## Dynamic Forwarding (SOCKS5 Proxy)

Create a SOCKS5 proxy to forward all traffic from compatible clients through the tunnel:

``` bash
ssh -D 1080 user@ssh-server
```

This creates a SOCKS5 server on `localhost:1080`. Route traffic through it with curl:

``` bash
curl --socks5 127.0.0.1:1080 https://example.com
```

In Firefox: **Settings** → **Network** → **Proxy** → Manual proxy configuration → SOCKS Host: `127.0.0.1`, Port: `1080`.

## Persistent Tunnels with autossh

For long-lived tunnels, use `autossh` to automatically reconnect on failure. First, install it:

``` bash
sudo apt install autossh          # Debian/Ubuntu
sudo dnf install autossh          # RHEL/Fedora
sudo pacman -S autossh            # Arch
```

Run persistent local forwarding:

``` bash
autossh -M 20000 -f -N -L 8080:remote-server:3306 user@ssh-server
```

For remote forwarding:

``` bash
autossh -M 20001 -f -N -R 8888:localhost:3000 deploy@prod-server
```

For SOCKS proxy:

``` bash
autossh -M 20002 -f -D 1080 user@ssh-server
```

The `-M` port is used for connectivity testing; choose an unused port. The `-f` flag daemonizes the process.

To stop a background tunnel, find and kill it:

``` bash
ps aux | grep autossh
kill <pid>
```

## SSH Config for Persistent Tunnels

Define tunnels in `~/.ssh/config` to avoid manual commands:

    Host tunnel-db
        HostName ssh-server.example.com
        User deploy
        LocalForward 3306 db-server:3306
        LocalForward 5432 db-server:5432
        ControlMaster auto
        ControlPath ~/.ssh/control-tunnel-db
        ControlPersist 3600

Connect with:

``` bash
ssh tunnel-db -N -f
```

The `ControlMaster` settings enable connection multiplexing, reducing SSH overhead. `ControlPersist 3600` keeps the master connection alive for 1 hour, reusing it for subsequent commands.

For automation, combine with autossh:

``` bash
autossh -M 20000 -f -N -O ChecksumHost=yes tunnel-db
```

## Performance Considerations

SSH tunneling adds encryption overhead. For typical use cases (database access, web services), it’s adequate. For high-throughput scenarios:

- Enable compression with `-C` for high-latency links (trade CPU for bandwidth)
- Use persistent connections with multiplexing to avoid repeated handshakes
- Consider kernel-based forwarding (iptables, nftables) for trusted, high-throughput scenarios
- Monitor tunnel latency with `ssh -v` to identify bottlenecks

Check active tunnel statistics:

``` bash
ss -tnp | grep ssh
```

## Security Best Practices

- **Use SSH keys**, not passwords. For automated tunnels, use key-based authentication with `ssh-agent` or systemd user services
- **Restrict SSH keys** in your authorized_keys file to prevent unintended access:

<!-- -->

    restrict,command="/bin/false" ssh-rsa AAAA...

The `restrict` keyword disables port/agent/X11 forwarding for that key (OpenSSH 8.2+). `command="/bin/false"` prevents command execution.

- **Only forward what you need.** The SSH server can see unencrypted traffic between itself and the destination—don’t over-expose services
- **Avoid binding to 0.0.0.0** unless absolutely necessary
- **Audit active tunnels regularly:**

``` bash
ss -tnp | grep -E 'LISTEN.*ssh'
```

- **Use a jump host** (ProxyJump) for additional security when possible:

``` bash
ssh -J jump-host.example.com tunnel-db -N -f
```

This chains connections through the jump host instead of direct port forwarding, providing better auditability and access control.
