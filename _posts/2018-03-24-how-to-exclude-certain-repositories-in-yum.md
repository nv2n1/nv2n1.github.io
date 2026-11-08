---
title: "Excluding Specific Repositories in Yum"
date: 2018-03-24 08:16:53 +0000
layout: post
canonical: https://www.systutorials.com/how-to-exclude-certain-repositories-in-yum/
---

You’ll sometimes need to exclude specific repositories from package operations—typically when multiple repos provide the same package, mirror connectivity is unreliable, or you want to force installation from a trusted source. The `--disablerepo` flag lets you skip repos on a per-command basis.

## Basic syntax

``` bash
dnf --disablerepo=repoid1 --disablerepo=repoid2 install package-name
```

Add `--disablerepo` once for each repo you want to skip. You can also use glob patterns:

``` bash
dnf --disablerepo=google-* update
```

This would disable any repo matching `google-*`, like `google-chrome`, `google-talkplugin`, etc.

## Practical examples

Skip a single repo during an update:

``` bash
dnf --disablerepo=fedora-updates update
```

Install a package while excluding certain repos:

``` bash
dnf --disablerepo=rpmfusion-nonfree --disablerepo=copr-user install vlc
```

Use a wildcard pattern to disable all Chrome-related repos:

``` bash
dnf --disablerepo=google-* update
```

## Permanent repository disabling

For persistent exclusions, edit `/etc/yum.repos.d/` config files directly instead of using the flag every time. Find the repo’s config file and set `enabled=0`:

``` bash
cat /etc/yum.repos.d/google-chrome.repo
```

``` ini
[google-chrome]
name=Google - Chrome
baseurl=http://dl.google.com/linux/chrome/rpm/stable/$basearch
enabled=0
gpgcheck=1
gpgkey=https://dl.google.com/linux/linux_signing_key.pub
```

Then verify the change:

``` bash
dnf repolist all | grep google
```

## Checking which repos provide a package

Before excluding repos, see which ones have the package you need:

``` bash
dnf provides firefox
dnf search --all firefox
```

This shows you exactly which repos have what, so you can make informed exclusion decisions.

## Enabling a disabled repo temporarily

If you permanently disabled a repo, re-enable it for a single command:

``` bash
dnf --enablerepo=google-chrome install google-chrome
```

## Troubleshooting repo timeouts

If a specific repo times out frequently (common with geographically distant mirrors), you have better options than excluding it entirely:

**Change the mirror URL** in the repo config to a closer location:

``` bash
sudo nano /etc/yum.repos.d/google-chrome.repo
# Change baseurl to a CDN endpoint closer to you
```

**Set a timeout** to fail faster and fall back to other repos:

``` bash
echo "timeout=5" | sudo tee -a /etc/dnf/dnf.conf
```

**Use metalink or mirrorlist** instead of hardcoded URLs—these redirect to working mirrors automatically.

## Key differences from older yum

Modern DNF (dnf5) behaves identically to DNF 4.x for `--disablerepo` usage. RHEL 8+ and Fedora 22+ all use DNF by default, so these commands work across distributions. The old yum package manager is obsolete; CentOS 8+ and RHEL 8+ use DNF exclusively.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## 2026 Best Practices and Advanced Techniques

For Excluding Specific Repositories in Yum, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
