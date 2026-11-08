---
title: "Persisting iptables Rules on Linux"
date: 2018-03-24 11:44:52 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-configure-iptables-on-linux-mint-17-1/
---

Making firewall rules persistent across system reboots is essential for any production Linux system. While the original `iptables-persistent` approach works, modern systems typically use `ufw` (Uncomplicated Firewall) or `firewalld`, but understanding the underlying `iptables` mechanism is still valuable for lower-level control.

## Using iptables-persistent

The `iptables-persistent` package automatically saves and restores your firewall rules during boot. Install it first:

``` bash
sudo apt install iptables-persistent
```

During installation, you’ll be prompted to save current IPv4 and IPv6 rules. Answer “Yes” to both if you have existing rules you want to preserve.

## Creating and Testing Rules

Before saving rules permanently, test them. For example, to allow SSH and HTTP traffic while blocking everything else:

``` bash
sudo iptables -F  # Flush existing rules (careful with this)
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```

Verify your rules work:

``` bash
sudo iptables -L -n -v
```

## Saving Rules Permanently

Once you’ve tested and confirmed your rules work correctly, save them:

``` bash
sudo iptables-save | sudo tee /etc/iptables/rules.v4
sudo ip6tables-save | sudo tee /etc/iptables/rules.v6
```

The rules are stored in plain text files:

- `/etc/iptables/rules.v4` — IPv4 rules
- `/etc/iptables/rules.v6` — IPv6 rules

The `iptables-persistent` service will automatically load these files during boot.

## Verifying Persistence

After rebooting, confirm rules were restored:

``` bash
sudo iptables -L -n
sudo ip6tables -L -n
```

## Modern Alternatives

For new systems, consider these simpler options:

**Using ufw** (recommended for most users):

``` bash
sudo apt install ufw
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable
```

Rules are automatically persistent with `ufw`.

**Using firewalld** (if you prefer zone-based rules):

``` bash
sudo apt install firewalld
sudo systemctl enable firewalld
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

## Editing Rules Directly

You can edit the saved rules files directly if needed:

``` bash
sudo nano /etc/iptables/rules.v4
```

After editing, reload them:

``` bash
sudo iptables-restore < /etc/iptables/rules.v4
sudo ip6tables-restore < /etc/iptables/rules.v6
```

Or reload via the service:

``` bash
sudo systemctl restart iptables-persistent
```

## Troubleshooting

If rules don’t persist after reboot, check that the service is enabled:

``` bash
sudo systemctl enable iptables-persistent
sudo systemctl start iptables-persistent
```

View the service status:

``` bash
sudo systemctl status iptables-persistent
```

For debugging, check the actual rule files are readable and have correct syntax:

``` bash
sudo cat /etc/iptables/rules.v4
```

## 2026 Best Practices and Advanced Techniques

For Persisting iptables Rules on Linux, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
