---
title: "Building Distributed Systems on Linux"
date: 2013-07-12 16:32:17 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /linux-cluster-solutions/
---

Building and maintaining Linux clusters requires coordinated management of user accounts, storage, networking, and services across multiple machines. This guide covers practical approaches to common clustering challenges, from unified authentication to network isolation.

## Account and Storage Management

**Unified Authentication and Home Directories**

Centralizing user management across cluster nodes eliminates the overhead of maintaining individual user accounts on each machine. OpenLDAP provides directory services while automount handles dynamic NFS home directory mounting.

Key considerations:

- LDAP schema design for group management and supplementary groups
- Automount maps for reliable mount point setup across reboots
- UID/GID consistency across all nodes
- Network timeouts and failover behavior when the LDAP server is unreachable

See: \[\[unified-linux-login-and-home-directory-using-openldap-and-nfsautomount\|Unified Linux Login and Home Directory Using OpenLDAP and NFS/automount\]\]

**Home Directory Backup Strategy**

`rsync` remains the standard tool for incremental backup across the cluster. Script it via cron for nightly snapshots, implementing both push and pull backup patterns depending on your security model.

See: \[\[backup-linux-home-directory-using-rsync\|Backup Linux Home Directory Using rsync\]\]

**Encrypted Storage**

eCryptFS provides transparent encryption at the filesystem level, useful for protecting sensitive data stored on shared or backup systems without requiring full-disk encryption overhead.

See: \[\[setting-up-ecryptfs-in-linux\|Setting Up eCryptFS in Linux\]\]

## Network Configuration

**Gateway and Routing**

Modern clusters often require internal network segmentation and controlled external access. `nftables` has replaced `iptables` in newer distributions, though `iptables` syntax remains supported through compatibility layers. For new deployments, prefer `nftables` for cleaner rule management and better performance.

See: \[\[setting-up-gateway-using-iptables-and-route-on-linux\|Setting Up Gateway Using iptables and route on Linux\]\]

**DNS Cache Management**

Flushing DNS cache is necessary after network changes or when debugging resolution issues. Modern systemd-based systems use `systemd-resolved` instead of traditional resolvers:

``` bash
# systemd-resolved
sudo systemctl restart systemd-resolved

# Traditional nscd
sudo systemctl restart nscd
```

See: \[\[flush-dns-cache-of-linux-and-windows-client\|Flush DNS Cache of Linux and Windows Client\]\]

**Network Diagnostics**

Replace deprecated `ifconfig` with `ip` command suite and `ss` for socket statistics:

``` bash
# View interfaces and addresses
ip addr show

# View routing table
ip route show

# View network statistics
ss -tuln
```

See: \[\[finding-out-linux-network-configuration-information\|Finding out Linux Network Configuration Information\]\]

**MAC Address Spoofing**

Set temporary MAC addresses using `ip link`:

``` bash
ip link set dev eth0 address 00:11:22:33:44:55
```

For persistent changes, use NetworkManager or systemd-networkd configuration files.

See: \[\[changing-mac-address-in-linux-aka-mac-spoofing\|Changing MAC Address in Linux aka. MAC Spoofing\]\]

**Secure Inter-Cluster Networking**

Build encrypted overlay networks between distant cluster sites using WireGuard or OpenVPN for simpler management than iptables-based solutions. This approach scales better and provides cleaner isolation.

See: \[\[setting-up-vpn-like-network-between-several-clusters-using-iptables\|Setting Up VPN-like Network Between Several Clusters Using iptables\]\]

## Port Forwarding and Tunneling

**iptables-based Port Forwarding**

Direct port forwarding via iptables works for simple cases but requires careful management of state tracking and connection limits. Monitor resource usage when handling high-traffic ports.

See: \[\[port-forwarding-using-iptables\|Port Forwarding Using iptables\]\]

**SSH Tunneling**

SSH tunnels provide secure, encrypted forwarding with built-in authentication. Use `ssh -L` for local forwarding and `-R` for remote forwarding:

``` bash
# Local forwarding: access remote service as localhost:8080
ssh -L 8080:remote-host:80 gateway-host -N

# Remote forwarding: expose local service to remote machine
ssh -R 8080:localhost:3000 gateway-host -N
```

For persistent tunnels, use systemd service files instead of background processes.

See: \[\[port-forwarding-using-ssh-tunnel\|Port Forwarding Using SSH Tunnel\]\]

**Dynamic SOCKS Proxy**

Create a proxy tunnel with SSH for general traffic routing:

``` bash
ssh -D 1080 gateway-host -N
```

Configure applications or system-wide proxy settings to use `localhost:1080`.

See: \[\[proxy-using-ssh-tunnel\|Proxy Using ssh Tunnel\]\]

## NFS Configuration

**NFS Port Binding**

Lock NFS daemons to specific ports for firewall filtering and reliable cluster communication:

``` bash
# /etc/nfs.conf or /etc/nfs.conf.d/
[nfsd]
port=2049

[mountd]
port=20048

[statd]
port=26789
```

See: \[\[fixing-ports-used-by-nfs-server\|Fixing Ports Used by NFS Server\]\]

**Temporary Filesystem NFS Export**

Exporting `/dev/shm` via NFS creates a fast, shared memory pool for cluster-wide temporary data. Useful for intermediate computation results but remember all data is lost on reboot.

See: \[\[setting-up-a-nfs-server-on-top-of-tmpfs-devshm\|Setting Up a NFS Server on Top of tmpfs /dev/shm\]\]

## Package Management

**Version Pinning**

Modern package managers like `dnf` (successor to yum) support version constraints more cleanly:

``` bash
# dnf
sudo dnf install 'package-version-1.2.3'
sudo dnf versionlock add package
```

For reproducible clusters, use container images instead of managing package versions across nodes.

See: \[\[installing-specific-old-versions-of-packages-in-yum\]\]

**Kernel Updates**

Exclude kernel packages from updates to maintain stability across your cluster. With `dnf`:

``` bash
# /etc/dnf/dnf.conf
exclude=kernel*
```

Or use image-based updates (container rebuild and deploy) for better control.

See: \[\[making-yum-not-update-kernel\|Making yum Not Update Kernel\]\]

## Task Scheduling

**Cron Job Frequency**

The crontab format handles complex schedules. For jobs running less frequently than daily:

``` bash
# Every 14 days at 2 AM
0 2 */14 * * /path/to/script

# Every month on the 1st
0 0 1 * * /path/to/script

# Every 2 weeks (Sunday at 2 AM)
0 2 ? * SUN */2 /path/to/script
```

For more reliable scheduled tasks in modern clusters, use systemd timers instead of cron. They integrate with the service manager, log to journald, and support better error handling.

See: \[\[how-to-run-a-cron-job-every-two-weeks-months-days\|How to Run a cron Job Every Two Weeks / Months / Days\]\]
