---
title: "Redirecting Packets to the FORWARD Chain with iptables and DNAT"
date: 2018-04-02 15:25:40 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-divert-connection-or-packet-before-routing-decision-entering-the-default/
---

Intercepting traffic before normal routing decisions requires understanding packet flow through iptables chains. If you need incoming packets to bypass the INPUT chain and process through FORWARD instead, you’ll use the PREROUTING chain with Destination NAT (DNAT).

## Packet Flow Through iptables

When a packet arrives at your system, it traverses these chains in order:

1.  **PREROUTING** – Executes before the kernel’s routing decision. This is where you redirect traffic.
2.  **Routing decision** – Kernel determines if the packet is destined for a local process or should be forwarded through the system.
3.  **INPUT** – Processes packets bound for local applications.
4.  **FORWARD** – Processes packets the kernel will route through the system.
5.  **POSTROUTING** – Executes after routing decision, before transmission.

To force packets into FORWARD instead of INPUT, modify the destination address in PREROUTING. This changes the routing decision so the kernel treats the packet as forwarded traffic.

## Enable IP Forwarding

Before using DNAT to redirect traffic, enable IP forwarding:

``` bash
# Temporary (lost on reboot)
echo 1 > /proc/sys/net/ipv4/ip_forward

# Persistent (edit and run sysctl)
sysctl -w net.ipv4.ip_forward=1
```

For persistence across reboots, add this to `/etc/sysctl.d/99-forwarding.conf`:

    net.ipv4.ip_forward = 1

Then apply it:

``` bash
sysctl -p /etc/sysctl.d/99-forwarding.conf
```

## DNAT Rule Implementation

Use DNAT in the PREROUTING chain to change the packet’s destination address:

``` bash
# Redirect inbound traffic on port 443 from specific source
iptables -t nat -A PREROUTING -i eth0 -p tcp \
  -s 100.43.1.10 -d 192.168.1.100 --dport 443 \
  -j DNAT --to-destination 192.168.1.50:443

# Allow these packets through FORWARD chain
iptables -A FORWARD -i eth0 -p tcp \
  -s 100.43.1.10 --dport 443 -j ACCEPT

# Allow return traffic
iptables -A FORWARD -p tcp --sport 443 \
  -m state --state ESTABLISHED,RELATED -j ACCEPT
```

This redirects connections from `100.43.1.10` destined for `192.168.1.100:443` to `192.168.1.50:443` instead, and routes them through the FORWARD chain.

## Critical Configuration Points

**Match destination ports, not source ports**: Source ports are ephemeral and unreliable for filtering. Always use `--dport` in filter rules:

``` bash
# Good
iptables -A FORWARD -p tcp --dport 443 -j ACCEPT

# Avoid
iptables -A FORWARD -p tcp --sport 443 -j ACCEPT
```

**Use stateful rules**: Enable connection tracking to handle bidirectional traffic:

``` bash
iptables -A FORWARD -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A FORWARD -m state --state INVALID -j DROP
```

**Remove conflicting INPUT rules**: If you previously dropped port 443 traffic in the INPUT chain, remove or modify that rule:

``` bash
# List INPUT rules with line numbers
iptables -L INPUT -n -v --line-numbers

# Delete the conflicting rule (e.g., line 5)
iptables -D INPUT 5
```

## Complete Working Example

Here’s a minimal, functional ruleset:

``` bash
# Enable forwarding
sysctl -w net.ipv4.ip_forward=1

# Clear existing rules
iptables -t nat -F PREROUTING
iptables -F FORWARD

# NAT rule: redirect inbound HTTPS traffic
iptables -t nat -A PREROUTING -i eth0 -p tcp \
  -s 203.0.113.5 -d 192.168.1.100 --dport 443 \
  -j DNAT --to-destination 192.168.1.50:443

# FORWARD rules: allow the redirected traffic
iptables -A FORWARD -i eth0 -p tcp \
  -s 203.0.113.5 --dport 443 -j ACCEPT

iptables -A FORWARD -p tcp --sport 443 \
  -m state --state ESTABLISHED,RELATED -j ACCEPT

# Drop invalid packets
iptables -A FORWARD -m state --state INVALID -j DROP

# Masquerade outgoing traffic
iptables -t nat -A POSTROUTING -o eth0 \
  -m state --state NEW,RELATED,ESTABLISHED -j MASQUERADE
```

## Debugging and Verification

Check your active rules:

``` bash
# View all rules with line numbers
iptables -L -n -v --line-numbers

# View NAT table specifically
iptables -t nat -L -n -v --line-numbers

# Monitor active connections matching port 443
watch -n 1 'conntrack -L | grep 443'

# Check packet counters
iptables -L -n -v
```

If packets aren’t reaching FORWARD, verify with tcpdump:

``` bash
# Capture on ingress interface
sudo tcpdump -i eth0 -n tcp and port 443

# Capture on system with verbose output
sudo tcpdump -i any -n tcp and port 443 -vv
```

## Migration to nftables

Modern Linux systems (kernel 3.13+) support nftables, which offers cleaner syntax and better performance. The equivalent nftables rules:

``` bash
# Create table and chain
nft add table inet filter
nft add chain inet filter forward { type filter hook forward priority 0 \; }

# Add FORWARD rules
nft add rule inet filter forward ip saddr 203.0.113.5 tcp dport 443 accept
nft add rule inet filter forward tcp sport 443 ct state established,related accept

# Create NAT table for PREROUTING
nft add table inet nat
nft add chain inet nat prerouting { type nat hook prerouting priority 0 \; }
nft add rule inet nat prerouting ip saddr 203.0.113.5 tcp dport 443 dnat to 192.168.1.50:443

# View complete ruleset
nft list ruleset
```

nftables rules persist across reboots when saved to `/etc/nftables.conf`.
