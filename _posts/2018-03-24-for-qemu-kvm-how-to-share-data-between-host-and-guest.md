---
title: "Sharing Data Between QEMU/KVM Host and Guest"
date: 2018-03-24 11:54:03 +0000
author: "Weiwei Jia"
layout: post
categories: [system-administration-cloud]
canonical: /for-qemu-kvm-how-to-share-data-between-host-and-guest/
---

When running virtual machines with QEMU/KVM, you’ll frequently need to transfer files or share directories between the host and guest systems. Several methods work well depending on your use case and performance requirements.

## 9p (Virtio) Filesystem

The 9p protocol is the most straightforward approach for sharing directories. It’s lightweight and doesn’t require additional guest agents.

**Host setup:**

Add this to your QEMU command line:

``` bash
-fsdev local,security_model=passthrough,id=fsdev0,path=/path/on/host \
-device virtio-9p-pci,fsdev=fsdev0,mount_tag=hostshare
```

**Guest setup:**

Mount the shared directory inside the VM:

``` bash
sudo mkdir -p /mnt/host
sudo mount -t 9p -o trans=virtio hostshare /mnt/host
```

To make this persistent, add to guest `/etc/fstab`:

    hostshare /mnt/host 9p trans=virtio,nofail 0 0

The `security_model=passthrough` preserves file permissions exactly as they exist on the host. If you need to run QEMU as an unprivileged user, use `security_model=mapped-xattr` instead, though this adds overhead.

## VIRTIO-FS (Recommended for Performance)

For better performance and proper permission handling, use virtiofs. This approach uses a separate daemon and is now the preferred method for shared filesystems.

**Host setup with libvirt:**

Define the filesystem in your XML domain:

``` xml
<filesystem type="mount" accessmode="passthrough">
  <driver type="virtiofs"/>
  <source dir="/path/on/host"/>
  <target dir="hostshare"/>
</filesystem>
```

**Host setup with raw QEMU:**

``` bash
-object memory-backend-memfd,id=mem,size=2G \
-numa node,memdev=mem \
-chardev socket,id=char0,path=/tmp/vhost-fs.sock \
-device vhost-user-fs-pci,chardev=char0,tag=hostshare \
-object memory-backend-file,id=mem,size=2G,mem-path=/dev/shm,share=on
```

Then launch virtiofsd on the host (part of qemu package on most distributions):

``` bash
virtiofsd --socket-path=/tmp/vhost-fs.sock --shared-dir=/path/on/host
```

**Guest mount:**

``` bash
sudo mkdir -p /mnt/host
sudo mount -t virtiofs hostshare /mnt/host
```

Virtiofs requires a 5.4+ kernel on the guest and offers better I/O performance with proper caching.

## Network-Based Sharing

For scenarios where filesystem sharing isn’t practical, use standard network protocols.

**NFS:**

On the host:

``` bash
sudo exportfs -o rw,fsid=0,insecure,no_subtree_check,async 192.168.122.1:/path/on/host
```

Mount in guest:

``` bash
sudo mount -t nfs 192.168.122.1:/path/on/host /mnt/host
```

**SSHFS:**

Mount via SSH from the guest:

``` bash
sshfs user@host.ip:/path/on/host /mnt/host
```

This works well for one-off transfers but has higher latency than filesystem-level sharing.

## Direct File Transfer

For simple one-time transfers, use `virsh` or standard tools:

``` bash
virsh domfile-get guest-name /path/in/guest /path/on/host
virsh domfile-put host-file /path/in/guest
```

Or through SSH if the guest has network access:

``` bash
scp user@guest-ip:/path/in/guest /path/on/host
```

## Spice USB Redirection

For interactive use, Spice allows USB device passthrough and clipboard sharing:

``` bash
-spice port=5900,disable-ticketing=on \
-device virtio-serial-pci \
-chardev spicevmc,id=spicechannel0,name=vdagent \
-device virtserialport,chardev=spicechannel0,name=com.redhat.spice.0
```

Connect with `remote-viewer` or `virt-viewer` to use clipboard sharing and USB redirection.

## Security Considerations

- **9p passthrough mode** runs with host user permissions; isolate sensitive data or use mapped mode
- **Virtiofs** with `--allow-direct-io` adds complexity but improves performance for large files
- **NFS** requires firewall rules; use `nfsstat` to debug mount issues
- Always verify file permissions after mounting shared directories
- For production VMs, consider containerized workloads (Docker, Podman) running inside the guest instead of shared mounts

## Debugging Shared Filesystem Issues

Check guest kernel messages:

``` bash
dmesg | grep -i 9p
dmesg | grep -i virtio
```

Verify host-side file access:

``` bash
ls -la /path/on/host
getfacl /path/on/host
```

For virtiofs daemon issues:

``` bash
ps aux | grep virtiofsd
journalctl -u virtiofs.service
```

Choose 9p for simplicity, virtiofs for performance, and network methods when you need isolation or firewall traversal.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Sharing Data Between QEMU/KVM Host and Guest with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Sharing Data Between QEMU/KVM Host and Guest. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
