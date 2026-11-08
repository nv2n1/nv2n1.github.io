---
title: "Building VMs with VMware Player and QEMU Images"
date: 2013-07-12 16:31:32 +0000
modified: 2026-04-12 16:53:30 +0000
author: "Eric Ma"
layout: post
categories: [testing-devops]
canonical: /creating-and-running-virtual-machine-using-vmware-player-and-qemu-img/
---

Free virtualization on Linux has multiple solid options. While VMware Player is still available, QEMU combined with libvirt has become the standard approach for most sysadmins. This guide covers creating VM disk images and configurations that work across multiple hypervisors.

## Creating Virtual Disk Images

The first step is creating a virtual disk. QEMU’s `qemu-img` tool handles this across multiple formats:

``` bash
qemu-img create -f qcow2 ubuntu-22.04.qcow2 20G
```

Common formats:

- **qcow2** — Default for QEMU/KVM. Supports snapshots, compression, and copy-on-write. Use this for most cases.
- **vmdk** — VMware format. Still compatible with QEMU, useful if you need VMware Player compatibility.
- **raw** — Unformatted. Fastest but inflexible. Only use if you need direct disk access.

For a production VM, allocate appropriate resources. A modern Linux desktop needs at least 20GB; servers typically need 50GB+.

You can check image info at any time:

``` bash
qemu-img info ubuntu-22.04.qcow2
```

Resize an existing image:

``` bash
qemu-img resize ubuntu-22.04.qcow2 +10G
```

## Configuring the Virtual Machine

Modern VMs are best managed through libvirt rather than raw QEMU commands or hand-written configuration files. Create an XML definition:

``` xml
<domain type='kvm'>
  <name>ubuntu-22-04</name>
  <memory unit='MiB'>4096</memory>
  <currentMemory unit='MiB'>4096</currentMemory>
  <vcpu placement='static'>2</vcpu>
  <os>
    <type arch='x86_64'>hvm</type>
    <boot dev='hd'/>
  </os>
  <devices>
    <emulator>/usr/bin/qemu-system-x86_64</emulator>
    <disk type='file' device='disk'>
      <driver name='qemu' type='qcow2'/>
      <source file='/var/lib/libvirt/images/ubuntu-22-04.qcow2'/>
      <target dev='vda' bus='virtio'/>
    </disk>
    <interface type='network'>
      <source network='default'/>
      <model type='virtio'/>
    </interface>
    <console type='pty'>
      <target type='virtio' port='0'/>
    </console>
    <graphics type='vnc' port='-1' autoport='yes'/>
  </devices>
</domain>
```

Save this as `ubuntu-22-04.xml` and define it:

``` bash
virsh define ubuntu-22-04.xml
```

## Running the VM

If using libvirt:

``` bash
virsh start ubuntu-22-04
virsh console ubuntu-22-04
```

For direct QEMU usage (without libvirt):

``` bash
qemu-system-x86_64 \
  -m 4096 \
  -smp 2 \
  -drive file=ubuntu-22-04.qcow2,format=qcow2 \
  -net nic,model=virtio \
  -net user \
  -enable-kvm \
  -display vnc=:0
```

The `-enable-kvm` flag uses hardware virtualization if available, critical for performance. Connect via VNC:

``` bash
vncviewer localhost:5900
```

## For Windows Guests

If you’re running Windows (a rare scenario nowadays, but still happens), allocate more resources:

``` bash
qemu-img create -f qcow2 windows-vm.qcow2 50G
```

Use the Windows ISO during initial install. Pass through USB devices if needed:

``` bash
qemu-system-x86_64 \
  -m 8192 \
  -smp 4 \
  -drive file=windows-vm.qcow2,format=qcow2 \
  -usb \
  -device usb-host,vendorid=0x1234,productid=0x5678 \
  -enable-kvm \
  -display vnc=:0
```

## Managing Snapshots

QEMU’s snapshot feature is invaluable for testing:

``` bash
qemu-img snapshot -c backup1 ubuntu-22-04.qcow2
qemu-img snapshot -l ubuntu-22-04.qcow2
qemu-img snapshot -d backup1 ubuntu-22-04.qcow2
```

Or via libvirt:

``` bash
virsh snapshot-create-as ubuntu-22-04 my-snapshot --description "Pre-update backup"
virsh snapshot-revert ubuntu-22-04 my-snapshot
```

## Performance Tuning

- Use `virtio` drivers for disk and network instead of legacy emulated devices
- Enable nested paging: add `-cpu host` to QEMU or set CPU mode to `host-passthrough` in libvirt
- For production, mount images directly with `nbd`:

``` bash
modprobe nbd
qemu-nbd -c /dev/nbd0 ubuntu-22-04.qcow2
mount /dev/nbd0p1 /mnt
umount /mnt
qemu-nbd -d /dev/nbd0
```

Modern hypervisor management tools like Proxmox or KVM/libvirt are better long-term choices than VMware Player for Linux-based environments. They offer better integration with infrastructure-as-code and container orchestration platforms.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Building VMs with VMware Player and QEMU Images with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Building VMs with VMware Player and QEMU Images. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
