---
title: "Installing Fedora 17 PV Guest on Xen with PXE Boot"
date: 2013-07-12 16:32:32 +0000
layout: post
canonical: https://www.systutorials.com/installing-fedora-17-domain-u-on-xen-with-pxe-booting/
---

Xen remains in production use across cloud providers (AWS EC2, Citrix Hypervisor) and large infrastructure deployments, though KVM has become the default hypervisor for most Linux distributions. This guide covers installing a Fedora Domain-U on a Xen Dom0 using PXE boot, applicable to current Fedora releases.

## Prerequisites

- A working Xen Dom0 installation
- LVM backing store for VM disk images (higher performance than file-based)
- PXE-capable network boot environment
- Network connectivity between Dom0 and Domain-U
- xl toolstack (modern replacement for deprecated xm)

## Obtaining PXE Boot Images

Download the latest Fedora PXE boot images from the official repository:

``` bash
wget http://archive.fedoraproject.org/pub/fedora/linux/releases/41/Fedora/x86_64/os/images/pxeboot/vmlinuz
wget http://archive.fedoraproject.org/pub/fedora/linux/releases/41/Fedora/x86_64/os/images/pxeboot/initrd.img
```

Place these in a location accessible to Dom0, such as `/var/lib/xen/pxeboot/`.

## Domain-U Configuration

Create a configuration file for the new Domain-U. Here’s a working example with modern conventions:

    name="vm-10.1.0.235"
    vcpus=4
    memory=2048
    disk=['phy:/dev/vg_xen/vm-10.1.0.235,xvda,w']
    vif=['bridge=br0']
    on_reboot="restart"
    on_crash="restart"
    kernel="/var/lib/xen/pxeboot/vmlinuz"
    ramdisk="/var/lib/xen/pxeboot/initrd.img"
    extra="root=live:http://archive.fedoraproject.org/pub/fedora/linux/releases/41/Fedora/x86_64/os/LiveOS/squashfs.img ip=10.1.0.235::10.1.0.2:255.255.0.0:vm235:eth0:none nameserver=8.8.8.8"

Key points:

- Use `xl` commands instead of the deprecated `xm`
- Network bridge should match your Dom0 configuration (typically `br0`, not `eth0`)
- Disk paths use `phy:` for direct block device access, which is faster than file-based backing
- The `extra` field configures networking and Anaconda installer options
- VM naming convention includes a descriptive prefix (e.g., `vm-`)

## Network Configuration

The `extra` parameter requires careful configuration. The IP assignment follows this format:

    ip=<client>:<server>:<gateway>:<netmask>:<hostname>:<interface>:<autoconf>

For static configuration:

- `client`: VM IP address (10.1.0.235)
- `server`: DHCP/PXE server IP (leave blank if using this format)
- `gateway`: Default gateway (10.1.0.2)
- `netmask`: Network mask (255.255.0.0)
- `hostname`: Hostname or interface identifier
- `interface`: Network device name (eth0)
- `autoconf`: none for static, dhcp for DHCP

For DHCP assignment, simplify to:

    extra="root=live:http://archive.fedoraproject.org/pub/fedora/linux/releases/41/Fedora/x86_64/os/LiveOS/squashfs.img ip=dhcp nameserver=8.8.8.8"

## Creating the LVM Backing Store

Create a logical volume for the Domain-U disk:

``` bash
lvcreate -L 50G -n vm-10.1.0.235 vg_xen
```

Verify creation:

``` bash
lvs /dev/vg_xen/vm-10.1.0.235
```

## Launching the Domain-U

Use `xl` to create and start the Domain-U:

``` bash
xl create /path/to/vm-10.1.0.235.cfg
```

Monitor the installation console:

``` bash
xl console vm-10.1.0.235
```

Press Ctrl+\] to exit the console.

## Troubleshooting

**Installation hangs or fails to fetch packages**: Verify network connectivity from the Domain-U. Check that the HTTP mirror URL is accessible and the interface configuration in the `extra` field is correct.

**Boot fails with “block-attach” errors**: Ensure the LVM logical volume exists and is properly formatted. Check Dom0 LVM status with `lvs`.

**Network unreachable**: Verify the bridge configuration on Dom0:

``` bash
brctl show
```

Ensure the Domain-U network interface is attached to the correct bridge.

**Anaconda installer not starting**: Consult <a href="https://anaconda-project.readthedocs.io/en/latest/" rel="nofollow noopener" target="_blank">Anaconda boot options</a> for complete parameter documentation. Test with verbose output by adding `rd.debug` to the `extra` field.

## Post-Installation

After successful installation, the Domain-U will reboot. Remove the PXE boot kernel and ramdisk from the configuration, update to use the installed kernel:

``` bash
kernel="/var/lib/xen/domU/vm-10.1.0.235/boot/vmlinuz-<version>"
ramdisk="/var/lib/xen/domU/vm-10.1.0.235/boot/initramfs-<version>.img"
```

Or configure the Domain-U for PV GRUB2 boot if preferred, allowing filesystem-based boot selection.

## Performance Considerations

- Use LVM backing for better I/O performance than file-based disks
- Allocate vCPUs proportional to workload; overallocation on Dom0 causes context switching overhead
- Monitor memory pressure: overcommitting memory leads to balloon driver activity and performance degradation
- Use vif rate limiting if network QoS is required

Xen remains a solid choice for production virtualization when KVM doesn’t meet specific requirements or when integrating with existing Xen infrastructure.
