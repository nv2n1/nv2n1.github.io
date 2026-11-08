---
title: "Prevent systemd-tmpfiles from Deleting Specific /tmp Files"
date: 2018-03-24 11:47:26 +0000
modified: 2026-04-12 16:53:02 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-make-fedora-linux-not-clean-some-files-in-tmp/
---

Fedora uses `systemd-tmpfiles` to automatically clean up temporary files and directories. By default, this includes volatile files in `/tmp/`, which can cause problems for applications that rely on files persisting there — like HDFS DataNodes that store their PID files as `hadoop-hadoop-datanode.pid`.

## How systemd-tmpfiles Works

The `systemd-tmpfiles` service runs periodically (typically daily and at boot) to clean up files based on rules defined in configuration files under `/usr/lib/tmpfiles.d/` and `/etc/tmpfiles.d/`. The main rule for `/tmp/` is usually in `/usr/lib/tmpfiles.d/tmp.conf`.

Check the current configuration:

``` bash
cat /usr/lib/tmpfiles.d/tmp.conf
```

You’ll see rules like `d /tmp 1777 root root 10d` which tells systemd to clean files older than 10 days.

## Excluding Specific Files

To prevent certain files from being cleaned, create a custom configuration file in `/etc/tmpfiles.d/` (this directory takes precedence over `/usr/lib/tmpfiles.d/`):

``` bash
sudo nano /etc/tmpfiles.d/exclude-tmp.conf
```

Add exclusion rules for the files you want to preserve. The format uses the `x` type to exclude paths:

    # Exclude HDFS PID files
    x /tmp/hadoop-*.pid

    # Exclude other application PID files
    x /tmp/myapp-*.pid

    # Exclude specific directories
    x /tmp/myapp-temp/*

Save the file and verify the syntax:

``` bash
systemd-tmpfiles --dry-run --clean
```

The `--dry-run` flag shows what would be cleaned without actually removing anything.

## Understanding tmpfiles.d Format

The main field types you’ll encounter:

- `d` — create directory if missing
- `f` — create regular file if missing
- `x` — exclude path from cleanup (most important for your use case)
- `X` — exclude directory contents recursively
- `e` — set permissions/ownership on existing files
- `z` — set SELinux labels

Each rule follows: `TYPE PATH MODE UID GID AGE ARGUMENT`

For exclusions, you typically only need:

    x /path/to/exclude

## Preserving Application State

If you’re running applications that need persistent state in `/tmp/`, consider these alternatives:

1.  **Use `/var/lib/` instead** — Designed for application data that should survive reboots:

    ``` bash
    mkdir -p /var/lib/myapp
    ```

2.  **Use `/run/` for runtime data** — Backed by tmpfs but with different cleanup policies:

    ``` bash
    mkdir -p /run/myapp
    ```

3.  **Configure application-specific tmpfiles.d rules** — Create application-specific cleanup rules:

        # /etc/tmpfiles.d/hadoop.conf
        d /tmp/hadoop 0755 hadoop hadoop 30d
        x /tmp/hadoop/*.pid

## Managing Cleanup Intervals

View the current tmpfiles cleanup schedule:

``` bash
systemctl status systemd-tmpfiles-clean.timer
```

To see when it last ran:

``` bash
journalctl -u systemd-tmpfiles-clean.service -n 10
```

If you need to manually trigger cleanup (useful for testing):

``` bash
sudo systemd-tmpfiles --clean
```

Or to clean everything matching a pattern immediately:

``` bash
sudo systemd-tmpfiles --clean /etc/tmpfiles.d/exclude-tmp.conf
```

## Verification

After creating your exclusion rules, verify they work by:

1.  Creating test files:

    ``` bash
    touch /tmp/hadoop-test.pid /tmp/other-test.tmp
    ```

2.  Running tmpfiles manually:

    ``` bash
    sudo systemd-tmpfiles --clean
    ```

3.  Checking what remains:

    ``` bash
    ls -la /tmp/ | grep -E 'hadoop|other'
    ```

The PID file should persist while other temporary files are cleaned as expected.

For Hadoop specifically, the best practice is to configure `HADOOP_PID_DIR` in your `hadoop-env.sh` to point to a directory under `/var/run/` or `/var/lib/` rather than `/tmp/`, which gives you more control over persistence and permissions.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Prevent systemd-tmpfiles from Deleting Specific /tmp Files with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Prevent systemd-tmpfiles from Deleting Specific /tmp Files. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
