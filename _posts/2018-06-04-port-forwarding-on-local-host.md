---
title: "Port Forwarding with iptables and nftables"
date: 2018-06-04 15:26:08 +0000
modified: 2026-04-11 17:12:02 +0000
author: "Q A"
layout: post
categories: [databases-storage]
canonical: /port-forwarding-on-local-host/
---

Local port forwarding on the same host requires understanding how netfilter processes packets based on their origin. The critical distinction: traffic from external sources hits the PREROUTING chain, but packets originating locally traverse the OUTPUT chain instead. Miss either one, and your forwarding won’t work.

## The core problem

When you forward UDP port 500 to port 2500 on localhost, you need rules in both chains. Add only a PREROUTING rule and local applications connecting to port 500 will bypass it entirely — they skip PREROUTING and hit OUTPUT instead.

``` bash
# This alone won't work for local traffic
iptables -t nat -A PREROUTING -d 10.8.1.200/32 -p udp --dport 500 -j REDIRECT --to-ports 2500
```

External packets work fine. Local packets don’t. You need both chains.

## Using REDIRECT (recommended approach)

REDIRECT is simpler and more reliable than DNAT for localhost-to-localhost forwarding. It automatically rewrites the destination to the loopback interface without routing complexity:

``` bash
# Handle external traffic
iptables -t nat -A PREROUTING -d 10.8.1.200/32 -p udp --dport 500 -j REDIRECT --to-ports 2500

# Handle local traffic
iptables -t nat -A OUTPUT -d 10.8.1.200/32 -p udp --dport 500 -j REDIRECT --to-ports 2500
```

This works for UDP and TCP. For TCP, omit the protocol specification or use `-p tcp`:

``` bash
# TCP forwarding
iptables -t nat -A PREROUTING -d 10.8.1.200/32 -p tcp --dport 500 -j REDIRECT --to-ports 2500
iptables -t nat -A OUTPUT -d 10.8.1.200/32 -p tcp --dport 500 -j REDIRECT --to-ports 2500
```

## Testing the setup

Start a listener on the target port in one terminal:

``` bash
# Using nc (netcat)
nc -l -u -p 2500

# Or with socat for more control
socat UDP-LISTEN:2500,reuseaddr -
```

Send traffic from another terminal:

``` bash
echo "test message" | nc -u 127.0.0.1 500
```

The listener should receive the message. If it doesn’t, check your rules with `iptables -t nat -S` and verify no firewall is blocking port 2500.

## Alternative: DNAT with OUTPUT rules

If you prefer DNAT over REDIRECT:

``` bash
iptables -t nat -A PREROUTING -d 10.8.1.200/32 -p udp --dport 500 -j DNAT --to-destination 10.8.1.200:2500
iptables -t nat -A OUTPUT -d 10.8.1.200/32 -p udp --dport 500 -j DNAT --to-destination 10.8.1.200:2500

# Allow the redirected traffic in the forward chain
iptables -A FORWARD -p udp -d 10.8.1.200/32 --dport 2500 -j ACCEPT
```

DNAT requires explicit FORWARD rules. REDIRECT handles this more elegantly and is preferred for localhost scenarios.

## Using nftables (modern alternative)

nftables is the modern replacement for iptables. If your system supports it (most distributions now do), use nftables instead:

``` bash
# Redirect inbound traffic
nft add rule inet filter input iifname "lo" udp dport 500 redirect to 2500

# Or for a specific address
nft add rule inet nat prerouting meta protocol ip ip daddr 10.8.1.200 udp dport 500 redirect to 2500
nft add rule inet nat output meta protocol ip ip daddr 10.8.1.200 udp dport 500 redirect to 2500
```

List your rules to verify:

``` bash
nft list ruleset
```

Save the configuration:

``` bash
nft list ruleset > /etc/nftables.conf
systemctl enable nftables
systemctl restart nftables
```

## Making iptables rules persistent

iptables rules flush on reboot. Choose one method below based on your distribution:

**Debian/Ubuntu with iptables-persistent:**

``` bash
apt install iptables-persistent
iptables-save > /etc/iptables/rules.v4
systemctl enable iptables-persistent
systemctl start iptables-persistent
```

After making rule changes, update the saved rules:

``` bash
iptables-save > /etc/iptables/rules.v4
```

**RHEL/CentOS/Fedora with firewalld:**

``` bash
firewall-cmd --permanent --add-forward-port=port=500:proto=udp:toport=2500
firewall-cmd --reload
```

Verify persistence:

``` bash
firewall-cmd --list-forward-ports
```

**With nftables:**

``` bash
systemctl enable nftables
systemctl start nftables
```

nftables loads `/etc/nftables.conf` on boot if the service is enabled.

## Verifying your setup

Check that rules are loaded:

``` bash
# View all nat rules
iptables -t nat -S

# View all filter rules
iptables -S

# With nftables
nft list ruleset
```

Verify IP forwarding is enabled (required for cross-interface forwarding):

``` bash
cat /proc/sys/net/ipv4/ip_forward
```

If it returns 0, enable it:

``` bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```

Make it persistent:

``` bash
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.d/99-forwarding.conf
sysctl -p /etc/sysctl.d/99-forwarding.conf
```

## Debugging common issues

**Traffic reaches the listener but responses don’t return:** Check that your listener is binding to the forwarded port, not just listening on all interfaces. Use `netstat -tlnup` or `ss -tlnup` to verify.

**Local traffic doesn’t forward but external does:** You forgot the OUTPUT chain rule. Add it with the same parameters as your PREROUTING rule.

**Rules work temporarily but disappear after reboot:** You haven’t made them persistent. Use iptables-persistent, firewalld, or nftables to persist rules across reboots.

**Port already in use:** Verify nothing else is listening on the target port:

``` bash
ss -tlnup | grep 2500
lsof -i :2500
```
