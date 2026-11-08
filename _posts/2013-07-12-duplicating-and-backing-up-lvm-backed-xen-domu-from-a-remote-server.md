---
title: "Backing Up LVM-Based Xen DomUs Over the Network"
date: 2013-07-12 16:32:18 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /duplicating-and-backing-up-lvm-backed-xen-domu-from-a-remote-server/
---

LVM snapshots provide a fast, efficient way to duplicate virtual machines across servers. This technique applies to any LVM-backed hypervisor including Xen, KVM, and Proxmox. The process uses LVM snapshots on the source server, then transfers the snapshot image to the destination using standard Unix tools.

### Scenario

- Source server: `10.0.0.10` with VM stored in `/dev/vg_xen/vm-10.0.0.123`
- Destination server: `10.0.0.11` where we’ll create `/dev/vg_xen/vm-10.0.0.124`
- New VM IP address: `10.0.0.124`
- For backup-only workflows, you can stop after step 3

### Step 1: Create an LVM Snapshot on the Source Server

Create a snapshot of the source logical volume. The snapshot size should match or exceed the actual data used (not the full volume size). If the source has 20GB allocated but only 5GB used, a 10GB snapshot is sufficient:

``` bash
lvcreate -L20480 -s -n 'vm-10.0.0.123-snapshot' /dev/vg_xen/vm-10.0.0.123
```

**Critical**: Shut down the source VM before creating the snapshot to ensure clean filesystem state and avoid dirty cache writes. Even with snapshots, a running system can leave the filesystem in an inconsistent state.

``` bash
xl shutdown vm-10.0.0.123
```

Or for KVM:

``` bash
virsh shutdown vm-10.0.0.123
```

### Step 2: Image the Snapshot

Transfer the snapshot to a file using `dd`. Use a block size appropriate for your storage—4M is generally faster than 1K for modern disks:

``` bash
dd if=/dev/vg_xen/vm-10.0.0.123-snapshot of=/home/backups/vm-10.0.0.123-lv.img bs=4M conv=fsync
```

The `conv=fsync` option ensures data is written to disk and not buffered, preventing data loss on unexpected shutdown. For faster transfers if bandwidth is the bottleneck, pipe through compression:

``` bash
dd if=/dev/vg_xen/vm-10.0.0.123-snapshot bs=4M conv=fsync | gzip -1 > /home/backups/vm-10.0.0.123-lv.img.gz
```

Use level 1 compression (`-1`) to minimize CPU overhead while still achieving 20-30% size reduction. Once complete, remove the snapshot:

``` bash
lvremove -f /dev/vg_xen/vm-10.0.0.123-snapshot
```

### Step 3: Transfer the Image to the Destination Server

Use `scp` or `rsync`. `rsync` is preferable for large files since it can resume and verify checksums:

``` bash
rsync -avz --progress /home/backups/vm-10.0.0.123-lv.img root@10.0.0.11:/home/backups/
```

For encrypted, high-speed transfer over SSH, rsync uses the SSH cipher configured in your SSH config. Avoid manually specifying weak ciphers—modern SSH (OpenSSH 7.1+) disables arcfour by default for security reasons. Instead, ensure your SSH config uses reasonable defaults:

``` bash
# ~/.ssh/config
Host 10.0.0.11
    Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com
    Compression yes
```

If the image is compressed, decompress on arrival:

``` bash
gunzip /home/backups/vm-10.0.0.123-lv.img.gz
```

### Step 4: Create a Logical Volume on the Destination

On the destination server, create a new logical volume with the same size:

``` bash
lvcreate -L20480 -n 'vm-10.0.0.124' vg_xen
```

### Step 5: Write the Image to the New Logical Volume

``` bash
dd if=/home/backups/vm-10.0.0.123-lv.img of=/dev/vg_xen/vm-10.0.0.124 bs=4M conv=fsync
```

Verify the write succeeded by checking inode counts match:

``` bash
dumpe2fs /dev/vg_xen/vm-10.0.0.124 | grep "Inode count"
dumpe2fs /home/backups/vm-10.0.0.123-lv.img | grep "Inode count"
```

### Step 6: Create VM Configuration

For Xen (legacy xl config):

    name="10.0.0.124"
    cpus=2
    memory=2048
    disk=['phy:vg_xen/vm-10.0.0.124,xvda,w']
    vif=['bridge=xenbr0']
    bootloader = "/usr/bin/pygrub"
    on_reboot = 'restart'
    on_crash = 'restart'

For KVM/libvirt (define via XML):

``` bash
virt-install --name vm-10.0.0.124 --memory 2048 --vcpus 2 \
  --disk /dev/vg_xen/vm-10.0.0.124 --import --os-type linux
```

### Step 7: Boot and Configure the VM

Start the VM:

``` bash
xl create /etc/xen/vm-10.0.0.124.cfg
xl console vm-10.0.0.124
```

Or for libvirt:

``` bash
virsh start vm-10.0.0.124
virsh console vm-10.0.0.124
```

Inside the guest, update network configuration. For systemd-networkd:

``` bash
cat > /etc/systemd/network/10-eth0.network << EOF
[Match]
Name=eth0

[Network]
Address=10.0.0.124/24
Gateway=10.0.0.1
DNS=8.8.8.8
EOF
systemctl restart systemd-networkd
```

For older systems using `/etc/sysconfig/network-scripts/`:

``` bash
sed -i 's/IPADDR=10.0.0.123/IPADDR=10.0.0.124/' /etc/sysconfig/network-scripts/ifcfg-eth0
# Remove HWADDR if using bridge networking
sed -i '/^HWADDR=/d' /etc/sysconfig/network-scripts/ifcfg-eth0
systemctl restart network
```

Exit the console with **Ctrl+\]** for Xen or **Ctrl+^** for some libvirt setups.

### Automation

Wrap these steps in a Bash script for repeatable deployments:

``` bash
#!/bin/bash
SOURCE_HOST="10.0.0.10"
SOURCE_LV="/dev/vg_xen/vm-10.0.0.123"
DEST_LV="/dev/vg_xen/vm-10.0.0.124"
BACKUP_PATH="/home/backups"

# Remote: create snapshot and image
ssh root@$SOURCE_HOST <<'REMOTE'
lvcreate -L20480 -s -n 'vm-10.0.0.123-snapshot' /dev/vg_xen/vm-10.0.0.123
dd if=/dev/vg_xen/vm-10.0.0.123-snapshot of=/home/backups/vm-10.0.0.123-lv.img bs=4M conv=fsync
lvremove -f /dev/vg_xen/vm-10.0.0.123-snapshot
REMOTE

# Local: transfer and write
rsync -avz root@$SOURCE_HOST:$BACKUP_PATH/vm-10.0.0.123-lv.img $BACKUP_PATH/
lvcreate -L20480 -n 'vm-10.0.0.124' vg_xen
dd if=$BACKUP_PATH/vm-10.0.0.123-lv.img of=$DEST_LV bs=4M conv=fsync
```

### Performance Considerations

- **Block size**: Use 4M or 16M for modern storage; 1K is too small and creates unnecessary overhead
- **Compression**: Only compress for network transfer; decompress before writing to avoid CPU bottleneck
- **Snapshot size**: Monitor snapshot usage during the dd phase; if it fills, the snapshot becomes invalid. Use `lvs` to monitor
- **Parallel transfers**: For multiple VMs, transfer images concurrently to better saturate network bandwidth
