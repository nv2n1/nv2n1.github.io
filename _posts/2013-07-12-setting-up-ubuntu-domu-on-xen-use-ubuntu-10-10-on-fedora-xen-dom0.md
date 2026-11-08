---
title: "Setting Up Ubuntu 10.10 as a Xen DomU on Fedora"
date: 2013-07-12 16:32:23 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/setting-up-ubuntu-domu-on-xen-use-ubuntu-10-10-on-fedora-xen-dom0/
---

This post describes Xen DomU setup procedures from the early 2010s. While Xen remains critical infrastructure for cloud providers like AWS EC2 and Citrix Hypervisor, it’s rarely deployed for new on-premises virtualization projects.

**For modern Linux virtualization, consider:**

- **KVM/QEMU**: The default hypervisor in most Linux distributions, better community support, and tighter kernel integration
- **Proxmox VE or oVirt**: Full-featured open-source virtualization platforms
- **Containers (Docker, Podman, Kubernetes)**: For workload isolation without full VM overhead
- **Cloud services (AWS, Azure, GCP)**: For managed infrastructure

If you’re maintaining an existing Xen deployment or working with legacy enterprise infrastructure, the concepts below remain relevant. Otherwise, invest your time in KVM-based solutions.

## Understanding Xen Architecture

Xen uses a hypervisor-based architecture with a privileged management domain (Dom0) that controls guest domains (DomU). Dom0 has direct hardware access; DomU guests run unprivileged, communicating with Dom0 through I/O rings.

Key differences from KVM:

- Separate hypervisor rather than kernel module
- Manual kernel/ramdisk management for guests
- Dedicated toolstack (xl/libxl in modern versions)
- Better performance for CPU-bound workloads on certain configurations

## Prerequisites

- Xen hypervisor installed and running on Dom0
- LVM volume group created for DomU storage
- Network bridge configured (e.g., `eth2` for guest traffic)
- Root access on Dom0

## Installation Media and DomU Creation

Xen DomU requires special installation media. Standard live ISO images won’t boot under the hypervisor. Use the network installer instead:

``` bash
wget https://archive.ubuntu.com/ubuntu/dists/jammy/main/installer-amd64/current/images/netboot/mini.iso
```

(Note: Ubuntu 10.10 reached end-of-life in 2011. Use Ubuntu 22.04 LTS for production systems.)

Create an initial configuration file for the installer (`ubuntu-install.cfg`):

    name = "vm-ubuntu"
    vcpus = 2
    memory = 2048
    vif = [ 'bridge=eth2' ]
    disk = [ 'file:/home/xen/mini.iso,xvdc:cdrom,r', 'phy:vg_xen/vm-ubuntu,xvda,w' ]
    bootloader = "/usr/bin/pygrub"
    on_reboot = 'restart'
    on_crash = 'restart'

Key fields:

- `name`: VM hostname/identifier
- `vcpus`: Number of virtual CPUs
- `memory`: RAM in MB
- `vif`: Virtual network interface (bridge to physical network)
- `disk`: Storage devices — the cdrom and primary disk
- `bootloader`: Use pygrub to read the guest kernel from the disk

Create the LVM volume first:

``` bash
lvcreate -L 50G -n vm-ubuntu vg_xen
```

Start the DomU and begin installation:

``` bash
xl create -c ubuntu-install.cfg
```

The `-c` flag connects the console. Complete the installation wizard using the text-based installer. When finished, shut down the guest.

## Booting the Installed Guest

After installation, pygrub may fail to boot Ubuntu correctly because it doesn’t fully understand Ubuntu’s GRUB configuration. The reliable approach is to extract the kernel and initramfs from the guest disk and boot them directly from Dom0.

First, mount the guest’s root filesystem:

``` bash
mkdir -p /mnt/guest
mount /dev/vg_xen/vm-ubuntu /mnt/guest
```

Copy the kernel and initramfs to Dom0:

``` bash
mkdir -p /home/xen/vm-ubuntu
cp /mnt/guest/boot/vmlinuz-* /home/xen/vm-ubuntu/
cp /mnt/guest/boot/initrd.img-* /home/xen/vm-ubuntu/
```

Extract the root filesystem UUID from the guest’s GRUB configuration:

``` bash
grep "root=" /mnt/guest/boot/grub/grub.cfg | head -n1
```

This will output something like:

    linux   /boot/vmlinuz-5.15.0-... root=UUID=a1b2c3d4-e5f6-7890-1234-567890abcdef ro

Create the production configuration file (`ubuntu-run.cfg`):

    name = "vm-ubuntu"
    vcpus = 2
    memory = 2048
    vif = [ 'bridge=eth2' ]
    kernel = "/home/xen/vm-ubuntu/vmlinuz-5.15.0-86-generic"
    ramdisk = "/home/xen/vm-ubuntu/initrd.img-5.15.0-86-generic"
    extra = "root=UUID=a1b2c3d4-e5f6-7890-1234-567890abcdef ro"
    disk = [ 'phy:vg_xen/vm-ubuntu,xvda,w' ]
    on_reboot = 'restart'
    on_crash = 'restart'

Replace the UUID with the actual value from your guest. Start the guest:

``` bash
xl create -c ubuntu-run.cfg
```

If you update the kernel inside the guest, you must copy the new kernel/initramfs to Dom0 and update the configuration file. This is the primary operational burden of running Xen.

## Automation and Management

For production deployments, automate kernel updates:

``` bash
#!/bin/bash
GUEST_MOUNT="/mnt/guest-$$"
mount /dev/vg_xen/vm-ubuntu "$GUEST_MOUNT"
cp "$GUEST_MOUNT"/boot/vmlinuz-* /home/xen/vm-ubuntu/
cp "$GUEST_MOUNT"/boot/initrd.img-* /home/xen/vm-ubuntu/
umount "$GUEST_MOUNT"
xl reboot vm-ubuntu
```

Store guest configuration files in version control to track changes. Consider libvirt’s Xen driver if you need a unified management interface across multiple hypervisors.

## Deprecation Path

For new projects, migrate to KVM. Convert Xen guests using `virt-v2v`:

``` bash
virt-v2v -i xen xen://server/vm-ubuntu -o libvirt -os vg_kvm
```

This tool handles disk format conversion and driver adjustments automatically.
