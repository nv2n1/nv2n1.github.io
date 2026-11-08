---
title: "Configuring QEMU Guest Network Access Over Wireless"
date: 2018-03-24 11:43:30 +0000
author: "Weiwei Jia"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-config-network-in-host-wireless-network-for-qemu-guest-os/
---

When your host machine connects to the network via WiFi, giving QEMU guests network access requires a different approach than traditional bridged networking. Since wireless interfaces typically don’t support bridge mode, you’ll need to use NAT (Network Address Translation) or a tap device with masquerading.

## Understanding your options

**NAT mode** is the simplest approach—the host acts as a router, translating between guest traffic and the wireless network. This works out of the box with modern QEMU but has limitations: guests can’t be reached from the host or other machines on the network, and port forwarding becomes necessary for inbound connections.

**User mode networking** is even simpler and requires no setup, but it’s slower and has stricter limitations on what protocols work.

**Tap with masquerading** gives guests direct network access while using the wireless interface as the uplink. This is more complex to configure but more flexible.

## Setting up NAT with tap devices

NAT is usually your best choice. You’ll need a helper script and proper iptables rules.

Create `/etc/qemu-ifup`:

``` bash
#!/bin/bash
# Enable IP forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward

# Configure the tap interface
ip link set $1 up
ip addr add 192.168.122.1/24 dev $1

# Add masquerading rule for your wireless interface
iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
iptables -A FORWARD -i $1 -o wlan0 -j ACCEPT
iptables -A FORWARD -i wlan0 -o $1 -m state --state RELATED,ESTABLISHED -j ACCEPT
```

Replace `wlan0` with your actual wireless interface name. Make it executable:

``` bash
chmod +x /etc/qemu-ifup
```

Create `/etc/qemu-ifdown` to clean up when guests stop:

``` bash
#!/bin/bash
ip link set $1 down
```

``` bash
chmod +x /etc/qemu-ifdown
```

## Launching the guest

Start your guest with proper tap and network configuration:

``` bash
sudo qemu-system-x86_64 \
  -enable-kvm \
  -m 2048 \
  -drive file=guest.qcow2,format=qcow2 \
  -netdev tap,id=net0,ifname=tap0,script=/etc/qemu-ifup,downscript=/etc/qemu-ifdown \
  -device virtio-net-pci,netdev=net0 \
  -display vnc=127.0.0.1:0
```

Note the modern syntax using `-netdev` and `-device` instead of the older `-net` flags, which improves performance and reliability.

## Guest configuration

Inside the guest, configure your network interface to use DHCP or static IP. For a static address on the 192.168.122.0/24 network:

**Linux guest example:**

``` bash
# Using ip command
ip addr add 192.168.122.100/24 dev eth0
ip route add default via 192.168.122.1

# Or edit /etc/network/interfaces for Debian/Ubuntu
auto eth0
iface eth0 inet static
  address 192.168.122.100
  netmask 255.255.255.0
  gateway 192.168.122.1
```

**For DHCP**, configure your host to run dnsmasq on the tap interface or install libvirt, which handles all this automatically.

## Using libvirt (recommended)

For repeated guest launches, libvirt abstracts away the complexity:

``` bash
virsh net-start default
virt-install \
  --name myguest \
  --memory 2048 \
  --vcpus 2 \
  --disk path=/var/lib/libvirt/images/guest.qcow2 \
  --network network=default \
  --graphics vnc=127.0.0.1:0 \
  --os-variant linux2024
```

This automatically configures NAT, DHCP, and DNS for your guests without manual iptables rules.

## Troubleshooting

If guests can’t reach the network:

- Verify IP forwarding is enabled: `cat /proc/sys/net/ipv4/ip_forward` should return `1`
- Check iptables rules: `sudo iptables -L -n` and `sudo iptables -t nat -L -n`
- Confirm the tap interface exists: `ip link show`
- Test connectivity from guest to host gateway: `ping 192.168.122.1`
- Check guest DNS resolution: `cat /etc/resolv.conf` inside the guest should point to a valid resolver

For persistent iptables rules across reboots, use `iptables-persistent` or firewalld rules rather than manual commands.
