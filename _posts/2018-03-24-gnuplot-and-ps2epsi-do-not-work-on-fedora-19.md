---
title: "Troubleshooting gnuplot and ps2epsi on Fedora 19"
date: 2018-03-24 08:17:17 +0000
layout: post
canonical: https://www.systutorials.com/gnuplot-and-ps2epsi-do-not-work-on-fedora-19/
---

If gnuplot or ps2epsi fails to run or produces excessive warnings on modern Fedora systems, you’re likely hitting a fontconfig deprecation issue. The symptom is repeated warnings like:

    Fontconfig warning: "/etc/fonts/conf.d/50-user.conf", line 14: reading configurations from ~/.fonts.conf is deprecated.

This happens because `/etc/fonts/conf.d/50-user.conf` still includes a deprecated reference to `~/.fonts.conf`. While the warning alone doesn’t break functionality in all cases, it can cause gnuplot to hang, fail silently, or produce corrupted output—especially when generating PostScript or EPS files.

## The Fix

The simplest solution is to remove the deprecated include directive from the fontconfig configuration:

``` bash
sudo nano /etc/fonts/conf.d/50-user.conf
```

Find this line:

``` xml
<include ignore_missing="yes" deprecated="yes">~/.fonts.conf</include>
```

Comment it out or delete it entirely:

``` xml
<!-- <include ignore_missing="yes" deprecated="yes">~/.fonts.conf</include> -->
```

Save the file (Ctrl+X, then Y in nano) and test your gnuplot command:

``` bash
gnuplot
```

The warnings should disappear and gnuplot should function normally.

## Why This Happens

Fontconfig deprecated the `~/.fonts.conf` user configuration file in favor of `~/.config/fontconfig/fonts.conf`. The old include statement remains in the default Fedora fontconfig for backward compatibility, but modern versions of fontconfig (2.13+) emit warnings when processing it. These warnings can interfere with tools that parse gnuplot’s output or expect clean stdout/stderr.

## Preventing This on Fresh Installs

If you’re setting up a new Fedora system, you can avoid this issue entirely by creating a proper modern fontconfig setup:

``` bash
mkdir -p ~/.config/fontconfig
touch ~/.config/fontconfig/fonts.conf
```

Then add your custom font settings to `~/.config/fontconfig/fonts.conf` instead of `~/.fonts.conf`. Fedora’s default configuration will skip the deprecated file if it doesn’t exist.

## Related Issues

If you’re using ps2epsi specifically and still encounter problems after fixing fontconfig, verify that Ghostscript is installed and up-to-date:

``` bash
dnf install ghostscript
```

For gnuplot, ensure you have the full gnuplot package with terminal support:

``` bash
dnf install gnuplot gnuplot-common
```

Test PostScript output generation directly:

``` bash
echo "plot sin(x)" | gnuplot -e "set terminal postscript; set output 'test.ps'"
```

If the PostScript file generates without warnings and contains valid content, your fontconfig issue is resolved.

## Related Linux Commands

These related commands are often used alongside the tools discussed in this article:

- man command-name – Read the manual page for any command
- which command-name – Find the location of an executable
- rpm -qa or dpkg -l – List installed packages
- journalctl -u service-name – Check service logs
- ss -tulpn – List listening ports and services

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## 2026 Best Practices and Advanced Techniques

For Troubleshooting gnuplot and ps2epsi on Fedora 19, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
