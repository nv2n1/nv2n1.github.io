---
title: "Mount LVM Volumes from External Hard Drives on Linux"
date: 2018-03-24 11:47:16 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-mount-lvm-volume-from-an-external-hard-disk-on-centos/
---

When you connect an external hard drive with LVM volumes to a RHEL, CentOS, or Rocky Linux system, the logical volumes don’t automatically appear in `/dev`. Unlike some distributions that handle this automatically, you need to manually activate them using `vgchange`.

## Activating LVM Volumes

First, plug in your external drive. Then activate all logical volumes in the volume group:

``` bash
sudo vgchange -aay
```

This command scans for volume groups on all connected devices and activates their logical volumes. The `-aay` flags mean:

- `-a` (activate): Controls availability of logical volumes for I/O
- `ay` (auto-activate): Activates volumes matching the `activation/auto_activation_volume_list` in `/etc/lvm/lvm.conf`

Once activated, your volumes appear as device nodes at `/dev/VolumeGroupName/LogicalVolumeName`.

## Finding Your Volume Group Name

If you’re unsure of your volume group names, scan for them first:

``` bash
sudo pvscan
```

This displays all physical volumes (your external drive’s partitions) and their associated volume groups. You’ll see output like:

      PV /dev/sdc1   VG vg_external   lvm2 [50.00 GiB / 10.00 GiB free]

Then list the logical volumes in that group:

``` bash
sudo lvs vg_external
```

Or to see all volume groups at once:

``` bash
sudo vgs
```

## Mounting the Volume

After activation, mount the logical volume like any standard partition:

``` bash
sudo mount /dev/vg_external/data /mnt/external
```

For persistent mounting across reboots, add an entry to `/etc/fstab`:

    /dev/vg_external/data  /mnt/external  ext4  defaults  0  2

## Dealing with Active Volumes

If you need to exclusively activate a volume (useful in clustered environments), use:

``` bash
sudo vgchange -aey vg_external
```

The `-e` flag activates exclusively on a single node, preventing simultaneous access from multiple hosts.

To deactivate volumes when you’re done (before safely removing the drive):

``` bash
sudo vgchange -an vg_external
```

## Troubleshooting Activation Issues

If `vgchange -aay` doesn’t activate your volumes, check for metadata issues:

``` bash
sudo vgck vg_external
```

If metadata is corrupted, attempt repair:

``` bash
sudo vgck --repairmissing vg_external
```

For volumes that won’t activate due to missing physical volumes, you can still try force-activating them:

``` bash
sudo vgchange -aay --partial vg_external
```

This allows activation even if the volume group is incomplete, though you risk data loss if critical PVs are missing.

## Safe Removal

Before disconnecting the external drive, always deactivate the volumes:

``` bash
sudo umount /mnt/external
sudo vgchange -an vg_external
sudo vgexport vg_external
```

Then safely eject the drive using your system’s eject mechanism or `udisksctl`:

``` bash
sudo udisksctl power-off -b /dev/sdc
```

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
