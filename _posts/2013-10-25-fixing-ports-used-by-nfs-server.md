---
title: "Configuring Static Ports for NFSv3 RPC Services"
date: 2013-10-25 12:47:25 +0000
layout: post
canonical: https://www.systutorials.com/fixing-ports-used-by-nfs-server/
---

NFSv3 uses multiple RPC services, each requiring its own port assignment. Without explicit configuration, rpcbind assigns random high ports to four critical services, making firewall rules unmaintainable. Modern deployments should prioritize NFSv4 with Kerberos, but legacy NFSv3 environments remain common enough to warrant proper port management.

The NFS service stack includes seven RPC programs:

| Service | Program | Default Behavior | Configuration |
|----|----|----|----|
| rpcbind | portmapper | TCP/UDP 111 (fixed) | Not configurable |
| nfsd | NFS daemon | TCP/UDP 2049 (fixed) | Not configurable |
| mountd | Mount daemon | Random high port | MOUNTD_PORT |
| lockd | Network lock manager | Random high ports | LOCKD_TCPPORT, LOCKD_UDPPORT |
| statd | Network status monitor | Random high port | STATD_PORT |
| rquotad | Remote quota daemon | Random high port | RQUOTAD_PORT |

The four randomized services create operational friction. Each restart potentially assigns different ports, requiring firewall adjustments and breaking port forwarding configurations.

## Setting Static Port Configuration

### RHEL/CentOS/Rocky Systems

Edit `/etc/sysconfig/nfs` and add these assignments:

    RQUOTAD_PORT=875
    LOCKD_TCPPORT=32803
    LOCKD_UDPPORT=32769
    MOUNTD_PORT=892
    STATD_PORT=662

These port numbers follow IANA conventions and avoid conflicts with standard services. Ensure no spaces surround the equals signs—the parser is strict about whitespace.

### Debian/Ubuntu Systems

On newer Debian-based distributions, use `/etc/nfs.conf` instead. Add a `[nfsd]` section:

    [nfsd]
    port = 2049

    [mountd]
    port = 892

    [statd]
    port = 662
    port-min = 32768
    port-max = 32769

    [lockd]
    port = 32803

The `port-min` and `port-max` parameters for statd constrain the UDP port to a single value when you can’t specify it directly.

### Applying Configuration Changes

After editing the configuration file, restart all NFS services:

``` bash
systemctl restart nfs-server
systemctl restart rpc-statd
systemctl restart rpc-mountd
systemctl restart rpc-lockd
```

Some systems may require rpcbind restart:

``` bash
systemctl restart rpcbind
```

Wait a few seconds between restarts to allow sockets to fully release.

## Verifying Port Assignments

Use `rpcinfo` to confirm all services bind to configured ports:

``` bash
rpcinfo -p localhost
```

Expected output should show:

    program vers proto   port
    100000    2   tcp    111  portmapper
    100000    2   udp    111  portmapper
    100024    1   tcp    662  status
    100024    1   udp    662  status
    100011    1   tcp    875  rquotad
    100011    2   tcp    875  rquotad
    100011    1   udp    875  rquotad
    100011    2   udp    875  rquotad
    100003    2   tcp   2049  nfs
    100003    3   tcp   2049  nfs
    100003    4   tcp   2049  nfs
    100003    2   udp   2049  nfs
    100003    3   udp   2049  nfs
    100003    4   udp   2049  nfs
    100021    1   tcp  32803  nlockmgr
    100021    3   tcp  32803  nlockmgr
    100021    4   tcp  32803  nlockmgr
    100021    1   udp  32769  nlockmgr
    100021    3   udp  32769  nlockmgr
    100021    4   udp  32769  nlockmgr
    100005    1   tcp    892  mountd
    100005    2   tcp    892  mountd
    100005    3   tcp    892  mountd
    100005    1   udp    892  mountd
    100005    2   udp    892  mountd
    100005    3   udp    892  mountd

If any services still show random ports in the 32000+ range, troubleshoot:

- Check `/etc/sysconfig/nfs` for syntax errors (no spaces around `=`)
- Verify `/etc/nfs.conf` doesn’t override your settings with conflicting values
- Check `systemctl status nfs-server` for errors during startup
- Review `journalctl -u nfs-server -n 30` for binding failures
- Confirm SELinux isn’t blocking ports with `ausearch -m avc -ts recent | grep nfsd`

## Firewall Configuration with firewalld

Once ports are static, open them in the firewall. Create a custom firewalld service for consistency:

Create `/etc/firewalld/services/nfsv3.xml`:

``` xml
<?xml version="1.0" encoding="utf-8"?>
<service>
  <short>NFSv3</short>
  <description>NFS Version 3 with static RPC ports</description>
  <port protocol="tcp" port="111"/>
  <port protocol="udp" port="111"/>
  <port protocol="tcp" port="2049"/>
  <port protocol="udp" port="2049"/>
  <port protocol="tcp" port="662"/>
  <port protocol="udp" port="662"/>
  <port protocol="tcp" port="875"/>
  <port protocol="udp" port="875"/>
  <port protocol="tcp" port="892"/>
  <port protocol="udp" port="892"/>
  <port protocol="tcp" port="32803"/>
  <port protocol="udp" port="32769"/>
</service>
```

Enable the service:

``` bash
firewall-cmd --permanent --add-service=nfsv3
firewall-cmd --reload
```

Verify with:

``` bash
firewall-cmd --list-services
firewall-cmd --permanent --list-ports
```

For source-restricted access, create a zone rule instead:

``` bash
firewall-cmd --permanent --zone=internal --add-source=192.168.1.0/24
firewall-cmd --permanent --zone=internal --add-service=nfsv3
firewall-cmd --reload
```

## Firewall Configuration with iptables

If running legacy iptables, add rules for each port:

``` bash
for proto in tcp udp; do
  iptables -A INPUT -p $proto --dport 111 -j ACCEPT
  iptables -A INPUT -p $proto --dport 662 -j ACCEPT
  iptables -A INPUT -p $proto --dport 875 -j ACCEPT
  iptables -A INPUT -p $proto --dport 892 -j ACCEPT
  iptables -A INPUT -p $proto --dport 2049 -j ACCEPT
done

iptables -A INPUT -p tcp --dport 32803 -j ACCEPT
iptables -A INPUT -p udp --dport 32769 -j ACCEPT
```

Persist these rules:

``` bash
iptables-save > /etc/iptables/rules.v4
```

For nftables (modern replacement for iptables):

```nftables
table inet filter {
  chain input {
    tcp dport { 111, 662, 875, 892, 2049, 32803 } accept
    udp dport { 111, 662, 875, 892, 2049, 32769 } accept
  }
}
```

## Export Configuration

A functional `/etc/sysconfig/nfs`:

    # Static RPC port assignment
    RQUOTAD_PORT=875
    LOCKD_TCPPORT=32803
    LOCKD_UDPPORT=32769
    MOUNTD_PORT=892
    STATD_PORT=662

    # Optional: increase nfsd thread pool for many clients
    RPCNFSDCOUNT=32

    # Optional: disable NFSv4 for v3-only legacy environments
    # RPCNFSDARGS="-N 4"

Configure shared exports in `/etc/exports`:

    /var/nfs/share  192.168.1.0/24(rw,sync,no_subtree_check,root_squash)
    /var/nfs/ro     192.168.1.0/24(ro,sync,no_subtree_check,root_squash)
    /var/nfs/home   192.168.1.100(rw,sync,no_subtree_check,all_squash,anonuid=1000,anongid=1000)

After any changes to `/etc/exports`:

``` bash
exportfs -ra
exportfs -v
```

The `-v` flag shows all currently exported filesystems and their options.

## Client-Side Requirements

NFS clients need outbound access to:

- Port 111/tcp and 111/udp (rpcbind registration)
- Port 2049/tcp and 2049/udp (nfsd)
- Port 892/tcp and 892/udp (mountd)
- Port 32803/tcp and 32769/udp (lockd)
- Ephemeral ports for NFS callbacks (typically 1024–65535)

Configure client firewalls accordingly. On the client, mount NFSv3 shares with:

``` bash
mount -t nfs -o vers=3,proto=tcp,hard,intr 192.168.1.50:/var/nfs/share /mnt/nfs
```

Use TCP over UDP for better performance and reliability across higher-latency networks.

## Troubleshooting Port Binding Failures

**Service won’t start or bind to configured ports:**

Check for conflicting processes:

``` bash
netstat -tlnp | grep -E ":(111|662|875|892|2049|32803|32769)"
ss -tlnp | grep -E ":(111|662|875|892|2049|32803|32769)"
```

Review detailed service errors:

``` bash
journalctl -u nfs-server -u rpc-mountd -u rpc-statd --no-pager -n 50
```

Check SELinux contexts if enabled:

``` bash
ausearch -m avc -ts recent | grep -E "nfsd|mountd|statd|lockd"
semanage port -l | grep nfs
```

If NFS services still can’t bind, verify kernel NFS modules are loaded:

``` bash
lsmod | grep -E "nfsd|lockd|sunrpc"
```

Load them if missing:

``` bash
modprobe nfsd
modprobe lockd
```

## Security Limitations

Static port configuration is operationally necessary but insufficient for NFSv3 security. The protocol has inherent weaknesses:

- No authentication beyond UID/GID spoofing
- No encryption in transit
- Susceptible to port hijacking and packet forgery

**Minimum hardening steps:**

- Always use `root_squash` in `/etc/exports` to prevent root privilege escalation
- Restrict NFS to isolated, trusted network segments (not Internet-facing)
- Limit exports to specific client IPs using `/etc/exports` source restrictions
- Monitor access with tcpdump or network IDS for unauthorized clients
- Encrypt NFS traffic with VPN (IPsec, WireGuard) when crossing untrusted networks

**For production systems, migrate to NFSv4.1+ with Kerberos:**

    /var/nfs/share  192.168.1.0/24(rw,sync,no_subtree_check,sec=krb5p)

NFSv4 consolidates all RPC services into a single port (2049), reduces random port complexity, and adds authentication and encryption options.
