---
title: "Backing Up Emails from IMAP and POP3 Servers"
date: 2018-03-24 11:42:59 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-back-up-emails-from-the-email-server/
---

If you’re syncing emails with tools like offlineimap, you might notice a problem: when an email is deleted from the server, it’s also deleted locally. That’s by design—offlineimap performs *synchronization*, not backup.

For actual backups, you need a tool that retrieves emails without deleting the originals. This post covers the best approaches in 2026.

## getmail: The Modern Choice

`getmail` is the simplest and most reliable option for email backup. Unlike offlineimap, it retrieves messages without synchronizing deletions back to the server.

### Basic getmail Setup

Install getmail:

``` bash
sudo apt install getmail6  # Debian/Ubuntu
sudo dnf install getmail   # Fedora/RHEL
```

Create a config file at `~/.getmail/getmailrc`:

``` ini
[retriever]
type = IMAP4SSL
server = imap.gmail.com
username = your-email@gmail.com
password = your-app-password
port = 993

[destination]
type = Maildir
path = ~/Maildir/

[options]
verbose = 2
read_all = false
```

For POP3:

``` ini
[retriever]
type = POP3SSL
server = pop.gmail.com
username = your-email@gmail.com
password = your-app-password
port = 995
```

Run the backup:

``` bash
getmail --getmaildir ~/.getmail
```

Schedule it with cron for regular backups:

``` bash
0 2 * * * /usr/bin/getmail --getmaildir ~/.getmail >> ~/.getmail/backup.log 2>&1
```

### Why getmail Over Alternatives

- **fetchmail + procmail**: Older combination that works but requires more configuration
- **mbsync**: Good for sync, not ideal for one-way backups
- **imapbackup**: Limited to Gmail
- **getmail**: Straightforward, actively maintained, supports IMAP4 and POP3

## Gmail-Specific Considerations

Gmail requires an app-specific password if you use two-factor authentication. Generate one in your Google Account settings under Security.

For large Gmail accounts, be aware of IMAP rate limits. Use `read_all = false` to only fetch unread messages on first run, then remove the option for subsequent runs.

## Mbox Format Alternative

If you prefer mbox format instead of Maildir:

``` ini
[destination]
type = Mboxrd
path = ~/mail-backup.mbox
```

Mbox is a single-file format that’s easier to archive but slower for large mailboxes.

## Verifying Your Backup

Check what getmail retrieved:

``` bash
find ~/Maildir -type f -name "cur" -o -name "new" | xargs wc -l
```

Or count messages:

``` bash
find ~/Maildir -type f | wc -l
```

For mbox format:

``` bash
grep "^From " ~/mail-backup.mbox | wc -l
```

## Handling Multiple Accounts

Create separate config files for each account:

``` bash
~/.getmail/gmail.rc
~/.getmail/work.rc
~/.getmail/personal.rc
```

Run all at once:

``` bash
getmail --getmaildir ~/.getmail --rcfile gmail.rc --rcfile work.rc
```

Or in your cron job:

``` bash
0 2 * * * getmail --getmaildir ~/.getmail --all-folders
```

## Incremental Backups

getmail tracks which emails it’s already fetched, so running it multiple times won’t duplicate messages. This makes it ideal for regular incremental backups.

``` bash
# First run: fetches everything
getmail --getmaildir ~/.getmail

# Second run: fetches only new messages since last run
getmail --getmaildir ~/.getmail
```

## Troubleshooting Connection Issues

If getmail fails to connect:

``` bash
# Test IMAP connectivity
openssl s_client -connect imap.gmail.com:993

# Test POP3 connectivity
openssl s_client -connect pop.gmail.com:995
```

Check your firewall isn’t blocking port 993 (IMAP) or 995 (POP3).

For persistent issues, enable verbose logging:

``` ini
[options]
verbose = 3
```

getmail gives you reliable, one-way email backup without the complexity of sync tools or the limitations of old fetchmail setups.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Backing Up Emails from IMAP and POP3 Servers with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

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

This comprehensive guide provides extended knowledge for Backing Up Emails from IMAP and POP3 Servers. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
