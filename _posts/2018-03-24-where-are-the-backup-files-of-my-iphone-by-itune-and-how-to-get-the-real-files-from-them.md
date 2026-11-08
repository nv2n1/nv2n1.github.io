---
title: "How to Find and Extract Files from iPhone iTunes Backups"
date: 2018-03-24 08:16:20 +0000
modified: 2026-04-12 16:07:07 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /where-are-the-backup-files-of-my-iphone-by-itune-and-how-to-get-the-real-files-from-them/
---

iTunes backups are stored in device-specific directories. The location depends on your operating system:

**macOS:**

    ~/Library/Application Support/MobileSync/Backup/

**Windows:**

    %APPDATA%\Apple Computer\MobileSync\Backup

On Windows, the easiest way to navigate there is to press `Win + R`, type `%appdata%` and hit Enter, then navigate to `Apple Computer\MobileSync\Backup\`.

## Understanding iTunes Backup Files

iTunes stores backups as a collection of files with hashed names. You won’t see recognizable filenames like “Photos” or “Messages”—instead you’ll find files named with 40-character SHA-1 hashes (e.g., `3d0d7e5af71c5ce4a404a6b0b05fb7a69e6cb292`).

Each backup folder also contains a `Manifest.db` file (SQLite database) and an `Info.plist` file. The manifest file maps the hashed filenames to their actual locations within the backup structure.

## Extracting Data from iTunes Backups

### Using sqlite3 (Command Line)

For unencrypted backups, you can query the manifest directly:

``` bash
sqlite3 ~/Library/Application\ Support/MobileSync/Backup/[backup-id]/Manifest.db ".tables"
```

This shows available tables. To see the file mappings:

``` bash
sqlite3 ~/Library/Application\ Support/MobileSync/Backup/[backup-id]/Manifest.db "SELECT * FROM Files LIMIT 10;"
```

However, manually extracting data this way is tedious and requires understanding the SQLite schema for each iOS version.

### Using Extraction Tools

Third-party tools handle the complexity:

- **iPhone Backup Extractor** — GUI-based tool with a free tier suitable for basic extraction
- **iExplorer** — Cross-platform tool that mounts backups as virtual drives
- **PhoneRescue** — Handles encrypted and unencrypted backups
- **SQLite Browser (DB Browser for SQLite)** — Open-source tool for direct SQLite inspection of unencrypted backups

### Encrypted Backups

If you enabled encryption in iTunes (Settings \> Summary \> Back Up to This Computer \> Encrypt iPhone Backup), the files are protected. Most tools can decrypt and extract from encrypted backups if you provide the password, but command-line sqlite3 queries won’t work directly.

For encrypted backups, use a dedicated extraction tool that supports decryption—most modern tools do, but verify before purchasing.

## Important Limitations

iTunes (and its successor, Finder on macOS) backups don’t capture everything. App data within each app is backed up, but some data like cached content, settings within apps, or app-specific databases may not be fully recoverable. The backup structure varies by iOS version, so extraction tools need to be compatible with your backup’s iOS version.

iCloud backups have different storage locations and are more difficult to access locally, so if you’re trying to recover data from an iCloud backup, you’ll need to restore to a device or use specialized cloud recovery services.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
