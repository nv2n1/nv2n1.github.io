---
title: "Linux Server Boot Notifications via Email"
date: 2018-03-24 11:45:36 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-email-admins-automatically-after-a-linux-server-starts/
---

Managing a cluster of servers, you’ll want to be notified when they come back online after restarts or unexpected reboots. Email notifications on boot let you track infrastructure changes and catch potential issues early.

## Using crontab @reboot

The simplest approach is a crontab `@reboot` entry that runs once at startup. This executes before most services fully initialize, making it reliable for boot detection.

Add this to your crontab on each server:

``` bash
@reboot /usr/local/bin/send-boot-notification.sh
```

Create the script at `/usr/local/bin/send-boot-notification.sh`:

``` bash
#!/bin/bash

HOSTNAME=$(hostname)
TIMESTAMP=$(date)
TO_ADDR="admins@example.com"
FROM_ADDR="monitoring@example.com"
SMTP_SERVER="smtp.example.com"

{
    echo "Server: $HOSTNAME"
    echo "Boot Time: $TIMESTAMP"
    echo "Uptime: $(uptime)"
    echo "IP Addresses:"
    ip addr show | grep "inet " | awk '{print $2}'
} | mail -s "[$HOSTNAME] Server started" -r "$FROM_ADDR" "$TO_ADDR"
```

Make it executable:

``` bash
chmod +x /usr/local/bin/send-boot-notification.sh
```

Edit your crontab:

``` bash
crontab -e
```

Add the line:

    @reboot /usr/local/bin/send-boot-notification.sh

## Using systemd (Recommended)

Modern distributions should use systemd instead of cron. Create a service file at `/etc/systemd/system/boot-notification.service`:

``` ini
[Unit]
Description=Send boot notification email
After=network-online.target
Wants=network-online.target

[Service]
Type=oneshot
User=root
ExecStart=/usr/local/bin/send-boot-notification.sh
RemainAfterExit=yes

[Install]
WantedBy=multi-user.target
```

Enable and test it:

``` bash
sudo systemctl daemon-reload
sudo systemctl enable boot-notification.service
```

The `After=network-online.target` ensures the network is ready before sending email, avoiding failures on boot.

## Email Configuration

Use the standard `mail` command (from mailutils or postfix):

``` bash
echo "Server booted" | mail -s "Subject" admin@example.com
```

If your server needs to relay through an external SMTP server, configure `/etc/ssmtp/ssmtp.conf`:

    root=monitoring@example.com
    mailhub=smtp.example.com:587
    AuthUser=smtp_user
    AuthPass=smtp_password
    UseSTARTTLS=YES

Then use `ssmtp` instead:

``` bash
echo "Server booted" | ssmtp admin@example.com
```

For Gmail or other providers requiring authentication, `ssmtp` is simpler than `mailx`.

## Practical Example: Boot Notification with System Info

Here’s a more detailed script that includes useful diagnostics:

``` bash
#!/bin/bash

HOSTNAME=$(hostname -f)
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S %Z')
BOOT_TIME=$(date -d "$(uptime -s)" '+%Y-%m-%d %H:%M:%S')
KERNEL=$(uname -r)
TO_ADDR="ops-team@example.com"

{
    echo "Hostname: $HOSTNAME"
    echo "Boot Time: $BOOT_TIME"
    echo "Notification Time: $TIMESTAMP"
    echo "Kernel: $KERNEL"
    echo "Uptime: $(uptime | sed 's/^.*up //')"
    echo ""
    echo "Network Interfaces:"
    ip -br addr show
    echo ""
    echo "Disk Usage:"
    df -h | grep -v "^Filesystem"
} | mail -s "[$HOSTNAME] System booted" "$TO_ADDR"
```

## Troubleshooting

If emails aren’t sending:

- Check that `postfix` or `ssmtp` is running: `systemctl status postfix`
- Verify mail logs: `tail -f /var/log/mail.log`
- Test email manually: `echo "test" | mail -s "test" admin@example.com`
- Ensure DNS can resolve your SMTP server: `host smtp.example.com`
- For systemd services, check the journal: `journalctl -u boot-notification.service -n 20`

## Multiple Recipients

To email multiple admins, use a distribution list or add multiple `-r` flags:

``` bash
mail -s "Subject" admin1@example.com admin2@example.com < message.txt
```

Or write addresses to a file and use:

``` bash
mail -s "Subject" $(cat /etc/boot-notify-recipients.txt) < message.txt
```

The systemd approach is preferred on modern distributions because it handles dependencies, logging, and can be easily monitored with standard tools like `journalctl`.

## 2026 Best Practices and Advanced Techniques

For Linux Server Boot Notifications via Email, understanding both fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

## Troubleshooting and Debugging

When issues arise, a systematic approach saves time. Start by checking logs for error messages or warnings. Test individual components in isolation before integrating them. Use verbose modes and debug flags to gather more information when standard output is not enough to diagnose the problem.

## Performance Optimization

- Monitor system resources to identify bottlenecks
- Use caching strategies to reduce redundant computation
- Keep software updated for security patches and performance improvements
- Profile code before applying optimizations
- Use connection pooling for network operations

## Security Considerations

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data in transit, and follow the principle of least privilege for access controls. Regular security audits and penetration testing help maintain system integrity.

## Related Tools and Commands

These complementary tools expand your capabilities:

- Monitoring: top, htop, iotop, vmstat for resources
- Networking: ping, traceroute, ss, tcpdump for connectivity
- Files: find, locate, fd for searching; rsync for syncing
- Logs: journalctl, dmesg, tail -f for monitoring
- Testing: curl for HTTP requests, nc for ports, openssl for crypto

## Integration with Modern Workflows

Consider automation and containerization for consistency across environments. Infrastructure as code tools enable reproducible deployments. CI/CD pipelines automate testing and deployment, reducing human error and speeding up delivery cycles.

## Quick Reference

This extended guide covers the topic beyond the original article scope. For specialized needs, refer to official documentation or community resources. Practice in test environments before production deployment.
