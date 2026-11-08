---
title: "Configuring Chrome\u2019s Proxy Settings from the Linux Command Line"
date: 2018-03-24 08:15:46 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-set-google-chromes-proxy-settings-in-command-line-on-linux/
---

Chrome supports proxy configuration via command-line flags, which is useful for scripting, automation, or testing without touching the GUI settings. This works across all major Linux distributions.

## Basic proxy configuration

Use the `--proxy-server` flag when launching Chrome:

``` bash
google-chrome --proxy-server="socks://localhost:8080"
```

## Proxy scheme formats

The proxy specification follows this format:

    [<proxy-scheme>://]<proxy-host>[:<proxy-port>]

Supported schemes:

- `http` — HTTP proxy (default if omitted)
- `https` — HTTPS proxy
- `socks` or `socks5` — SOCKS v5 proxy
- `socks4` — SOCKS v4 proxy

If you don’t specify a scheme, Chrome assumes HTTP.

## Common examples

HTTP proxy with explicit scheme:

``` bash
google-chrome --proxy-server="http://proxy.example.com:3128"
```

HTTP proxy without scheme (same result):

``` bash
google-chrome --proxy-server="proxy.example.com:3128"
```

SOCKS v5 proxy:

``` bash
google-chrome --proxy-server="socks5://foobar:1080"
```

Localhost proxy for debugging:

``` bash
google-chrome --proxy-server="socks://127.0.0.1:8080"
```

## Proxy bypass list

To exclude certain hosts from proxying, use `--proxy-bypass-list`:

``` bash
google-chrome --proxy-server="http://proxy.example.com:3128" \
  --proxy-bypass-list="localhost,127.0.0.1,.internal.company.com"
```

Patterns in the bypass list use wildcards. Entries without a dot match exact hostnames, while `.domain.com` matches all subdomains.

## PAC file configuration

For more complex proxy routing, use a Proxy Auto-Config (PAC) file:

``` bash
google-chrome --proxy-pac-url="http://proxy.example.com/proxy.pac"
```

The PAC file is fetched and evaluated by Chrome to determine proxy selection based on URL patterns.

## Direct proxy (no proxy)

To explicitly disable proxying:

``` bash
google-chrome --proxy-server="direct://"
```

## Combining with other flags

Proxy flags work alongside other Chrome options:

``` bash
google-chrome --proxy-server="socks://localhost:8080" \
  --user-data-dir=/tmp/chrome-profile \
  --no-sandbox \
  https://example.com
```

## Persistent configuration via policy

For system-wide or managed deployment, configure proxies via Chrome policies instead of command-line flags. Create `/etc/chromium-browser/policies/managed/proxy_config.json`:

``` json
{
  "ProxySettings": {
    "ProxyMode": "fixed_servers",
    "ProxyServer": "socks5://localhost:1080",
    "ProxyBypassList": "localhost,127.0.0.1"
  }
}
```

Ensure proper permissions:

``` bash
sudo chmod 644 /etc/chromium-browser/policies/managed/proxy_config.json
```

This approach survives Chrome updates and restarts, unlike command-line flags which apply only to that instance.

## Troubleshooting

- Chrome won’t start with proxy flags? Try `chromium` instead of `google-chrome` — some distributions use the open-source Chromium package
- Test connectivity to your proxy: `nc -zv proxy.example.com 3128`
- Check Chrome’s net log for proxy issues: `--net-log-level=1 --log-net-log=/tmp/net.log`
- If using SOCKS, verify the SOCKS server listens on the specified port: `ss -tlnp | grep SOCKS_PORT`

Command-line proxy configuration is ephemeral and applies only to that browser instance. For persistent settings across all Chrome launches, use the GUI settings or implement policy files as shown above.

## Related Linux Commands

These related commands are often used alongside the tools discussed in this article:

- man command-name – Read the manual page for any command
- which command-name – Find the location of an executable
- rpm -qa or dpkg -l – List installed packages
- journalctl -u service-name – Check service logs
- ss -tulpn – List listening ports and services

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Configuring Chrome’s Proxy Settings from the Linux Command Line with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Configuring Chrome’s Proxy Settings from the Linux Command Line. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
