---
title: "Cloning LVM-Backed Xen Domains"
date: 2013-07-12 16:32:18 +0000
modified: 2026-04-12 05:28:20 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /duplicating-lvm-backed-xen-domu/
---

LVM snapshots provide an efficient way to duplicate virtual machines in seconds rather than minutes. Instead of copying an entire filesystem, snapshots leverage copy-on-write semantics—physical blocks are only duplicated when the source or snapshot is modified. This approach works well for any LVM-backed virtualization platform, though Xen is used here as an example.

**Note**: Xen remains in production use (AWS EC2, Citrix Hypervisor), but KVM has become the default hypervisor for most Linux distributions. Modern alternatives include KVM with libvirt, QEMU, or container solutions like Docker and Kubernetes. The snapshot principles here apply to any LVM-backed hypervisor.

## Setup

This guide assumes:

- Existing Xen DomU backed by LVM logical volume `/dev/vg_xen/vm-10.0.0.123`
- Target clone: `vm-10.0.0.124` with IP `10.0.0.124`
- New volume stored in `vm-10.0.0.124` in the `vg_xen` volume group

## Step 1: Create the LVM Snapshot

First, shut down the source VM to avoid in-flight writes:

``` bash
xm shutdown vm-10.0.0.123
```

Create a snapshot of the logical volume with the same capacity as the original:

``` bash
lvcreate -L20G -s -n vm-10.0.0.124 /dev/vg_xen/vm-10.0.0.123
```

The `-L20G` allocates 20G of metadata space for tracking changes. Size this based on expected write volume during the snapshot’s lifetime. If the snapshot fills up, it becomes invalid and the VM stops. Monitor snapshot usage:

``` bash
lvs -o lv_name,lv_size,data_percent /dev/vg_xen
```

Alternatively, use `-l` for percentage-based allocation:

``` bash
lvcreate -l 10%ORIGIN -s -n vm-10.0.0.124 /dev/vg_xen/vm-10.0.0.123
```

## Step 2: Create the VM Configuration

Create a configuration file for the new DomU at `/etc/xen/vm-10.0.0.124.cfg` (or your preferred path):

``` ini
name = "vm-10.0.0.124"
type = "pv"
cpus = 2
memory = 2048
disk = ["phy:/dev/vg_xen/vm-10.0.0.124,xvda,w"]
vif = ["bridge=br0"]
bootloader = "/usr/bin/pygrub"
on_reboot = "restart"
on_crash = "restart"
```

Update the `name`, `disk`, and `vif` parameters as needed. Use modern Xen syntax with `type = "pv"` for paravirtualized guests or `type = "hvm"` for full virtualization. The `bridge=br0` example uses the common bridge0 interface; adjust to match your network setup.

## Step 3: Start the VM and Reconfigure

Start the new VM with console attached:

``` bash
xl create -c /etc/xen/vm-10.0.0.124.cfg
```

(Use `xl` instead of the deprecated `xm` command in modern Xen versions.)

Once booted, log in and update network configuration. For systemd-based systems (RHEL 8+, modern Debian/Ubuntu):

``` bash
sudo vi /etc/sysconfig/network-scripts/ifcfg-eth0
# or
sudo vi /etc/netplan/01-netcfg.yaml
```

For RHEL/CentOS style, update the interface file:

``` ini
TYPE=Ethernet
BOOTPROTO=none
DEVICE=eth0
IPADDR=10.0.0.124
NETMASK=255.255.255.0
GATEWAY=10.0.0.1
DNS1=8.8.8.8
ONBOOT=yes
```

Remove the `HWADDR` line if using bridge networking to allow the VM to receive a new MAC address.

For netplan (Debian/Ubuntu):

``` yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: false
      addresses: [10.0.0.124/24]
      gateway4: 10.0.0.1
      nameservers:
        addresses: [8.8.8.8]
```

Apply the changes:

``` bash
sudo systemctl restart networking
# or
sudo netplan apply
```

Exit the console with `Ctrl + ]`.

## Monitoring and Cleanup

The snapshot persists until explicitly removed. Monitor its status:

``` bash
lvdisplay /dev/vg_xen/vm-10.0.0.124
```

Once the cloned VM is stable and you no longer need the snapshot, convert it to a full logical volume by merging it back, or simply keep it as a separate volume if the snapshot served its purpose. To remove the snapshot relationship entirely and commit all changes:

``` bash
lvconvert --merge /dev/vg_xen/vm-10.0.0.124
```

This merges the snapshot data back into the origin volume. The snapshot relationship is then removed.

## Automation

This process is easily scriptable. A shell script can automate snapshot creation, configuration templating, and VM startup, reducing manual effort to seconds.

``` bash
#!/bin/bash

SOURCE_VM="vm-10.0.0.123"
TARGET_VM="vm-10.0.0.124"
TARGET_IP="10.0.0.124"
VG="vg_xen"
SIZE="20G"

# Create snapshot
lvcreate -L${SIZE} -s -n ${TARGET_VM} /dev/${VG}/${SOURCE_VM}

# Create config from template
sed "s/@HOSTNAME@/${TARGET_VM}/g; s/@IP@/${TARGET_IP}/g" \
  /etc/xen/template.cfg > /etc/xen/${TARGET_VM}.cfg

# Start VM
xl create /etc/xen/${TARGET_VM}.cfg
```

Customize the template and variables to match your environment. This approach scales well for bulk VM provisioning.
