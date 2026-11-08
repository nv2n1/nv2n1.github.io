---
title: "Clearing DNS Cache on Linux and Windows"
date: 2013-07-12 16:31:51 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/flush-dns-cache-of-linux-and-windows-client/
---

DNS caching helps reduce lookups but sometimes you need to clear it after DNS changes, certificate updates, or to troubleshoot resolution issues.

### Modern Linux with systemd-resolved

Most contemporary Linux distributions use `systemd-resolved` as the default DNS resolver. Flush the cache with:

``` bash
sudo systemctl restart systemd-resolved
```

Or use the `resolvectl` command:

``` bash
sudo resolvectl flush-caches
```

To verify the cache was cleared:

``` bash
resolvectl statistics
```

### Linux with NetworkManager

If your system uses NetworkManager alongside systemd-resolved:

``` bash
sudo systemctl restart NetworkManager
```

This restarts the DNS integration but doesn’t always flush all caches. For thorough clearing, combine it with:

``` bash
sudo systemctl restart systemd-resolved
```

### Legacy: nscd (Name Service Cache Daemon)

Older distributions or systems still running `nscd`:

``` bash
sudo systemctl restart nscd
```

Or via init scripts on systems without systemd:

``` bash
sudo service nscd restart
```

Check if nscd is running:

``` bash
systemctl status nscd
```

### Checking Current DNS Configuration

View your active DNS resolver:

``` bash
resolvectl status
```

On systems using `/etc/resolv.conf`:

``` bash
cat /etc/resolv.conf
```

Note that on modern systems, `/etc/resolv.conf` is often a symlink to `/run/systemd/resolve/resolv.conf` and is managed automatically.

## Flushing DNS Cache on Windows

### Windows 10/11 (and Server 2016+)

Open PowerShell or Command Prompt as Administrator and run:

``` cmd
ipconfig /flushdns
```

Verify the flush succeeded:

``` cmd
ipconfig /displaydns
```

To clear DNS cache using PowerShell:

``` powershell
Clear-DnsClientCache
```

View current cached entries:

``` powershell
Get-DnsClientCache
```

### Clearing Windows DNS via Group Policy

For domain-joined systems, you can also flush DNS on remote machines:

``` powershell
Invoke-Command -ComputerName <hostname> -ScriptBlock { Clear-DnsClientCache }
```

### Older Windows (XP through Windows 7)

While no longer supported, the command remains:

``` cmd
ipconfig /flushdns
```

Run this from an Administrator command prompt.

## Browser-Level DNS Cache

Browsers maintain their own DNS caches separate from the OS. This is useful during development or when troubleshooting specific services.

### Chrome/Chromium

Navigate to:

    chrome://net-internals/#dns

Click “Clear host cache” to flush Chrome’s DNS cache. You can also view recent DNS queries on this page.

### Firefox

Firefox doesn’t expose a direct DNS cache flush in the UI. Instead, restart the browser or access `about:networking#dns` to view DNS information. For debugging, use:

``` bash
about:config
```

Search for `network.dnsCacheExpiration` and reduce the value (in seconds) to force faster cache expiration.

### Edge

Navigate to:

    edge://net-internals/#dns

Same functionality as Chrome since Edge uses Chromium.

## Troubleshooting DNS Issues

After flushing caches, verify DNS resolution:

``` bash
# Test DNS resolution
nslookup example.com
dig example.com
getent hosts example.com
```

On Windows:

``` cmd
nslookup example.com
```

If issues persist after flushing, check that your DNS servers are correctly configured:

``` bash
resolvectl query example.com
```

This shows which resolver handled the request and helps identify configuration problems.

## 2026 Best Practices and Advanced Techniques

For Clearing DNS Cache on Linux and Windows, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
