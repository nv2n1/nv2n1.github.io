---
title: "Checking Network Adapter Speed with ethtool in Linux"
date: 2018-03-24 11:47:03 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-find-a-network-adapters-speed-in-linux/
---

When you need to verify the current link speed of a network interface — whether it’s running at 10Mbps, 100Mbps, 1Gbps, or higher — `ethtool` is the standard tool for the job.

## Using ethtool to check interface speed

The basic command is straightforward:

``` bash
ethtool eth0
```

Replace `eth0` with your actual interface name. Here’s sample output:

    Settings for eth0:
        Supported ports: [ TP MII ]
        Supported link modes:   10baseT/Half 10baseT/Full 
                                100baseT/Half 100baseT/Full 
                                1000baseT/Half 1000baseT/Full 
        Supported pause frame use: No
        Supports auto-negotiation: Yes
        Advertised link modes:  10baseT/Half 10baseT/Full 
                                100baseT/Half 100baseT/Full 
                                1000baseT/Half 1000baseT/Full 
        Advertised pause frame use: Symmetric Receive-only
        Advertised auto-negotiation: Yes
        Link partner advertised link modes:  10baseT/Half 10baseT/Full 
                                             100baseT/Half 100baseT/Full 
                                             1000baseT/Full 
        Link partner advertised pause frame use: No
        Link partner advertised auto-negotiation: Yes
        Speed: 1000Mb/s
        Duplex: Full
        Port: MII
        PHYAD: 0
        Transceiver: internal
        Auto-negotiation: on
        Supports Wake-on: pumbg
        Wake-on: g
        Current message level: 0x00000033 (51)
                       drv probe ifdown ifup
        Link detected: yes

The key lines are **Speed** and **Duplex**. In this example, the interface is connected at 1000Mb/s (1Gbps) in full duplex mode.

## Quick speed check only

If you only want the speed without all the extra details, use:

``` bash
ethtool eth0 | grep Speed
```

Output:

    Speed: 1000Mb/s

## Check all interfaces at once

To see the speed of all active interfaces:

``` bash
for iface in $(ip link show | grep -E '^[0-9]+:' | awk '{print $2}' | tr -d ':'); do
    echo "=== $iface ==="
    ethtool "$iface" 2>/dev/null | grep -E 'Speed|Duplex|Link detected'
done
```

## Understanding the output

- **Speed**: The negotiated link speed (1000Mb/s = 1Gbps)
- **Duplex**: Full duplex is standard; half duplex is rare and usually indicates a problem
- **Link detected**: yes/no — whether the cable is connected
- **Auto-negotiation**: Whether speed was automatically negotiated with the switch
- **Supported link modes**: The speeds this adapter *can* run at

## Important: Link speed vs actual throughput

The speed shown by `ethtool` is the **hardware link speed** — the negotiated connection between your NIC and the switch. This is not the same as actual throughput. You’ll see lower real-world speeds due to:

- Protocol overhead (TCP/IP headers, Ethernet frames)
- Network congestion
- Duplex mismatch (if one side is set to half duplex)
- Cable quality or distance issues

To measure actual throughput, use tools like `iperf3`:

``` bash
# On receiver
iperf3 -s

# On sender
iperf3 -c <receiver_ip>
```

## Troubleshooting slow speeds

If your interface is negotiating at 100Mbps or 10Mbps when it should be faster:

1.  Check if autonegotiation is enabled: `ethtool eth0 | grep Auto-negotiation`

2.  Force a specific speed (use with caution):

    ``` bash
    sudo ethtool -s eth0 speed 1000 duplex full autoneg on
    ```

3.  Restart the interface:

    ``` bash
    sudo ip link set eth0 down
    sudo ip link set eth0 up
    ```

4.  Verify the cable and switch port — bad cables or faulty switch ports are common causes

Make permanent speed settings in `/etc/network/interfaces` (Debian/Ubuntu) or NetworkManager configuration files rather than using command-line flags, which don’t persist across reboots.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Checking Network Adapter Speed with ethtool in Linux with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Checking Network Adapter Speed with ethtool in Linux. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
