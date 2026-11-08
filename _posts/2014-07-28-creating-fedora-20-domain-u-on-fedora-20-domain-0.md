---
title: "Creating a Xen DomU Guest on Fedora Dom0"
date: 2014-07-28 00:03:57 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /creating-fedora-20-domain-u-on-fedora-20-domain-0/
---

A file-backed VBD stores the entire VM disk in a single file on the Dom0 filesystem. This approach works well for testing and development, though LVM-backed or disk-backed storage provides better performance for production workloads.

Create a working directory and a 20GB sparse file-backed VBD:

``` bash
mkdir -p /home/xen/f41install
cd /home/xen/f41install
dd if=/dev/zero of=./vmdisk0 bs=1k seek=20480k count=1
```

The sparse file only consumes disk space as the VM writes to it, rather than allocating the full 20GB upfront. For production deployments with high I/O demands, LVM-backed volumes offer superior performance and snapshot capabilities.

## Download Fedora Installation Kernel and Initramfs

Fetch the pxeboot kernel and initramfs from the Fedora mirror network:

``` bash
cd /home/xen/f41install/
wget https://mirrors.fedoraproject.org/pub/fedora/linux/releases/41/Fedora/x86_64/os/images/pxeboot/vmlinuz
wget https://mirrors.fedoraproject.org/pub/fedora/linux/releases/41/Fedora/x86_64/os/images/pxeboot/initrd.img
```

If the primary mirror is unreachable, try the Fedora archive:

    https://archives.fedoraproject.org/pub/archive/fedora/linux/releases/

## Create Installation Domain Configuration

Create a `vm.run` file with the installation parameters. This configuration boots the installation kernel and streams the Fedora live image over HTTPS:

``` bash
name="f41install"
vcpus=2
memory=2048
disk = ['file:/home/xen/f41install/vmdisk0,xvda,w']
vif = ['bridge=xenbr0']
kernel="/home/xen/f41install/vmlinuz"
ramdisk="/home/xen/f41install/initrd.img"
extra="root=live:https://mirrors.fedoraproject.org/pub/fedora/linux/releases/41/Fedora/x86_64/os/LiveOS/squashfs.img"
on_reboot = 'restart'
on_crash = 'restart'
```

The VM will obtain network configuration via DHCP by default. To assign a static IP instead, modify the `extra` parameter:

``` bash
extra="root=live:https://mirrors.fedoraproject.org/pub/fedora/linux/releases/41/Fedora/x86_64/os/LiveOS/squashfs.img ip=10.8.1.210::10.8.1.1:255.255.0.0:vm210:eth0:none nameserver=8.8.8.8"
```

The kernel boot parameter format follows Anaconda documentation. Both HTTP and HTTPS protocols are supported for the live image.

## Start Installation and Complete Setup

Launch the DomU and attach to its console:

``` bash
xl create -c vm.run
```

The Anaconda installer will boot. Select “Text mode” to proceed with the interactive installation. When you need to detach from the console without shutting down the VM, press `Ctrl+]`. Reconnect anytime with:

``` bash
xl console f41install
```

After Anaconda completes and the VM reboots, it will attempt installation again since the config still specifies the pxeboot kernel. Shut down the VM cleanly:

``` bash
xl shutdown f41install
```

Wait a moment for graceful shutdown. If the VM doesn’t shut down within 30 seconds, force it with:

``` bash
xl destroy f41install
```

## Prepare DomU for Persistent Deployment

The installed VBD is now ready to duplicate and configure for actual use. Copy the installation directory to a new location with a meaningful name:

``` bash
cp -r /home/xen/f41install /home/xen/vm-10.8.1.210
```

Create a production `vm.run` configuration in `/home/xen/vm-10.8.1.210/`:

``` bash
name="vm-10.8.1.210"
vcpus=2
memory=2048
disk = ['file:/home/xen/vm-10.8.1.210/vmdisk0,xvda,w']
vif = ['bridge=xenbr0']
bootloader = "pygrub"
on_reboot = 'restart'
on_crash = 'restart'
```

Using `pygrub` extracts the kernel directly from the DomU’s grub configuration, eliminating the need to maintain pxeboot kernels in Dom0. Kernel updates within the guest apply automatically without modifying Dom0 settings, significantly simplifying long-term VM management.

## Boot and Access the DomU

Start the configured domain:

``` bash
xl create /home/xen/vm-10.8.1.210/vm.run
```

Connect to its console:

``` bash
xl console vm-10.8.1.210
```

Log in with credentials set during installation. The VM now boots from its own kernel via PyGrub.

## Managing Multiple VMs

For additional VMs, duplicate the working `vmdisk0` and create new `vm.run` files with unique names and IP addresses. When duplicating disk images, preserve sparse file behavior and save space:

``` bash
cp --sparse=always /home/xen/vm-10.8.1.210/vmdisk0 /home/xen/vm-10.8.1.211/vmdisk0
```

Keep the original installation directory separate from deployed VM directories. This prevents accidental modifications to your template and makes housekeeping easier across multiple deployments.

For monitoring and management, use `xl list` to view all running domains, `xl mem-set` to adjust memory allocation, and `xl vcpu-set` to modify vCPU count without a reboot. These tools allow dynamic resource tuning without service interruption.
