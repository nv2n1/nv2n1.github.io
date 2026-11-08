---
title: "Configuring Multiple Static IP Addresses on a Xen VM"
date: 2018-03-24 11:50:52 +0000
modified: 2026-04-12 16:07:40 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-add-two-static-ips-for-a-xen-vm/
---

Configuring multiple static IP addresses on a Xen VM is useful for hosting multiple services, SSL certificates, or failover scenarios. The approach depends on your underlying Linux distribution and whether you’re using traditional network configuration or modern network managers.

## Using ip Command for Immediate Changes

The quickest way to add a secondary IP is with the `ip` command:

``` bash
sudo ip addr add 192.168.1.100/24 dev eth0
sudo ip addr add 192.168.1.101/24 dev eth0
```

Verify the addresses are active:

``` bash
ip addr show eth0
```

This approach works immediately but won’t persist across reboots. Use it for testing or temporary configurations.

## Persistent Configuration with Netplan (Ubuntu/Debian)

Modern Ubuntu and Debian systems use Netplan. Edit or create `/etc/netplan/01-netcfg.yaml`:

``` yaml
network:
  version: 2
  renderer: networkd
  ethernets:
    eth0:
      dhcp4: no
      addresses:
        - 192.168.1.50/24
        - 192.168.1.100/24
        - 192.168.1.101/24
      routes:
        - to: 0.0.0.0/0
          via: 192.168.1.1
      nameservers:
        addresses: [8.8.8.8, 8.8.4.4]
```

Apply the configuration:

``` bash
sudo netplan apply
```

## Persistent Configuration with ifupdown (Legacy Debian/Ubuntu)

For older systems still using `/etc/network/interfaces`:

``` bash
auto eth0
iface eth0 inet static
    address 192.168.1.50
    netmask 255.255.255.0
    gateway 192.168.1.1

iface eth0 inet static
    address 192.168.1.100
    netmask 255.255.255.0

iface eth0 inet static
    address 192.168.1.101
    netmask 255.255.255.0
```

Restart networking:

``` bash
sudo systemctl restart networking
```

## Configuration with NetworkManager (RHEL/CentOS/Fedora)

Create a connection profile in `/etc/NetworkManager/conf.d/` or use nmcli:

``` bash
sudo nmcli connection add type ethernet ifname eth0 con-name eth0 ip4 192.168.1.50/24 gw4 192.168.1.1
sudo nmcli connection modify eth0 +ipv4.addresses "192.168.1.100/24 192.168.1.101/24"
sudo nmcli connection up eth0
```

Verify with:

``` bash
nmcli device show eth0
```

## Important Considerations

**MAC addresses**: Each additional IP can have its own MAC address in Xen. Configure this in your domain XML or via xl command:

``` bash
xl network-attach vm-name type=phy backend=0 vif=mac=00:16:3e:5f:6c:01
```

**Routing**: Ensure your Xen bridge or network backend routes traffic to all configured IPs. On the host, check bridge settings with `brctl show` or `bridge link`.

**Firewall rules**: Verify iptables or firewalld rules allow traffic to all IPs:

``` bash
sudo firewall-cmd --permanent --add-rich-rule='rule family="ipv4" destination address="192.168.1.100/24" accept'
sudo firewall-cmd --reload
```

**IPv6**: Add IPv6 addresses similarly. In Netplan:

``` yaml
addresses:
  - 192.168.1.100/24
  - 2001:db8::1/64
```

## Testing Connectivity

From another machine, ping each address:

``` bash
ping 192.168.1.100
ping 192.168.1.101
```

Check listening services are bound to specific IPs:

``` bash
sudo ss -tulpn | grep LISTEN
```

If services bind to all interfaces (`0.0.0.0`), they’ll respond on any configured IP. Bind to specific IPs in your application or web server configuration if needed.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
