---
title: "Setting Up Xen Dom0 on Fedora 12 with Kernel 2.6.29"
date: 2013-07-12 16:32:03 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /setting-up-xen-dom0-on-fedora-xen-3-4-1-with-linux-kernel-2-6-29-on-fedora-12/
---

Xen remains a production hypervisor for enterprise deployments (AWS EC2, Citrix Hypervisor), though KVM has become the default for most Linux distributions. If you’re deploying Xen in 2026, you’ll likely be working with recent stable releases rather than the legacy versions covered in older guides.

This guide covers building a modern Xen Dom0 environment on current Fedora. Xen and kernel versions move faster than they did a decade ago, so check the <a href="https://xenproject.org/" rel="nofollow noopener" target="_blank">official Xen release page</a> for the latest stable build matching your hardware support requirements.

## Hardware Considerations

Modern Xen deployments typically run on:

- Xeon or EPYC processors with hardware virtualization (VT-x or AMD-V)
- Server-class motherboards with IOMMU support (Intel VT-d or AMD-Vi)
- ECC memory (strongly recommended for production)
- NVMe or SSD storage for Dom0 and guest performance

Older hardware may work but lacks features like PCI passthrough and nested virtualization. Check your CPU against the <a href="https://wiki.xenproject.org/" rel="nofollow noopener" target="_blank">Xen CPU support matrix</a>.

## Building Xen from Source

Fetch the latest stable release from xenproject.org:

``` bash
mkdir -p /usr/src/xen
cd /usr/src/xen
wget https://downloads.xenproject.org/release/xen/xen-VERSION.tar.gz
tar -xf xen-VERSION.tar.gz
cd xen-VERSION
```

Install build dependencies on Fedora:

``` bash
sudo dnf install gcc make python3-devel libuuid-devel zlib-devel \
  openssl-devel ncurses-devel bison flex perl xz-devel git
```

Build the hypervisor, tools, and documentation:

``` bash
make -j$(nproc) dist-xen dist-tools dist-docs
cd dist
sudo sh ./install.sh
```

The installation script places binaries in `/usr/lib/xen/`, Dom0 kernel in `/boot/`, and tools in `/usr/bin/`.

## Kernel Configuration

Xen requires a Dom0 kernel built with specific options. Use your distribution’s kernel source or compile from upstream. If building custom, ensure these options in your kernel `.config`:

    CONFIG_XEN=y
    CONFIG_XEN_DOM0=y
    CONFIG_XEN_DEV_EVTCHN=y
    CONFIG_XEN_BACKEND=y
    CONFIG_XEN_BLKDEV_BACKEND=y
    CONFIG_XEN_NETDEV_BACKEND=y
    CONFIG_SWIOTLB=y
    CONFIG_HAVE_EFFICIENT_UNALIGNED_ACCESS=y

For HVM guest support:

    CONFIG_KVM=y
    CONFIG_HVM=y

Build and install:

``` bash
make -j$(nproc)
sudo make modules_install install
```

If using Fedora’s standard kernel, check whether Xen support is already compiled in:

``` bash
grep -i xen /boot/config-$(uname -r)
```

## Bootloader Configuration

Update your EFI boot entries or GRUB2 configuration. For GRUB2:

``` bash
sudo grubby --add-kernel=/boot/vmlinuz-VERSION --title="Fedora with Xen" \
  --initrd=/boot/initramfs-VERSION.img --args="dom0_mem=1024M,max:4096M"
```

Set Xen as default:

``` bash
sudo grubby --set-default-index=0
```

Key Dom0 kernel parameters:

- `dom0_mem=1024M,max:4096M` — Allocate 1GB initially, cap at 4GB
- `iommu=1` — Enable IOMMU for device passthrough
- `console=vga` — Use VGA for early boot output
- `loglevel=debug` — Increase verbosity for troubleshooting

Reboot into Xen:

``` bash
sudo reboot
```

Verify you’re running Xen:

``` bash
xl info
```

Output should show `xen_version` and `xen_scheduler` (typically credit2 in modern builds):

    host                   : fedora41.example.com
    release                : 6.7.0-xen
    xen_major              : 4
    xen_minor              : 18
    xen_scheduler          : credit2
    total_memory           : 16384
    free_memory            : 12288

## Daemon and Service Configuration

Enable Xen services for automatic startup. On modern Fedora, use systemd:

``` bash
sudo systemctl enable xend
sudo systemctl start xend
sudo systemctl enable xendomains
sudo systemctl start xendomains
```

Check service status:

``` bash
sudo systemctl status xend
sudo systemctl status xendomains
```

View logs in real time:

``` bash
sudo journalctl -u xend -f
```

Disable KSM tuning to avoid conflicts:

``` bash
sudo systemctl disable ksmtuned
```

## Managing Virtual Machines

List running domains:

``` bash
xl list
```

Create a guest configuration file (`vm-ubuntu.cfg`):

    name = "ubuntu-guest-1"
    memory = 2048
    vcpus = 2
    vif = [ 'mac=00:16:3e:5f:60:01,bridge=xenbr0' ]
    disk = [ '/var/lib/xen/images/ubuntu.img,xvda,w' ]
    kernel = "/var/lib/xen/images/vmlinuz"
    ramdisk = "/var/lib/xen/images/initrd.img"
    bootloader = "pygrub"

Create and start the guest:

``` bash
xl create -c vm-ubuntu.cfg
```

The `-c` flag connects to the console automatically. Suspend/resume guests:

``` bash
xl pause ubuntu-guest-1
xl unpause ubuntu-guest-1
```

Shut down cleanly:

``` bash
xl shutdown ubuntu-guest-1
```

Force destruction if shutdown fails:

``` bash
xl destroy ubuntu-guest-1
```

## PCI Passthrough (Advanced)

For direct device access (GPU, NIC), enable IOMMU in kernel parameters, then hide devices from Dom0:

``` bash
grep -i iommu /boot/config-$(uname -r)
```

Find your device:

``` bash
lspci | grep -i nvidia
```

Hide from Dom0 by adding to kernel parameters:

``` bash
sudo grubby --update-kernel=ALL \
  --args="pciback.hide=(0000:85:00.0)(0000:85:00.1)"
```

Reboot and attach to guest in config:

    pci = [ '85:00.0', '85:00.1' ]

## Troubleshooting

Check hypervisor logs:

``` bash
dmesg | grep Xen
```

Verify Dom0 is using Xen kernel:

``` bash
uname -r
cat /proc/xen/capabilities
```

If `xend` fails to start, check for port conflicts:

``` bash
sudo lsof -i :8006
```

Monitor resource usage:

``` bash
xl top
```

For nested virtualization or KVM guests under Xen, verify capabilities:

``` bash
xl info | grep hvm
```

Xen remains stable for production workloads but requires careful planning around hardware support, kernel configuration, and ongoing maintenance. For new projects, evaluate whether KVM or containerization better fits your infrastructure needs.
