---
title: "Sending Gmail Emails via mailx on Linux"
date: 2013-07-12 16:31:59 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /sending-email-from-mailx-command-in-linux-using-gmails-smtp/
---

The mailx (or s-nail on modern distributions) command remains useful for scripted email delivery, particularly when you need to send alerts or notifications automatically. Gmail’s SMTP service works well for this, though it requires TLS authentication and specific configuration.

## Prerequisites

Most Linux distributions include mailx or s-nail by default. On systems using s-nail (Ubuntu 20.04+, Debian 11+, Fedora), the commands below work identically — just replace `mailx` with `s-nail`. You’ll also need either a Gmail account or, better, an App Password if you have 2-Step Verification enabled.

### Setting up an App Password

If you use Google’s 2-Step Verification, you must generate an App Password rather than using your account password. This is more secure and can be revoked independently:

1.  Go to <a href="https://myaccount.google.com/apppasswords" rel="nofollow noopener" target="_blank">https://myaccount.google.com/apppasswords</a>
2.  Select “Mail” and “Linux”
3.  Google generates a 16-character password — use this instead of your Gmail password
4.  If you don’t use 2-Step Verification, you can use your Gmail password directly, though App Passwords are still recommended

## Quick Command-Line Method

Send email directly without configuration files:

``` bash
echo "Email body goes here" | mailx -v \
  -s "Subject Line" \
  -S smtp=smtp://smtp.gmail.com:587 \
  -S smtp-use-starttls \
  -S ssl-verify=ignore \
  -S smtp-auth=login \
  -S smtp-auth-user=your-email@gmail.com \
  -S smtp-auth-password="your-app-password" \
  -S from="Your Name <your-email@gmail.com>" \
  recipient@example.com
```

For interactive input (paste or type content, then press Ctrl+D):

``` bash
mailx -v \
  -s "Subject Line" \
  -S smtp=smtp://smtp.gmail.com:587 \
  -S smtp-use-starttls \
  -S ssl-verify=ignore \
  -S smtp-auth=login \
  -S smtp-auth-user=your-email@gmail.com \
  -S smtp-auth-password="your-app-password" \
  -S from="Your Name <your-email@gmail.com>" \
  recipient@example.com
```

**Caution:** Command-line passwords are visible to other users via `ps` output. Prefer interactive input or use the configuration file method below.

## Configuration File Method (Recommended)

Create `~/.mailrc`:

    set smtp=smtp://smtp.gmail.com:587
    set smtp-use-starttls
    set ssl-verify=ignore
    set smtp-auth=login
    set smtp-auth-user=your-email@gmail.com
    set smtp-auth-password="your-app-password"
    set from="Your Name <your-email@gmail.com>"

Restrict file permissions immediately:

``` bash
chmod 600 ~/.mailrc
```

Now send email with a simpler command:

``` bash
echo "Email body" | mailx -v -s "Subject Line" recipient@example.com
```

Or interactively:

``` bash
mailx -v -s "Subject Line" recipient@example.com
# Type your message, then press Ctrl+D
```

## Certificate/CA Bundle Issues

If you encounter certificate verification errors despite `-S ssl-verify=ignore`, your system’s CA bundle might be outdated. Most modern distributions (Ubuntu 20.04+, Debian 11+, Fedora 36+) have current CA certificates.

If you still experience issues, you can specify an alternative CA bundle:

``` bash
-S ssl-ca-file=/etc/ssl/certs/ca-certificates.crt
```

On older systems, you can use Firefox’s certificate store if available:

``` bash
-S nss-config-dir=~/.mozilla/firefox/xxxxxxxx.default
```

Find your Firefox profile directory by listing `~/.mozilla/firefox/`.

## Practical Examples

Send a simple system alert:

``` bash
#!/bin/bash
HOSTNAME=$(hostname)
LOAD=$(uptime)
echo "System: $HOSTNAME
Load: $LOAD" | mailx -v \
  -s "System Status Alert" \
  -S smtp=smtp://smtp.gmail.com:587 \
  -S smtp-use-starttls \
  -S ssl-verify=ignore \
  -S smtp-auth=login \
  -S smtp-auth-user=alerts@gmail.com \
  -S smtp-auth-password="app-password" \
  -S from="Monitoring <alerts@gmail.com>" \
  admin@example.com
```

Send with file attachment (s-nail/mailx extension):

``` bash
mailx -v \
  -s "Backup Report" \
  -a /path/to/backup.log \
  -S smtp=smtp://smtp.gmail.com:587 \
  -S smtp-use-starttls \
  -S ssl-verify=ignore \
  -S smtp-auth=login \
  -S smtp-auth-user=alerts@gmail.com \
  -S smtp-auth-password="app-password" \
  -S from="Backup <alerts@gmail.com>" \
  admin@example.com
```

Send to multiple recipients:

``` bash
echo "Body" | mailx -v -s "Subject" \
  user1@example.com user2@example.com user3@example.com
```

## Debugging Connection Issues

Use the verbose flag (`-v`) to see SMTP negotiation details, which helps diagnose authentication or connectivity problems. If connection fails entirely, verify:

- Gmail allows “Less secure app access” (if not using App Passwords)
- Firewall allows outbound connections on port 587
- Your network doesn’t block SMTP
- The recipient address is valid

## Security Considerations

- Store passwords only in `~/.mailrc` with `chmod 600` permissions
- Prefer App Passwords over account passwords
- Never hardcode passwords in shell scripts
- For unattended scripts, consider rotating App Passwords periodically
- The `-S ssl-verify=ignore` flag disables certificate verification — acceptable for internal scripts, but reconsider for sensitive communications
