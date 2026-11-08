---
title: "Installing SSHFS on CentOS 7"
date: 2018-03-24 11:51:02 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-install-sshfs-on-centos-7/
---

SSHFS (SSH Filesystem) mounts a remote filesystem over SSH, letting you interact with remote files as if they were local. It uses SFTP under the hood, so no additional server configuration is needed beyond SSH access.

## Install SSHFS on CentOS 7

```wp-block-code
# Enable EPEL repository
sudo yum install epel-release

# Install sshfs
sudo yum install fuse-sshfs
```

## Basic Mount

```wp-block-code
# Mount a remote directory
sshfs user@remote-host:/path/to/remote /mnt/remote

# Mount with specific port
sshfs -p 2222 user@remote-host:/home/user /mnt/remote

# Mount as read-only
sshfs -o ro user@remote-host:/data /mnt/remote
```

## Unmount

```wp-block-code
# Unmount the filesystem
fusermount -u /mnt/remote

# Or use umount
umount /mnt/remote
```

## Mount at Boot with fstab

Add an entry to `/etc/fstab` for automatic mounting:

```wp-block-code
sshfs#user@remote-host:/path/to/remote  /mnt/remote  fuse  defaults,allow_other,reconnect,identityFile=/home/user/.ssh/id_rsa  0  0
```

Key fstab options:

- `allow_other` — Allow other users to access the mount
- `reconnect` — Automatically reconnect if the connection drops
- `identityFile` — Path to SSH private key for authentication
- `ServerAliveInterval=15` — Keep the connection alive
- `ServerAliveCountMax=3` — Number of keepalive failures before disconnect

## Performance Tuning

SSHFS performance depends on network latency and SSH overhead. Improve it with these options:

```wp-block-code
# Enable SSH compression (helpful on slow connections)
sshfs -C user@remote:/data /mnt/remote

# Increase cache size
sshfs -o cache=yes -o cache_timeout=60 -o cache_stat_timeout=60 user@remote:/data /mnt/remote

# Use a faster cipher
sshfs -o Cipher=aes128-gcm@openssh.com user@remote:/data /mnt/remote
```

## Troubleshooting Connection Drops

**Connection hangs after idle period:**

```wp-block-code
sshfs -o reconnect -o ServerAliveInterval=15 -o ServerAliveCountMax=3 user@remote:/data /mnt/remote
```

**Permission denied on mount:**

```wp-block-code
# Check that your user can write to the mount point
mkdir -p /mnt/remote
chmod 755 /mnt/remote

# For user-specific mounts, use a directory in your home
mkdir ~/remote
sshfs user@remote:/home/user ~/remote
```

**Transport endpoint not connected:**

```wp-block-code
# Force unmount and remount
fusermount -uz /mnt/remote
sshfs user@remote:/data /mnt/remote
```

## SSHFS vs NFS vs Samba

- **SSHFS** — Zero server config, encrypted, slower. Best for occasional remote access.
- **NFS** — Fastest, no encryption overhead. Best for trusted LAN environments.
- **Samba/SMB** — Good Windows compatibility, moderate speed. Best for mixed OS environments.

SSHFS is ideal when you need secure file access to a remote server without setting up NFS or Samba. Any server with SSH running is immediately accessible.

## Using SSH Keys for Passwordless Mounts

```wp-block-code
# Generate a key pair (if not already done)
ssh-keygen -t ed25519

# Copy the key to the remote server
ssh-copy-id user@remote-host

# Now mount without password prompt
sshfs user@remote-host:/home/user /mnt/remote
```

For fstab mounts, key-based authentication is essential since interactive password entry isn’t available during boot.

## Quick Reference

- `sshfs user@host:/remote /local` — Mount remote directory
- `fusermount -u /local` — Unmount
- `-o reconnect` — Auto-reconnect on disconnect
- `-C` — Enable compression
- `-o allow_other` — Allow other users to access

## SSHFS for Development Workflows

SSHFS works well for remote development. A common pattern is mounting a remote project directory and editing files locally:

```wp-block-code
# Mount remote project
mkdir -p ~/projects/myapp
sshfs -o reconnect,ServerAliveInterval=15 user@devserver:/opt/myapp ~/projects/myapp

# Edit files locally with your preferred IDE
code ~/projects/myapp

# Changes sync immediately to the remote server
```

For better performance with many small files (node_modules, .git), exclude them:

```wp-block-code
sshfs -o reconnect -o entry_timeout=60 -o attr_timeout=60 -o ac_timeout=60 user@remote:/project /mnt/project
```

However, SSHFS is not ideal for heavy I/O workloads like compilation or large git operations. For those, use SSH directly or set up a proper NFS share.

## Alternatives to SSHFS

**rclone mount** — Supports many cloud storage backends with FUSE:

```wp-block-code
rclone mount remote:bucket /mnt/cloud
```

**s3fs** — Mount S3-compatible buckets:

```wp-block-code
s3fs mybucket /mnt/s3 -o passwd_file=$HOME/.passwd-s3fs
```

**goofys** — High-performance S3 mounting optimized for speed.
