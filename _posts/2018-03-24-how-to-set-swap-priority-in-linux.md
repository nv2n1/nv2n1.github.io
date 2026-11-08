---
title: "Setting Process Swap Priority in Linux"
date: 2018-03-24 08:14:11 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-set-swap-priority-in-linux/
---

Linux can manage multiple swap partitions or files simultaneously, each with an assigned priority. The kernel allocates swap pages from highest to lowest priority, with round-robin allocation among equally-prioritized areas.

## Setting Swap Priority with swapon

Use the `swapon` command to activate a swap partition and set its priority:

``` bash
swapon -p 10 /dev/sdc1
```

The `-p` flag sets the priority (0-32767, higher number = higher priority). You can also deactivate and reactivate with a new priority:

``` bash
swapoff /dev/sdc1
swapon -p 10 /dev/sdc1
```

## Persistent Configuration via /etc/fstab

To make swap priority persist across reboots, add entries to `/etc/fstab`:

    /dev/sdc1 swap swap pri=10 0 0
    /dev/sdc2 swap swap pri=5  0 0

Reload swap configuration:

``` bash
swapoff -a
swapon -a
```

## Priority Behavior

**Priority assignment rules:**

- Higher numeric values have higher priority
- Default priority is -2 if not specified
- Newly enabled swaps default lower than existing ones
- Swap areas with different priorities: higher priority exhausts first before kernel touches lower priority
- Swap areas with equal priority: kernel allocates pages round-robin between them

**Practical example:** If you have an SSD and a mechanical drive, set the SSD to priority 10 and the mechanical drive to priority 5. The kernel will fill the SSD first, only using the mechanical drive when the SSD is full.

## Viewing Current Swap Configuration

Check active swap areas and their priorities:

``` bash
swapon --show
```

Output example:

    NAME      TYPE      SIZE USED PRIO
    /dev/sdc1 partition 4.0G   0B   10
    /dev/sdc2 partition 2.0G   0B    5

Or use the older but still functional method:

``` bash
cat /proc/swaps
```

## Dynamic Priority Adjustment Without Downtime

You cannot change swap priority on a live partition directly. To adjust priorities safely:

1.  Create the new swap configuration in `/etc/fstab`
2.  Activate with `swapon -a`
3.  Let the system gradually move to the new configuration
4.  Deactivate old swap with `swapoff /dev/old_partition`

Alternatively, for a controlled migration:

``` bash
swapon -p 15 /dev/new_swap  # New higher priority
# Traffic naturally shifts to higher priority
swapoff /dev/old_swap       # Disable old swap after migration
```

## Multiple Swaps on Same Device

You can create multiple swap partitions on the same physical device:

``` bash
# Create two 2GB swap partitions on /dev/sdc
sudo fdisk /dev/sdc
# Create /dev/sdc1 and /dev/sdc2, type 82 (Linux swap)

sudo mkswap /dev/sdc1
sudo mkswap /dev/sdc2

swapon -p 10 /dev/sdc1
swapon -p 8  /dev/sdc2
```

This can be useful for load distribution across the same device, though priority ordering is typically more important than parallelism within a single drive.

## Swap Files vs Partitions

Modern systems often use swap files instead of partitions for flexibility:

``` bash
# Create 4GB swap file
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon -p 10 /swapfile
```

Add to `/etc/fstab`:

    /swapfile none swap sw,pri=10 0 0

Swap files have negligible performance difference from partitions on modern filesystems and offer easier resizing.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Setting Process Swap Priority in Linux with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Setting Process Swap Priority in Linux. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
