---
title: "Installing EncFS on CentOS 6"
date: 2018-03-24 11:51:35 +0000
modified: 2026-04-12 08:38:53 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-install-encfs-on-centos-6/
---

EncFS provides an encrypted filesystem in user space — files are encrypted on the fly and stored in an existing directory. It’s lighter than LUKS and doesn’t require root access or dedicated partitions. Here’s how to set it up on CentOS 6.

## Install EncFS

EncFS is available from the EPEL repository:

```wp-block-code
# Enable EPEL
sudo yum install epel-release

# Install EncFS
sudo yum install encfs
```

EncFS requires FUSE (Filesystem in Userspace), which should be installed as a dependency.

## Create an Encrypted Directory

```wp-block-code
# Create the encrypted storage and mount point
mkdir ~/.encrypted
mkdir ~/encrypted

# Initialize the encrypted filesystem
encfs ~/.encrypted ~/encrypted
```

On first run, EncFS asks configuration questions:

- **Security level:** Choose “p” for paranoid (AES-256, 4096-bit key) or “x” for expert mode
- **Password:** Set a strong encryption password — this cannot be recovered if lost

After setup, `~/encrypted` is your decrypted view. Any files placed here are automatically encrypted and stored in `~/.encrypted`.

## Mount and Unmount

```wp-block-code
# Mount the encrypted directory
encfs ~/.encrypted ~/encrypted

# Unmount when done
fusermount -u ~/encrypted
```

To mount automatically at login, add to your session startup scripts. You can also create a helper script:

```wp-block-code
#!/bin/bash
# ~/mount_encrypted.sh
encfs --extpass="cat ~/.encfs_password" ~/.encrypted ~/encrypted
```

**Note:** Storing the password in a file reduces security. Only use this if you understand the tradeoff.

## Configuration Options

EncFS stores its configuration in `~/.encrypted/.encfs6.xml`. Key settings:

- **Cipher:** AES (default) or Blowfish
- **Key size:** 192 or 256 bits
- **Block size:** 1024 bytes (default) or 4096 for better performance with large files
- **Name encoding:** Block or stream (block is default, stream is more secure but slower)
- **Filesystem block MAC:** Adds integrity checking with a per-block MAC header

## Performance Considerations

EncFS runs in userspace, so it’s slower than kernel-level encryption (LUKS). Expect:

- 10-30% overhead for sequential reads and writes
- Higher overhead for many small files due to per-file encryption setup
- Block MAC headers add 8 bytes per filesystem block, increasing storage requirements

For large files (video, archives), the overhead is minimal. For directories with thousands of small files, consider LUKS instead.

## Backup Considerations

To back up encrypted data:

```wp-block-code
# Back up the raw encrypted directory (don't need to mount)
tar -czf encrypted_backup.tar.gz ~/.encrypted/

# Or use rsync to a remote location
rsync -av ~/.encrypted/ user@backup-server:~/encrypted_backup/
```

The backup contains encrypted filenames and content — no plaintext is exposed. The `.encfs6.xml` configuration file must also be backed up separately, as you need both the password and the config to decrypt.

## EncFS vs Other Encryption Tools

**EncFS vs LUKS:**

- EncFS — no root needed, uses existing directory, slower, per-file encryption
- LUKS — needs root, dedicated partition/volume, faster, block-level encryption

**EncFS vs CryFS:**

- CryFS — similar concept but hides file sizes and directory structure better
- EncFS — more mature, faster, but leaks some metadata (file sizes, approximate names)

**EncFS vs gocryptfs:**

- gocryptfs — Go-based, actively maintained, better performance than EncFS
- EncFS — older, some known security weaknesses in default configuration

For new projects in 2026, gocryptfs or CryFS are generally recommended over EncFS due to active maintenance and stronger security defaults.
