---
title: "Monitoring All IMAP Folders for New Messages in Thunderbird"
date: 2018-03-24 11:43:10 +0000
modified: 2026-04-12 16:07:03 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-make-thunderbird-check-for-new-messages-in-all-imap-folders/
---

By default, Thunderbird only checks the Inbox folder for new messages when using IMAP accounts. If you receive emails that bypass your Inbox or use multiple folders for organization, you’ll want to enable checking across all IMAP folders.

## Method 1: Using the Config Editor (Recommended)

The most direct approach is to modify Thunderbird’s configuration through the Config Editor:

1.  Open Thunderbird and go to **Edit \> Preferences** (Linux/Windows) or **Thunderbird \> Preferences** (macOS)
2.  Navigate to the **Advanced** tab
3.  Click the **Config Editor** button
4.  In the search box, type: `mail.check_all_imap_folders_for_new`
5.  Double-click the entry to toggle it from `false` to `true`
6.  Restart Thunderbird

Thunderbird will now check all subscribed IMAP folders when you trigger a “Get New Messages” action.

## Method 2: Per-Folder Configuration

If you only want to check specific folders (not all), you can configure individual folders instead:

1.  Right-click any IMAP folder
2.  Select **Properties**
3.  Check the box for **“Check this folder for new messages”**
4.  Click **OK**

This approach gives you fine-grained control and is useful if you have many archived or inactive folders you don’t want checked.

## Method 3: Account-Level Settings

You can also adjust this at the account level for more granular control:

1.  Right-click your IMAP account in the folder pane
2.  Select **Settings**
3.  Go to **Server Settings**
4.  Look for options related to checking folders for new mail

The available options depend on your Thunderbird version and configuration, but usually you can specify whether to check only the Inbox or all subscribed folders.

## Important Notes

- This setting only affects subscribed folders. Make sure the folders you want checked are actually subscribed in Thunderbird (right-click account \> **Subscribe** to manage subscriptions)
- Checking all folders increases server load and may slow down mail checks on accounts with many folders
- The setting applies globally to all IMAP accounts; you cannot set it per-account through the config editor
- If you’re using an older version of Thunderbird, the preference path may be slightly different, but the config editor method remains the most reliable approach

## Verify It’s Working

After enabling this setting, trigger a manual mail check:

- Press **F5** or go to **File \> Get New Messages**
- Watch the status bar to confirm Thunderbird is checking multiple folders
- Check the Thunderbird log if needed: **Help \> Troubleshooting Information \> Show Folder** to access logs for debugging

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
