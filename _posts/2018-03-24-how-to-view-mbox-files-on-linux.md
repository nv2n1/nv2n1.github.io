---
title: "Reading and Managing .mbox Files in Linux"
date: 2018-03-24 11:43:10 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-view-mbox-files-on-linux/
---

The `.mbox` format stores email messages as plain text in a single file, with each message separated by a “From ” line. If you have archived emails or need to work with mailbox exports, here are the practical ways to read and manipulate them on Linux.

## Using Thunderbird

Thunderbird remains a solid option for viewing `.mbox` files with a graphical interface. Drop your `.mbox` file into Thunderbird’s Local Folders directory and restart the application — it will automatically index the messages and display them.

Find your Local Folders path in Thunderbird by opening **Edit → Preferences → Files and Folders** and looking for the Local Folders location. On Linux, it’s typically:

    ~/.thunderbird/<profile-id>/Mail/Local Folders

The profile ID is a random string like `3d1ss5n8.default`. You can also check `~/.thunderbird/profiles.ini` to find all your profile paths.

Once you’ve copied the `.mbox` file there, restart Thunderbird and you’ll see a new folder with your messages.

## Command-line Tools

For headless systems or automation, command-line tools are more efficient.

### Using formail (from procmail)

The `formail` utility splits `.mbox` files into individual messages:

``` bash
formail -ds sh -c 'cat > message_$$.txt' < myfile.mbox
```

This creates separate files for each email. Install it via `procmail` package on most distributions.

### Using mbox2maildir

Convert `.mbox` to the more modern Maildir format with `mb2md`:

``` bash
mb2md -s myfile.mbox -d ./output_maildir
```

This creates a directory structure that’s easier to query and manage. Install with:

``` bash
apt install mb2md  # Debian/Ubuntu
pacman -S mb2md    # Arch
```

### Viewing with grep and sed

For quick inspection without specialized tools:

``` bash
# Count total messages
grep -c "^From " myfile.mbox

# Extract Subject lines
grep "^Subject: " myfile.mbox

# Extract a specific message by sender
grep -A 100 "^From: john@example.com" myfile.mbox | head -n 50
```

The `^From` pattern (with space) marks message boundaries. Each email starts with this line.

## Using Mutt or NeoMutt

These terminal email clients can read `.mbox` files directly:

``` bash
mutt -f myfile.mbox
```

This opens the mailbox in an interactive interface where you can browse, search, and extract messages. NeoMutt (a maintained fork) works the same way and is available in most package repositories.

## Python for Programmatic Access

For automation or parsing, Python’s `mailbox` module is reliable:

``` python
import mailbox

mbox = mailbox.mbox('myfile.mbox')
for i, message in enumerate(mbox):
    print(f"Message {i}: {message['Subject']} from {message['From']}")
```

Install the `secure-smtplib` package if you need better MIME handling:

``` bash
pip install secure-smtplib
```

## Converting to Other Formats

To convert `.mbox` to `.eml` (individual message files):

``` bash
formail -ds sh -c 'cat > "message_$$.eml"' < myfile.mbox
```

Or to `.maildir` format for better indexing:

``` bash
mbsync -C /dev/null -c - <<EOF | mbsync -c /dev/stdin
IMAPAccount local
Host localhost
User $(whoami)
Pass ""
IMAPStore localstore
Account local
Channel local
Master :local:
Slave ./maildir
Create Slave
Sync All
EOF
```

For most users, `mb2md` is simpler for this conversion.

## Checking File Integrity

Large `.mbox` files can become corrupted. Verify structure:

``` bash
# Count expected message boundaries
wc -l myfile.mbox
grep "^From " myfile.mbox | wc -l

# Look for malformed lines
grep -v "^From " myfile.mbox | grep -v "^$" | head -20
```

If counts are far off, the file may have line breaks inside message bodies that need repair.
