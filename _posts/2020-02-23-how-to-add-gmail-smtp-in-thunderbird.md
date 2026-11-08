---
title: "Gmail SMTP Setup in Thunderbird Using OAuth2"
date: 2020-02-23 03:26:49 +0000
layout: post
canonical: https://www.systutorials.com/how-to-add-gmail-smtp-in-thunderbird/
---

Gmail requires OAuth2 authentication for SMTP access — direct passwords have been disabled entirely. This is the only supported method for sending mail through Gmail in Thunderbird, whether you’re using a personal or Workspace account.

## OAuth2 Setup

Open Thunderbird and go to **Account Settings → Outgoing Server (SMTP)**. Click **Add** and configure these settings:

- **Server name:** smtp.gmail.com
- **Port:** 587
- **Connection security:** STARTTLS
- **Authentication method:** OAuth2
- **User Name:** your.email@gmail.com

When you click **OK**, Thunderbird launches a browser window asking you to sign in with your Google account and grant mail-sending permissions. Your actual password never enters Thunderbird — OAuth2 exchanges it for a limited, revocable token instead.

## Why OAuth2 Matters

This approach beats password authentication in several ways:

- Your real password never leaves Google’s servers
- You can revoke Thunderbird’s access anytime without changing your Gmail password
- Google logs which apps have permissions to your account
- Two-factor authentication works without configuration
- Permissions are limited in scope — Thunderbird can only send mail, not read it

## Google Workspace Considerations

For Workspace accounts (user@company.com), the SMTP settings are identical, but additional restrictions may apply:

- Your Workspace admin must explicitly allow SMTP access for third-party applications
- Use your full Workspace email address in the **User Name** field
- The OAuth2 authorization flow works only if your admin has approved it
- Contact your admin if the authorization window doesn’t appear or returns a permission error

## Troubleshooting Common Problems

**Authentication failed when sending**

Thunderbird may have cached stale credentials. Delete the Gmail account entirely (**Account Settings → Account Actions → Delete Account**), restart Thunderbird, and re-add it. This forces a fresh OAuth2 authorization.

**Failed to initialize OAuth2 during authorization**

Verify you’re using your complete Gmail address including @gmail.com. For Workspace accounts, confirm with your admin that third-party SMTP access is enabled.

**Authorization window doesn’t appear**

Check for network restrictions blocking the connection:

- On Linux, verify your firewall allows Thunderbird to reach accounts.google.com: `sudo ufw allow out 443` (adjust for your firewall)
- If using SELinux or AppArmor, check policies restricting Thunderbird’s network access
- Temporarily disable any local proxy or VPN to isolate the issue
- Test DNS resolution: `nslookup accounts.google.com` or `dig accounts.google.com`

**Invalid credentials despite correct settings**

OAuth2 tokens expire after extended inactivity. Delete the account and re-authorize. If this happens frequently, ensure Thunderbird is configured to sync on a reasonable schedule (not disabled entirely).

**Wrong port or connection type errors**

STARTTLS requires port 587. Port 465 uses implicit TLS and won’t work with STARTTLS. Verify your firewall allows outbound connections on port 587: `telnet smtp.gmail.com 587` (expect a 220 response).

## App Passwords as a Last Resort

If OAuth2 won’t work despite troubleshooting, use an app password (less secure, but functional):

1.  Visit <a href="https://myaccount.google.com" rel="nofollow noopener" target="_blank">myaccount.google.com</a> → **Security**
2.  Enable **2-Step Verification** if not already active
3.  Scroll to **App passwords**
4.  Select **Mail** and **Linux** (or your device type)
5.  Google generates a 16-character password
6.  In Thunderbird, set **Authentication method** to **Normal password** and paste this generated password

This works but bypasses OAuth2’s security benefits. Use it only when OAuth2 fails after troubleshooting.

## Enable Debug Logging

To diagnose persistent issues:

1.  Go to **Help → Troubleshooting Information**
2.  Scroll to **Logging** and enable debug mode for SMTP
3.  Restart Thunderbird and attempt to send
4.  Check the generated logs for specific error messages

The logs typically reveal token expiration, DNS resolution failures, firewall blocks, or authentication timeouts that aren’t obvious from user-facing errors.

## Verify the Configuration

Send a test email to confirm everything works. Once OAuth2 is functioning, it requires no further adjustment unless you change Gmail’s security settings or explicitly revoke Thunderbird’s access through your Google Account security settings page.
