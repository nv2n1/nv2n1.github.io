---
title: "How to Configure DNF and YUM to Cache Downloaded RPM Packages"
date: 2020-09-13 13:01:26 +0000
author: "David Yang"
layout: post
canonical: https://www.systutorials.com/how-to-make-dnf-and-yum-save-downloaded-rpm-packages/
---

DNF and YUM automatically download RPM packages and their dependencies during installation. If you need to build offline installation media, create local mirrors, or avoid repeated downloads across multiple systems, you’ll want to preserve those packages instead of letting them disappear from cache after installation.

This is especially useful for:

- Building offline installation repositories
- Preparing packages for air-gapped environments
- Creating custom installation media
- Pre-staging updates across multiple machines without re-downloading

## Method 1: Download Packages Without Installing

The most straightforward approach is to download packages and their dependencies without performing any transaction:

``` bash
dnf install --downloadonly --downloaddir=/var/cache/rpms/ package-name
```

For multiple packages:

``` bash
dnf install --downloadonly --downloaddir=/var/cache/rpms/ package1 package2 package3
```

DNF will resolve all dependencies, download them, and exit without installing anything. The `--downloaddir` option specifies where to store the RPMs. Without this flag, packages are downloaded to DNF’s default cache directory (`/var/cache/dnf/`), which may be cleaned automatically.

### Installing Downloaded Packages

Once you have the packages cached, install them locally:

``` bash
dnf install /var/cache/rpms/*.rpm
```

Or install a specific package:

``` bash
dnf install /var/cache/rpms/package-name-*.rpm
```

### Handling Repository Metadata

When working with cached packages, you may need to create repository metadata if distributing them elsewhere. Use `createrepo`:

``` bash
createrepo /var/cache/rpms/
```

This generates the necessary metadata files (`repomd.xml`, `primary.xml.gz`, etc.) so other systems can treat the directory as a proper repository.

## Method 2: Enable Global Package Caching

Configure DNF to preserve all downloaded packages permanently by editing `/etc/dnf/dnf.conf`:

``` ini
[main]
keepcache=True
```

With `keepcache=True`, packages remain in `/var/cache/dnf/` even after successful installation. Without this setting (the default), DNF cleans the cache after transactions complete.

**Important considerations:**

- This is a system-wide setting affecting all users and all transactions
- Cache directory grows over time and requires periodic cleanup
- Useful if you frequently reinstall or troubleshoot systems
- Not ideal for space-constrained environments

To manually clean cached packages later:

``` bash
dnf clean all
```

This removes all cached packages but preserves repository metadata.

## Method 3: Download Updates for Offline Systems

To download available updates without applying them immediately:

``` bash
dnf upgrade --downloadonly --downloaddir=/var/cache/rpms/
```

This is valuable for staging critical updates, testing on a separate system, or preparing updates for distribution to multiple machines.

## Practical Workflow Example

Here’s a typical scenario: preparing packages for a fleet of machines without internet access.

1.  Download packages and dependencies:

    ``` bash
    dnf install --downloadonly --downloaddir=/mnt/repo/ nginx postgresql postgresql-server
    ```

2.  Create repository metadata:

    ``` bash
    createrepo /mnt/repo/
    ```

3.  Transfer `/mnt/repo/` to target systems via USB, NFS, or local mirror

4.  On target systems, add a local repository (`/etc/yum.repos.d/local.repo`):

    ``` ini
    [local]
    name=Local Repository
    baseurl=file:///mnt/repo/
    enabled=1
    gpgcheck=0
    ```

5.  Install from the local repository:

    ``` bash
    dnf install nginx postgresql postgresql-server
    ```

## Useful Related Commands

Check available packages before downloading:

``` bash
dnf list available | grep package-name
```

Download a package for a different system architecture:

``` bash
dnf install --downloadonly --downloaddir=/var/cache/rpms/ --forcearch=x86_64 package-name
```

Get dependency information without downloading:

``` bash
dnf deplist package-name
```

## Notes for RHEL/CentOS Systems

RHEL and CentOS Stream use DNF (DNF5 on RHEL 9.4+). The syntax remains identical. If using legacy YUM on older RHEL 7 systems, the same `--downloadonly` and `--downloaddir` options work, though repository configuration may differ.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers How to Configure DNF and YUM to Cache Downloaded RPM Packages with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for How to Configure DNF and YUM to Cache Downloaded RPM Packages. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
