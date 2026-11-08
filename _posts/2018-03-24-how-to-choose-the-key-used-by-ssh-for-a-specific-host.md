---
title: "How to Specify Which SSH Key to Use for a Host"
date: 2018-03-24 11:50:25 +0000
layout: post
canonical: https://www.systutorials.com/how-to-choose-the-key-used-by-ssh-for-a-specific-host/
---

SSH key management becomes critical when you’re handling multiple identities across different hosts. By default, `ssh` tries keys in a specific order, but you can explicitly configure which key to use for particular hosts through the SSH config file.

## Using ~/.ssh/config

The cleanest approach is to define host-specific key configurations in `~/.ssh/config`. This file lets you set connection parameters per host without modifying your system-wide SSH settings or passing flags every time.

Create or edit `~/.ssh/config`:

    Host github.com
        User git
        IdentityFile ~/.ssh/github_rsa
        IdentitiesOnly yes

    Host server.example.com
        User deploy
        IdentityFile ~/.ssh/deploy_ed25519
        IdentitiesOnly yes

    Host *.internal.corp
        User sysadmin
        IdentityFile ~/.ssh/corp_key
        IdentitiesOnly yes

Key parameters:

- `IdentityFile` — the private key to use for this host
- `IdentitiesOnly yes` — tells SSH to use *only* the specified key, ignoring other keys in your ssh-agent or default locations
- Wildcards like `*.internal.corp` match multiple hosts with a single rule

Ensure your config file has restricted permissions:

``` bash
chmod 600 ~/.ssh/config
```

## Why Use IdentitiesOnly

Without `IdentitiesOnly yes`, SSH tries keys in this order:

1.  Keys explicitly passed with `-i`
2.  Keys loaded in ssh-agent
3.  Default locations like `~/.ssh/id_rsa`, `~/.ssh/id_ed25519`

This can cause authentication failures or expose unintended key attempts. Setting `IdentitiesOnly yes` prevents SSH from cycling through irrelevant keys, which is especially important when:

- A host has strict failed login limits
- You’re managing dozens of keys
- You want predictable, auditable authentication behavior

## Command-Line Override

If you need a one-off connection with a specific key, use the `-i` flag:

``` bash
ssh -i ~/.ssh/custom_key user@host.example.com
```

For multiple keys in a single command (rare, but useful for complex scenarios):

``` bash
ssh -i ~/.ssh/key1 -i ~/.ssh/key2 user@host.example.com
```

SSH tries them in order until one succeeds.

## Using ssh-agent for Multiple Keys

If you prefer managing keys through `ssh-agent` rather than config files, load specific keys with their host restrictions:

``` bash
ssh-add -t 3600 ~/.ssh/github_rsa
ssh-add -t 3600 ~/.ssh/corp_key
```

The `-t` flag specifies a timeout in seconds. List loaded keys with:

``` bash
ssh-add -l
```

Remove a specific key:

``` bash
ssh-add -d ~/.ssh/github_rsa
```

Clear all keys:

``` bash
ssh-add -D
```

When using ssh-agent, `IdentitiesOnly yes` in your config still prevents SSH from trying unnecessary keys, keeping your authentication path efficient.

## Best Practices

**Use ed25519 keys when possible.** They’re smaller, faster, and more secure than RSA:

``` bash
ssh-keygen -t ed25519 -f ~/.ssh/myhost_key -C "user@machine"
```

**Keep separate keys per purpose.** Use one key for GitHub, another for production, another for internal infrastructure. This limits blast radius if a key is compromised.

**Match key permissions strictly:**

``` bash
chmod 600 ~/.ssh/id_ed25519
chmod 644 ~/.ssh/id_ed25519.pub
```

**Test your config** before relying on it:

``` bash
ssh -v user@host.example.com
```

The verbose output shows which identity file SSH selected, confirming your config is working as intended.

**Never hardcode keys in scripts or containers.** Use SSH agent forwarding or mounted secrets instead. In container environments, inject keys at runtime via volume mounts or orchestration-level secret management.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers How to Specify Which SSH Key to Use for a Host with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for How to Specify Which SSH Key to Use for a Host. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
