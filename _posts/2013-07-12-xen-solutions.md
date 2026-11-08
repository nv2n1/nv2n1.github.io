---
title: "Setting Up Linux Xen Dom0 and DomU Virtual Machines"
date: 2013-07-12 16:32:15 +0000
modified: 2026-04-12 05:28:09 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /xen-solutions/
---

Xen remains a critical hypervisor in production environments—AWS EC2, Citrix Hypervisor, and other cloud platforms rely on it—but most Linux distributions now default to KVM for general-purpose virtualization. If you’re working with Xen specifically, this guide covers Dom0 and DomU setup on modern distributions.

## When to Use Xen

Xen is worth considering if you need:

- Para-virtualization (PV) for lower overhead on older hardware
- Hardware virtualization (HVM) with strong isolation guarantees
- Migration between Xen hosts (live migration is mature)
- Integration with existing Xen infrastructure (cloud providers, enterprise deployments)

For new projects, evaluate KVM/libvirt or container-based solutions first. Xen requires more manual configuration and has a smaller community ecosystem compared to KVM.

## Dom0 Installation and Configuration

Dom0 (the privileged domain) manages all virtual machines. Install it on a bare-metal system.

### Installing Xen on Fedora 41

Fedora provides Xen packages via the standard repositories:

``` bash
sudo dnf install xen xen-hypervisor xen-libs
```

Install the Xen-patched kernel. Modern Fedora kernels support Xen dom0 natively, but verify boot configuration:

``` bash
sudo dnf install xen-dom0-tools kernel-xen
```

Enable and start Xen services:

``` bash
sudo systemctl enable xend
sudo systemctl start xend
```

Verify the hypervisor is running:

``` bash
sudo xl info
```

This outputs hypervisor version, available cores, and memory—confirm your system is running under Xen.

### Configuring Dom0 CPU and Memory

Xen boots with default allocations. Adjust Dom0’s resources to prevent it from consuming all system memory and CPU:

Edit `/etc/xen/xen` (or your bootloader config):

    dom0_mem=2G dom0_max_vcpus=2

This caps Dom0 to 2GB RAM and 2 vCPUs. Adjust based on your hardware and workload. Restart for changes to take effect.

Check current allocation:

``` bash
sudo xl domctl dom0 getdomaininfo
```

## DomU Installation and Configuration

DomUs are guest domains. Use LVM-backed storage for snapshots, easy resizing, and performance.

### Create LVM Backing for DomU

Set up a volume group and logical volumes:

``` bash
sudo lvcreate -L 20G -n vm1-root vg0
sudo lvcreate -L 5G -n vm1-swap vg0
```

### Install DomU with PXE

Create a PXE configuration in `/etc/xen/vm1.cfg`:

    name = "vm1"
    memory = 2048
    vcpus = 2
    vif = ["bridge=xenbr0"]
    disk = ["phy:/dev/vg0/vm1-root,xvda,w", "phy:/dev/vg0/vm1-swap,xvdb,w"]
    bootloader = "pygrub"
    on_poweroff = "destroy"
    on_reboot = "restart"
    on_crash = "restart"

For PXE boot:

    bootloader = "pxelinux"
    kernel = "/boot/vmlinuz-5.10.0-xen"
    ramdisk = "/boot/initrd-5.10.0-xen"

Create and start the domain:

``` bash
sudo xl create /etc/xen/vm1.cfg
sudo xl console vm1
```

Install the guest OS. For Fedora 41:

``` bash
virt-install --paravirt --virt-type xen --name vm1 \
  --memory 2048 --vcpus 2 \
  --disk phy:/dev/vg0/vm1-root,bus=xen \
  --location http://mirror.example.com/fedora/releases/41/Server/x86_64/os/ \
  --network bridge=xenbr0
```

Unmodified Fedora 41 kernels work with Xen HVM and PV domains using pv_ops drivers—no Xenified kernel needed for the guest.

## Managing DomU VMs

### List Running Domains

``` bash
sudo xl list
```

### Duplicate an LVM-Backed DomU

Snapshot and clone efficiently:

``` bash
sudo lvcreate -L 20G -s -n vm2-root /dev/vg0/vm1-root
sudo lvcreate -L 5G -s -n vm2-swap /dev/vg0/vm1-swap
```

Copy the configuration:

``` bash
sudo cp /etc/xen/vm1.cfg /etc/xen/vm2.cfg
```

Edit vm2.cfg to change the name and vif MAC address:

    name = "vm2"
    vif = ["mac=00:16:3e:00:00:02,bridge=xenbr0"]

Start the new domain:

``` bash
sudo xl create /etc/xen/vm2.cfg
```

### Backup DomU

Snapshot the LVM volumes and mount for backup:

``` bash
sudo lvcreate -L 0 -s -n vm1-backup /dev/vg0/vm1-root
sudo mkdir -p /mnt/backup
sudo mount /dev/vg0/vm1-backup /mnt/backup
sudo tar czf vm1-backup.tar.gz -C /mnt/backup .
sudo umount /mnt/backup
sudo lvremove -f /dev/vg0/vm1-backup
```

### Migrate DomU Between Hosts

Live migrate over the network:

``` bash
sudo xl migrate vm1 target-host
```

Both hosts must have the target LVM volume group and identical Xen/kernel versions.

## Performance Tuning

Use HVM (hardware virtual machine) mode for unmodified guests but accept higher overhead. PV (para-virtual) guests perform better but require PV drivers in the guest OS.

For I/O intensive workloads, use LVM snapshots with copy-on-write for efficient snapshots, and consider dedicated network bridges per VM.

## Troubleshooting

Check hypervisor logs:

``` bash
sudo journalctl -u xend -n 50
```

Verify DomU boot:

``` bash
sudo xl console vm1
```

If a DomU won’t start, check syntax in its cfg file:

``` bash
sudo xl create -f /etc/xen/vm1.cfg
```

The `-f` flag provides detailed error output.

For migration issues, ensure both hosts can reach each other and have matching hardware/kernel versions. Use `xl migrate -D` for dry-run diagnostics.
