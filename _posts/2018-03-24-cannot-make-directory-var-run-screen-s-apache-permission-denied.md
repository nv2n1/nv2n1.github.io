---
title: "How to Fix `/var/run/screen/S-apache` Permission Denied Error"
date: 2018-03-24 11:54:03 +0000
layout: post
canonical: https://www.systutorials.com/cannot-make-directory-var-run-screen-s-apache-permission-denied/
---

The error “Cannot make directory ‘/var/run/screen/S-apache’: Permission denied” typically means the screen session directory can’t be created under `/var/run/screen/`. This happens when screen lacks proper permissions or when security policies block the operation.

## Verify screen installation and permissions

First, confirm screen is installed with correct permissions:

``` bash
$ ls -la $(which screen)
-rwxr-sr-x 1 root screen 474288 Aug 28 18:59 /usr/bin/screen
```

The key detail is the `s` in the group permission field (the fourth position) — this setgid bit allows screen to create directories owned by the `screen` group.

Check the `/var/run/screen` directory:

``` bash
$ ls -la /var/run/ | grep screen
drwxrwxr-x 3 root screen 60 Aug 28 18:59 screen
```

It should be owned by `root:screen` with `775` permissions. If permissions are wrong, fix them:

``` bash
$ sudo chmod 775 /var/run/screen
$ sudo chgrp screen /var/run/screen
```

If screen isn’t installed or permissions are mangled, reinstall it:

``` bash
# CentOS/RHEL
$ sudo yum reinstall screen

# Debian/Ubuntu
$ sudo apt reinstall screen
```

## Check SELinux policies

On CentOS 7 and RHEL systems, SELinux often blocks screen operations. Check the audit log after attempting to use screen as the apache user:

``` bash
$ sudo tail -f /var/log/audit/audit.log | grep -i screen
```

Look for denial messages. If you see SELinux blocks, check the specific denial:

``` bash
$ sudo ausearch -m avc -ts recent | grep screen
```

Generate a policy module to allow the operation:

``` bash
$ sudo ausearch -m avc -ts recent | audit2allow -a -M screen_fix
$ sudo semodule -i screen_fix.pp
```

For a quicker workaround, set the context on the screen directory:

``` bash
$ sudo chcon -R -t user_devpts_t /var/run/screen
```

## Verify the fix

Test that the non-root user can now create screen sessions:

``` bash
$ sudo -u apache screen -S test -d
$ sudo -u apache screen -list
There is a screen on:
    test    (Detached)
1 Socket in /var/run/screen/S-apache.

# Clean up
$ sudo -u apache screen -S test -X quit
```

## Additional considerations

If you’re running apache under a different user (not the default `apache`), replace it with the actual username. The group permission issue is the most common cause — screen relies on the `screen` group to manage the runtime directory, and without proper setgid permissions, unprivileged users can’t create their session directories.

On modern systems with systemd, `/var/run` is mounted as a tmpfs that gets recreated on boot. If permissions reset after reboot, create a tmpfiles.d configuration:

``` bash
$ sudo tee /etc/tmpfiles.d/screen.conf > /dev/null << EOF
d /var/run/screen 0775 root screen -
EOF
```

This ensures permissions persist across reboots.

## 2026 Best Practices and Advanced Techniques

For How to Fix \`/var/run/screen/S-apache\` Permission Denied Error, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
