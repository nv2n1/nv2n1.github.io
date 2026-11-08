---
title: "Connecting Multiple Clusters with iptables NAT"
date: 2013-07-12 16:32:20 +0000
layout: post
canonical: https://www.systutorials.com/setting-up-vpn-like-network-between-several-clusters-using-iptables/
---

Connecting servers with internal IPs across multiple clusters over the internet is a common infrastructure requirement. While a traditional VPN is the standard approach, you can implement similar functionality using iptables and Network Address Translation (NAT) rules, often with lower overhead than VPN solutions.

This method works by forwarding traffic between clusters at the IP layer, effectively creating a tunnel-like connection without the encryption or authentication overhead of a true VPN. It’s suitable for private networks where all traffic stays within your infrastructure.

## Architecture Overview

The basic setup involves:

- Multiple clusters, each with internal (private) IP ranges
- Gateway nodes in each cluster with both internal and public IPs
- iptables rules on gateway nodes to forward and translate traffic between clusters
- Routing tables configured to direct cross-cluster traffic through the gateways

Each cluster needs a designated gateway server that will handle inter-cluster traffic. This server must have connectivity to gateways in other clusters (either through public IPs or direct network links).

## Configuration Steps

### Step 1: Enable IP Forwarding

On each gateway node, enable kernel packet forwarding:

``` bash
sysctl -w net.ipv4.ip_forward=1
```

Make this persistent across reboots:

``` bash
echo "net.ipv4.ip_forward=1" >> /etc/sysctl.d/99-forwarding.conf
sysctl -p /etc/sysctl.d/99-forwarding.conf
```

### Step 2: Configure iptables Rules

Set up NAT rules on each gateway to translate traffic destined for other clusters. For a two-cluster setup:

**Cluster A gateway** (internal subnet 10.0.1.0/24, other cluster 10.0.2.0/24):

``` bash
# Allow forwarding between clusters
iptables -A FORWARD -i eth0 -o eth1 -j ACCEPT
iptables -A FORWARD -i eth1 -o eth0 -j ACCEPT

# NAT outgoing traffic to other cluster
iptables -t nat -A POSTROUTING -d 10.0.2.0/24 -o eth0 -j MASQUERADE

# NAT return traffic
iptables -t nat -A PREROUTING -i eth0 -s 10.0.2.0/24 -d 10.0.1.0/24 -j DNAT --to-destination 10.0.1.0/24
```

Replace interface names (eth0, eth1) with your actual interfaces. Typically, one interface connects to the internal cluster network and another to the internet.

### Step 3: Add Static Routes

On non-gateway nodes in each cluster, add routes directing traffic for other clusters through the local gateway:

``` bash
ip route add 10.0.2.0/24 via 10.0.1.1 dev eth0
```

Where 10.0.1.1 is the internal IP of your gateway and 10.0.2.0/24 is the remote cluster subnet.

To persist routes on systems using netplan:

``` yaml
network:
  version: 2
  ethernets:
    eth0:
      addresses:
        - 10.0.1.10/24
      gateway4: 10.0.1.1
      routes:
        - to: 10.0.2.0/24
          via: 10.0.1.1
```

On systems using ifcfg (RHEL/CentOS), add to `/etc/sysconfig/network-scripts/route-eth0`:

    10.0.2.0/24 via 10.0.1.1 dev eth0

### Step 4: Save iptables Rules

Use iptables-persistent (Debian/Ubuntu) or firewalld (RHEL/CentOS 7+) to persist rules:

**Debian/Ubuntu:**

``` bash
apt-get install iptables-persistent
iptables-save > /etc/iptables/rules.v4
```

**RHEL/CentOS with firewalld:**

``` bash
firewall-cmd --permanent --add-rich-rule='rule family="ipv4" source address="10.0.2.0/24" accept'
firewall-cmd --reload
```

For multiple clusters, configure additional rules for each cluster pair. Gateway servers will need rules for all other cluster subnets.

## Testing Connectivity

From a node in Cluster A, test connectivity to a node in Cluster B:

``` bash
ping 10.0.2.50
traceroute 10.0.2.50
```

Monitor the gateway for traffic:

``` bash
tcpdump -i eth0 -n host 10.0.2.50
```

Check current NAT translations:

``` bash
conntrack -L
```

## Performance Considerations

This iptables-based approach avoids VPN encryption overhead, making it faster for high-throughput scenarios. However:

- No encryption — all traffic is sent in plaintext
- No authentication — relies on network isolation
- Requires manual route management at scale
- Gateway becomes a single point of failure per cluster

For production setups with stringent security requirements, consider WireGuard or traditional VPN solutions instead. For internal infrastructure within data centers or private networks, this method works well.

## Scaling to Multiple Clusters

For three or more clusters, configure each gateway with rules for all other cluster subnets:

``` bash
# On Cluster A gateway, for Clusters B and C
iptables -t nat -A POSTROUTING -d 10.0.2.0/24 -o eth0 -j MASQUERADE
iptables -t nat -A POSTROUTING -d 10.0.3.0/24 -o eth0 -j MASQUERADE
```

Add corresponding routes on all non-gateway nodes pointing to their local gateway. With many clusters, consider implementing this with configuration management tools like Ansible to avoid manual errors.

## Debugging Connection Issues

If connectivity fails, check these in order:

1.  Verify IP forwarding is enabled: `sysctl net.ipv4.ip_forward`
2.  Check routes exist: `ip route show`
3.  Verify firewall rules: `iptables -L -v` and `iptables -t nat -L -v`
4.  Confirm DNS resolution if using hostnames: `nslookup hostname`
5.  Test with tcpdump to see if packets reach the gateway
6.  Check MTU if packets are lost: `ip link show eth0`

This approach provides a lightweight alternative to traditional VPNs for internal cluster networking, provided your security model tolerates unencrypted traffic within your network boundary.
