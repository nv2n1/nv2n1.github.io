---
title: "NFS Server on tmpfs: Setup and Caveats"
date: 2013-07-12 16:32:04 +0000
modified: 2026-04-12 05:27:42 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /setting-up-a-nfs-server-on-top-of-tmpfs-devshm/
---

tmpfs delivers exceptional I/O performance since it lives entirely in RAM. Exporting it via NFS can be useful for temporary caches, build artifacts, or high-speed data sharing between systems on a trusted network.

The catch: NFS needs additional configuration to export pseudo-filesystems like `/dev/shm`. Without the right settings, you’ll hit access denied errors or fsid warnings.

## Prerequisites

Ensure NFS utilities and the NFS server daemon are installed and running:

``` bash
# Debian/Ubuntu
sudo apt install nfs-kernel-server

# RHEL/CentOS/Fedora
sudo dnf install nfs-utils
sudo systemctl enable --now nfs-server
```

Verify the service is active:

``` bash
sudo systemctl status nfs-server
```

## Configuring /dev/shm Export

Edit `/etc/exports` and add an entry for `/dev/shm`. The critical requirement is the `fsid` option—NFS uses this to uniquely identify the filesystem for NFSv3 and protocol negotiation:

``` bash
# /etc/exports
/dev/shm 10.0.0.0/24(rw,fsid=1,sync)
```

Breaking down the options:

- `rw` — read/write access
- `fsid=1` — assigns a unique filesystem ID (required for pseudo-filesystems like tmpfs)
- `sync` — ensure writes are committed to storage before responding (safer, slightly slower)

Alternatively, use `async` if you prioritize speed over durability for temporary data:

``` bash
/dev/shm 10.0.0.0/24(rw,fsid=1,async)
```

Other useful options to consider:

- `no_subtree_check` — improves performance by skipping subtree permission checks (acceptable for temporary exports)
- `no_all_squash` — preserves UID/GID mapping from clients (use `all_squash` to map all requests to a specific user if you need isolation)

A more complete example:

``` bash
/dev/shm 10.0.0.0/24(rw,fsid=1,sync,no_subtree_check,no_all_squash)
```

## Applying Changes

After editing `/etc/exports`, reload the NFS server:

``` bash
sudo exportfs -a
```

The `-a` flag applies all entries. Verify the export was registered:

``` bash
sudo exportfs -v
```

You should see `/dev/shm` listed with the fsid option. Check for warnings—if exportfs complains, review your syntax.

## Mounting from a Client

On any client system with NFS utilities installed, mount the export:

``` bash
sudo mkdir -p /mnt/nfs_tmpfs
sudo mount -t nfs -o vers=4.1,hard,intr 10.0.0.x:/dev/shm /mnt/nfs_tmpfs
```

Use NFSv4.1 or later for better reliability and performance than NFSv3. The `hard` option ensures the client retries indefinitely if the server is unreachable, and `intr` allows interrupting hung mounts with Ctrl+C.

Verify the mount:

``` bash
mount | grep nfs_tmpfs
df -h /mnt/nfs_tmpfs
```

To mount automatically at boot, add an entry to `/etc/fstab`:

``` bash
10.0.0.x:/dev/shm /mnt/nfs_tmpfs nfs vers=4.1,hard,intr,x-systemd-automount 0 0
```

## Important Considerations

**Data persistence**: `/dev/shm` is volatile. Rebooting the NFS server erases all data. Never rely on it for anything that must survive a reboot.

**Security**: This setup assumes a trusted network. Without Kerberos or TLS (NFSv4.2 with encryption), NFS traffic is not encrypted. For production or untrusted networks, configure Kerberos authentication via `/etc/krb5.keytab` or use a VPN tunnel.

**Size limits**: Check your tmpfs mount size:

``` bash
mount | grep shm
df -h /dev/shm
```

By default, `/dev/shm` uses half of system RAM. Resize it if needed:

``` bash
sudo mount -o remount,size=16G /dev/shm
```

Make this permanent in `/etc/fstab`:

``` bash
tmpfs /dev/shm tmpfs size=16G,defaults 0 0
```

**Firewall**: Ensure NFS ports are reachable. NFS uses dynamic ports; open the NFS service properly:

``` bash
# UFW (Ubuntu)
sudo ufw allow nfs

# firewalld (RHEL/CentOS)
sudo firewall-cmd --permanent --add-service=nfs
sudo firewall-cmd --reload
```

## Troubleshooting

If the mount fails with “access denied”:

- Verify the client IP matches the subnet in `/etc/exports`
- Re-run `sudo exportfs -a` on the server
- Check `sudo exportfs -v` to confirm the entry is registered
- Review server logs: `sudo journalctl -u nfs-server -n 20`

If the mount succeeds but permissions are wrong, check UID/GID mapping. Use `id` on both systems to verify alignment, or adjust `all_squash` and `anonuid`/`anongid` options in `/etc/exports`.
