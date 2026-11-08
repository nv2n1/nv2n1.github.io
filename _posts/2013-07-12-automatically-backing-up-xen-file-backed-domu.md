---
title: "Automating Backups of Xen File-backed VMs"
date: 2013-07-12 16:31:55 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/automatically-backing-up-xen-file-backed-domu/
---

Xen remains in production use (AWS EC2, Citrix Hypervisor), though KVM has become the standard Linux hypervisor. This guide covers automating backups for file-backed Xen virtual machines. The approach adapts to other hypervisors like KVM with minimal modification.

## Architecture and Prerequisites

The backup system assumes:

- Virtual machines stored in `/lhome/xen/` with individual directories per VM (e.g., `/lhome/xen/vm-10/`)
- Raw disk image files follow naming convention `vmdisk0`
- Configuration files available for VM recreation
- Two backup destinations: local secondary storage and remote backup host
- SSH passwordless authentication already configured between hosts

Compression ratios typically range from 20GB uncompressed to 3-4GB compressed, making network and storage overhead manageable.

## Backup Process Overview

1.  **VM snapshot**: Check running VMs → shutdown → copy disk image → restart
2.  **Local compression**: Compress copied images on local secondary storage
3.  **Remote transfer**: SCP compressed archives to backup host

For scheduling via cron weekly with backups every other week, the marker file approach handles alternating execution. For manual invocation, remove the marker file logic.

## Implementation

``` bash
#!/bin/bash

# Backup script for file-backed Xen DomU
# Runs via cron; adjust paths and VM list for your environment

mark_file="/tmp/xen-bak-marker"
log_file="/lhome/xen/bak.log"
err_log_file="/lhome/xen/bak_err.log"
xen_dir="/lhome/xen"
local_bak_dir="/lhome/xen-bak-tmp"
bak_remote="xenbak@backup_host1:/lhome/xenbak"
vm_list="10.10.10.111 10.10.10.112"

# Rotate logs
[ -f "$log_file" ] && mv "$log_file" "$log_file.old"
[ -f "$err_log_file" ] && mv "$err_log_file" "$err_log_file.old"

exec 1>"$log_file"
exec 2>"$err_log_file"

# Skip if already ran this week (alternating schedule)
if [ -e "$mark_file" ]; then
    rm -f "$mark_file"
    exit 0
else
    touch "$mark_file"
fi

echo "=== Backup started at $(date) ==="

# Identify running VMs
running_vms=""
for vm_id in $vm_list; do
    if xl list 2>/dev/null | grep -q "^vm-$vm_id "; then
        echo "VM vm-$vm_id is running"
        running_vms="$running_vms $vm_id"
    else
        echo "VM vm-$vm_id is not running, skipping"
    fi
done

if [ -z "$running_vms" ]; then
    echo "No running VMs found, exiting"
    exit 0
fi

echo "Backup targets: $running_vms"

# Backup each VM
for vm_id in $running_vms; do
    echo "--- Processing vm-$vm_id at $(date) ---"

    # Shutdown VM
    echo "Shutting down vm-$vm_id"
    xl shutdown vm-$vm_id
    sleep 30

    # Verify shutdown
    if xl list 2>/dev/null | grep -q "^vm-$vm_id "; then
        echo "ERROR: vm-$vm_id did not shutdown, forcing"
        xl destroy vm-$vm_id
        sleep 10
    fi

    # Copy disk image and config
    echo "Copying disk image for vm-$vm_id"
    if [ ! -f "$xen_dir/vm-$vm_id/vmdisk0" ]; then
        echo "ERROR: Disk image not found at $xen_dir/vm-$vm_id/vmdisk0"
        continue
    fi

    cp "$xen_dir/vm-$vm_id/vmdisk0" "$local_bak_dir/vmdisk0-$vm_id" || {
        echo "ERROR: Failed to copy disk image"
        continue
    }

    [ -f "$xen_dir/vm-$vm_id/vm.cfg" ] && \
        cp "$xen_dir/vm-$vm_id/vm.cfg" "$local_bak_dir/vm.cfg-$vm_id"

    # Restart VM
    echo "Restarting vm-$vm_id"
    xl create "$xen_dir/vm-$vm_id/vm.cfg"

    sleep 15
    if ! xl list 2>/dev/null | grep -q "^vm-$vm_id "; then
        echo "WARNING: vm-$vm_id did not restart correctly"
    fi
done

# Compress local backups
echo "--- Compressing backups at $(date) ---"
for vm_id in $running_vms; do
    echo "Compressing vm-$vm_id"
    tar --remove-files -czf "$local_bak_dir/vmdisk0-$vm_id.tar.gz" \
        -C "$local_bak_dir" "vmdisk0-$vm_id" 2>/dev/null

    [ -f "$local_bak_dir/vm.cfg-$vm_id" ] && \
        tar -czf "$local_bak_dir/vm.cfg-$vm_id.tar.gz" \
        -C "$local_bak_dir" "vm.cfg-$vm_id" && \
        rm -f "$local_bak_dir/vm.cfg-$vm_id"
done

# Transfer to remote
echo "--- Transferring to remote at $(date) ---"
for vm_id in $running_vms; do
    echo "Copying vm-$vm_id to $bak_remote"
    if scp "$local_bak_dir/vmdisk0-$vm_id.tar.gz" "$bak_remote/" 2>&1; then
        rm -f "$local_bak_dir/vmdisk0-$vm_id.tar.gz"
        echo "Successfully backed up vm-$vm_id"
    else
        echo "ERROR: Failed to transfer vm-$vm_id"
    fi
done

echo "=== Backup completed at $(date) ==="
scp "$log_file" "$bak_remote/bak-latest.log"
```

## Key Changes and Considerations

**Xen toolstack**: Replace deprecated `xm` commands with `xl`. The `xm` toolstack hasn’t been maintained since Xen 4.2; `xl` is the current standard.

**Error handling**: Add explicit checks after shutdown and restart operations. Force destroy if graceful shutdown fails to prevent stale locks.

**Config handling**: Backup VM configuration files separately, enabling full restoration if needed.

**SSH key setup**: Passwordless authentication requires proper SSH key deployment:

``` bash
ssh-keygen -t ed25519 -N "" -f ~/.ssh/xen_backup
# Copy public key to backup host
ssh-copy-id -i ~/.ssh/xen_backup.pub xenbak@backup_host1
# Configure SSH to use specific key for backup operations
```

**Remote verification**: Periodically test restore procedures. A backup is only valid if you’ve verified recovery.

**Snapshots and LVM**: For Xen on LVM, consider LVM snapshots to reduce VM downtime:

``` bash
lvcreate -L10G -s -n vm_snapshot /dev/vg0/vm_disk
# Mount and backup snapshot instead
```

**Retention policy**: Implement cleanup of old backups on both local and remote systems to manage storage costs.

**Monitoring**: Log backup duration and sizes. Alert on failures:

``` bash
backup_size=$(du -sh "$local_bak_dir" | cut -f1)
echo "Backup size: $backup_size" >> "$log_file"
grep -i error "$err_log_file" && mail -s "Backup errors" admin@example.com < "$err_log_file"
```
