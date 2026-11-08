---
title: "Automatically Adding New SSH Hosts to Known Hosts"
date: 2018-03-24 08:04:42 +0000
author: "Q A"
layout: post
categories: [scripting-utilities]
canonical: /howto-ssh-automatically-add-new-hosts-to-the-list-of-known-hosts/
---

When managing many systems, manually confirming host keys for each new connection gets tedious fast. You can configure SSH to automatically add unknown hosts to `~/.ssh/known_hosts` without prompting.

## The Risk Trade-off

Before implementing this, understand what you’re doing: disabling strict host key checking opens you to man-in-the-middle attacks. Only use this in trusted networks where you control the network infrastructure. For production access to critical systems, keep `StrictHostKeyChecking` enabled.

## Method 1: Per-Command Option

Use the `-o` flag to disable strict host key checking for a single connection:

``` bash
ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null username@host
```

The `UserKnownHostsFile=/dev/null` variant discards the key entirely (useful for one-off connections). To actually save the key, use:

``` bash
ssh -o StrictHostKeyChecking=accept-new username@host
```

The `accept-new` option (available in OpenSSH 7.6+) automatically adds the host key only if it’s new, but still rejects keys that changed — a safer middle ground than disabling checks entirely.

## Method 2: SSH Config File

For hosts you connect to regularly, add rules to `~/.ssh/config`:

    Host 10.*
        StrictHostKeyChecking accept-new
        User ubuntu
        IdentityFile ~/.ssh/id_rsa

This applies to all hosts matching the pattern. You can be more specific:

    Host prod-db-01
        HostName 10.1.2.50
        User postgres
        StrictHostKeyChecking accept-new
        IdentityFile ~/.ssh/db_key

    Host staging-*
        User deploy
        StrictHostKeyChecking accept-new
        IdentityFile ~/.ssh/deploy_key

## Method 3: Global Configuration

Edit `/etc/ssh/ssh_config` (system-wide) or `~/.ssh/config` (user-specific) to set defaults:

    Host *
        StrictHostKeyChecking accept-new
        UserKnownHostsFile ~/.ssh/known_hosts

This applies to all hosts unless overridden per-host. Again, only do this in trusted environments.

## Using with Automation Tools

When running Ansible, Terraform, or scripts that SSH to many hosts:

``` bash
# Ansible
ansible-playbook site.yml -e ansible_ssh_common_args="-o StrictHostKeyChecking=accept-new"

# Terraform
export TF_VAR_ssh_options="-o StrictHostKeyChecking=accept-new"
```

Or set it in your automation config files:

``` yaml
# ansible.cfg
[defaults]
host_key_checking = False
```

For Ansible specifically, `host_key_checking = False` is equivalent to `StrictHostKeyChecking=no`.

## Viewing Your Known Hosts

After adding hosts, verify them with:

``` bash
ssh-keygen -l -f ~/.ssh/known_hosts
```

This shows fingerprints of all stored keys. If you suspect a key has changed:

``` bash
ssh-keygen -R hostname
```

This removes the host from `known_hosts`. The next connection will prompt you again (or auto-add if `accept-new` is set).

## Best Practices

- Use `accept-new` instead of `no` when possible — it balances convenience with security
- For interactive work, keep `StrictHostKeyChecking` enabled and manually approve new hosts
- In CI/CD pipelines, use `accept-new` or pass keys via deploy keys rather than disabling checks entirely
- Regularly audit `~/.ssh/known_hosts` for unexpected entries
- Use separate SSH keys for automation vs. interactive access
- Consider using SSH certificates (`~/.ssh/known_hosts.d/`) for larger deployments instead of host key files

## 2026 Best Practices and Advanced Techniques

For Automatically Adding New SSH Hosts to Known Hosts, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
