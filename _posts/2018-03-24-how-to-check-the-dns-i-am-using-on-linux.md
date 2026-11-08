---
title: "How to Check Your DNS Server on Linux"
date: 2018-03-24 11:44:35 +0000
layout: post
canonical: https://www.systutorials.com/how-to-check-the-dns-i-am-using-on-linux/
---

When you run `cat /etc/resolv.conf` on a modern Linux system, you’ll often see `nameserver 127.0.0.1` or `127.0.1.1` pointing to localhost. This doesn’t mean you’re actually using your ISP’s DNS directly — it usually means your system is running a local DNS stub resolver or caching service like systemd-resolved or dnsmasq. To find out which actual upstream DNS servers you’re using, you need to look elsewhere.

## Using systemd-resolved (Most Common)

Most modern Linux distributions now use **systemd-resolved** instead of traditional resolv.conf. Check your DNS configuration with:

``` bash
resolvectl status
```

This shows your configured DNS servers, search domains, and DNSSEC status. For a specific interface:

``` bash
resolvectl status eth0
```

You can also query DNS resolution statistics:

``` bash
resolvectl statistics
```

## Using NetworkManager

If you’re on a system with NetworkManager (common on Ubuntu, Fedora, and Mint):

``` bash
nmcli device show | grep IP4.DNS
```

This displays the DNS servers for all network interfaces. For a specific connection:

``` bash
nmcli connection show "Your Connection Name" | grep ipv4.dns
```

The older `nm-tool` command is deprecated and no longer available in current versions.

## Reading systemd-resolved Configuration

Check what DNS servers systemd-resolved is actually using:

``` bash
cat /etc/systemd/resolved.conf
```

Look for the `DNS=` and `FallbackDNS=` lines. If they’re commented out, your system uses DHCP-provided DNS servers (set by your network).

## Checking DHCP-Provided DNS

If your system gets DNS from DHCP, inspect what your DHCP client received:

``` bash
grep -i nameserver /var/lib/dhcp/dhclient.eth0.leases | tail -1
```

Replace `eth0` with your interface name. For systemd-networkd:

``` bash
networkctl status eth0
```

## Testing DNS Resolution

Verify which server actually handles your DNS queries:

``` bash
dig @127.0.0.1 example.com +short
```

Or trace the full resolution path:

``` bash
dig example.com +trace
```

For a quick check of all configured resolvers:

``` bash
getent ahosts example.com
```

## Temporary DNS Override

To test a different DNS server without changing your configuration:

``` bash
resolvectl query --server 8.8.8.8 example.com
```

Or with dig:

``` bash
dig @8.8.8.8 example.com
```

## Common DNS Services

- **systemd-resolved**: Default on most modern distributions
- **dnsmasq**: Often used with NetworkManager for caching
- **unbound**: A validating, recursive, and caching DNS resolver
- **bind**: Full-featured DNS server (overkill for most desktops)

Most desktop systems run a local stub resolver that caches queries and forwards unknown records to your ISP’s DNS or a public resolver like Cloudflare (1.1.1.1) or Google (8.8.8.8).

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
