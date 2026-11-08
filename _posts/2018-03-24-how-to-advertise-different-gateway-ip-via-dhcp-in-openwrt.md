---
title: "Configure Custom DHCP Gateway IP in OpenWrt"
date: 2018-03-24 11:48:01 +0000
modified: 2026-04-12 16:31:11 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-advertise-different-gateway-ip-via-dhcp-in-openwrt/
---

When clients connect to your OpenWRT router via DHCP, they typically receive the router itself as the default gateway. Sometimes you need to advertise a different gateway — whether you’re running a proxy, load balancer, or multi-gateway setup on your network. This is done via DHCP option 3 (the router option in the DHCP specification).

## Understanding DHCP Option 3

DHCP option 3 tells clients which IP address to use as their default gateway. By default, OpenWRT advertises its own LAN IP. You can override this to point clients to a different gateway on the network.

The format is simple: `3,<gateway-ip>`. For example, to advertise `192.168.1.2` as the gateway, you’d use:

    3,192.168.1.2

## Method 1: Via UCI Command Line

SSH into your router and use `uci` to add the DHCP option:

``` bash
uci add_list dhcp.lan.dhcp_option="3,192.168.1.2"
uci commit dhcp
/etc/init.d/dnsmasq restart
```

Verify the option was saved:

``` bash
uci get dhcp.lan.dhcp_option
```

If you need to remove or replace the option:

``` bash
uci del dhcp.lan.dhcp_option
uci commit dhcp
/etc/init.d/dnsmasq restart
```

## Method 2: Via LuCI Web Interface

1.  Navigate to **Network** → **Interfaces**
2.  Click **Edit** on the LAN interface
3.  Go to the **DHCP Server** tab
4.  In the **DHCP-Options** field, enter: `3,192.168.1.2`
5.  Click **Save & Apply**

The web interface will validate and apply the change immediately.

## Adding Multiple DHCP Options

If you need to set additional options alongside the gateway, add them on separate lines in LuCI, or use multiple `uci add_list` commands:

``` bash
uci add_list dhcp.lan.dhcp_option="3,192.168.1.2"
uci add_list dhcp.lan.dhcp_option="6,8.8.8.8,8.8.4.4"
uci commit dhcp
/etc/init.d/dnsmasq restart
```

This example sets gateway to `192.168.1.2` and DNS servers to Google’s public DNS.

## Verifying the Configuration

Test that clients receive the correct gateway:

**On a Linux client:**

``` bash
dhclient -v eth0
```

Check the offered options in the output, or inspect `/var/lib/dhcp/dhclient.leases`.

**On Windows:**

``` powershell
ipconfig /release
ipconfig /renew
ipconfig /all
```

Look for “Default Gateway” in the output.

## Important Considerations

- The custom gateway IP must exist and be reachable on your network, otherwise clients will lose connectivity.
- This option only affects new DHCP leases. Existing clients may need to renew their lease (`dhclient -r && dhclient` on Linux, or release/renew on Windows).
- If you’re advertising a different gateway, ensure routing is properly configured on that device to forward traffic appropriately.
- For WAN-facing traffic, verify your routing table and firewall rules accept the traffic from clients.

## Reverting to Default

To restore the default behavior (router advertises itself as gateway), simply remove the custom option:

``` bash
uci del dhcp.lan.dhcp_option
uci commit dhcp
/etc/init.d/dnsmasq restart
```

## 2026 Best Practices and Advanced Techniques

For Configure Custom DHCP Gateway IP in OpenWrt, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling and keep-alive for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for system resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for real-time monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
