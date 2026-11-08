---
title: "Setting Up Firefox Sync: A Step-by-Step Guide"
date: 2018-03-24 08:04:32 +0000
author: "Q A"
layout: post
categories: [development-best-practices]
canonical: /how-to-set-up-firefox-sync/
---

Firefox Sync lets you keep bookmarks, passwords, history, open tabs, and settings synchronized across all your devices. It’s built on Mozilla’s infrastructure and doesn’t require a separate account beyond your Firefox account.

### Prerequisites

- Firefox 22 or later (current versions are 2024+)
- A Mozilla Firefox Account
- Devices running Windows, macOS, Linux, iOS, or Android

### Initial Setup on Your First Device

1.  Open Firefox and click the menu button (≡) in the top-right corner
2.  Select **Settings** → **Sync**
3.  Click **Sign in to Sync**
4.  Enter your Firefox Account email and password, or create a new account
5.  Verify your email address if prompted
6.  Review the data sync options and adjust if needed (passwords, bookmarks, history, etc.)

Once logged in, Firefox will begin syncing immediately in the background.

### Adding Additional Devices

On each additional device:

1.  Open Firefox and navigate to **Settings** → **Sync**
2.  Click **Sign in to Sync**
3.  Use the same Firefox Account credentials
4.  Verify the device when prompted (you may receive a verification email)

All synced data will download automatically once authentication completes.

### Customizing What Syncs

By default, Firefox syncs bookmarks, history, passwords, open tabs, and settings. To adjust what syncs:

1.  Go to **Settings** → **Sync** → **Manage Account**
2.  Under “Choose what to sync,” toggle categories on or off
3.  Changes take effect immediately

If you disable password syncing but have sensitive credentials stored locally, Firefox keeps them on that device only.

### Managing Connected Devices

View all devices connected to your account:

1.  Go to **Settings** → **Sync** → **Manage Account**
2.  Look for the “Devices” section
3.  You can rename devices or disconnect them individually

Disconnecting a device removes it from your sync chain but doesn’t delete local data on that device.

### Signing Out of Sync

To stop syncing on a device without deleting your account:

1.  Go to **Settings** → **Sync**
2.  Click **Sign out** at the bottom

Local data remains intact. To delete all sync data from your account entirely, you must do so through your Firefox Account settings at accounts.firefox.com.

### Troubleshooting Common Issues

**Sync not starting**: Check your internet connection and ensure you’re using the correct Firefox Account credentials. Try signing out and back in.

**Password sync not working**: Verify that “Passwords” is enabled in sync settings. On some systems, OS-level credential managers may interfere—check Firefox’s password manager settings.

**Data not appearing on new device**: Wait a few minutes for the initial sync to complete. If devices don’t sync within 10 minutes, sign out and sign back in on the problem device.

**Device verification fails**: Check your email for verification messages. Spam filters sometimes catch these—whitelist accounts@firefox.com.

### Security Considerations

- Firefox Sync uses end-to-end encryption for sensitive data like passwords
- Your Firefox Account password never syncs; only the sync key does
- If your Firefox Account is compromised, immediately change your password at accounts.firefox.com
- Using a strong, unique password for your Firefox Account is essential

### Advanced: Manual Sync Key Management

If you need to manage your sync key manually or reset it:

1.  Visit accounts.firefox.com
2.  Go to **Security** → **Sync**
3.  You can view or reset your sync encryption key

Resetting your sync key will disconnect all devices and require re-authentication.
