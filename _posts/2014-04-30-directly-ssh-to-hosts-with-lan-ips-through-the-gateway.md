---
title: "SSH Through a Gateway to Internal Networks Using ProxyCommand"
date: 2014-04-30 04:38:18 +0000
modified: 2026-04-11 16:22:40 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /directly-ssh-to-hosts-with-lan-ips-through-the-gateway/
---

You’ve got internal hosts on RFC 1918 addresses (10.0.3.0/24, 172.16.0.0/12, etc.) behind a gateway, and you need SSH access to them from your workstation. Traditional solutions involve iptables port forwarding, non-standard ports, and a maintenance nightmare. ProxyCommand offers a cleaner approach: direct SSH connections to internal IPs that actually work.

## How ProxyCommand Works

SSH’s `ProxyCommand` directive executes a command to establish your connection. Instead of connecting directly to an unreachable internal IP:

1.  SSH connects to your gateway normally
2.  The gateway pipes the connection through `nc` (netcat) or `socat`
3.  Those tools bridge your SSH client to the internal host’s SSH daemon
4.  From your perspective, you’ve SSH’d directly to the internal IP

It’s transparent. No persistent tunnels. No weird port mappings to remember.

## Prerequisites

- Key-based SSH access to the gateway (no passwords in the proxy chain)
- `nc` or `socat` installed on the gateway
- SSH client on your local machine (OpenSSH 7.3+)

## Basic Configuration

Edit `~/.ssh/config`:

    Host 10.0.3.*
      ProxyCommand ssh -q gateway.example.org nc %h %p

Secure it:

``` bash
chmod 600 ~/.ssh/config
```

That’s it. Now connect:

``` bash
ssh user@10.0.3.100
ssh 10.0.3.50
```

Your SSH client expands this to:

``` bash
ssh -q gateway.example.org nc 10.0.3.100 22
```

The gateway executes `nc 10.0.3.100 22`, which opens a TCP tunnel. Your local SSH client communicates through it as if you’re connected directly.

## Expanding Across Multiple Networks

Add more patterns:

    Host 10.0.3.* 10.0.4.*
      ProxyCommand ssh -q gateway.example.org nc %h %p

    Host 172.16.*.*
      ProxyCommand ssh -q gateway.example.org nc %h %p

For multiple gateways serving different subnets:

    Host 10.0.3.*
      ProxyCommand ssh -q gateway-a.example.org nc %h %p

    Host 10.0.4.*
      ProxyCommand ssh -q gateway-b.example.org nc %h %p

## Practical Options

**Non-standard gateway SSH port:**

    Host 10.0.3.*
      ProxyCommand ssh -q -p 2222 gateway.example.org nc %h %p

**Different username on gateway:**

    Host 10.0.3.*
      ProxyCommand ssh -q sysadmin@gateway.example.org nc %h %p

**Using socat instead of netcat:**

    Host 10.0.3.*
      ProxyCommand ssh -q gateway.example.org socat - TCP:%h:%p

**Combined with other SSH directives:**

    Host 10.0.3.*
      ProxyCommand ssh -q gateway.example.org nc %h %p
      User sysadmin
      IdentityFile ~/.ssh/id_rsa_internal
      StrictHostKeyChecking accept-new
      ConnectTimeout 5

## Modern Alternative: SSH Jump (-J)

OpenSSH 7.3+ supports the `-J` flag, which is essentially syntactic sugar for ProxyCommand:

``` bash
ssh -J gateway.example.org user@10.0.3.100
```

For a permanent config, use the `ProxyJump` directive:

    Host 10.0.3.*
      ProxyJump gateway.example.org
      User sysadmin

`ProxyJump` is cleaner and recommended for new setups. It handles the netcat plumbing automatically. Use `ProxyCommand` when you need fine-grained control or logging.

## Debugging

Connection hanging or failing? Test methodically.

**Verify gateway access:**

``` bash
ssh -v gateway.example.org
```

**Check netcat on the gateway:**

``` bash
ssh gateway.example.org which nc
```

**Test the proxy command directly:**

``` bash
ssh -v -q gateway.example.org nc 10.0.3.100 22
```

This should hang while connecting to the internal host’s SSH daemon (press Ctrl+C). If it fails immediately, the internal host is unreachable from the gateway.

**Test from gateway to internal host:**

``` bash
ssh gateway.example.org nc -zv 10.0.3.100 22
```

The `-z` flag just checks if the port is open without establishing a full connection.

**Full verbose SSH test:**

``` bash
ssh -vvv user@10.0.3.100
```

Look for lines starting with `Executing proxy command` to confirm ProxyCommand is being invoked.

## Security Considerations

- **Keys only:** ProxyCommand must use key-based authentication. Password prompts in the proxy chain hang your session and expose you to man-in-the-middle attacks.
- **Gateway access control:** Restrict SSH access to the gateway (IP whitelisting, firewall rules).
- **Network isolation:** This assumes your internal network is properly isolated from untrusted networks.
- **Audit logging:** Enable logging on the gateway to track who’s accessing internal hosts.
- **Command restrictions:** For tighter security, configure sshd on the gateway with `Match` blocks to limit what commands can be proxied.

## When to Use Alternatives

**For one-off connections:**

``` bash
ssh -J gateway.example.org user@10.0.3.100
```

**For broader network access (not just SSH):**\
Consider a VPN. ProxyCommand is SSH-specific.

**For teams and complex access control:**\
A bastion host with restricted commands and audit logging beats simple ProxyCommand.

## Summary

ProxyCommand lets you treat internal hosts as if they’re directly reachable, without port forwarding chaos or firewall rules. Set it once in `~/.ssh/config`, authenticate with keys, and you’re done. For modern OpenSSH, `ProxyJump` is the simpler option. Both scale well and integrate seamlessly with your existing SSH setup.
