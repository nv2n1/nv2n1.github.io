---
title: "Checking Package Versions in Ubuntu"
date: 2018-03-24 11:43:05 +0000
modified: 2026-04-12 16:48:34 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-find-all-available-versions-of-a-package-in-dpkg-apt-get-or-aptitude/
---

When you need to see what versions of a package are available in your Ubuntu repositories, there are several approaches depending on how much detail you need.

## Using apt-cache showpkg

The most direct method is `apt-cache showpkg`, which lists all available versions along with their repository sources:

``` bash
apt-cache showpkg thunderbird
```

This output shows version numbers, the repositories they’re available from, and reverse dependencies. The format is verbose, but useful when you need to see exactly which repositories provide each version.

## Using apt-cache policy (cleaner output)

For a more readable display, `apt-cache policy` is often better:

``` bash
apt-cache policy thunderbird
```

This shows the currently installed version (if any), the candidate version that will be installed by default, and a table of all available versions with their repository sources.

## Using apt-cache madison

To list available versions with their repositories in a compact table:

``` bash
apt-cache madison thunderbird
```

Note: `apt-cache search` returns package names and descriptions only, never versions, so it cannot be used to list versions.

## Using apt list (modern approach)

On Ubuntu 16.04 and newer, `apt list` provides cleaner output:

``` bash
apt list --all-versions thunderbird
```

This shows each available version with its repository in an easy-to-scan format. Add `--upgradable` to see only versions newer than what’s installed:

``` bash
apt list --upgradable
```

## Installing a specific version

Once you’ve identified the version you want, install it explicitly:

``` bash
sudo apt install thunderbird=1:31.1.1+build1-0ubuntu0.14.04.1
```

Then keep it from being upgraded; `apt-mark hold` takes a package name, not a version:

``` bash
sudo apt-mark hold thunderbird
```

Later, unhold it with:

``` bash
sudo apt-mark unhold thunderbird
```

## Checking PPAs and third-party sources

If you’re using PPAs (Personal Package Archives), versions may differ. Check which PPAs provide a package:

``` bash
apt-cache policy thunderbird | grep -A 5 "Candidate:"
```

Or list all enabled PPAs:

``` bash
apt-cache policy
```

## Finding versions in specific Ubuntu releases

If you need to check what version is available in a different Ubuntu release, you can query Launchpad or the package tracker directly, or temporarily enable that release’s sources and run `apt update` followed by the commands above.

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

## 2026 Best Practices and Advanced Techniques

For Checking Package Versions in Ubuntu, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
