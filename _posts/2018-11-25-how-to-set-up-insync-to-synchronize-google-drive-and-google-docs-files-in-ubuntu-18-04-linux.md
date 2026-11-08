---
title: "Installing and Configuring Insync for Google Drive on Linux"
date: 2018-11-25 05:54:57 +0000
modified: 2026-04-11 15:43:01 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-set-up-insync-to-synchronize-google-drive-and-google-docs-files-in-ubuntu-18-04-linux/
---

Google Drive remains the dominant cloud storage platform, but Linux users still lack an official client. Insync fills this gap—it’s a third-party sync tool that actually works well and maintains local file access rather than relying on virtual filesystems.

## Why Insync Over Alternatives

Insync’s main advantage is that Google Drive files appear in your actual filesystem with proper directory structure and filenames. Unlike GNOME Online Accounts, which uses virtual mounts only accessible through Nautilus, Insync gives you real files you can access from any application.

The most valuable feature for many users is Google Docs/Sheets/Slides conversion. Insync can download converted copies of these files (as DOCX, XLSX, or PPTX) whether you created them or they were shared with you. Changes sync bidirectionally. This is genuinely useful for backup purposes and for workflows where you need native Office files alongside cloud documents.

Insync costs \$29.99 for a one-time license, but a 15-day free trial lets you test whether the features justify the cost. It supports Ubuntu, Debian, Linux Mint, Fedora, and other distributions.

## Installation on Ubuntu/Debian/Mint

**Add the GPG key:**

``` bash
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://d2t3ff60b2tol4.cloudfront.net/linux/key.asc | \
  sudo gpg --dearmor -o /etc/apt/keyrings/insync-archive-keyring.gpg
```

**Add the repository:**

For Ubuntu 24.04 LTS (Noble):

``` bash
echo "deb [signed-by=/etc/apt/keyrings/insync-archive-keyring.gpg] http://apt.insync.io/ubuntu noble non-free contrib" | \
  sudo tee /etc/apt/sources.list.d/insync.list
```

For Ubuntu 22.04 LTS (Jammy):

``` bash
echo "deb [signed-by=/etc/apt/keyrings/insync-archive-keyring.gpg] http://apt.insync.io/ubuntu jammy non-free contrib" | \
  sudo tee /etc/apt/sources.list.d/insync.list
```

For Debian 12 (Bookworm):

``` bash
echo "deb [signed-by=/etc/apt/keyrings/insync-archive-keyring.gpg] http://apt.insync.io/debian bookworm non-free contrib" | \
  sudo tee /etc/apt/sources.list.d/insync.list
```

For Linux Mint 21.x (based on Jammy):

``` bash
echo "deb [signed-by=/etc/apt/keyrings/insync-archive-keyring.gpg] http://apt.insync.io/ubuntu jammy non-free contrib" | \
  sudo tee /etc/apt/sources.list.d/insync.list
```

**Update and install:**

``` bash
sudo apt update
sudo apt install insync
```

The installation adds the required `fs.inotify.max_user_watches` kernel parameter automatically to handle large directory watching.

## File Manager Integration

Insync integrates with multiple file managers. Install the appropriate plugin for your environment:

``` bash
# For GNOME (Nautilus)
sudo apt install insync-nautilus

# For KDE (Dolphin)
sudo apt install insync-dolphin

# For Cinnamon (Nemo)
sudo apt install insync-nemo

# For Xfce (Thunar)
sudo apt install insync-thunar

# For MATE (Caja)
sudo apt install insync-caja
```

These plugins add context menu options to open files in Google Drive web view and display sync status badges.

## Initial Setup

Launch Insync from your application menu or run:

``` bash
insync start
```

The first time, you’ll see the authentication window. Click to authorize access to your Google account. Insync only requests Google Drive permissions—it doesn’t ask for full account access.

Once authorized, Insync begins syncing immediately. By default, it creates an `~/Insync` folder containing your Drive contents mirrored locally.

## Configuring Google Docs Conversion

To enable Office file conversion (essential if you work with Google Docs):

1.  Right-click the Insync system tray icon → **Preferences**
2.  Select your Google account
3.  Under **File Conversion**, check:
    - “Convert Google Docs to .docx”
    - “Convert Google Sheets to .xlsx”
    - “Convert Google Slides to .pptx”

Insync will download converted versions alongside the original files. Edits to converted files sync back to Google Drive.

## Handling Multiple Accounts

To sync multiple Google Drive accounts:

1.  Click **Add Account** in Insync preferences
2.  Authorize the additional account
3.  Configure conversion and sync settings per account

Each account syncs to its own folder under `~/Insync`.

## Bandwidth and Selective Sync

For large Drive accounts, you can selectively sync folders:

1.  Open Insync preferences
2.  Under your account, click **Selective Sync**
3.  Uncheck folders you don’t need locally

This saves bandwidth and disk space for archived or rarely-accessed content.

## Troubleshooting

If sync stalls, restart the daemon:

``` bash
insync quit
insync start
```

Check sync status:

``` bash
insync get_status
```

For detailed logs:

``` bash
insync get_log
```

If you hit the inotify limit with very large local filesystems, manually increase it:

``` bash
echo "fs.inotify.max_user_watches = 2097152" | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

## Alternatives Worth Considering

**Rclone** is a lightweight command-line option for syncing Google Drive without a GUI or daemon—good if you only need periodic backups. **Nextcloud** works well if you self-host. **GNOME Online Accounts** is built-in but limited to read-only virtual mounts.

For active editing workflows where you need real files and want Google Docs integration, Insync remains the most complete solution for Linux.
