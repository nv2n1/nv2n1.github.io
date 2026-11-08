---
title: "Exporting NFSv4 Shares to External Networks"
date: 2017-12-16 03:22:41 +0000
modified: 2026-04-11 17:51:11 +0000
author: "Eric Ma"
layout: post
categories: [development-best-practices]
canonical: /export-nfsv4-server-external-networks/
---

NFSv4 significantly simplifies network exposure compared to NFSv3. Where NFSv3 requires managing multiple dynamic ports (mountd, statd, lockd), NFSv4 uses only port 111 (rpcbind) and port 2049 (NFS). This makes firewall configuration and port forwarding straightforward.

For production environments, consider implementing Kerberos authentication (krb5, krb5i, or krb5p) instead of relying solely on network-based access control. However, basic port forwarding remains a valid approach for many deployments.

### Network Setup Example

This guide assumes:

- External network: 192.168.0.0/16
- Gateway external IP: 192.168.1.100
- NFS server internal IP: 10.2.2.2
- NFS export path: /nfs/data

Replace these values with your actual network configuration.

### Configure Port Forwarding on the Gateway

Set up NAT rules to forward both TCP and UDP traffic for ports 111 and 2049 from the gateway to the internal NFS server:

``` bash
iptables -t nat -A PREROUTING -d 192.168.1.100/32 -p tcp -m tcp --dport 2049 -j DNAT --to-destination 10.2.2.2:2049
iptables -t nat -A PREROUTING -d 192.168.1.100/32 -p udp -m udp --dport 2049 -j DNAT --to-destination 10.2.2.2:2049
iptables -t nat -A PREROUTING -d 192.168.1.100/32 -p tcp -m tcp --dport 111 -j DNAT --to-destination 10.2.2.2:111
iptables -t nat -A PREROUTING -d 192.168.1.100/32 -p udp -m udp --dport 111 -j DNAT --to-destination 10.2.2.2:111
```

If you’re using nftables (the modern replacement for iptables), the equivalent rules are:

``` bash
nft add rule nat prerouting ip daddr 192.168.1.100 tcp dport 2049 dnat to 10.2.2.2:2049
nft add rule nat prerouting ip daddr 192.168.1.100 udp dport 2049 dnat to 10.2.2.2:2049
nft add rule nat prerouting ip daddr 192.168.1.100 tcp dport 111 dnat to 10.2.2.2:111
nft add rule nat prerouting ip daddr 192.168.1.100 udp dport 111 dnat to 10.2.2.2:111
```

Persist your rules according to your system’s firewall management tool. On systemd-based systems, save iptables rules with `iptables-save` or use `firewalld` with permanent rules. For nftables, save the ruleset with `nft list ruleset > /etc/nftables.conf`.

### Configure the NFS Server

On the NFS server (10.2.2.2), edit `/etc/exports` and add the external network subnet with appropriate permissions:

    /nfs/data 192.168.0.0/16(rw,sync,no_root_squash,no_subtree_check)

Key export options explained:

- `rw` — read/write access
- `sync` — force synchronous writes (safer than async, standard for production)
- `no_root_squash` — allows root user on clients to have root privileges on the server (use carefully)
- `no_subtree_check` — disables subtree checking, improving performance

Apply the configuration:

``` bash
exportfs -a
```

Verify the export:

``` bash
exportfs -v
```

Output should show:

    /nfs/data       192.168.0.0/16(sync,wdelay,hide,no_subtree_check,no_auth_nlm,no_acl,no_root_squash)

Ensure `nfs-server` is enabled and running:

``` bash
systemctl enable nfs-server
systemctl start nfs-server
```

### Mount from External Network Client

On a client in the external network (192.168.0.0/16), mount the exported filesystem:

``` bash
mount -t nfs4 192.168.1.100:/nfs/data /nfs
```

For NFSv4, specifying the version explicitly with `-t nfs4` ensures you’re using version 4 and avoids fallback to older protocols.

Add the mount to `/etc/fstab` for persistence:

    192.168.1.100:/nfs/data /nfs nfs4 defaults,hard,intr,_netdev 0 0

The `_netdev` option tells the system to wait for network availability before mounting.

### Troubleshooting

If the mount fails, verify connectivity to the gateway:

``` bash
ping 192.168.1.100
telnet 192.168.1.100 2049
```

Check the NFS server logs:

``` bash
journalctl -u nfs-server -f
```

Verify port forwarding rules are active:

``` bash
iptables -t nat -L -v -n
# or for nftables:
nft list ruleset
```

Confirm the NFS server is listening on both ports:

``` bash
ss -tlnp | grep -E ':(111|2049)'
```

### Security Considerations

Network-based access control via IP ranges provides minimal security. For external network access, implement:

- Kerberos authentication (krb5, krb5i, or krb5p flavors)
- VPN tunneling to the internal network
- Host-based firewall rules limiting client access
- Regular auditing of NFS access logs

Using `no_root_squash` is generally unsafe — consider root_squash (default) unless you have specific requirements for root access from clients.
