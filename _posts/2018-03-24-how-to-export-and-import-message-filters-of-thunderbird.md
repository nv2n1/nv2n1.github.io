---
title: "Exporting and Importing Thunderbird Message Filters"
date: 2018-03-24 08:21:05 +0000
layout: post
canonical: https://www.systutorials.com/how-to-export-and-import-message-filters-of-thunderbird/
---

Thunderbird stores message filters in per-account configuration files, making it inconvenient to replicate filters across multiple accounts or installations. Rather than recreating filters manually, you can copy filter files directly or use symbolic links to keep filters synchronized.

## Where Thunderbird Stores Filters

Thunderbird saves filter rules in `msgFilterRules.dat`, a plain text configuration file. Each account maintains its own copy in its local mail directory. On Linux, your profile location is `~/.thunderbird/`.

Find all filter files across your profile:

``` bash
find ~/.thunderbird/ -name msgFilterRules.dat
```

Output typically shows:

    ~/.thunderbird/[profile-hash].default/Mail/Local Folders/msgFilterRules.dat
    ~/.thunderbird/[profile-hash].default/Mail/[account-name]/msgFilterRules.dat

Account-specific filters live in their respective mail directories. The Local Folders filter file can serve as a central source for distributing filters to multiple accounts.

## Backing Up and Copying Filters Between Accounts

Before making any changes, close Thunderbird completely. Thunderbird rewrites `msgFilterRules.dat` on exit, so any manual edits while the application runs will be lost.

To copy filters from one account to another:

``` bash
# Close Thunderbird first
cp ~/.thunderbird/[profile].default/Mail/[source-account]/msgFilterRules.dat \
   ~/.thunderbird/[profile].default/Mail/[dest-account]/msgFilterRules.dat
```

Replace `[profile]`, `[source-account]`, and `[dest-account]` with your actual profile hash and account names.

If your filters reference custom headers, also copy that setting from `prefs.js`:

``` bash
grep mailnews.customHeaders ~/.thunderbird/[profile].default/prefs.js
```

Add the output to the destination profile’s `prefs.js` if the setting doesn’t already exist.

## Using Symbolic Links for Unified Filters

For a cleaner approach that keeps all accounts synchronized without manual duplication, use symbolic links. This way, editing filters in one place affects all linked accounts.

Choose a source filter file (Local Folders works well if you don’t use it for mail storage):

``` bash
SOURCE="$HOME/.thunderbird/[profile].default/Mail/Local Folders/msgFilterRules.dat"
```

For each account that should use these filters, replace its filter file with a symbolic link:

``` bash
cd ~/.thunderbird/[profile].default/Mail/[account-name]/
ln -bsv ../../Mail/Local\ Folders/msgFilterRules.dat msgFilterRules.dat
```

The `-b` flag backs up the original `msgFilterRules.dat` as `msgFilterRules.dat~` before creating the link, preserving your previous configuration.

Verify the links are in place:

``` bash
ls -la ~/.thunderbird/[profile].default/Mail/*/msgFilterRules.dat
```

All symlinked accounts now reference the same filter file.

## Restoring Symlinks After GUI Edits

When you edit filters through the Thunderbird GUI (Message → Filters and Search → Mail Filters), Thunderbird may replace the symlink with a regular file. After making filter changes, verify your symlinks:

``` bash
ls -l ~/.thunderbird/[profile].default/Mail/[account-name]/msgFilterRules.dat
```

If a symlink was replaced with a regular file, restore it:

``` bash
rm ~/.thoroughbird/[profile].default/Mail/[account-name]/msgFilterRules.dat
ln -bsv ../../Mail/Local\ Folders/msgFilterRules.dat msgFilterRules.dat
```

Restart Thunderbird to reload the filters.

## Direct Editing of Filter Files

The `msgFilterRules.dat` file is plain text and can be edited directly while Thunderbird is closed. This is useful for bulk modifications, merging filters from multiple sources, or version control.

Each filter rule follows this structure:

    [num1]
    name=Filter Name
    enabled=yes
    account=account-name
    action=copy
    actionValue=/path/to/folder
    condition="Subject contains test OR From contains example@example.com"

Always back up before manual edits:

``` bash
cp msgFilterRules.dat msgFilterRules.dat.backup
```

Edit with your preferred text editor:

``` bash
vim ~/.thunderbird/[profile].default/Mail/[account-name]/msgFilterRules.dat
```

Common filter actions include:

- `action=copy` — Copy matching messages to a folder
- `action=move` — Move matching messages to a folder
- `action=delete` — Permanently delete matching messages
- `action=mark` — Mark messages as read, flagged, or with a tag

Conditions support boolean logic with `AND`, `OR`, and `NOT` operators:

    condition="(Subject contains Invoice) AND (From contains @company.com)"

## Syncing Filters Across Multiple Machines

For different machines, copy the filter file via SSH:

``` bash
scp user@remote-machine:~/.thunderbird/[profile].default/Mail/Local\ Folders/msgFilterRules.dat ~/
```

Then import using the backup-and-copy method described earlier.

For multiple profiles on the same machine, replicate the symlink approach for each profile directory.

## Troubleshooting

If filters don’t appear after importing, check:

- The destination account folder exists
- Thunderbird was closed before copying files
- File permissions are readable by your user
- The folder paths in filter actions exist and are accessible

Restart Thunderbird after any manual changes to `msgFilterRules.dat`. The application caches filter rules in memory, so it won’t recognize direct file edits until restart.
