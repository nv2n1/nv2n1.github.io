---
title: "How to Back Up Linux Home Directories with rsync"
date: 2013-07-12 16:32:03 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /backup-linux-home-directory-using-rsync/
---

rsync is a reliable choice for backing up your Linux home directory, especially when dealing with large files and incremental changes. Unlike git (which struggles with files \>5GB), rsync efficiently handles large files and only transfers what’s changed on subsequent runs.

## Basic Backup Command

The fundamental syntax is straightforward:

``` bash
rsync -avxP \
  /path/to/directory/to/backup \
  /path/to/directory/for/storing/backup
```

Breaking down the flags:

- `-a` (archive mode): Preserves permissions, timestamps, ownership, and recursively copies directories
- `-v` (verbose): Shows files being transferred
- `-x` (one-file-system): Doesn’t cross filesystem boundaries — useful for excluding mounted volumes like `/dev`, `/proc`, `/sys`
- `-P`: Combines `--progress` (shows transfer progress) and `--partial` (keeps incomplete files if interrupted, allowing resumption)

## Practical Example

To back up your home directory to an external drive mounted at `/mnt/backup`:

``` bash
rsync -avxP ~/. /mnt/backup/home-backup/
```

Note the trailing slash on the source — this copies the *contents* of your home directory rather than the directory itself.

## Handling Deletions

By default, rsync preserves files in the destination that no longer exist in the source. This is intentional safety behavior. If you want rsync to mirror the source exactly (deleting files from the backup if they’re removed from your home directory), add the `--delete` flag:

``` bash
rsync -avxP --delete ~/. /mnt/backup/home-backup/
```

Use this carefully — it’s permanent.

## Additional Useful Flags

Consider adding these flags depending on your needs:

``` bash
rsync -avxP --delete --exclude='.cache' --exclude='.local/share/Trash' ~/. /mnt/backup/home-backup/
```

- `--exclude`: Skips specific patterns. Common excludes include `.cache`, `.local/share/Trash`, and `.mozilla/firefox/*/Cache`
- `--exclude-from=FILE`: Read exclude patterns from a file (one per line)
- `--stats`: Displays transfer statistics after completion
- `--dry-run`: Preview what would be transferred without actually copying

## Remote Backups

rsync works seamlessly over SSH. To backup to a remote server:

``` bash
rsync -avxP -e ssh ~/. user@remote-host:/backup/home-backup/
```

The `-e ssh` flag specifies SSH as the transport. Ensure SSH key authentication is configured for non-interactive backups.

## Automating with cron

For regular backups, add a cron job. Create or edit `crontab -e`:

``` bash
# Weekly backup every Sunday at 2 AM
0 2 * * 0 rsync -avxP --delete ~/. /mnt/backup/home-backup/ >> /var/log/rsync-backup.log 2>&1
```

Redirect output to a log file to monitor backup success. For sensitive operations, consider using `--log-file` instead:

``` bash
rsync -avxP --delete --log-file=/var/log/rsync-backup.log ~/. /mnt/backup/home-backup/
```

## Performance Tips

- **First run**: The initial backup will take time. Subsequent runs transfer only changed files.
- **Bandwidth limiting**: Use `--bwlimit=KBPS` on remote backups to avoid saturating your connection.
- **Symlinks**: rsync preserves symlinks by default with `-a`. Use `--copy-links` to copy symlink targets instead if needed.
- **Checksums**: By default, rsync uses file modification time and size. Add `-c` (checksum) for strict verification if you suspect corruption, though it’s slower.

## Permission and Ownership

If backing up as a non-root user, rsync preserves whatever permissions you can read. If files are owned by other users and you don’t have read access, rsync will skip them. For complete backups, run as root:

``` bash
sudo rsync -avxP --delete ~/. /mnt/backup/home-backup/
```

However, be careful with sudo and rsync — always double-check your source and destination paths.

rsync is resilient and handles interrupted transfers gracefully. If a backup is interrupted, re-running the same command resumes where it left off, transferring only the remaining portions of incomplete files.
