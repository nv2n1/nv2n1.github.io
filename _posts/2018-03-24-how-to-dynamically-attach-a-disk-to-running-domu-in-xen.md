---
title: "Attaching a Disk to a Running Xen DomU"
date: 2018-03-24 11:44:21 +0000
author: "Eric Ma"
layout: post
categories: [development-best-practices]
canonical: /how-to-dynamically-attach-a-disk-to-running-domu-in-xen/
---

Attaching storage to a running Xen DomU without rebooting is straightforward using the `xl` toolstack. This is useful when you need to add capacity, attach backup storage, or provision new volumes without downtime.

## Basic Disk Attachment

To attach a logical volume or physical disk to a running DomU, use `xl block-attach` on Dom0:

``` bash
xl block-attach vm-228 phy:vg_xen/vm-228-large xvdb w
```

This attaches the logical volume `vg_xen/vm-228-large` to domain `vm-228` as device `/dev/xvdb` with write permissions. Inside the guest, the new block device appears immediately without requiring a reboot.

## Command Syntax

The full `xl block-attach` syntax is:

``` bash
xl block-attach <Domain> <BackendDevice> <FrontendDevice> [<Mode>] [<BackendDomain>]
```

Parameters:

- **Domain**: The target DomU name or ID
- **BackendDevice**: The source on Dom0 — can be a logical volume (`phy:vg_name/lv_name`), physical device (`/dev/sdX`), or file-backed loop device (`file:/path/to/img`)
- **FrontendDevice**: Device name as it appears in the guest (e.g., `xvdb`, `xvdc`)
- **Mode**: `r` for read-only, `w` for read-write (default is `w`)
- **BackendDomain**: Advanced option; usually omitted (defaults to Dom0)

## Practical Examples

Attach a logical volume with read-write access:

``` bash
xl block-attach web-server phy:vg_data/backup-vol xvdc w
```

Attach a physical disk or partition read-only:

``` bash
xl block-attach archive-vm /dev/sdf xvdd r
```

Attach a file-backed image:

``` bash
xl block-attach test-vm file:/var/lib/xen/images/test-disk.img xvde w
```

## USB Drive Passthrough

You can also pass through an entire USB drive to a DomU:

``` bash
xl block-attach vm-228 /dev/sde xvde w
```

**Important**: Pass through the entire device (`/dev/sde`), not a partition (`/dev/sde1`). Before attaching, ensure the drive is not mounted on Dom0:

``` bash
umount /dev/sde* 2>/dev/null || true
xl block-attach vm-228 /dev/sde xvde w
```

If the system auto-mounts the USB drive, unmount it first. The guest will now have exclusive access to the entire disk.

## Verifying Attachment

Inside the guest, verify the new device exists:

``` bash
lsblk
# or
ls -l /dev/xvdb
```

If the device doesn’t appear immediately, check dmesg on both Dom0 and the guest for errors.

## Detaching Disks

Remove a disk attachment without shutting down the guest:

``` bash
xl block-detach vm-228 xvde
```

Use the frontend device name (the name as seen in the guest), not the backend. You may need to unmount the filesystem first:

``` bash
umount /mnt/data
xl block-detach vm-228 xvde
```

## Listing Active Block Devices

View all block devices attached to a DomU:

``` bash
xl block-list vm-228
```

This shows both the frontend device name (in the guest) and backend identifier.

## Persistence Across Reboots

Dynamic attachment does not persist across DomU reboots. To make the attachment permanent, add it to the DomU’s configuration file (usually in `/etc/xen/vm-228.cfg` or `/etc/xen/vm-228`):

    disk = [ 'phy:vg_xen/vm-228-large,xvdb,w' ]

Then reload the configuration if your Xen setup supports it, or the attachment will be restored on next boot.

## Legacy xm Toolstack

If your system still uses the older `xm` toolstack instead of `xl`, replace `xl` with `xm` in all commands:

``` bash
xm block-attach vm-228 phy:vg_xen/vm-228-large xvdb w
xm block-detach vm-228 xvde
xm block-list vm-228
```

The syntax and behavior are identical. Most modern Xen deployments use `xl`; `xm` is deprecated.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Attaching a Disk to a Running Xen DomU with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Attaching a Disk to a Running Xen DomU. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
