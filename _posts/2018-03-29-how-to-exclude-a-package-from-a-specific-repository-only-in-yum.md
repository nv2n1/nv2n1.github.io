---
title: "Exclude a Package from a Specific Repository in Yum"
date: 2018-03-29 08:47:37 +0000
author: "Q A"
layout: post
categories: [testing-devops]
canonical: /how-to-exclude-a-package-from-a-specific-repository-only-in-yum/
---

When managing packages on RHEL, CentOS, AlmaLinux, or Fedora, you sometimes need to prevent a package from being installed or updated from a particular repository. This is useful when multiple repos provide the same package and you want to control which version gets pulled in.

## Repository-specific exclusions with DNF

Modern systems use DNF (which supersedes yum in Fedora 22+ and RHEL 8+). The core approach is similar across versions, but DNF offers better granularity.

### Command-line exclusion

To exclude a package from a specific repo during installation or update:

``` bash
dnf install my-package --exclude=my-package
```

However, this excludes from *all* repos. To exclude only from a specific repository, use the `excludepkgs` directive in that repo’s configuration:

### Repository-level exclusions

Edit the repository config file directly. For example, to exclude a package from EPEL:

``` bash
# /etc/yum.repos.d/epel.repo
[epel]
name=Extra Packages for Enterprise Linux
baseurl=https://download.fedoraproject.org/pub/epel/$releasever/Everything/$basearch/
enabled=1
gpgcheck=1
excludepkgs=nginx*
```

This prevents any package matching `nginx*` from being installed or updated from EPEL, while still allowing it from other enabled repos.

### Global exclusions in dnf.conf

For system-wide exclusions in the main configuration:

``` bash
# /etc/dnf/dnf.conf
[main]
exclude=kernel-* php-*
```

Separate multiple packages with spaces. Use wildcards (`*`) to match package patterns. This applies globally unless overridden at the repository level.

## Checking which repository provides a package

Before excluding, verify which repos provide a package:

``` bash
dnf repoquery --available nginx
```

Output shows the repo and version:

    nginx-1.24.0-1.fc40.x86_64    @fedora
    nginx-1.25.2-1.el9.x86_64     @epel

## Using module streams for version selection

RHEL 8+ and Fedora systems often provide multiple versions via AppStreams (module streams). Instead of excluding packages, switch between versions:

``` bash
# List available streams
dnf module list nodejs

# Switch to a specific stream
dnf module enable nodejs:18

# Install from the enabled stream
dnf install nodejs
```

This approach is cleaner than exclusions for packages with multiple maintained versions (Node.js, PostgreSQL, etc.).

## Excluding with constraints

For finer control, use DNF’s `--best` flag combined with version pinning:

``` bash
# Install latest but exclude beta versions
dnf install 'my-package >= 2.0' --exclude='my-package-*beta*'
```

## Persistent repo-specific exclusions

Create or modify repo files in `/etc/yum.repos.d/` or `/etc/dnf/repos.d/`:

``` bash
# /etc/yum.repos.d/local-custom.repo
[local-custom]
name=Local Custom Repository
baseurl=file:///opt/local/repo
enabled=1
priority=10
excludepkgs=conflicting-app* old-lib*
```

The `priority` setting (1-99, lower is higher priority) also influences which repo’s package gets selected when multiple repos provide the same package.

## Verifying exclusions

Check what’s actually excluded:

``` bash
dnf config-manager --dump-variable=excludepkgs
```

Or check a specific repo:

``` bash
dnf config-manager --dump-variable=excludepkgs --repo=epel
```

## Temporary overrides

To temporarily bypass exclusions for a single operation:

``` bash
dnf install my-package --setopt=exclude=
```

This clears all exclusions for that command only.

## Important notes

- Repository-level exclusions take precedence over global settings
- Wildcards use shell globbing (not regex): `nginx*`, `php-*`, `kernel-*`
- Exclusions apply to both install and update operations
- If you exclude a package that’s required as a dependency, DNF will fail — use module streams or dependency resolution instead
- Check `/var/log/dnf.log` to see which packages were skipped due to exclusions

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Exclude a Package from a Specific Repository in Yum with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Exclude a Package from a Specific Repository in Yum. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
