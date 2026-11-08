---
title: "Setting up Xen Dom0 on Fedora 12 with Kernel 2.6.32.13"
date: 2013-07-12 16:32:16 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /setting-up-stable-xen-dom0-with-fedora-xen-3-4-3-with-xenified-linux-kernel-2-6-32-13-in-fedora-12/
---

Xen remains a production-grade hypervisor used in enterprise environments (AWS EC2, Citrix Hypervisor), though KVM has become the default for most Linux distributions. This guide covers building a stable Xen Dom0 on current Fedora releases using modern kernel sources.

### Hardware Considerations

This guide assumes server-class hardware with:

- Intel or AMD processor with virtualization extensions (VT-x or AMD-V)
- Minimum 8GB RAM (16GB+ recommended for multiple DomUs)
- Dedicated storage for Dom0 and DomU images
- IOMMU support for device passthrough (optional but recommended)

### Prerequisites

Ensure SELinux is disabled before proceeding:

``` bash
# setenforce 0
```

Update your system and remove conflicting packages:

``` bash
# dnf update -y
# dnf remove -y xen* libvirt* qemu*
```

Install build dependencies:

``` bash
# dnf groupinstall -y "Development Tools" "Development Libraries"
# dnf install -y \
  make gcc kernel-devel \
  wget git patch \
  bridge-utils \
  dev86 glibc-devel glibc-devel.i686 \
  e2fsprogs-devel mkinitrd \
  iasl xz-devel bzip2-devel \
  pciutils-devel SDL-devel libX11-devel gtk2-devel \
  python3-devel libuuid-devel yajl-devel
```

### Building Xen Hypervisor and Tools

Download and extract Xen. As of 2026, check xen.org for the latest stable release (typically 4.x series):

``` bash
$ cd /tmp
$ wget https://releases.xen.org/xen-4.18.tar.gz
$ tar xf xen-4.18.tar.gz
$ cd xen-4.18
```

Build Xen and tools:

``` bash
$ ./configure --prefix=/usr --sysconfdir=/etc
$ make -j$(nproc) dist
$ sudo make install-dist
```

Update boot configuration to include Xen:

``` bash
# grub2-mkconfig -o /boot/grub2/grub.cfg
```

### Building Xenified Kernel

Modern Xen Dom0 support is integrated into mainline Linux kernels (6.x series). No external patches are required for recent Xen versions.

Download the kernel source matching your Fedora release:

``` bash
$ cd /tmp
$ wget https://cdn.kernel.org/pub/linux/kernel/v6.x/linux-6.8.tar.xz
$ tar xf linux-6.8.tar.xz
$ cd linux-6.8
```

Configure the kernel for Xen Dom0:

``` bash
$ make menuconfig
```

Enable these options:

    Processor type and features --->
      [*] Symmetric multi-processing support
      [*] Xen guest support
      [*]   Dom0 support

    Device Drivers --->
      XEN --->
        [*] Backend driver support
        [*]   Block-device backend driver
        [*]   Network-device backend driver
        [*]   PCI-device backend driver
        [*] Frontend driver support
        [*]   Block-device frontend driver
        [*]   Network-device frontend driver

Build and install:

``` bash
$ make -j$(nproc)
$ sudo make modules_install install
```

Regenerate GRUB configuration:

``` bash
# grub2-mkconfig -o /boot/grub2/grub.cfg
```

### Configuring Xen Services

Enable Xen services to start at boot:

``` bash
# systemctl enable xen
# systemctl enable xendomains
```

On older systems using SysVinit:

``` bash
# chkconfig --add xend
# chkconfig --add xendomains
```

Verify the configuration:

``` bash
# systemctl status xen
```

### Booting Xen Dom0

Reboot and select the Xen entry from GRUB. After boot, verify Xen is running:

``` bash
# xl info
```

This command displays Dom0 memory, CPU count, and Xen version. Check domain status:

``` bash
# xl list
```

### Network Bridge Configuration

For DomU networking, create a bridge on Dom0:

``` bash
# nmcli connection add type bridge ifname br0 con-name bridge-br0
# nmcli connection add type bridge-slave ifname eth0 master bridge-br0
# nmcli connection down bridge-br0
# nmcli connection up bridge-br0
```

Or edit `/etc/sysconfig/network-scripts/` for legacy systems.

### Performance Tuning

Reserve CPU cores and memory for Dom0 to improve stability:

Add to GRUB kernel parameters:

    xen-dom0=max_vcpus=2 dom0_mem=2048M

Then rebuild GRUB:

``` bash
# grub2-mkconfig -o /boot/grub2/grub.cfg
```

Pin Dom0 vCPUs to physical cores:

``` bash
# xl vcpu-pin Domain-0 0 0
# xl vcpu-pin Domain-0 1 1
```

### Common Issues

**Xen fails to initialize**: Verify CPU virtualization support is enabled in BIOS. Check `dmesg` for error messages.

**DomU refuses to start**: Confirm bridge configuration with `brctl show`. Check domain XML syntax with `xl create -n domain.cfg`.

**Performance degradation**: Monitor Dom0 CPU and memory with `xl top`. Check I/O contention using `iostat` and adjust DomU resource allocations.

For additional DomU configuration and advanced Xen solutions, refer to the Xen documentation and community forums.
