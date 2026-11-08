---
title: "Resizing a KVM Virtual Disk: A Step-by-Step Guide"
date: 2018-03-24 11:55:28 +0000
modified: 2026-04-12 16:51:49 +0000
author: "Weiwei Jia"
layout: post
categories: [system-administration-cloud]
canonical: /how-to-resize-a-virtual-disk-of-kvm/
---

Expanding a VM’s storage is a routine operation in KVM environments. The process has two distinct phases: expanding the raw disk capacity and then growing the partitions and filesystems to use that space.

## Resizing the Disk Image

The first step is to increase the virtual disk size using `qemu-img`:

``` bash
qemu-img resize disk.qcow2 +10G
```

This adds 10GB to the image. You can also specify an absolute size:

``` bash
qemu-img resize disk.qcow2 50G
```

For raw image files, the syntax is identical:

``` bash
qemu-img resize disk.raw +20G
```

The VM must be shut down before resizing. If you attempt to resize a disk while the guest is running, `qemu-img` will refuse with an error unless you use the `--shrink` flag (which is dangerous and rarely needed).

You can check the current size of an image before resizing:

``` bash
qemu-img info disk.qcow2
```

## Growing Partitions and Filesystems

After resizing the image, shut down the guest and boot it back up. The new space won’t be available until the guest’s partition table and filesystem are expanded.

### Using virt-resize (Recommended)

For qcow2-backed VMs, `virt-resize` from the `libguestfs-tools` package handles partition and filesystem expansion in one step without needing to boot the guest:

``` bash
virt-resize --expand /dev/sda3 disk.qcow2 disk-resized.qcow2
```

This expands the last partition (`/dev/sda3`) to fill available space. You can then replace the original image:

``` bash
mv disk-resized.qcow2 disk.qcow2
```

`virt-resize` works offline, making it safer for production VMs. It handles most common filesystem types automatically.

### Manual Expansion Inside the Guest

If you prefer to expand partitions manually or are working with LVM/Ceph-backed disks, boot the guest and resize from inside:

**For ext4:**

``` bash
sudo fdisk /dev/sda
# Delete the partition, recreate it with larger size, save and exit
sudo resize2fs /dev/sda3
```

Or use `parted` for non-destructive resizing:

``` bash
sudo parted /dev/sda
(parted) resizepart 3 100%
(parted) quit
sudo resize2fs /dev/sda3
```

**For XFS:**

``` bash
sudo parted /dev/sda
(parted) resizepart 3 100%
(parted) quit
sudo xfs_growfs /
```

XFS can grow while mounted, so you don’t need to unmount.

**For LVM:**

If your guest uses LVM, expand the physical volume first:

``` bash
sudo pvresize /dev/sda3
sudo lvextend -l +100%FREE /dev/vg0/lv_root
sudo resize2fs /dev/vg0/lv_root
```

## Storage Backend Considerations

**qcow2 files:** Use the commands above directly.

**Raw images:** `qemu-img resize` works the same way. `virt-resize` also supports raw images.

**LVM-backed disks:** Resize the logical volume instead:

``` bash
sudo lvresize -L +10G /dev/vg0/vm-disk
```

Then grow the guest’s filesystem as shown above.

**Ceph RBD images:** Expand the RBD volume:

``` bash
rbd resize --size 50G pool/image-name
```

Then resize the guest filesystem.

## Verification

After resizing, verify the changes:

``` bash
df -h
lsblk
parted /dev/sda print
```

If you resized LVM or Ceph, also check:

``` bash
pvs
lvs
```

Watch for any filesystem or partition errors. Most modern filesystems handle online growth well, but always keep backups of important VMs before major storage operations.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Resizing a KVM Virtual Disk: A Step-by-Step Guide with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Resizing a KVM Virtual Disk: A Step-by-Step Guide. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
