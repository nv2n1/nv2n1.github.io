---
title: "Export Chrome Passwords to a Text File on Linux"
date: 2018-03-24 11:48:01 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-export-google-chrome-password-on-linux/
---

Chrome stores passwords encrypted in the system keyring (GNOME Keyring, KWallet, or Pass depending on your desktop environment). To export them in plain text, you’ll need to create a temporary Chrome profile with basic (unencrypted) password storage, sync your passwords from Google Cloud, then extract them from the SQLite database.

## Prerequisites

- Chrome or Chromium installed
- `sqlite3` command-line tool (`sudo apt install sqlite3` on Debian/Ubuntu)
- Active Google Account with synced passwords
- All Chrome windows closed before starting

## Export Steps

**Step 1: Close Chrome completely**

Make sure no Chrome processes are running:

``` bash
killall chrome chromium chromium-browser 2>/dev/null
```

**Step 2: Launch Chrome with basic password storage**

Create a temporary profile with unencrypted passwords:

``` bash
google-chrome --user-data-dir=/tmp/chrome-tmp --password-store=basic
```

Or for Chromium:

``` bash
chromium --user-data-dir=/tmp/chrome-tmp --password-store=basic
```

**Step 3: Sync passwords from your Google Account**

In the Chrome window that opens, sign into your Google Account in Settings → Passwords. Wait 3–5 minutes for passwords to sync from the cloud. Then close Chrome completely.

**Step 4: Navigate to the Chrome profile directory**

``` bash
cd /tmp/chrome-tmp/Default
```

**Step 5: Extract passwords using sqlite3**

Open the Login Data SQLite database:

``` bash
sqlite3 'Login Data'
```

At the `sqlite>` prompt, run:

``` sql
.mode csv
.headers on
.separator ","
.output chrome_passwords.csv
SELECT origin_url, username_value, password_value FROM logins WHERE blacklisted_by_user = 0;
.exit
```

This exports only non-blacklisted passwords. Adjust the query as needed—for example, to see all columns:

``` sql
.mode column
.headers on
SELECT * FROM logins;
```

Your passwords are now in `chrome_passwords.csv` in the current directory.

## Security Considerations

- **This file contains plaintext passwords.** Keep it secure and delete it after use:

``` bash
shred -vfz -n 3 chrome_passwords.csv
```

- The temporary profile `/tmp/chrome-tmp` is world-readable. Consider using a more restricted location if sensitive data is at stake.
- Delete the temporary profile when done:

``` bash
rm -rf /tmp/chrome-tmp
```

## Alternative: Direct SQLite Query

If you want to skip the CSV file, query passwords directly:

``` bash
sqlite3 /tmp/chrome-tmp/Default/'Login Data' "SELECT origin_url, username_value, password_value FROM logins;"
```

## Troubleshooting

**“database is locked” error**: Chrome or another process still has the database open. Ensure Chrome is fully closed and no other terminals are accessing it.

**Passwords not synced**: Make sure you waited long enough after signing in. Check Chrome’s sync status in Settings → About.

**KWallet/GNOME Keyring prompts still appear**: The `--password-store=basic` flag may be ignored if your system defaults to a keyring. Try also adding `--password-store=detect` or explicitly setting environment variables:

``` bash
CHROME_PASSWORD_STORE=basic google-chrome --user-data-dir=/tmp/chrome-tmp --password-store=basic
```

**Permission denied on Login Data**: The file may be owned by a different user if you’ve run Chrome as root. Use `ls -la` to check ownership and adjust permissions if needed.

## 2026 Best Practices and Advanced Techniques

For Export Chrome Passwords to a Text File on Linux, understanding both the fundamentals and modern practices ensures you can work efficiently and avoid common pitfalls. This guide extends the core article with practical advice for 2026 workflows.

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
