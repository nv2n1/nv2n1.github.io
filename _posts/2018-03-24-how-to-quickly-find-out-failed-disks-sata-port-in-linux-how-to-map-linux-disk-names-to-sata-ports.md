---
title: "Mapping Linux Disk Names to SATA Ports"
date: 2018-03-24 08:14:29 +0000
layout: post
canonical: https://www.systutorials.com/how-to-quickly-find-out-failed-disks-sata-port-in-linux-how-to-map-linux-disk-names-to-sata-ports/
---

When a disk fails on a server with multiple drives, you need to identify which physical SATA port it’s connected to. Linux device names (sda, sdb, etc.) don’t necessarily map to SATA port order, especially after disk failures or in systems with mixed storage.

## Using `lsblk` with Device Paths

The `lsblk` command provides a quick overview of all block devices:

``` bash
lsblk -o NAME,SIZE,SERIAL,DEVPATH
```

The `DEVPATH` output shows the hardware path but doesn’t directly reveal SATA port numbers. For a clearer mapping, combine it with sysfs information:

``` bash
for disk in /sys/block/sd*; do
  name=$(basename $disk)
  devpath=$(cat $disk/device/uevent | grep DEVPATH | cut -d= -f2)
  serial=$(cat $disk/device/vpd_pg80 2>/dev/null | tail -1 | tr -d ' ' || echo "N/A")
  echo "$name: $devpath (Serial: $serial)"
done
```

## Examining sysfs Directly

The most reliable approach is inspecting sysfs, which contains the actual hardware topology:

``` bash
ls -la /sys/block/sda/device
```

This reveals the physical path. For AHCI controllers (most modern SATA), look at:

``` bash
readlink -f /sys/block/sda
```

This gives the full device path. For example:

    /sys/devices/pci0000:00/0000:00:1f.2/ata1/host0/target0:0:0/0:0:0:0

The `ata1` section indicates the SATA controller channel. `ata1` = port 0, `ata2` = port 1, etc.

## Using `dmesg` and `hdparm`

Check kernel messages for disk enumeration:

``` bash
dmesg | grep -i "sata\|ata" | grep -i "sda"
```

This shows which ATA port the kernel assigned to each disk during boot. For a specific disk:

``` bash
hdparm -i /dev/sda | grep -i "model\|serial"
```

## Building a Comprehensive Mapping Script

Create a script that correlates device names with physical ports:

``` bash
#!/bin/bash
echo "Device | SATA Port | Model | Serial"
echo "-------|-----------|-------|-------"

for disk in /sys/block/sd*; do
  name=$(basename $disk)

  # Extract ATA port number from sysfs path
  devpath=$(readlink -f $disk/device)
  ata_port=$(echo "$devpath" | grep -oP 'ata\K\d+' | head -1)

  if [ -z "$ata_port" ]; then
    ata_port="N/A"
  else
    # ATA numbering starts at 1, but ports at 0
    ata_port=$((ata_port - 1))
  fi

  # Get model and serial
  model=$(cat $disk/device/model 2>/dev/null | xargs || echo "Unknown")
  serial=$(cat $disk/device/serial 2>/dev/null | xargs || echo "Unknown")

  echo "$name | $ata_port | $model | $serial"
done
```

## Using `smartctl` for Detailed Information

If you have smartmontools installed, `smartctl` provides comprehensive disk details:

``` bash
smartctl -i /dev/sda
```

This includes model, serial number, and health status. For failing disks:

``` bash
for disk in /sys/block/sd*; do
  name=$(basename $disk)
  status=$(smartctl -H /dev/$name 2>/dev/null | grep "PASSED\|FAILED" || echo "Unknown")
  echo "$name: $status"
done
```

## NVMe and Non-SATA Disks

Modern systems often use NVMe or SAS drives. For NVMe:

``` bash
nvme list
```

For SAS disks, check `/sys/class/sas_device/` or use `lsscsi`:

``` bash
lsscsi -t
```

## Practical Troubleshooting Steps

1.  **Identify the failing disk**: Check system logs or monitoring tools for I/O errors
2.  **Get device name**: Use `dmesg`, `smartctl`, or `syslog` to confirm which `/dev/sdX` is problematic
3.  **Map to physical port**: Use the sysfs method above to correlate with SATA port
4.  **Cross-reference with BIOS**: Many servers allow viewing SATA port assignments in BIOS—compare with Linux findings
5.  **Document the mapping**: Create a server inventory sheet with physical port → Linux device name correlation

When swapping failed disks, physically label each SATA port on your server for future reference. This saves troubleshooting time on subsequent failures.
