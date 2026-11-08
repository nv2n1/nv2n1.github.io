---
title: "SSH Keep-Alive: Preventing Idle Connection Timeouts"
date: 2015-09-13 03:44:41 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-keep-linux-ssh-session-alive-from-disconnecting/
---

SSH connections dropping during idle periods is a persistent issue in production environments. Both client and server configurations provide built-in keep-alive mechanisms designed specifically for this problem. Stop running `while true; do uptime; sleep 30; done` — there are proper solutions.

## Client-side configuration

### Per-user SSH config

Add to `~/.ssh/config`:

    Host *
        ServerAliveInterval 60
        ServerAliveCountMax 3

`ServerAliveInterval 60` sends a keep-alive packet every 60 seconds. `ServerAliveCountMax 3` means the connection drops after 3 missed responses (180 seconds total), preventing hung sessions. Adjust the interval based on your firewall’s idle timeout — common values are 60, 120, or 300 seconds.

For a single connection without editing config:

``` bash
ssh -o ServerAliveInterval=60 -o ServerAliveCountMax=3 user@example.com
```

### System-wide client configuration

Edit `/etc/ssh/ssh_config` to apply settings to all users on the system:

    Host *
        ServerAliveInterval 60
        ServerAliveCountMax 3

Individual user configs in `~/.ssh/config` override these system-wide settings.

## Server-side configuration

Server-side configuration is the better approach in most environments — it works regardless of client configuration and requires no per-user setup.

Edit `/etc/ssh/sshd_config`:

    ClientAliveInterval 60
    ClientAliveCountMax 3

The server sends keep-alive probes every 60 seconds. After 3 missed responses, the connection terminates. This prevents zombie sessions from consuming resources.

Reload sshd to apply changes:

``` bash
sudo systemctl reload sshd
```

Verify the syntax without reloading:

``` bash
sudo sshd -t
```

Existing connections retain their original parameters — only new connections pick up the new settings.

## Choosing intervals based on network conditions

**Reliable networks** (office, data center): Use `ServerAliveInterval 300` (5 minutes). This reduces unnecessary traffic while maintaining stability.

**Less stable connections** (VPN, mobile, wireless): Use `ServerAliveInterval 60` or `120`. Shorter intervals catch disconnects faster but increase bandwidth usage slightly.

**Long-running commands**: Keep-alive messages don’t interfere with active sessions. The interval only matters during idle time.

**Jump hosts/bastion servers**: Configure keep-alive on both the bastion’s sshd and your client config — multiple network hops compound connection instability.

## Troubleshooting

**Connection still drops despite configuration**: Your firewall or NAT gateway may have a lower idle timeout than your SSH keep-alive interval. Lower the interval below the gateway’s timeout — if it’s 5 minutes, use 4 minutes (240 seconds).

**TCPKeepAlive vs ServerAliveInterval**: `TCPKeepAlive` (enabled by default) relies on OS-level TCP keep-alive, which varies across networks. `ServerAliveInterval` sends SSH-level packets and is more reliable. Use `ServerAliveInterval` for predictable results across different environments.

**No effect after editing sshd_config**: Reload sshd with `systemctl reload sshd`. Existing connections use their original parameters.

## Testing your configuration

Create a test SSH session and monitor for keep-alive packets:

``` bash
ssh -vv user@example.com
```

The `-vv` flag shows debug output including keep-alive packets. You should see messages like `debug1: Sending SSH2_MSG_GLOBAL_REQUEST` at regular intervals during idle time.

Alternatively, use tcpdump to verify packets are actually being sent:

``` bash
sudo tcpdump -i any 'tcp port 22' -n
```

Look for traffic during periods of inactivity — packets at your configured interval indicate keep-alive is working.

## Production recommendations

**Default approach**: Configure `ClientAliveInterval 60` and `ClientAliveCountMax 3` on the server. This is the most maintainable and requires no per-user client configuration.

**Mixed client types**: Also set `ServerAliveInterval 60` in your personal `~/.ssh/config` as a secondary safety net, especially when connecting through corporate proxies or multiple NAT layers.

**Monitoring**: Check `/var/log/auth.log` (or `/var/log/secure` on RHEL systems) for `Timeout, client not responding` messages. These indicate problematic timeouts where you should lower your intervals.

**Unusual scenarios**: For mosh (mobile shell) or when standard SSH keep-alive fails, consider `TCPKeepAlive yes` combined with lower `ServerAliveInterval` values, or use `ProxyCommand` with `-N` for port forwarding scenarios.
