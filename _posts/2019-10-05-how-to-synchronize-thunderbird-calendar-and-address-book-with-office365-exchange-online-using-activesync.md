---
title: "Sync Thunderbird with Office 365 Using TbSync"
date: 2019-10-05 12:09:13 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-synchronize-thunderbird-calendar-and-address-book-with-office365-exchange-online-using-activesync/
---

Thunderbird’s built-in calendar support (Lightning) handles local calendars, but you need two extensions to sync with Exchange Online:

- **TbSync** — manages cloud account synchronization for contacts, calendars, and tasks
- **Provider for Exchange ActiveSync** — adds ActiveSync protocol support to TbSync

Install both from Thunderbird’s Add-ons Manager:

1.  Open Thunderbird and go to Menu → Add-ons and Themes
2.  Search for “TbSync” and click Install
3.  Search for “Provider for Exchange ActiveSync” and click Install
4.  Restart Thunderbird

## Configure TbSync for Exchange Online

After installation, add your Exchange account:

1.  Go to Menu → Settings → Add-ons and Features
2.  Select TbSync from the left sidebar
3.  Click **Account actions** → **Add new account** → **Exchange ActiveSync**

In the dialog, enter:

- **Email address** — your Office 365 email (e.g., `user@yourdomain.com`)
- **Password** — your Office 365 app password (see MFA section below)
- **Server URL** — leave blank for autodiscovery

Click **Autodiscover settings** and TbSync will query Microsoft’s autodiscovery service to configure your account automatically. This usually completes in seconds.

## Handle Multi-Factor Authentication

If your Office 365 account uses MFA (recommended), you must generate an app-specific password:

1.  Log into your Microsoft account at <a href="https://account.microsoft.com/security" rel="nofollow noopener" target="_blank">https://account.microsoft.com/security</a>
2.  Navigate to **App passwords**
3.  Select **Mail** and **Thunderbird** (or create a custom entry)
4.  Microsoft generates a 16-character password
5.  Use this app password in TbSync instead of your regular password

Regular passwords won’t authenticate if MFA is enabled. This approach is more secure than disabling MFA.

## Select Resources to Sync

Once the account is added, expand it in TbSync to see available resources:

1.  Check the box next to your account name to enable it
2.  Click the dropdown arrow to expand resource options
3.  Enable what you need:
    - **Contacts** — your Office 365 address book
    - **Calendars** — Exchange calendars (including shared calendars you have access to)
    - **Tasks** — Exchange task lists (optional)
4.  Click **Synchronize now** for the initial sync

## Configure Automatic Synchronization

To keep data current without manual intervention:

1.  Select your account in TbSync
2.  Set **Periodic synchronization (in minutes)** to an interval (10–15 minutes for frequent updates, 30–60 minutes to reduce bandwidth)
3.  Click **Save**

TbSync will now sync automatically at your specified interval.

## Selective Sync

If you have many calendars or contacts, reduce sync overhead by syncing only what you use:

1.  Expand the account in TbSync
2.  Uncheck calendars or contacts you don’t need locally
3.  Only enabled resources sync

This is particularly useful in enterprise environments where you have access to dozens of shared calendars but actively use only a few.

## Verify Synchronization

After the initial sync:

- Open **Address Book** (Menu → Address Book) to view imported contacts
- Click the Calendar icon in the sidebar to view synced calendars

Your Exchange calendars appear in the left sidebar under their original Exchange names. Events created in Thunderbird sync back to Exchange Online automatically, and changes made in Outlook or OWA appear in Thunderbird after the next sync interval.

## Troubleshooting

**Autodiscovery fails**

If automatic detection doesn’t work, manually enter the Exchange Online server URL:

    https://outlook.office365.com/EAS/Exchange.asmx

**Authentication errors**

- Verify you’re using an app password if MFA is enabled (not your regular password)
- Test credentials by logging into <a href="https://outlook.office365.com" rel="nofollow noopener" target="_blank">https://outlook.office365.com</a> directly in your browser
- Check that your app password was generated correctly (16 characters, no spaces)

**Contacts or calendars don’t appear**

- Confirm resources are enabled in TbSync’s account settings
- Verify contacts and calendars exist in Exchange Online by logging into Outlook Web Access (OWA)
- For shared calendars, confirm you have at least Read access through OWA
- Manually trigger a sync by clicking **Synchronize now**

**Sync timeouts or hangs**

- Increase the periodic synchronization interval to 30+ minutes
- Check your internet connection — ActiveSync is sensitive to latency
- Disable unused resources (like Tasks) to reduce sync payload
- Check Thunderbird’s error console (Menu → Tools → Developer Tools → Browser Console) for detailed errors

**Calendar events sync one way only**

- Verify calendar permissions in Exchange for shared calendars
- Right-click the calendar name in Thunderbird and confirm **Read only** is unchecked
- Force a full resync by disabling and re-enabling the calendar resource in TbSync

**Sync interval seems slower than expected**

- Reduce the number of enabled resources
- Check for network congestion or DNS resolution issues
- Lower the sync interval value to trigger more frequent background syncs (this won’t speed up individual syncs, but reduces perceived delay)
