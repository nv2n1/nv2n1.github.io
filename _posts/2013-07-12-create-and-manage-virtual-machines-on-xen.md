---
title: "Managing Virtual Machines on Xen: A Getting Started Guide"
date: 2013-07-12 16:31:39 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /create-and-manage-virtual-machines-on-xen/
---

Xen remains a robust hypervisor for production environments—AWS EC2, Citrix Hypervisor, and many hosting providers still rely on it. However, KVM has become the default for most Linux distributions due to simpler management and better integration with standard tooling. For new deployments on standard Linux, evaluate KVM with libvirt or container solutions like Docker and Kubernetes. That said, if you’re working with existing Xen infrastructure or need its advanced features, here’s how to create and manage virtual machines.

## File-Backed Virtual Block Devices

File-backed VBDs are practical for testing and small deployments. They’re easy to duplicate—just copy the file and update the configuration. For production, consider LVM-backed or real block devices for better performance.

Create a 20GB sparse file-backed VBD:

``` bash
truncate -s 20G vmdisk0
```

Or with dd if you prefer:

``` bash
dd if=/dev/zero of=vmdisk0 bs=1M seek=20480 count=1
```

Format with ext4 (ext3 is obsolete):

``` bash
mkfs.ext4 vmdisk0
```

## Installing a DomU via PXE

Download the kernel and initrd for your distribution. For Fedora 41:

``` bash
wget https://mirrors.kernel.org/fedora/releases/41/Server/x86_64/os/images/pxeboot/vmlinuz
wget https://mirrors.kernel.org/fedora/releases/41/Server/x86_64/os/images/pxeboot/initrd.img
```

Create an installation profile `f41-install.cfg`:

    name = "f41-install"
    memory = 1536
    vcpus = 2
    disk = [ 'file:/home/xen/vmdisk0,xvda,w' ]
    vif = [ 'bridge=xenbr0' ]
    kernel = "/home/xen/fedora/vmlinuz"
    ramdisk = "/home/xen/fedora/initrd.img"
    extra = "ip=dhcp"
    on_reboot = 'restart'
    on_crash = 'restart'

If your Xen toolstack supports blktap2, use `tap:aio:` instead of `file:` for better performance. However, blktap2 is deprecated in newer Xen versions—stick with `file:` for compatibility.

Start the VM:

``` bash
xl create f41-install.cfg
```

Note: Modern Xen uses `xl` instead of the older `xm` command. `xm` is deprecated and may not exist in recent distributions.

Connect to the console:

``` bash
xl console f41-install
```

Complete the installation using the network. Typical Fedora mirrors work fine.

## Persistent DomU Configuration

After installation, create a run profile `vm1.cfg`:

    name = "vm1"
    memory = 1536
    vcpus = 2
    disk = [ 'file:/home/xen/vmdisk0,xvda,w' ]
    vif = [ 'bridge=xenbr0' ]
    bootloader = "/usr/lib/xen/boot/pygrub"
    on_reboot = 'restart'
    on_crash = 'restart'

PyGrub reads the guest’s bootloader configuration, allowing the DomU to manage its own kernel updates without Dom0 intervention.

Start the VM:

``` bash
xl create vm1.cfg
```

## Managing DomUs with xl

Start a VM from configuration:

``` bash
xl create vm1.cfg
```

List running VMs:

``` bash
xl list
```

Expected output:

    Name                   ID     Mem   VCPUs   State   Time(s)
    Domain-0               0     2048     8    r-----   134.2
    vm1                   10     1536     2    -b----     5.4
    vm2                   11     1536     2    -b----     5.1

Connect to VM console:

``` bash
xl console vm1
```

Graceful shutdown:

``` bash
xl shutdown vm1
```

Force shutdown:

``` bash
xl destroy vm1
```

Reboot:

``` bash
xl reboot vm1
```

Get resource usage:

``` bash
xl top
```

Pause a VM (useful for snapshots):

``` bash
xl pause vm1
```

Resume a paused VM:

``` bash
xl unpause vm1
```

Check VM details:

``` bash
xl dominfo vm1
```

## Duplicating VMs

Once a DomU is configured, duplication is straightforward:

``` bash
cp vmdisk0 vmdisk1
cp vm1.cfg vm2.cfg
```

Edit `vm2.cfg` to change the name and any other parameters:

    name = "vm2"
    disk = [ 'file:/home/xen/vmdisk1,xvda,w' ]

Start the new VM:

``` bash
xl create vm2.cfg
```

## Persistent VM Auto-Start

To have VMs start automatically on Dom0 boot, place their configuration files in `/etc/xen/auto/`:

``` bash
cp vm1.cfg /etc/xen/auto/vm1.cfg
```

The Xen toolstack will create them during startup.

## Modern Alternatives

For new deployments, consider:

- **KVM with libvirt**: Standard on most Linux distributions, better tooling ecosystem
- **Containers**: Docker/Podman for applications that don’t need full VMs
- **Cloud-native solutions**: Kubernetes for orchestration if managing multiple machines

If you’re maintaining existing Xen infrastructure, `xl` provides all necessary management. Avoid `xm`—it’s unmaintained and missing features in current Xen versions.
