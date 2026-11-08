---
title: "Multi-Hop SSH Connections with ProxyJump and ProxyCommand"
date: 2018-03-24 08:22:31 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /direct-multi-hop-ssh-connection/
---

When you need to reach a server through one or more intermediate hosts, you can establish a direct connection without manually chaining SSH sessions. This is essential for accessing internal servers that aren’t directly reachable from your workstation.

## The scenario

    laptop ----> proxy ----> server

You want to connect to `server.example.com` through `proxy.example.com` as if it were directly accessible.

## ProxyJump (recommended for modern OpenSSH)

ProxyJump is the cleanest approach and has been standard since OpenSSH 7.3. It handles all the tunneling details transparently.

Add to your `~/.ssh/config`:

    Host server.example.com
        HostName server.example.com
        ProxyJump proxy.example.com
        User appuser

Then connect normally:

``` bash
ssh server.example.com
```

Or use it inline for one-off connections:

``` bash
ssh -J proxy.example.com server.example.com
```

For multiple hops, chain proxies with commas:

``` bash
ssh -J proxy1.example.com,proxy2.example.com,proxy3.example.com server.example.com
```

This is far cleaner than nested ProxyCommand configurations and handles multiplexing automatically.

## Better organization with named hosts

Separate your proxy definitions from target servers for maintainability:

    Host bastion
        HostName proxy.example.com
        User adminuser
        IdentityFile ~/.ssh/keys/bastion_ed25519

    Host internal-server
        HostName server.example.com
        User appuser
        IdentityFile ~/.ssh/keys/internal_ed25519
        ProxyJump bastion

Now you can reference the proxy by name:

``` bash
ssh internal-server
```

## ProxyCommand (alternative for older systems)

If you’re stuck with OpenSSH \< 7.3, ProxyCommand still works:

    Host server.example.com
        HostName server.example.com
        ProxyCommand ssh -q proxy.example.com -W %h:%p
        User appuser

The `-W %h:%p` option tells SSH to forward standard input and output to the target host (`%h`) on the specified port (`%p`). This is more portable than netcat but requires the proxy host to support SSH’s `-W` flag.

## SSH key-based authentication

All multi-hop methods work best with key-based authentication. Generate a strong key on your client:

``` bash
ssh-keygen -t ed25519 -C "user@laptop"
```

Distribute the public key to all intermediate hosts and the final server:

``` bash
ssh-copy-id -i ~/.ssh/id_ed25519.pub adminuser@proxy.example.com
ssh-copy-id -i ~/.ssh/id_ed25519.pub appuser@server.example.com
```

For different usernames across hosts, specify them in `~/.ssh/config` as shown above, and `ssh-copy-id` will use the correct one.

## Connection multiplexing for performance

Enable SSH connection reuse in your config to avoid repeated authentication handshakes:

    Host *
        ControlMaster auto
        ControlPath ~/.ssh/control-%h-%p-%r
        ControlPersist 300

With this setup, subsequent connections through the same proxy within 5 minutes reuse the existing tunnel, significantly speeding up operations.

## Testing and troubleshooting

Verify your SSH config is correct:

``` bash
ssh -G server.example.com
```

This prints the resolved configuration without connecting.

Test the proxy first:

``` bash
ssh -v bastion echo "Proxy reachable"
```

Then test the full chain with verbose output:

``` bash
ssh -vv internal-server
```

Use `-vv` or even `-vvv` for detailed debugging of authentication failures or connection issues.

For quick syntax validation without connecting:

``` bash
ssh -T server.example.com
```

The `-T` flag disables pseudoterminal allocation, useful for verifying connectivity without needing an interactive shell.

## Security considerations

- Restrict proxy access with firewall rules to only necessary ports and source IPs
- Use different SSH keys for different security zones (bastion vs. internal hosts)
- Monitor proxy logs for unusual connection patterns
- Set `ProxyUseFdpass yes` in your config if your proxy is also an OpenSSH 5.4+ client—this avoids re-authentication on the proxy for subsequent hops
- Consider disabling password authentication on the proxy entirely and requiring SSH keys only

## Chaining without config (one-off connections)

For temporary access without modifying `~/.ssh/config`, you can chain commands:

``` bash
ssh -t proxy.example.com ssh server.example.com
```

The `-t` flag allocates a pseudoterminal, allowing interactive shell access on the final server. Without it, you lose your terminal. However, this method is less elegant and doesn’t benefit from connection multiplexing or other optimizations.
