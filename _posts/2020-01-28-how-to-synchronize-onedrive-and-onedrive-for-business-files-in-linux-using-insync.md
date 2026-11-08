---
title: "Sync OneDrive and OneDrive for Business on Linux with Insync"
date: 2020-01-28 10:05:37 +0000
author: "David Yang"
layout: post
canonical: https://www.systutorials.com/how-to-synchronize-onedrive-and-onedrive-for-business-files-in-linux-using-insync/
---

Insync is a third-party sync client that fills the gap left by Microsoft’s lack of native Linux support for OneDrive. It handles both personal OneDrive and OneDrive for Business accounts reliably and integrates cleanly with your desktop environment.

## Installation

### Debian/Ubuntu/Linux Mint

``` bash
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys ACCAF35C
sudo add-apt-repository "deb http://apt.insync.io/debian $(lsb_release -cs) non-free contrib"
sudo apt update
sudo apt install insync
```

### Fedora/RHEL/CentOS

``` bash
sudo rpm --import https://d2t3ff60b2tol4.cloudfront.net/builds/insync.gpg
sudo tee /etc/yum.repos.d/insync.repo > /dev/null <<EOF
[insync]
name=insync repo
baseurl=http://yum.insync.io/fedora/\$releasever
gpgcheck=1
gpgkey=https://d2t3ff60b2tol4.cloudfront.net/builds/insync.gpg
enabled=1
EOF
sudo dnf install insync
```

### File Manager Integration (Optional)

For seamless integration with your file manager, install the Nautilus extension:

``` bash
sudo apt install insync-nautilus    # Debian/Ubuntu
sudo dnf install insync-nautilus    # Fedora/RHEL
```

This adds overlay icons showing sync status directly in your file browser.

## Starting Insync

Launch the daemon:

``` bash
insync start
```

Insync runs as a background daemon and appears in your system tray. Verify it’s running:

``` bash
insync status
```

You can also autostart Insync on login by adding it to your desktop environment’s startup applications, or by creating a systemd user service:

``` bash
mkdir -p ~/.config/systemd/user
cat > ~/.config/systemd/user/insync.service <<EOF
[Unit]
Description=Insync
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
ExecStart=/usr/bin/insync start --foreground
ExecStop=/usr/bin/insync quit
Restart=on-failure

[Install]
WantedBy=default.target
EOF
systemctl --user enable insync
systemctl --user start insync
```

## Adding Your Account

Click the Insync tray icon or launch the GUI. A browser window opens redirecting you to Microsoft’s OAuth authorization page. Log in with your Microsoft account — this works for both personal OneDrive and Office 365 accounts.

After authorizing, the browser redirects back to confirm successful authentication. Your account is now linked to the Insync daemon.

## Configuring Synchronization

Once authenticated, Insync prompts you to configure sync settings:

- **Local base folder**: Choose where files sync locally (e.g., `~/OneDrive`). Insync creates the directory if it doesn’t exist.
- **Selective sync**: Choose to sync your entire OneDrive or only specific folders. This is essential if you have limited disk space.

To modify sync folders after setup, right-click the Insync tray icon, select **Preferences** → **Accounts** → your account, then toggle individual folders on or off.

## Monitoring Sync Status

Check real-time sync status from the command line:

``` bash
insync get-status
```

Expected output:

    Account: user@example.com
    Status: Syncing
    Remote changes: 0
    Local changes: 0

If you installed the Nautilus extension, file manager overlays show:

- **Green checkmark**: synced
- **Blue arrows**: actively syncing
- **Red X**: sync error

For detailed debugging, check the logs:

``` bash
tail -f ~/.config/Insync/logs/insync.log
```

## Common Operations

**Pause syncing** (useful before disconnecting or for heavy local work):

``` bash
insync pause
```

**Resume syncing**:

``` bash
insync resume
```

**Stop the daemon**:

``` bash
insync quit
```

**Restart**:

``` bash
insync quit && insync start
```

## Re-Authentication

If you need to re-authenticate an account (after password changes, enabling two-factor authentication, or SSO changes):

1.  Right-click the Insync tray icon
2.  Select **Preferences** → **Accounts**
3.  Remove the account
4.  Add it again

This is sometimes necessary with Office 365 single sign-on or after organizational policy updates.

## OneDrive for Business

OneDrive for Business (SharePoint-backed storage) works identically to personal OneDrive. Insync automatically detects your account type and handles it appropriately.

If you have both personal and business accounts, add multiple accounts to Insync — each syncs independently with its own base folder and selective sync settings.

**Important**: Business accounts may have sync restrictions enforced by your organization’s admin policies. If sync fails, is slow, or behaves unexpectedly, contact your IT department to check tenant-level sync policies. They may have disabled certain sync features or rate-limited your account.

## Handling Large Syncs

For large OneDrive folders (10GB+), consider these strategies:

- Start with selective sync enabled, syncing only essential folders
- Sync during off-peak hours or overnight to avoid bandwidth contention
- Monitor CPU and disk I/O: `iotop` and `top` are useful for tracking resource usage
- Check available disk space: `df -h ~/OneDrive` should show plenty of free space

## Licensing

Insync offers a free trial with full functionality. After the trial expires, a perpetual license costs around \$30 USD. Premium support is available separately. The license is perpetual — you own it, and don’t need an annual renewal.
