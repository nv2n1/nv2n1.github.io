---
title: "Retrieving VM IP Addresses in KVM with virsh"
date: 2018-03-24 11:51:02 +0000
layout: post
canonical: https://www.systutorials.com/how-to-get-the-ip-addresses-of-vms-in-kvm-with-virsh/
---

When you create VMs in KVM, they’re typically assigned IP addresses via DHCP. Finding those addresses so you can SSH in requires a few steps. Here are the practical approaches.

## Using virsh domiflist and ARP

The traditional method combines `virsh domiflist` to get the VM’s MAC address, then looks it up in the ARP table:

``` bash
$ virsh domiflist hvm1
 Interface  Type       Source     Model       MAC
 -------------------------------------------------------
 vnet0      network    default    virtio      52:54:00:1c:36:cd
```

Note the MAC address (52:54:00:1c:36:cd). Then check the ARP table:

``` bash
$ arp -e
Address                  HWtype  HWaddress           Flags Mask            Iface
10.80.1.17               ether   52:54:00:2b:08:c3   C                     br0
10.80.1.16               ether   52:54:00:78:02:89   C                     br0
192.168.122.210          ether   52:54:00:1c:36:cd   C                     virbr0
```

Match the MAC from `domiflist` with the ARP entry. In this case, hvm1 has IP 192.168.122.210.

## Using virsh domifaddr (Better Approach)

Modern versions of libvirt (0.10.0+) provide a more direct method with `virsh domifaddr`:

``` bash
$ virsh domifaddr hvm1
 Name       MAC address          IPv4 Address     IPv6 Address
 ---------------------------------------------------------------
 vnet0      52:54:00:1c:36:cd    192.168.122.210  --
```

This works only if the guest has QEMU Guest Agent installed and running, or if libvirt can query the VM’s network configuration directly. This is the preferred approach as it eliminates the need to cross-reference ARP tables.

## Using ip Command (With QEMU Guest Agent)

If your guest has the QEMU Guest Agent (`qemu-guest-agent` package) installed, you can also use:

``` bash
$ virsh qemu-agent-command hvm1 '{"execute":"guest-network-get-interfaces"}'
```

This directly queries the guest’s network interfaces. Install the agent in the guest:

``` bash
# Debian/Ubuntu
sudo apt-get install qemu-guest-agent

# RHEL/CentOS/Fedora
sudo yum install qemu-guest-agent

# Then restart the guest agent service
sudo systemctl restart qemu-guest-agent
```

## Scripting Multiple VMs

To get IP addresses for all running VMs:

``` bash
#!/bin/bash
for vm in $(virsh list --name); do
    echo "VM: $vm"
    virsh domifaddr "$vm" 2>/dev/null || {
        # Fallback to ARP method
        mac=$(virsh domiflist "$vm" | awk 'NR>2 {print $NF}' | grep -oE '([0-9a-f]{2}:){5}[0-9a-f]{2}')
        arp -e | grep -i "$mac" | awk '{print $1}'
    }
done
```

## Troubleshooting

**domifaddr returns nothing:** The guest doesn’t have the QEMU Guest Agent running. Either install it or rely on ARP lookups. Note that some guests behind complex networking setups may not appear in local ARP tables if they’re on different network segments.

**ARP entry not appearing:** The VM hasn’t sent any ARP requests yet. SSH or ping into the VM’s network from another host to trigger an ARP entry. Alternatively, run `arp-scan` or `nmap` on your network range:

``` bash
sudo arp-scan -l
sudo nmap -sn 192.168.122.0/24
```

**IP keeps changing:** Configure static IP addresses in the guest or use DHCP reservations in your libvirt network definition to assign consistent IPs based on MAC address.

## Persistent DHCP Reservations

Edit your libvirt network to reserve IPs by MAC:

``` bash
$ virsh net-edit default
```

Add this inside the `<network>` block:

``` xml
<dhcp>
  <range start='192.168.122.2' end='192.168.122.254' />
  <host mac='52:54:00:1c:36:cd' name='hvm1' ip='192.168.122.100' />
</dhcp>
```

Then restart the network:

``` bash
$ virsh net-destroy default
$ virsh net-start default
```

The `virsh domifaddr` approach is the cleanest for modern setups, but understanding the ARP method provides a fallback when guest tools aren’t available.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Retrieving VM IP Addresses in KVM with virsh with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Retrieving VM IP Addresses in KVM with virsh. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
