---
title: "Where Linux Applications Store Configuration and Data Files"
date: 2017-12-31 06:57:03 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /evolution-save-data-configure-files-linux/
---

Evolution is a full-featured personal information management suite that handles email, contacts, calendars, and tasks. It includes enterprise features like native Microsoft Exchange support and integrates deeply with GNOME’s ecosystem. To troubleshoot issues, migrate data, back up configurations, or secure your setup, you need to know where Evolution stores everything.

Evolution follows the XDG Base Directory Specification, which standardizes where applications store their files. This means its configuration and data are distributed across three main locations under your home directory.

## Password Storage with GNOME Keyring

Evolution doesn’t store passwords as plain text. Instead, it delegates password storage to GNOME Keyring, which encrypts credentials at rest. The keyring is unlocked automatically when you log in, so passwords remain inaccessible to other users or processes.

If you need to view, edit, or delete stored passwords, use Seahorse (the GNOME Keyring GUI):

``` bash
seahorse
```

From there, navigate to the Passwords section and search for Evolution-related entries. You can also delete compromised credentials directly from this interface.

## Configuration Files

All Evolution configuration lives under `$HOME/.config/evolution/`. This is the primary location for all settings except cached data.

### Account Settings and Sources

Account configurations—including IMAP, POP, Exchange, and CalDAV settings—are stored in:

    $HOME/.config/evolution/sources/

Each account gets its own `.source` file in this directory. These are text-based configuration files that define connection parameters, authentication methods, and sync intervals. Editing these directly isn’t recommended; use the GUI instead. However, they’re valuable for backup or migration purposes.

### Keyboard Shortcuts

Evolution’s keyboard shortcut mappings are stored in:

    $HOME/.config/evolution/accels

This is a plain-text GtkAccelMap file. You can edit it manually to customize shortcuts, though the Evolution preferences GUI is usually more convenient. Each line maps an action to a key combination:

    (gtk_accel_path "<Actions>/mail-toolbar/mail-send" "<Primary>Return")
    (gtk_accel_path "<Actions>/mail-message/mail-delete" "Delete")

To find the action name for a specific menu item, open the accels file and search for relevant keywords.

### GSettings and dconf

Some Evolution settings are stored in the GSettings database (backed by dconf files):

    $HOME/.config/dconf/user

To browse and modify these settings graphically, install and use dconf-editor:

``` bash
sudo apt install dconf-editor  # Debian/Ubuntu
sudo dnf install dconf-editor  # Fedora/RHEL
```

Launch it and navigate to `/org/gnome/evolution/` to see available options. Command-line users can query settings with:

``` bash
gsettings list-schemas | grep evolution
gsettings get org.gnome.evolution.mail show-preview
```

## Data Files

User data—emails, contacts, calendar events, and tasks—lives in:

    $HOME/.local/share/evolution/

This directory structure typically includes:

- `calendar/` — calendar events and task lists
- `contacts/` — address book entries
- `mail/` — email messages (for local accounts and IMAP caches)
- `tasks/` — standalone tasks

### Understanding Mail Storage

For local mail accounts, Evolution stores messages as individual files in the mail directory structure. For IMAP accounts, the actual messages remain on the server, but Evolution caches them locally.

### Cached Data

Disposable caches (which can be safely deleted) are stored in:

    $HOME/.cache/evolution/

Common cached items include:

- IMAP folder summaries and message headers
- Calendar event thumbnails
- Contact photos
- Temporary downloaded attachments

Clearing this directory will force Evolution to re-download and re-cache data on next sync, which can resolve corruption issues:

``` bash
rm -rf $HOME/.cache/evolution/
```

After clearing the cache, restart Evolution and let it rebuild the cache. This typically takes a few minutes for large mailboxes.

## Backing Up and Restoring

To back up your entire Evolution setup:

``` bash
tar -czf evolution-backup.tar.gz \
  ~/.config/evolution/ \
  ~/.local/share/evolution/ \
  ~/.config/dconf/user
```

To restore from backup:

``` bash
tar -xzf evolution-backup.tar.gz -C ~/
```

Always close Evolution before backing up or restoring.

## Migrating Between Systems

When moving Evolution to a new machine:

1.  Back up the three directories listed above
2.  Install Evolution on the new system
3.  Restore the backup
4.  Restart Evolution and let it re-synchronize with servers

For sensitive data, verify that `~/.local/share/evolution/` lives on encrypted storage. If you’re concerned about email exposure, consider storing the mail directory on a separate encrypted partition or using full-disk encryption.

## Troubleshooting

If Evolution behaves unexpectedly, clear the cache first before rebuilding the configuration:

``` bash
rm -rf ~/.cache/evolution/
```

For more aggressive troubleshooting, temporarily move the entire config directory and let Evolution regenerate defaults:

``` bash
mv ~/.config/evolution ~/.config/evolution.bak
```

Restart Evolution to create fresh configuration, then gradually restore settings from the backup.
