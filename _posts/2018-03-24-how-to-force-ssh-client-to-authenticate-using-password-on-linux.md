---
title: "Disable SSH Key Authentication to Require Passwords"
date: 2018-03-24 11:48:19 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-force-ssh-client-to-authenticate-using-password-on-linux/
---

When you have SSH key-based authentication set up, the client will prefer it by default. This can make it difficult to test whether password authentication is working—especially after changing a password or troubleshooting login issues.

## Force password-only authentication

Use the `-o PreferredAuthentications=password` flag:

``` bash
ssh -o PreferredAuthentications=password username@host
```

This tells SSH to use password authentication exclusively, bypassing any configured keys.

## Why this matters

SSH tries authentication methods in a specific order. By default, it attempts public key authentication first, then falls back to other methods. If a valid key exists, it succeeds immediately without prompting for a password. This means you could change your password and never know if it works.

## Related authentication options

You can combine multiple authentication methods with a comma-separated list if you want to specify fallback behavior:

``` bash
# Try password first, then key-based auth
ssh -o PreferredAuthentications=password,publickey username@host

# Only allow public key authentication
ssh -o PreferredAuthentications=publickey username@host
```

## Disable key authentication entirely

If you want to temporarily prevent SSH from using keys at all, disable them:

``` bash
ssh -o PubkeyAuthentication=no username@host
```

This is useful when testing password policies or when you suspect a key is interfering with authentication.

## Making it persistent in your SSH config

For hosts where you want password auth by default, add this to `~/.ssh/config`:

    Host testserver
        HostName example.com
        User username
        PreferredAuthentications password

Then simply `ssh testserver` will use password auth.

## Available authentication methods

SSH supports several authentication mechanisms, tried in the order specified by `PreferredAuthentications`:

- **publickey** — public/private key pairs
- **password** — plaintext password (over encrypted channel)
- **keyboard-interactive** — challenge-response (includes TOTP, 2FA)
- **gssapi-with-mic** — Kerberos/GSSAPI authentication
- **hostbased** — host-based authentication (rarely used)

You can check what methods a server accepts by attempting connection and observing the output, or examine `/etc/ssh/sshd_config` on the server if you have access.

## Debugging authentication issues

When testing authentication, enable verbose output to see which methods are attempted:

``` bash
ssh -vv -o PreferredAuthentications=password username@host
```

The `-vv` flag shows detailed connection information, including which authentication methods succeed or fail. This is invaluable for diagnosing why a particular method isn’t working.

## Network Diagnostic Commands

When troubleshooting network connectivity:

- ping host – Test basic connectivity
- traceroute host – Trace the path packets take
- ss -tulpn – Show listening ports
- ip addr show – Display network interfaces
- nmcli device status – NetworkManager device status
- curl -I url – Check HTTP headers

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## 2026 Best Practices and Advanced Techniques

For Disable SSH Key Authentication to Require Passwords, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
