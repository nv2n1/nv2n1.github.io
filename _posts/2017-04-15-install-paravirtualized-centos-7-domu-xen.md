---
title: "Installing a Paravirtualized DomU on Xen with Rocky Linux 9"
date: 2017-04-15 06:48:14 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/install-paravirtualized-centos-7-domu-xen/
---

Xen remains a solid hypervisor choice for specific workloads, though KVM dominates most Linux distributions today. This guide covers installing a paravirtualized DomU on Xen using modern tooling and Rocky Linux 9, which requires specific kernel parameters during installation.

## Why Paravirtualization Matters

Paravirtualized guests communicate directly with the hypervisor rather than emulating hardware, resulting in better performance for I/O-bound workloads. Network throughput and disk I/O latency both improve significantly with paravirtualized drivers. However, this requires explicit kernel support and careful configuration during installation—the standard installation flow won’t work without additional parameters.

You trade flexibility (the guest must know it’s virtualized) for performance, which makes sense for dedicated server workloads but less so for general-purpose VMs.

## Download Installation Media

Download the PXE boot images for Rocky Linux 9. You’ll need the kernel and initial ramdisk to bootstrap the installer:

``` bash
mkdir -p /home/xen/rocky9
cd /home/xen/rocky9
wget https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/images/pxeboot/vmlinuz
wget https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/images/pxeboot/initrd.img
```

Use the official Rocky Linux repository rather than archived CentOS mirrors. If you encounter unexpected kernel panics after installation, check your Xen logs with `xl dmesg`. Test thoroughly before deploying to production.

## Create the Installation Configuration

Create `rocky9.cfg` in your VM directory with the installation parameters:

    name="rocky9install"
    vcpus=4
    memory=2048
    disk=['file:/home/xen/rocky9/vmdisk0,xvda,w']
    vif=['bridge=xenbr0']
    on_reboot="restart"
    on_crash="restart"
    kernel="/home/xen/rocky9/vmlinuz"
    ramdisk="/home/xen/rocky9/initrd.img"
    extra="ksdevice= inst.repo=https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/ ip=10.0.0.222::10.0.0.2:255.255.255.0:rocky9:eth0:none nameserver=8.8.8.8"

The `extra` field is critical—it passes kernel arguments directly to the installer:

- `ksdevice=` – Skips hardware probing for the kickstart device
- `inst.repo=` – Points to the installation repository (must be accessible from your VM)
- `ip=` – Format is `address::gateway:netmask:hostname:interface:autoconf`
- `nameserver=` – DNS resolver for package downloads

Adjust the IP address, gateway, and netmask to match your network. For DHCP instead of static IP, use `ip=dhcp` and omit the explicit address parameters.

For multiple DNS servers, add additional `nameserver=` parameters on the same line. If your Dom0 uses NetworkManager, verify the bridge configuration with `nmcli connection show` rather than relying on the older `brctl` tool.

## Prepare the Disk Image

Create a 20GB disk image using `truncate` for efficiency on modern systems:

``` bash
truncate -s 20G /home/xen/rocky9/vmdisk0
```

This allocates the file faster than `dd` on systems with sparse file support. Verify the file was created with the correct size:

``` bash
ls -lh /home/xen/rocky9/vmdisk0
```

If you’re using LVM volumes instead of raw files, the configuration remains identical—just reference the logical volume path in the disk line:

    disk=['phy:/dev/vg0/rocky9,xvda,w']

## Start Installation

Launch the VM in console mode:

``` bash
xl create -c /home/xen/rocky9/rocky9.cfg
```

The `-c` flag attaches the console so you can interact with the installer. Monitor package downloads and follow the standard Rocky Linux 9 installation prompts. Choose text mode if prompted by the graphical installer.

Watch for network timeouts during package downloads—if the installer hangs, your bridge configuration is likely incorrect. Press Ctrl+Alt+F2 to drop to a shell and test connectivity:

``` bash
ip addr show
ping 8.8.8.8
```

Once the installation completes and the VM shuts down, proceed to the production boot configuration.

## Boot with Pygrub

After installation completes, create the production configuration file, `rocky9-prod.cfg`:

    name="rocky9"
    vcpus=4
    memory=2048
    disk=['file:/home/xen/rocky9/vmdisk0,xvda,w']
    vif=['bridge=xenbr0']
    on_reboot="restart"
    on_crash="restart"
    bootloader="pygrub"

Key differences from the installation config:

- Removed `kernel`, `ramdisk`, and `extra` parameters
- Added `bootloader="pygrub"` to use the in-guest bootloader

Start the VM:

``` bash
xl create -c /home/xen/rocky9/rocky9-prod.cfg
```

Pygrub reads the GRUB2 configuration inside the guest and boots accordingly. This is cleaner than managing kernels on the Dom0 side. If GRUB2 changes (kernel updates), the VM automatically picks up the new configuration on next boot.

For guests requiring specific tuning parameters, you can still pass arguments via the Xen configuration without specifying a kernel. Use the `extra=` line with just your tuning parameters and let pygrub handle bootloader selection.

## Troubleshooting

### Kernel panics or hardware errors during installation

Check Dom0 logs with `xl dmesg`. Some Rocky Linux kernels have compatibility issues with certain Xen versions. Enable serial console logging in the guest kernel parameters to capture panic details:

    extra="console=hvc0 inst.repo=https://dl.rockylinux.org/pub/rocky/9/AppStream/x86_64/os/ ..."

Verify your Xen version supports paravirtualized guests with `xl info | grep xen_major`.

### Network not available during installation

Verify the bridge exists on Dom0:

``` bash
ip link show
nmcli connection show
```

Ensure the `ip=` parameter is syntactically correct—missing colons or incorrect netmask notation will silently fail. Test manually on a test guest to validate the network setup:

``` bash
ip addr add 10.0.0.222/24 dev eth0
ping 8.8.8.8
```

If using NetworkManager, ensure the bridge connection is active:

``` bash
nmcli connection up <bridge-name>
```

### Pygrub fails to find bootloader

Check that GRUB2 was installed during package selection. Some minimal installations might skip it. Boot back into the installation config and install grub2-tools:

``` bash
yum install grub2-tools
grub2-mkconfig -o /boot/grub2/grub.cfg
```

Then reboot the VM with the production config.

### VM hangs on shutdown

Some Rocky Linux versions hang during reboot in paravirtualized mode due to ACPI/reboot handler issues. Try adding `extra="acpi=off"` to your production config and test:

    extra="acpi=off"

If the guest still hangs, use `xl destroy <domain>` from Dom0 to force shutdown.

### Disk performance is poor

Verify you’re using paravirtualized block device names (`xvda` not `sda`). Check that the guest kernel has xen-blkfront drivers loaded:

``` bash
lsmod | grep xen
```

If missing, rebuild the initramfs including xen drivers:

``` bash
dracut -f --add xen
```

## Performance Tuning

For production deployments, consider these additional parameters:

- **Memory balloon**: Add `memory=2048` and `maxmem=4096` to allow dynamic memory adjustment without VM restart
- **VCPU pinning**: Pin vCPUs to specific physical cores on Dom0 to reduce context switching
- **Credit scheduler tuning**: Adjust Xen scheduler parameters in Dom0 for latency-sensitive workloads

Monitor guest performance with `xl stats` on Dom0 and verify paravirtual device utilization with `xenstat` if available in your Xen build.
