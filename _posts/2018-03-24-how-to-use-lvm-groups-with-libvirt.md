---
title: "Managing LVM Storage with libvirt"
date: 2018-03-24 08:19:46 +0000
author: "Q A"
layout: post
categories: [system-administration-cloud]
canonical: /how-to-use-lvm-groups-with-libvirt/
---

By default, libvirt stores VM images as files in `/var/lib/libvirt/images/`. While functional, this approach limits flexibility. LVM (Logical Volume Management) provides better control over disk space, snapshots, and performance tuning. Using LVM volumes as libvirt storage pools lets you manage VM storage like block devices rather than files, giving you faster provisioning, atomic snapshots, and better resource allocation.

## Prerequisites

You’ll need:

- A working libvirt installation (`libvirtd` running)
- An existing LVM volume group with available space
- `virsh` CLI tool
- Appropriate permissions (typically root or libvirt group membership)

If you don’t have LVM set up yet, create a volume group first:

``` bash
# Create physical volume
pvcreate /dev/sdb

# Create volume group
vgcreate vg-libvirt /dev/sdb

# Verify
vgs
```

## Adding an LVM Volume Group as a Storage Pool

The cleanest approach is to define the LVM volume group as a libvirt storage pool using XML.

### Via virsh

Create a pool definition file:

``` xml
<pool type='logical'>
  <name>vg-libvirt</name>
  <target>
    <path>/dev/vg-libvirt</path>
  </target>
</pool>
```

Save this as `lvm-pool.xml`, then define it:

``` bash
virsh pool-define lvm-pool.xml
virsh pool-start vg-libvirt
virsh pool-autostart vg-libvirt
```

Verify the pool is active:

``` bash
virsh pool-list --all
virsh pool-info vg-libvirt
```

### Via virt-manager GUI

If you prefer the GUI, open virt-manager and navigate to:

- File → Add Connection (if needed)
- Right-click the connection → Details → Storage
- Click the “+” button
- Select “Logical: LVM volume group”
- Choose your existing VG from the dropdown
- Confirm and the pool will be created

## Creating VMs in the LVM Pool

Once the pool is defined, you can create volumes within it and launch VMs using those volumes.

Create a logical volume for a VM:

``` bash
lvcreate -L 20G -n vm-disk1 vg-libvirt
```

Or let libvirt create the volume for you when defining a VM. In the VM XML, reference your pool:

``` xml
<disk type='volume' device='disk'>
  <driver name='qemu' type='raw'/>
  <source pool='vg-libvirt' volume='vm-disk1'/>
  <target dev='vda' bus='virtio'/>
</disk>
```

List volumes in your pool:

``` bash
virsh vol-list vg-libvirt
```

## Snapshots and Cloning

LVM snapshots are significantly faster with the logical pool type than with file-based storage.

Create a snapshot:

``` bash
lvcreate -L 5G -s -n vm-disk1-snap /dev/vg-libvirt/vm-disk1
```

Clone an existing volume:

``` bash
virsh vol-clone vg-libvirt vm-disk1 vm-disk1-clone
```

## Monitoring and Maintenance

Check pool and volume usage:

``` bash
virsh pool-info vg-libvirt
virsh vol-info vg-libvirt vm-disk1
```

Resize a logical volume if needed:

``` bash
lvextend -L +10G /dev/vg-libvirt/vm-disk1
```

Note: VM filesystems won’t automatically grow with the LV. You’ll need to extend partitions/filesystems inside the guest separately using standard tools like `growpart` or `parted`.

Delete a volume:

``` bash
virsh vol-delete --pool vg-libvirt vm-disk1
```

## Removing the Storage Pool

If you need to stop using the pool:

``` bash
virsh pool-destroy vg-libvirt      # Stop the pool
virsh pool-undefine vg-libvirt     # Remove the definition
```

This only removes the libvirt definition; your logical volumes remain intact on disk.

## Performance Considerations

- Use `type='raw'` for VM disks in LVM pools—it provides better performance than `qcow2`
- Consider using `cache='directsync'` or `cache='none'` for the disk cache mode if you’re not using filesystem-level caching
- LVM snapshots consume space in your VG; monitor available space regularly with `vgs` and `lvs`

LVM storage pools integrate seamlessly with libvirt and offer a robust alternative to file-based VM storage, especially for production environments where snapshot and cloning performance matter.
