---
title: "Email Backup: Comparing offlineimap, mbsync, and doveadm"
date: 2018-03-24 08:20:58 +0000
modified: 2026-04-11 17:45:17 +0000
author: "Eric Ma"
layout: post
categories: [functional-programming]
canonical: /how-to-back-up-a-complete-imap-account/
---

Backing up a complete IMAP account with thousands of messages across nested folders requires automation to preserve folder structure and avoid manual errors. This guide covers three modern tools and provides detailed setup for the most flexible option.

## Choosing your backup tool

**offlineimap** — Most flexible for complex folder structures and label handling. Active maintenance resumed, widely packaged.

**mbsync (isync)** — Lightweight and fast, excellent for large accounts (500k+ messages). Minimal configuration, efficient sync algorithm.

**doveadm** — Built-in to Dovecot servers, useful if backing up directly from your mail server. Best for local or nearby systems.

**imapync** — Simple one-way sync, good for straightforward backups, but less flexible for folder mapping.

This guide uses offlineimap for its maturity and control, but includes mbsync alternatives where applicable.

## Installing offlineimap

On Fedora/RHEL/CentOS:

``` bash
sudo dnf install offlineimap
```

On Debian/Ubuntu:

``` bash
sudo apt install offlineimap
```

On Arch:

``` bash
sudo pacman -S offlineimap
```

Verify installation:

``` bash
offlineimap --version
```

## Basic configuration

Create `~/.offlineimaprc`:

``` ini
[general]
accounts = MyIMAP
maxsyncaccount = 1
autorefresh = 0
socktimeout = 30

[Account MyIMAP]
localrepository = Local
remoterepository = Remote
synclabels = yes
readonly = true

[Repository Local]
type = Maildir
localfolders = ~/Mail/backup
createfolders = yes
sep = /

[Repository Remote]
type = IMAP
remotehost = imap.example.com
remoteuser = your.email@example.com
remotepass = your_password_here
ssl = yes
sslcacertfile = /etc/ssl/certs/ca-certificates.crt
keepalive = 60
timeout = 30
```

Key configuration points:

- `readonly = true` — Prevents accidental writes to the IMAP server during backup
- `ssl = yes` — Required for modern servers; verify your CA certificate path
- `createfolders = yes` — Creates local directories matching remote folder structure
- `socktimeout = 30` — Prevents hangs on slow connections
- `keepalive = 60` — Maintains connection stability; increase to 120 for large syncs

## Secure credential handling

Never store plaintext passwords in config files. Use a separate password file:

``` ini
[Repository Remote]
remotepassfile = ~/.config/offlineimap/password
```

Create the credentials file:

``` bash
mkdir -p ~/.config/offlineimap
echo "your_actual_password" > ~/.config/offlineimap/password
chmod 600 ~/.config/offlineimap/password
```

For OAuth2 or app-specific passwords, use the same approach — offlineimap accepts any credential string in the password file.

## Running your first backup

Start the sync:

``` bash
offlineimap
```

For a one-time run without interactive prompts:

``` bash
offlineimap -o -u Quiet
```

Monitor with verbose IMAP debugging:

``` bash
offlineimap -d IMAP
```

Watch progress in another terminal:

``` bash
watch -n 5 'find ~/Mail/backup -type f | wc -l'
```

## Handling large accounts

For accounts with 100k+ messages, optimize sync performance:

Add to `[Repository Remote]`:

``` ini
maxage = 90
timeout = 60
keepalive = 120
```

`maxage = 90` syncs only messages from the last 90 days initially. Remove this line in subsequent runs to fetch remaining older messages.

Run overnight in a persistent session:

``` bash
nohup offlineimap -u Quiet > ~/offlineimap.log 2>&1 &
```

Or use tmux:

``` bash
tmux new-session -d -s mailsync 'offlineimap'
```

## Working with backed-up emails

Emails are stored in Maildir format (each message as a separate file). Browse with mutt:

``` bash
mutt -f ~/Mail/backup/INBOX
```

Or use neomutt, Thunderbird, or Evolution with your backup directory as a local account.

Convert to mbox format for archival:

``` bash
find ~/Mail/backup -type d -mindepth 1 -exec bash -c 'cat "$0"/cur/* 2>/dev/null > "${0}.mbox"' {} \;
```

## Archiving for long-term storage

After successful sync, compress the backup:

``` bash
tar --lz4 -cf mail-backup-$(date +%Y%m%d).tar.lz4 ~/Mail/backup
```

Or with gzip:

``` bash
tar --gzip -cf mail-backup-$(date +%Y%m%d).tar.gz ~/Mail/backup
```

Verify archive integrity:

``` bash
tar -tf mail-backup-*.tar.lz4 | head -20
```

## Incremental backups with cron

Set up daily syncs to capture new messages:

``` bash
0 2 * * * /usr/bin/offlineimap -u Quiet 2>&1 | logger -t offlineimap
```

This runs at 2 AM daily, logs output to syslog. Subsequent runs only download new or changed messages, making incremental backups fast.

For monitoring:

``` bash
journalctl -t offlineimap -n 20
```

## Alternative: Using mbsync for faster large backups

If offlineimap is too slow for your account, try mbsync:

Install:

``` bash
sudo apt install isync  # or 'dnf install isync'
```

Create `~/.mbsyncrc`:

``` ini
IMAPAccount example
Host imap.example.com
User your.email@example.com
PassCmd "pass email/example"
SSLType IMAPS

IMAPStore remote
Account example

MaildirStore local
Path ~/Mail/backup/
Inbox ~/Mail/backup/INBOX
SubFolders Verbatim

Channel example
Far :remote:
Near :local:
Patterns *
Create Near
Sync Pull
Remove Near
Expunge Near
SyncState *
```

Run:

``` bash
mbsync -a
```

mbsync is often 3-5x faster than offlineimap for initial large syncs.

## Troubleshooting

**Sync hangs:**

``` ini
[Repository Remote]
timeout = 60
keepalive = 120
```

**SSL certificate errors:**

Verify the correct CA bundle path for your system:

- Fedora/RHEL: `/etc/pki/tls/certs/ca-bundle.crt`
- Debian/Ubuntu: `/etc/ssl/certs/ca-certificates.crt`
- Arch: `/etc/ca-certificates/extracted/tls-ca-bundle.pem`

Or fetch the server’s certificate directly:

``` bash
openssl s_client -connect imap.example.com:993 -showcerts < /dev/null 2>/dev/null | grep -A 20 'BEGIN CERTIFICATE' > server.crt
```

Then reference it:

``` ini
sslcacertfile = /path/to/server.crt
```

**Folder mapping issues:**

Manually map folders if automatic detection fails:

``` ini
[Repository Remote]
nametrans = lambda foldername: foldername.replace('[Gmail]/', 'backup-gmail-').replace('All Mail', 'archive')
```

**Connection timeouts on flaky networks:**

Use `autoresume = yes` to resume incomplete syncs:

``` ini
[general]
autoresume = yes
```

Check process logs:

``` bash
tail -f ~/.offlineimap/logs/IMAP.Remote
```
