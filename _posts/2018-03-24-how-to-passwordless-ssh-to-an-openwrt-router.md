---
title: "Passwordless SSH Setup for OpenWrt with Dropbear"
date: 2018-03-24 11:47:31 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-passwordless-ssh-to-an-openwrt-router/
---

OpenWrt runs Dropbear as its SSH server instead of OpenSSH. While Dropbear supports RSA and modern key types, the authorized_keys file lives in a different location, which causes `ssh-copy-id` to fail silently. Here’s how to set up key-based authentication properly.

## Why ssh-copy-id doesn’t work

`ssh-copy-id` looks for `~/.ssh/authorized_keys` on the remote system, which is OpenSSH’s default. Dropbear uses `/etc/dropbear/authorized_keys` instead. Additionally, on OpenWrt the root filesystem often uses limited storage, so permissions and file handling can differ from standard Linux distributions.

## Prerequisites

Make sure you have an SSH key pair on your local machine. If you don’t have one yet, generate it:

``` bash
ssh-keygen -t ed25519 -C "your-email@example.com"
```

Ed25519 keys are preferred over RSA for their security and smaller size — important on resource-constrained routers. If you need RSA for legacy compatibility, use `-t rsa -b 4096` instead.

## Add your public key to Dropbear

First, back up the existing authorized_keys file (if it exists):

``` bash
ssh root@YOUR_OPENWRT_ROUTER "cp /etc/dropbear/authorized_keys /etc/dropbear/authorized_keys.bak"
```

Then append your public key:

``` bash
cat ~/.ssh/id_ed25519.pub | ssh root@YOUR_OPENWRT_ROUTER "cat >> /etc/dropbear/authorized_keys"
```

Replace `id_ed25519.pub` with `id_rsa.pub` if you’re using RSA keys.

## Verify permissions

Dropbear can be strict about file permissions. SSH into the router and check:

``` bash
ssh root@YOUR_OPENWRT_ROUTER
ls -la /etc/dropbear/authorized_keys
```

The file should be readable by root. If permissions look wrong, fix them:

``` bash
chmod 600 /etc/dropbear/authorized_keys
chmod 700 /etc/dropbear
```

## Test passwordless login

Exit the SSH session and test from your local machine:

``` bash
ssh root@YOUR_OPENWRT_ROUTER
```

You should connect without being prompted for a password. If you still get a password prompt, check `/var/log/messages` on the router for Dropbear auth errors:

``` bash
logread | grep dropbear
```

## Multiple keys (optional)

If you want to add keys from multiple machines, append each public key on a separate line:

``` bash
cat ~/.ssh/id_ed25519.pub | ssh root@YOUR_OPENWRT_ROUTER "cat >> /etc/dropbear/authorized_keys"
```

Repeat this command on each client machine, or concatenate all public keys locally first and pipe them at once.

## Restrict root SSH access further (security)

Once passwordless auth is working, consider disabling root password login entirely. Edit `/etc/config/dropbear` on the router:

``` bash
uci set dropbear.@dropbear[0].PasswordAuth='0'
uci commit dropbear
/etc/init.d/dropbear restart
```

This prevents password-based attacks while keeping key-based access working. Always test the connection from a different terminal before doing this to avoid locking yourself out.

## Troubleshooting

- **Connection refused**: Dropbear may not be running. Start it with `/etc/init.d/dropbear start`
- **Permission denied (publickey)**: Check that `/etc/dropbear/authorized_keys` is world-readable and the public key is on a single line with no extra whitespace
- **Multiple keys not working**: Ensure each key is on its own line in authorized_keys, with no blank lines between them

## 2026 Best Practices and Advanced Techniques

For Passwordless SSH Setup for OpenWrt with Dropbear, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
