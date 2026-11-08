---
title: "How to Deactivate LVM Logical Volumes on Linux"
date: 2018-03-24 11:47:22 +0000
layout: post
canonical: https://www.systutorials.com/how-to-deactivate-a-lvm-logical-volume-on-linux/
---

You may need to deactivate a LVM volume group to make it unknown to the kernel — typically before removing disks, migrating storage, or performing maintenance. The `vgchange` command handles this with the `-a` (or `--activate`) flag.

## Basic deactivation

To deactivate a volume group named `vg`, use:

``` bash
vgchange -a n vg
```

The `-a n` flag tells `vgchange` to deactivate (n = no) the volume group. This will deactivate all logical volumes within that volume group.

## Unmounting before deactivation

Before deactivating, you must unmount all filesystems on the logical volumes. If you skip this step, the deactivation will fail:

``` bash
umount /mnt/lv1
umount /mnt/lv2
vgchange -a n vg
```

If a logical volume is still in use, `vgchange` will refuse to deactivate it and report an error like “device is busy”.

## Deactivating a single logical volume

To deactivate only a specific logical volume rather than the entire volume group, use `lvchange`:

``` bash
lvchange -a n vg/lv_name
```

This is useful when you need to keep other logical volumes in the group active while taking one offline.

## Verifying deactivation status

Check whether a volume group is active with `vgdisplay`:

``` bash
vgdisplay vg | grep Status
```

An active volume group will show `Status allocatable` while a deactivated one will show `Status read-only` or may not appear in `/dev/mapper` at all.

You can also list active logical volumes:

``` bash
lvs -o lv_name,lv_attr
```

The third character in the attributes field indicates activation status: `a` means active, `-` means inactive.

## Common scenarios

**Preparing for disk removal:** Deactivate the volume group, then safely remove the physical volumes or disks.

**Migrating LVM to new storage:** Deactivate on the old system, reactivate on the new system after the data is migrated.

**Troubleshooting:** If a logical volume is corrupted or causing kernel errors, deactivating it can prevent the system from attempting to mount it on reboot.

## Re-activating a volume group

To bring a deactivated volume group back online:

``` bash
vgchange -a y vg
```

The `-a y` flag reactivates (y = yes) the volume group, making its logical volumes accessible again. You can then mount the filesystems as needed.

## Handling activation errors

If `vgchange -a n` fails with “device is busy” even after unmounting, check for other processes holding the device:

``` bash
lsof | grep /dev/mapper/vg
fuser -m /dev/mapper/vg
```

Kill any lingering processes or close the files, then retry the deactivation. In some cases, restarting the system is necessary to fully release device locks.

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
