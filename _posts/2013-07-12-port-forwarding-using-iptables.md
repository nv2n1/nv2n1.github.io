---
title: "Linux Port Forwarding with iptables"
date: 2013-07-12 16:32:06 +0000
layout: post
canonical: https://www.systutorials.com/port-forwarding-using-iptables/
---

Port forwarding allows external hosts to reach services inside a private network by mapping traffic from a public address to an internal one. On Linux, this is implemented through iptables rules that modify packet headers as they traverse the kernel’s netfilter framework.

Common use cases include exposing HTTP/HTTPS servers from a private LAN to the internet, providing SSH access to internal machines, or redirecting traffic from low-numbered ports (which require root privileges) to higher-numbered ports running as unprivileged users.

## How iptables Works

iptables organizes rules into **tables** and **chains**. For port forwarding, you need to understand:

**Tables:**

- `nat` — Network Address Translation; modifies source or destination addresses
- `filter` — Packet filtering; accepts or drops packets
- `mangle` — Advanced packet modifications (less common for basic port forwarding)

**Chains in the nat table:**

- `PREROUTING` — Modifies destination addresses (DNAT) before routing
- `POSTROUTING` — Modifies source addresses (SNAT) after routing
- `OUTPUT` — Modifies packets originating from the firewall

**Chains in the filter table:**

- `INPUT` — Packets destined for the firewall itself
- `FORWARD` — Packets passing through the firewall to other networks
- `OUTPUT` — Packets originating from the firewall

When a port-forwarded packet arrives, it passes through: PREROUTING (nat) → routing decision → FORWARD (filter) → POSTROUTING (nat) → delivery to the internal host.

## Basic Port Forwarding Setup

This example forwards incoming HTTP traffic from a gateway’s public IP to an internal HTTP server.

**Network layout:**

    Internet (0.0.0.0/0)
        |
        | eth0: 7.8.9.10
    [Gateway/Firewall]
        | eth1: 192.168.1.1
        |
    LAN (192.168.1.0/24)
        |
        | 192.168.1.2:8080 (internal HTTP server)

**Prerequisites:**

- Enable IP forwarding on the gateway:

  ``` bash
  sysctl -w net.ipv4.ip_forward=1
  ```

- Make it persistent by adding `net.ipv4.ip_forward=1` to `/etc/sysctl.conf` or `/etc/sysctl.d/99-custom.conf`

- Verify it’s enabled: `sysctl net.ipv4.ip_forward`

**iptables rules for this scenario:**

``` bash
# DNAT: redirect port 80 traffic to internal server
iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j DNAT --to-destination 192.168.1.2:8080

# FORWARD: allow the forwarded traffic
iptables -A FORWARD -i eth0 -o eth1 -p tcp -d 192.168.1.2 --dport 8080 -j ACCEPT

# FORWARD: allow return traffic
iptables -A FORWARD -i eth1 -o eth0 -p tcp -s 192.168.1.2 --sport 8080 -j ACCEPT
```

The first rule rewrites the destination address from 7.8.9.10:80 to 192.168.1.2:8080. The second and third rules allow the forward and return packets through the filter table’s FORWARD chain (assuming your default policy drops traffic).

If the gateway itself needs to access the forwarded service, add an OUTPUT rule:

``` bash
iptables -A OUTPUT -t nat -p tcp --dport 80 -j DNAT --to-destination 192.168.1.2:8080
```

## Port Forwarding to Multiple Ports

Forward different external ports to different internal services:

``` bash
# Port 22 (SSH) → 192.168.1.2:22
iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 22 -j DNAT --to-destination 192.168.1.2:22
iptables -A FORWARD -i eth0 -o eth1 -p tcp -d 192.168.1.2 --dport 22 -j ACCEPT

# Port 443 (HTTPS) → 192.168.1.3:443
iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 443 -j DNAT --to-destination 192.168.1.3:443
iptables -A FORWARD -i eth0 -o eth1 -p tcp -d 192.168.1.3 --dport 443 -j ACCEPT
```

## Port Forwarding with Stateful Connections

Modern systems use connection tracking (`conntrack`) to handle reply packets automatically:

``` bash
# Single rule with state matching
iptables -A PREROUTING -t nat -i eth0 -p tcp --dport 80 -j DNAT --to-destination 192.168.1.2:8080
iptables -A FORWARD -i eth0 -o eth1 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth1 -o eth0 -m state --state ESTABLISHED,RELATED -j ACCEPT
```

The `conntrack` module caches connection state, so return packets are automatically matched without explicit rules for each direction.

Check conntrack entries:

``` bash
cat /proc/net/nf_conntrack
```

Each entry shows:

    ipv4 2 tcp 6 431581 ESTABLISHED
    src=7.8.9.20 dst=7.8.9.10 sport=53867 dport=80
    src=192.168.1.2 dst=7.8.9.20 sport=8080 dport=53867
    [ASSURED]

This reveals the original connection (external client to gateway public IP) and the translated connection (to internal server).

## Making Rules Persistent

iptables rules are lost on reboot. Save them with iptables-save or use a service manager:

**Using iptables-persistent (Debian/Ubuntu):**

``` bash
apt-get install iptables-persistent
iptables-save > /etc/iptables/rules.v4
systemctl enable iptables-persistent
```

**Using firewalld (alternative firewall manager):**

``` bash
firewall-cmd --permanent --add-forward-port=port=80:proto=tcp:toport=8080:toaddr=192.168.1.2
firewall-cmd --reload
```

**Manual approach with systemd:**

Create `/etc/systemd/system/iptables-restore.service`:

``` ini
[Unit]
Description=Restore iptables rules
After=network.target

[Service]
Type=oneshot
ExecStart=/sbin/iptables-restore /etc/iptables/rules.v4
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

Then enable it: `systemctl enable iptables-restore.service`

## Debugging Port Forwarding Issues

Check if rules are loaded:

``` bash
iptables -t nat -L -n -v
iptables -t filter -L -n -v
```

Monitor traffic in real-time:

``` bash
watch -n 1 'iptables -t nat -L -n -v | grep DNAT'
```

Verify IP forwarding is enabled:

``` bash
cat /proc/sys/net/ipv4/ip_forward
```

Test connectivity from an external machine:

``` bash
curl http://7.8.9.10
```

Enable verbose logging for dropped packets:

``` bash
iptables -A FORWARD -j LOG --log-prefix "FORWARD_DROP: " --log-level 7
tail -f /var/log/kern.log
```

## UDP Port Forwarding

The same approach works for UDP:

``` bash
# DNS forwarding (UDP port 53)
iptables -A PREROUTING -t nat -i eth0 -p udp --dport 53 -j DNAT --to-destination 192.168.1.2:53
iptables -A FORWARD -i eth0 -o eth1 -p udp -d 192.168.1.2 --dport 53 -j ACCEPT
iptables -A FORWARD -i eth1 -o eth0 -p udp -s 192.168.1.2 --sport 53 -j ACCEPT
```

## Performance Considerations

For high-traffic scenarios, monitor conntrack table saturation:

``` bash
cat /proc/sys/net/netfilter/nf_conntrack_max
cat /proc/net/netfilter/nf_conntrack_count
```

Increase limits if needed:

``` bash
sysctl -w net.netfilter.nf_conntrack_max=262144
echo "net.netfilter.nf_conntrack_max=262144" >> /etc/sysctl.conf
```

Consider switching to `nftables` for modern systems, as iptables is in maintenance mode. The syntax is different but offers better performance and flexibility.
