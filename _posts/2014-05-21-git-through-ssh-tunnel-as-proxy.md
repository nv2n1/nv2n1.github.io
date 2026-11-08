---
title: "Tunneling Git Traffic Through SSH Proxies"
date: 2014-05-21 14:55:13 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/git-through-ssh-tunnel-as-proxy/
---

You often need to access a Git server that only accepts internal connections, but you have SSH access to an intermediate host that can reach it. This is common in corporate environments where the Git server sits behind a firewall. You can tunnel Git traffic through the intermediate host without manually managing tunnels for each operation.

The setup looks like this:

    laptop --> proxy --> git-server

When you run `git push`, `git pull`, or any Git command, the connection automatically routes through the proxy to reach the Git server.

## Prerequisites

Ensure passwordless SSH authentication works from your local machine to the proxy host. This avoids repeated password prompts during Git operations.

Generate or use an existing SSH key:

``` bash
ssh-keygen -t ed25519 -C "your-email@example.com"
ssh-copy-id -i ~/.ssh/id_ed25519.pub user@proxy.example.com
```

Verify passwordless login:

``` bash
ssh user@proxy.example.com "echo 'Connection successful'"
```

If using the older `ProxyCommand` method (not recommended), confirm that netcat (`nc`) or `socat` is installed on the proxy host:

``` bash
ssh user@proxy.example.com "which nc"
```

## ProxyJump (Recommended Approach)

SSH 7.3+ (released 2016) supports `ProxyJump`, which is the modern, recommended method. It’s simpler than `ProxyCommand` and doesn’t require netcat on the proxy.

Add this to `~/.ssh/config` on your local machine:

    Host git-server.example.com
      User git
      ProxyJump user@proxy.example.com
      StrictHostKeyChecking accept-new

Replace:

- `git-server.example.com` with your actual Git server hostname
- `user` with your username on the proxy host
- `git` with the username on the Git server (usually `git` for self-hosted setups)

Clone a repository:

``` bash
git clone ssh://git@git-server.example.com/path/to/repo.git
```

Or use the shorthand syntax:

``` bash
git clone git@git-server.example.com:path/to/repo.git
```

All Git operations (`push`, `pull`, `fetch`) automatically use the SSH tunnel. The tunnel is transparent to Git — no special syntax needed.

## Chaining Multiple Proxies

If you need to tunnel through multiple hosts:

    Host git-server.example.com
      User git
      ProxyJump user@proxy1.example.com,user@proxy2.example.com
      StrictHostKeyChecking accept-new

SSH chains the connections automatically in order.

## Legacy Method: ProxyCommand with netcat

If you’re stuck with older SSH versions or need explicit control, use `ProxyCommand`:

    Host git-server.example.com
      User git
      ProxyCommand ssh -q user@proxy.example.com nc %h %p
      StrictHostKeyChecking accept-new

The `ProxyCommand` works as follows:

- `ssh -q user@proxy.example.com` — connects to the proxy quietly
- `nc %h %p` — uses netcat on the proxy to relay traffic to `%h` (the Git server) on port `%p` (22 for SSH)

This method requires `nc` on the proxy. If it’s missing:

``` bash
ssh user@proxy.example.com "which nc || which ncat"
```

Most distributions provide it as `netcat`, `ncat`, or `socat`.

## Non-Standard SSH Ports

For production environments where the Git server runs SSH on a non-standard port:

    Host git-server.example.com
      User git
      Port 2222
      ProxyJump user@proxy.example.com

## SSH Config Best Practices

Use specific host entries instead of wildcards to avoid unintended proxy routing:

    # Good — applies only to this server
    Host git-server.example.com
      ProxyJump user@proxy.example.com

    # Avoid — applies to all hosts matching the pattern
    Host *.example.com
      ProxyJump user@proxy.example.com

Control host key verification with `StrictHostKeyChecking` to handle first-time connections safely:

    Host git-server.example.com
      StrictHostKeyChecking accept-new
      UserKnownHostsFile ~/.ssh/known_hosts

This accepts the server key on first connection and stores it, then enforces strict checking on subsequent connections.

Ensure proper SSH key permissions:

``` bash
chmod 700 ~/.ssh
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

## Troubleshooting

If Git operations hang or fail, test the SSH connection directly:

``` bash
ssh -v git@git-server.example.com
```

The `-v` flag shows detailed connection info. Each hop in the chain should succeed.

Enable verbose Git output:

``` bash
GIT_SSH_COMMAND="ssh -v" git clone git@git-server.example.com:repo.git
```

If using `ProxyCommand` and netcat, verify it’s working on the proxy:

``` bash
ssh user@proxy.example.com "echo 'test' | nc git-server.example.com 22"
```

If `nc` isn’t available, switch to `ProxyJump` instead.

Check that your proxy host can actually reach the Git server by hostname and port:

``` bash
ssh user@proxy.example.com "ssh -v git@git-server.example.com"
```

If the proxy can’t resolve the Git server’s hostname, ensure DNS is configured or add an entry to the proxy’s `/etc/hosts`.
