---
title: "Installing and Configuring Xen Hypervisor on Fedora"
date: 2014-07-25 02:33:06 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /installing-xen-on-fedora-20-as-domain-0/
---

Xen remains a production-grade hypervisor used by major cloud providers like AWS and Citrix, though KVM has become the default for most Linux distributions. This guide covers setting up Xen Domain-0 (the privileged management domain) on modern Fedora systems.

## Installing Xen Packages

Install the required Xen packages:

``` bash
sudo dnf install xen xen-libs xen-runtime xen-dom0-tools
```

Modern Fedora kernels include pv_ops support required for Domain-0 operation, so no kernel patching is necessary. The `xen-dom0-tools` package provides essential management utilities like `xl` and `xm`.

Verify the installation:

``` bash
rpm -qa | grep xen
```

## Configuring the Boot Loader

Update GRUB2 to include the Xen hypervisor entry:

``` bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

On UEFI systems, use:

``` bash
sudo grub2-mkconfig -o /boot/efi/EFI/fedora/grub.cfg
```

Reboot and select the “Xen” entry from the GRUB2 boot menu. To set it as the default, edit `/etc/default/grub`:

``` bash
GRUB_DEFAULT='Fedora (Xen hypervisor)'
```

Then regenerate the configuration:

``` bash
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

After booting into Domain-0, verify Xen is functioning:

``` bash
xl info
```

This displays system information including Xen version, CPU count, memory allocation, and capabilities. A successful output confirms Domain-0 is operational.

## Setting Up Network Bridging for Guests

Xen guests require a bridge for network connectivity. Modern Fedora systems use `systemd-networkd` or NetworkManager, depending on your setup. If NetworkManager is active and you prefer traditional network management:

``` bash
sudo systemctl disable NetworkManager.service
sudo systemctl enable network.service
sudo systemctl start network.service
```

### Using systemd-networkd (Recommended for Modern Fedora)

Create a netdev file for the bridge `/etc/systemd/network/xenbr0.netdev`:

``` ini
[NetDev]
Name=xenbr0
Kind=bridge
```

Create a network configuration `/etc/systemd/network/xenbr0.network` for DHCP:

``` ini
[Match]
Name=xenbr0

[Network]
DHCP=ipv4
```

Or for static IP:

``` ini
[Match]
Name=xenbr0

[Network]
Address=192.168.1.50/24
Gateway=192.168.1.1
DNS=8.8.8.8
```

Create a configuration for your physical interface `/etc/systemd/network/enp0s25.network`:

``` ini
[Match]
Name=enp0s25

[Network]
Bridge=xenbr0
```

Apply the changes:

``` bash
sudo systemctl restart systemd-networkd
```

### Using Traditional Network Scripts

Create `/etc/sysconfig/network-scripts/ifcfg-xenbr0` for DHCP:

    DEVICE=xenbr0
    TYPE=Bridge
    ONBOOT=yes
    DELAY=0
    BOOTPROTO=dhcp

Or for static IP:

    DEVICE=xenbr0
    TYPE=Bridge
    ONBOOT=yes
    DELAY=0
    BOOTPROTO=static
    IPADDR=192.168.1.50
    NETMASK=255.255.255.0
    GATEWAY=192.168.1.1

Edit your physical network adapter’s configuration (e.g., `/etc/sysconfig/network-scripts/ifcfg-enp0s25`):

    BRIDGE=xenbr0

Restart the network service:

``` bash
sudo systemctl restart network.service
```

### Verify Bridge Setup

Verify the bridge is operational:

``` bash
ip addr show xenbr0
bridge link show
```

You should see the physical interface as a member of the bridge.

## Creating Guest Storage

Create an LVM logical volume for the guest:

``` bash
sudo lvcreate -L 20G -n vm-guest1 vg_xen
```

Or create a file-based disk image:

``` bash
sudo truncate -s 20G /var/lib/xen/images/guest1.img
```

## Creating a Domain-U (Guest) Configuration

Create a guest configuration file at `/etc/xen/vm-guest1.cfg`:

    name = "guest1"
    vcpus = 2
    memory = 2048
    disk = [ 'phy:/dev/vg_xen/vm-guest1,xvda,w' ]
    vif = [ 'bridge=xenbr0' ]
    bootloader = "/usr/bin/pygrub"
    on_reboot = "restart"
    on_crash = "restart"

Configuration options:

- **name**: Guest domain identifier
- **vcpus**: Virtual CPU count
- **memory**: RAM in MB
- **disk**: Block device mapping (`phy:` for physical volumes, `file:` for image files)
- **vif**: Virtual interface configuration with bridge binding
- **bootloader**: Use `pygrub` for PV guests or omit for HVM guests with direct kernel boot
- **on_reboot/on_crash**: Behavior policies

For file-based disk images:

    disk = [ 'file:/var/lib/xen/images/guest1.img,xvda,w' ]

For HVM guests with UEFI:

    name = "guest1-hvm"
    type = "hvm"
    vcpus = 4
    memory = 4096
    disk = [ 'file:/var/lib/xen/images/guest1-hvm.img,hda,w' ]
    vif = [ 'bridge=xenbr0' ]
    kernel = "/usr/lib/xen/boot/hvmloader"
    bios = "ovmf"

## Managing Guest Domains

Start a guest:

``` bash
xl create /etc/xen/vm-guest1.cfg
```

List running domains:

``` bash
xl list
```

Get detailed domain information:

``` bash
xl dominfo guest1
```

Connect to guest console:

``` bash
xl console guest1
```

Exit the console with `Ctrl+]`.

Pause and unpause a guest:

``` bash
xl pause guest1
xl unpause guest1
```

Destroy a guest:

``` bash
xl destroy guest1
```

Create a persistent guest that doesn’t auto-start:

``` bash
xl create -p /etc/xen/vm-guest1.cfg
```

The `-p` flag prevents immediate startup, allowing manual management.

## Monitoring and Troubleshooting

Check Xen daemon status:

``` bash
sudo systemctl status xen.service
```

View Xen logs in real-time:

``` bash
journalctl -u xen -f
```

Monitor resource usage across domains:

``` bash
xl top
```

Check domain-specific statistics:

``` bash
xl stats guest1
```

### Network Connectivity Issues

Verify bridge membership:

``` bash
bridge link show
ip link show
```

Ensure guest vif devices are properly attached to the bridge. Check for the guest’s vif peer on the host:

``` bash
ip link show | grep vif
```

If a guest loses network connectivity, verify the vif is active:

``` bash
xl vif-list guest1
```

Reconnect a vif if needed:

``` bash
xl network-detach guest1 0
xl network-attach guest1 bridge=xenbr0
```

### Console Access Issues

If console access fails, check if xenstored is running:

``` bash
sudo systemctl status xenstored
```

Restart Xen services if needed:

``` bash
sudo systemctl restart xen.service
```

## Enabling Domain-0 Autostart

To automatically start registered guests on boot, enable the service:

``` bash
sudo systemctl enable xen.service
sudo systemctl enable xendomains.service
```

Guests created with persistent configurations will auto-start. To disable autostart for a specific guest:

``` bash
xl shutdown guest1
xl destroy guest1
```

Then recreate it without `-p` if you want it to auto-start, or with `-p` if you manage it manually.
