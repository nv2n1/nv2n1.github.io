---
title: "Setting Up NFS Server and Client Configuration"
date: 2013-07-12 16:32:26 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-set-up-and-configure-nfs-server-and-clients/
---

### Package Installation

Install the required packages:

``` bash
dnf install nfs-utils
```

`nfs-utils` includes both server and client tools. The separate `rpcbind` package is no longer needed on modern systems — it’s handled as a dependency and runs as part of the NFS service.

### Configure /etc/exports

Edit `/etc/exports` to define which directories clients can mount and with what permissions. Each line specifies a directory, the clients allowed to access it, and mount options.

Example: allow the 10.0.0.0/24 subnet to mount `/home` with read/write access:

    /home 10.0.0.0/24(rw,sync,no_subtree_check,no_root_squash)

Common options:

- `rw` — read/write (default is `ro`)
- `sync` — flush writes to disk immediately (safer, slower)
- `async` — buffer writes (faster, riskier on power loss)
- `no_subtree_check` — disable subtree checking (recommended for modern setups)
- `no_root_squash` — allow root on client to write as root on server (security risk; avoid unless necessary)
- `root_squash` — map root to nobody (default, recommended)
- `all_squash` — map all users to nobody

For more granular control, specify individual hosts:

    /data 192.168.1.10(rw,sync) 192.168.1.11(ro,sync)

Or use CIDR notation for subnets:

    /var/backups 172.16.0.0/16(rw,sync)

After editing `/etc/exports`, apply the changes:

``` bash
exportfs -ra
```

Use `exportfs -v` to verify the current export list.

### Enable and Start the NFS Service

Enable NFS to start on boot:

``` bash
systemctl enable nfs-server
systemctl start nfs-server
```

Check the status:

``` bash
systemctl status nfs-server
```

### Firewall Configuration

NFS uses dynamic ports by default, which complicates firewall rules. To restrict NFS to fixed ports, edit `/etc/nfs.conf`:

    [nfsd]
    port = 2049

    [mountd]
    port = 20048

    [statd]
    port = 662

    [lockd]
    port = 32803

Then restart NFS:

``` bash
systemctl restart nfs-server
```

Allow these ports through the firewall using `firewalld`:

``` bash
firewall-cmd --permanent --add-port=2049/tcp
firewall-cmd --permanent --add-port=2049/udp
firewall-cmd --permanent --add-port=20048/tcp
firewall-cmd --permanent --add-port=20048/udp
firewall-cmd --permanent --add-port=662/tcp
firewall-cmd --permanent --add-port=662/udp
firewall-cmd --permanent --add-port=32803/tcp
firewall-cmd --permanent --add-port=32803/udp
firewall-cmd --reload
```

Or with `ufw` on Debian/Ubuntu systems:

``` bash
ufw allow 2049/tcp
ufw allow 2049/udp
ufw allow 20048/tcp
ufw allow 20048/udp
```

## Configure NFS Clients

### Package Installation

Install the client tools:

``` bash
dnf install nfs-utils
```

On Debian/Ubuntu:

``` bash
apt-get install nfs-common
```

### Mount the NFS Export

Create a mount point and mount the remote directory:

``` bash
mkdir -p /mnt/nfs
mount -t nfs SERVER_IP:/home /mnt/nfs
```

Specify NFS version explicitly (recommended for compatibility):

``` bash
mount -t nfs -o vers=4.2 SERVER_IP:/home /mnt/nfs
```

Verify the mount:

``` bash
mount | grep nfs
df -h /mnt/nfs
```

### Persistent Mounts with /etc/fstab

Add a line to `/etc/fstab` to mount on boot:

    SERVER_IP:/home /mnt/nfs nfs vers=4.2,defaults,_netdev 0 0

The `_netdev` option tells systemd the mount depends on network availability.

Then test:

``` bash
mount -a
```

### Automount with systemd

For automatic mounting only when accessed, create a systemd `.mount` file at `/etc/systemd/system/mnt-nfs.mount`:

``` ini
[Unit]
Description=NFS mount for /home
After=network-online.target
Wants=network-online.target

[Mount]
What=SERVER_IP:/home
Where=/mnt/nfs
Type=nfs
Options=vers=4.2,defaults

[Install]
WantedBy=multi-user.target
```

Enable and start it:

``` bash
systemctl daemon-reload
systemctl enable mnt-nfs.mount
systemctl start mnt-nfs.mount
```

## Debugging and Troubleshooting

### Server-side diagnostics

Check NFS service status:

``` bash
systemctl status nfs-server
systemctl status nfs-mountd
```

List exported directories:

``` bash
exportfs -v
```

Check which ports NFS is listening on:

``` bash
ss -tlnp | grep -E ':(2049|20048|662|32803)'
```

Show active NFS connections:

``` bash
nfsstat -s
```

Monitor NFS operations in real time:

``` bash
nfsstat -l
```

### Client-side diagnostics

Check if the NFS server export is accessible:

``` bash
showmount -e SERVER_IP
```

List currently mounted NFS shares:

``` bash
showmount -a
```

Verify RPC communication:

``` bash
rpcinfo -p SERVER_IP
```

Check mounted NFS filesystems and their status:

``` bash
nfsstat -c
mount | grep nfs
```

Test NFS performance:

``` bash
iozone -e -i 0 -i 1 -s 100M -+n -r 4k /mnt/nfs/testfile
```

### Common Issues

**Stale NFS file handle errors**: Usually caused by the server restarting while clients are connected. Unmount and remount the client:

``` bash
umount -f /mnt/nfs
mount -t nfs SERVER_IP:/home /mnt/nfs
```

**Slow performance**: Check network latency and consider using `async` mode (with risk) or tuning read/write buffer sizes:

``` bash
mount -t nfs -o vers=4.2,rsize=65536,wsize=65536 SERVER_IP:/home /mnt/nfs
```

**Permission denied**: Verify `/etc/exports` permissions and that the client IP is in the allowed range. Check file ownership on the server.

**Connection timeout**: Ensure the server is reachable (`ping`), firewall rules are correct, and NFS service is running on the server.
