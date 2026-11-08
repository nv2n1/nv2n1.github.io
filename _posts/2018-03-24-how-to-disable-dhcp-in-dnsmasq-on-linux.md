---
title: "Disabling DHCP in dnsmasq on Linux"
date: 2018-03-24 11:52:39 +0000
layout: post
canonical: https://www.systutorials.com/how-to-disable-dhcp-in-dnsmasq-on-linux/
---

If you’re running dnsmasq primarily for DNS resolution and don’t need its DHCP server capabilities, you’ll want to disable DHCP while keeping DNS functional. This is a common configuration for DNS-only setups or when another service handles DHCP.

## Default dnsmasq behavior

By default, dnsmasq ships with DHCP disabled. However, many distributions include preconfigured DHCP settings in `/etc/dnsmasq.conf` or supplementary config files in `/etc/dnsmasq.d/`. You need to identify and disable any DHCP-related directives.

## Disabling DHCP

The simplest approach is to comment out or remove all lines beginning with `dhcp-` in your configuration files:

``` bash
# View current DHCP configuration
grep -n "^dhcp-" /etc/dnsmasq.conf
```

Common DHCP directives you might encounter include:

- `dhcp-range` — defines the IP range for DHCP leases
- `dhcp-host` — static DHCP assignments
- `dhcp-option` — DHCP options (gateway, DNS, etc.)
- `dhcp-lease-max` — maximum concurrent leases
- `dhcp-leasefile` — location of the lease database

Edit `/etc/dnsmasq.conf` and comment out these lines with `#`:

``` bash
# Disable these DHCP directives
# dhcp-range=192.168.1.100,192.168.1.200,12h
# dhcp-option=option:router,192.168.1.1
# dhcp-leasefile=/var/lib/dnsmasq/dnsmasq.leases
```

Check `/etc/dnsmasq.d/` for additional config files that might define DHCP behavior:

``` bash
ls -la /etc/dnsmasq.d/
grep -r "^dhcp-" /etc/dnsmasq.d/
```

Some distributions place DHCP config in separate files like `/etc/dnsmasq.d/dhcp.conf`. Comment out or delete these as needed.

## Verify DNS-only configuration

Ensure your config retains DNS settings:

``` bash
# Check for DNS configuration
grep -E "^(listen-address|port|server=)" /etc/dnsmasq.conf
```

A minimal DNS-only setup might look like:

``` conf
# Listen only on localhost or specific interfaces
listen-address=127.0.0.1,::1
# Or for network-wide DNS:
listen-address=192.168.1.50

# DNS port (default 53)
port=53

# Disable DHCP entirely
no-dhcp-interface=

# Forward queries to upstream resolvers
server=8.8.8.8
server=8.8.4.4
```

## Restart and verify

After making changes, restart dnsmasq:

``` bash
sudo systemctl restart dnsmasq
```

Verify the service is running with DNS only:

``` bash
# Check dnsmasq is listening on port 53
sudo ss -tlnp | grep dnsmasq

# Test DNS resolution
dig @localhost example.com
nslookup example.com 127.0.0.1
```

Confirm DHCP is not listening on UDP port 67:

``` bash
sudo ss -tlnp | grep 67
# Should return no results
```

Check the systemd journal for any startup errors:

``` bash
sudo journalctl -u dnsmasq -n 20
```

## Configuration best practices

- Keep DHCP-related lines in a separate file (e.g., `/etc/dnsmasq.d/dhcp.conf`) and disable it entirely by renaming to `.bak` rather than scattering disables across multiple files
- Use the `no-dhcp-interface=*` directive as an explicit “disable all DHCP” statement if you want belt-and-suspenders redundancy
- Test DNS resolution from other machines on your network if dnsmasq is serving as a network-wide resolver
- Document your configuration — comment why you disabled DHCP and what service provides it instead (if applicable)

## 2026 Best Practices and Advanced Techniques

For Disabling DHCP in dnsmasq on Linux, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
