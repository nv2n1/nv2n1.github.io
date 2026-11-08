---
title: "Mount Google Drive on Linux Using rclone"
date: 2013-07-15 12:55:52 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /mounting-google-drive-on-linux/
---

rclone is the modern standard for mounting Google Drive on Linux — it’s actively maintained, handles authentication reliably, and works across distributions without compilation.

## Install rclone

Most distributions package rclone. Install via your package manager:

``` bash
# Debian/Ubuntu
sudo apt install rclone

# Fedora/RHEL
sudo dnf install rclone

# Arch
sudo pacman -S rclone
```

Or install the latest version directly:

``` bash
curl https://rclone.org/install.sh | sudo bash
```

## Configure rclone for Google Drive

Start the configuration wizard:

``` bash
rclone config
```

Follow the interactive prompts:

1.  Create a new remote — name it `gdrive` (or your preference)
2.  Choose `drive` as the storage type
3.  Leave client ID and secret blank (rclone uses built-in credentials)
4.  Select your preferred scope:
    - **Full access**: Access all files on your Drive
    - **Drive.file**: Access only app-created files (more restrictive, safer)
5.  Authorize by visiting the provided URL in your browser and grant permissions

This creates `~/.config/rclone/rclone.conf` with your credentials. Verify the file contains an `[gdrive]` section with your token.

## Mount Google Drive

Create a mount directory:

``` bash
mkdir -p ~/gdrive
```

Mount your Drive:

``` bash
rclone mount gdrive: ~/gdrive --vfs-cache-mode full &
```

Your Google Drive is now accessible at `~/gdrive`. The `--vfs-cache-mode full` flag caches files locally for better performance and offline access.

## Mount options

For better reliability and performance, use these options:

``` bash
rclone mount gdrive: ~/gdrive \
  --vfs-cache-mode full \
  --vfs-cache-max-age 168h \
  --cache-dir ~/.cache/rclone \
  --allow-other \
  --no-checksum \
  --dir-cache-time 1h
```

**What each option does:**

- `--vfs-cache-mode full` — Cache entire files locally for offline access and repeated read performance
- `--vfs-cache-max-age 168h` — Keep cached files for 7 days before re-fetching
- `--cache-dir ~/.cache/rclone` — Store cache in a dedicated directory (easier cleanup)
- `--allow-other` — Allow other system users to access the mount (requires `user_allow_other` in `/etc/fuse.conf`)
- `--no-checksum` — Skip checksum verification on uploads (faster, use only if you trust your network)
- `--dir-cache-time 1h` — Cache directory listings for 1 hour (reduces API calls)

## Unmount

Unmount the drive:

``` bash
fusermount -u ~/gdrive
```

Or if you mounted in the background:

``` bash
killall rclone
```

## Persistent mount with systemd

For automatic mounting on login and auto-recovery on failure, create a user systemd service.

Create `~/.config/systemd/user/rclone-gdrive.service`:

``` ini
[Unit]
Description=rclone Google Drive mount
After=network-online.target
Wants=network-online.target

[Service]
Type=notify
ExecStart=/usr/bin/rclone mount gdrive: %h/gdrive \
  --vfs-cache-mode full \
  --vfs-cache-max-age 168h \
  --cache-dir %h/.cache/rclone \
  --dir-cache-time 1h \
  --log-level INFO
ExecStop=/bin/fusermount -u %h/gdrive
Restart=on-failure
RestartSec=5

[Install]
WantedBy=default.target
```

Enable and start the service:

``` bash
systemctl --user daemon-reload
systemctl --user enable --now rclone-gdrive.service
```

Check status:

``` bash
systemctl --user status rclone-gdrive.service
journalctl --user -u rclone-gdrive.service -f
```

## Multiple Google Drive accounts

To mount multiple accounts, create separate remotes during `rclone config`. For example:

``` bash
rclone config
# Create remotes: [gdrive-personal], [gdrive-work], etc.
```

Then create separate systemd services for each:

``` bash
cp ~/.config/systemd/user/rclone-gdrive.service ~/.config/systemd/user/rclone-gdrive-work.service
```

Edit `rclone-gdrive-work.service` and change:

- `Description=rclone Google Drive mount (Work)`
- `ExecStart=/usr/bin/rclone mount gdrive-work: %h/gdrive-work ...`
- `ExecStop=/bin/fusermount -u %h/gdrive-work`

Then enable and start:

``` bash
systemctl --user daemon-reload
systemctl --user enable --now rclone-gdrive-work.service
```

## Security and performance considerations

**Credential security:** Credentials in `~/.config/rclone/rclone.conf` are stored in plain text. Restrict permissions:

``` bash
chmod 600 ~/.config/rclone/rclone.conf
chmod 700 ~/.config/rclone
```

**Quota management:** The mounted drive exposes your entire Google Drive. Avoid accidentally recursive copies with `cp -r` or `rsync`, which consume quota quickly. Use `rclone copy` for intentional transfers:

``` bash
# Safe transfer with rclone
rclone copy gdrive:path/to/folder ~/local-backup
```

**Initial indexing:** Large directories may take time to list on first access. Subsequent access is faster thanks to the directory cache and VFS cache.

**Bandwidth:** Repeated file access is served from the local cache, reducing API calls and bandwidth. Monitor `~/.cache/rclone` size; it persists until manually deleted.

**SELinux/AppArmor:** If the mount fails silently, check your system’s mandatory access control logs. You may need to configure policies to allow FUSE mounts.

**Symlinks:** FUSE mounts handle symlinks inconsistently across tools. Test symlink operations with your workflow before relying on them.
