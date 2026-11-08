---
title: "How to Clone Xen DomU Virtual Machines"
date: 2013-07-12 16:31:50 +0000
modified: 2026-04-12 17:00:34 +0000
author: "Eric Ma"
layout: post
categories: [system-administration-cloud]
canonical: /how-to-duplicate-xen-domu-virtual-machines/
---

Xen remains in active production use—particularly in cloud infrastructure like AWS EC2 and Citrix Hypervisor—though KVM has become the standard hypervisor for most Linux distributions. If you’re managing legacy Xen deployments, this guide covers the essential steps for cloning VBD-based DomU instances.

## Prerequisites

Before starting, ensure:

- The source VM is powered off (critical to avoid disk corruption)
- You have root access on the host domain (Dom0)
- VM files are stored in a consistent location (example: `/home/xen/`)
- Source VM structure: configuration file (`vm0-f11.run`) and virtual disk (`vmdisk0`)

## Step 1: Copy the VM Files

Copy the entire VM directory as root:

``` bash
cp -rv /home/xen/vm-f11-sample /home/xen/vm-10.0.0.213
```

**Critical**: Verify the source VM is shut down before copying. If it’s running, stop it first:

``` bash
xl shutdown vm0
```

For large disks, monitor the copy progress and verify disk space:

``` bash
df -h /home/xen/
du -sh /home/xen/vm-10.0.0.213/
```

File ownership will be root, which is appropriate for VM storage directories.

## Step 2: Update Configuration Files

Navigate to the new VM directory and rename the configuration file:

``` bash
cd /home/xen/vm-10.0.0.213
mv vm0-f11.run vm.run
```

Edit the configuration file with your preferred editor:

``` bash
vim vm.run
```

Update the following fields:

    name="10.0.0.213"
    memory=1024
    disk = ['file:/home/xen/vm-10.0.0.213/vmdisk0,xvda,w']
    vif = ['bridge=eth0']
    bootloader = "/usr/bin/pygrub"
    vcpus=2
    on_reboot = 'restart'
    on_crash = 'restart'

**Key changes**:

- `name`: Set to the new VM hostname or identifier
- `disk`: Update the path to match the new directory (`vm-10.0.0.213`)
- `vif`: Configure bridging based on your network setup (e.g., `bridge=eth0` or `bridge=virbr0`)

If cloning multiple VMs, consider parameterizing the disk path and memory allocation for consistency.

## Step 3: Boot and Configure the New VM

Create and start the new domain:

``` bash
xl create /home/xen/vm-10.0.0.213/vm.run
```

Connect to the console:

``` bash
xl console 10.0.0.213
```

Press Enter to see the login prompt. Log in with your credentials.

## Step 4: Update Network Configuration

For RHEL-based systems, edit the network interface configuration:

``` bash
vi /etc/sysconfig/network-scripts/ifcfg-eth0
```

Update the IP address:

    IPADDR=10.0.0.213
    NETMASK=255.255.255.0
    GATEWAY=10.0.0.1
    ONBOOT=yes

**Important**: Comment out or remove the `HWADDR` line if using Xen bridge networking. This prevents MAC address conflicts:

``` bash
# HWADDR=00:16:3e:xx:xx:xx
```

Restart the network interface:

``` bash
ifdown eth0
ifup eth0
```

Verify connectivity:

``` bash
ip addr show eth0
ping -c 4 10.0.0.1
```

Exit the console with `Ctrl + ]`.

## Step 5: Post-Configuration

Reset the VM from Dom0 to apply any remaining system changes:

``` bash
xl reset 10.0.0.213
```

Reconnect to verify the system boots cleanly:

``` bash
xl console 10.0.0.213
```

## Troubleshooting

**VM fails to start**: Check the configuration file syntax and verify the disk path is correct.

``` bash
xl create -c /home/xen/vm-10.0.0.213/vm.run
```

The `-c` flag attaches the console immediately, showing boot errors.

**Network connectivity issues**: Ensure the bridge interface exists on Dom0:

``` bash
brctl show
```

**Disk I/O errors**: If the source disk was corrupted or the copy was incomplete, verify the target disk:

``` bash
ls -lh /home/xen/vm-10.0.0.213/vmdisk0
```

## Automation Considerations

For repeated cloning, consider writing a shell script that:

- Validates the source VM is offline
- Copies files with rsync for resumable transfers
- Templaces configuration files with sed or awk
- Validates the target disk size matches the source

This reduces manual steps and human error, especially when managing multiple VM deployments.
