---
title: "Configuring a Linux Network Gateway with iptables and route"
date: 2013-07-12 16:31:58 +0000
layout: post
canonical: https://www.systutorials.com/setting-up-gateway-using-iptables-and-route-on-linux/
---

A Linux box serving as a network gateway needs two network interfaces:

- **eth0**: Connected to the local network (LAN) with IP 192.168.0.1
- **eth1**: Connected to the upstream network (Internet) with IP 198.51.100.1

The goal is to allow clients on the 192.168.0.0/16 network to route traffic through this gateway to reach external networks.

## Enable IP Forwarding

IP forwarding must be enabled on the gateway for it to relay packets between networks.

Using `sysctl`:

``` bash
sysctl -w net.ipv4.ip_forward=1
```

To make this permanent, add the following to `/etc/sysctl.d/99-forwarding.conf` (or `/etc/sysctl.conf` on older distributions):

    net.ipv4.ip_forward=1

Then apply it:

``` bash
sysctl -p /etc/sysctl.d/99-forwarding.conf
```

## Configure the Routing Table

Add a route for the local network to ensure traffic destined for 192.168.0.0/16 goes out eth0:

``` bash
ip route add 192.168.0.0/16 dev eth0
```

To make this persistent, add it to `/etc/netplan/01-gateway.yaml` (Ubuntu/Debian with netplan):

``` yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: false
      addresses:
        - 192.168.0.1/16
      routes:
        - to: 192.168.0.0/16
          scope: link
    eth1:
      dhcp4: true
```

Or use traditional `/etc/network/interfaces` on Debian-based systems:

    auto eth0
    iface eth0 inet static
        address 192.168.0.1
        netmask 255.255.0.0

## Set Up Source NAT with iptables

The gateway must rewrite the source IP of outgoing packets so replies return through it. Use SNAT for static IPs:

``` bash
iptables -t nat -A POSTROUTING ! -d 192.168.0.0/16 -o eth1 -j SNAT --to-source 198.51.100.1
```

This rule translates packets exiting eth1 (not destined for the local network) to use the gateway’s external IP. The `!` (negation) ensures local traffic within 192.168.0.0/16 is not masqueraded.

If your gateway’s external IP is dynamic (DHCP), use MASQUERADE instead:

``` bash
iptables -t nat -A POSTROUTING ! -d 192.168.0.0/16 -o eth1 -j MASQUERADE
```

MASQUERADE automatically uses the current IP of eth1, making it suitable for dialup or DHCP connections. However, established connections are dropped if the interface goes down, so SNAT is preferred for stable setups.

To persist iptables rules across reboots, use `iptables-persistent` (Debian/Ubuntu):

``` bash
apt install iptables-persistent
iptables-save > /etc/iptables/rules.v4
```

Or on RHEL-based systems, use firewalld for better rule management:

``` bash
firewall-cmd --permanent --add-masquerade --zone=public
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="192.168.0.0/16" masquerade'
firewall-cmd --reload
```

## Verify and Troubleshoot

Test that forwarding works by pinging an external IP from a client:

``` bash
ping 8.8.8.8
```

If packets are dropped, check your iptables rules:

``` bash
iptables -t nat -L -n -v
```

Ensure the POSTROUTING rule is present. If you need to reset all rules during testing:

``` bash
iptables -F
iptables -t nat -F
iptables -t mangle -F
```

Then reapply your rules. Be cautious—flushing rules exposes your gateway. Always rebuild security rules immediately.

## Client-Side Configuration

Configure clients on the LAN to use the gateway:

``` bash
ip route add default via 192.168.0.1 dev eth0
```

Or persistently with netplan on Ubuntu/Debian:

``` yaml
network:
  version: 2
  ethernets:
    eth0:
      dhcp4: false
      addresses:
        - 192.168.0.4/24
      routes:
        - to: 0.0.0.0/0
          via: 192.168.0.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
```

On RHEL-based systems using NetworkManager:

``` bash
nmcli con mod "System eth0" ipv4.gateway 192.168.0.1
nmcli con up "System eth0"
```

Set the DNS server to your ISP’s resolver or a public resolver like 8.8.8.8.

## Security Considerations

A gateway with open iptables rules is a security risk. Implement proper filtering:

``` bash
# Default policy: drop everything
iptables -P FORWARD DROP

# Allow established connections
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow traffic from LAN to external networks
iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT

# Prevent spoofing
iptables -A FORWARD -i eth1 -o eth0 -s 192.168.0.0/16 -j DROP
```

Always test filtering rules in a safe environment before deploying to production.
