---
title: "Sending Email from Linux with mailx via Internal SMTP"
date: 2013-10-28 05:30:00 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/sending-email-using-mailx-in-linux-through-internal-smtp/
---

mailx (heirloom-mailx) and s-nail are lightweight CLI tools for sending email from scripts, cron jobs, and system alerts. They’re especially useful in corporate or campus networks with internal SMTP servers that don’t require authentication.

## Installation

**Debian/Ubuntu:**

``` bash
apt install heirloom-mailx
```

**RHEL/CentOS/Fedora:**

``` bash
dnf install mailx
```

**Alpine:**

``` bash
apk add mailx
```

**Arch:**

``` bash
pacman -S s-nail
```

s-nail is a modern POSIX-compliant fork of mailx with better MIME support and is preferred on newer systems, though the command syntax remains compatible with the examples here.

## Basic Usage: Single Command

Send email without any configuration file:

``` bash
echo "Email body content" | mailx -v -s "Subject Line" \
  -S smtp=smtp.example.com \
  -S from="sender@example.com(Sender Name)" \
  recipient@example.com
```

Replace `smtp.example.com` with your SMTP server, `sender@example.com` with your sending address, and `recipient@example.com` with the destination.

The `-v` flag enables verbose output for debugging connection issues.

Send to multiple recipients:

``` bash
echo "Content" | mailx -v -s "Subject" \
  -S smtp=smtp.example.com \
  -S from="sender@example.com(Name)" \
  user1@example.com user2@example.com user3@example.com
```

## Configuration File Setup

For repeated use, add settings to `~/.mailrc`:

    set smtp=smtp://smtp.example.com
    set from="sender@example.com(Your Name)"
    set sendcharsets=utf-8

Then send email more simply:

``` bash
echo "Message body" | mailx -s "Subject" recipient@example.com
```

Restrict permissions to prevent credential exposure:

``` bash
chmod 600 ~/.mailrc
```

## Reading Email Body from Files

Send file content as the email body:

``` bash
mailx -v -s "Backup Report" admin@example.com < /path/to/report.txt
```

Pipe file contents directly:

``` bash
cat /var/log/app.log | mailx -v -s "Log Report" logs@example.com
```

Send output from a command:

``` bash
df -h | mailx -v -s "Disk Report" admin@example.com
```

## Adding Attachments

Include attachments with the `-a` flag:

``` bash
echo "Report attached" | mailx -v -s "Monthly Report" \
  -S smtp=smtp.example.com \
  -S from="sender@example.com(Name)" \
  -a /path/to/report.pdf \
  recipient@example.com
```

Multiple attachments require multiple `-a` flags:

``` bash
echo "Files attached" | mailx -v -s "Backup" \
  -S smtp=smtp.example.com \
  -S from="sender@example.com(Name)" \
  -a /path/to/file1.zip \
  -a /path/to/file2.txt \
  -a /path/to/file3.log \
  recipient@example.com
```

## SMTP Authentication

For servers requiring credentials, add authentication settings to `~/.mailrc`:

    set smtp=smtp://smtp.example.com
    set smtp-use-starttls
    set smtp-auth=login
    set smtp-auth-user=username@example.com
    set smtp-auth-password=your-password
    set from="username@example.com(Display Name)"

Or on the command line:

``` bash
echo "Content" | mailx -v -s "Subject" \
  -S smtp=smtp.example.com \
  -S smtp-use-starttls \
  -S smtp-auth=login \
  -S smtp-auth-user=username@example.com \
  -S smtp-auth-password=your-password \
  -S from="username@example.com(Name)" \
  recipient@example.com
```

**Security note:** Storing plaintext passwords in config files is risky. Use environment variables or a credential file with 600 permissions as a minimum, or consider using a local mail relay service like postfix with null authentication instead.

For OAuth2 or other modern auth methods, use `-S smtp-auth=xoauth2` with appropriate token setup, though local SMTP relays are simpler for most sysadmin use cases.

## Port Selection

- **Port 25:** Standard SMTP, no encryption (legacy, often blocked outbound)
- **Port 587:** SMTP with STARTTLS (recommended for authenticated relays)
- **Port 465:** SMTPS (SSL from connection start, less common but supported)

Specify port with the smtp setting:

``` bash
-S smtp=smtp://smtp.example.com:587
```

Enable STARTTLS for port 587:

``` bash
-S smtp-use-starttls
```

## Troubleshooting

Run with `-v` to see detailed connection logs:

``` bash
echo "Test" | mailx -v -s "Test" \
  -S smtp=smtp.example.com \
  recipient@example.com
```

**Connection refused:** Verify the SMTP server hostname and port. Check firewall rules allow outbound SMTP. Test connectivity with:

``` bash
nc -zv smtp.example.com 25
telnet smtp.example.com 587
```

**Authentication failed:** Verify credentials and authentication method (login, plain, cram-md5). Check if the SMTP server expects STARTTLS before authentication.

**Timeout:** Ensure network connectivity. Check if firewalls or ISPs block outbound port 25 (common). Try port 587 or 465 instead.

**Message not sending:** Review verbose output for SMTP error codes. Verify the `from` address is acceptable to the SMTP server.

## Practical Examples

**Daily log digest via cron:**

``` bash
0 2 * * * echo "Daily logs attached" | mailx -v -s "Daily Report $(date +\%Y-\%m-\%d)" \
  -S smtp=smtp.example.com \
  -S from="monitoring@example.com(System)" \
  -a /var/log/app.log \
  admin@example.com
```

**Disk usage alert:**

``` bash
#!/bin/bash
DISK_USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$DISK_USAGE" -gt 80 ]; then
  echo "Disk usage at $DISK_USAGE% on $(hostname)" | mailx -v \
    -s "ALERT: High Disk Usage" \
    -S smtp=smtp.example.com \
    -S from="alerts@example.com(System)" \
    admin@example.com
fi
```

**Backup completion notification:**

``` bash
#!/bin/bash
BACKUP_FILE="backup-$(date +%Y%m%d).tar.gz"
tar -czf "$BACKUP_FILE" /important/data && {
  echo "Backup completed successfully at $(date)" | mailx -v \
    -s "Backup Complete: $BACKUP_FILE" \
    -S smtp=smtp.example.com \
    -S from="backup@example.com(Backup System)" \
    -a "$BACKUP_FILE" \
    backups@example.com
}
```

**Database backup with compression notification:**

``` bash
#!/bin/bash
DUMP_FILE="db-backup-$(date +%Y%m%d-%H%M%S).sql.gz"
mysqldump -u user -p database | gzip > "$DUMP_FILE"
SIZE=$(du -h "$DUMP_FILE" | awk '{print $1}')
echo "Database backup completed. File size: $SIZE" | mailx -v \
  -s "DB Backup: $DUMP_FILE" \
  -S smtp=smtp.example.com \
  -S from="dba@example.com(Database)" \
  -a "$DUMP_FILE" \
  dba@example.com
```

## Integration with Monitoring Tools

Use mailx in custom monitoring scripts or cron jobs. For Nagios/Icinga or other monitoring systems, wrap it in a notification script:

``` bash
#!/bin/bash
# notification_wrapper.sh
RECIPIENT="$1"
SUBJECT="$2"
MESSAGE="$3"
SMTP_SERVER="smtp.example.com"

echo "$MESSAGE" | mailx -v -s "$SUBJECT" \
  -S smtp="$SMTP_SERVER" \
  -S from="monitoring@example.com(Alerts)" \
  "$RECIPIENT"
```

Call from monitoring alerts or as a custom notification handler.
