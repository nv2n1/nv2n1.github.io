---
title: "Controlling SCP Bandwidth with the -l Flag"
date: 2018-03-24 11:46:29 +0000
modified: 2026-04-12 08:38:55 +0000
author: "Eric Ma"
layout: post
categories: [programming-languages]
canonical: /how-to-limit-the-network-rate-used-by-scp-in-linux/
---

The `scp` command supports bandwidth limiting through the `-l` flag, which caps the transfer rate in Kbit/s. This prevents large file transfers from saturating your network connection.

## Basic Usage

The `-l` flag specifies the maximum bandwidth in kilobits per second (Kbit/s):

``` bash
# Limit to 1000 Kbit/s (approximately 125 KB/s)
scp -l 1000 largefile.tar.gz user@remote:/path/to/destination/

# Limit to 500 Kbit/s (approximately 62 KB/s)
scp -l 500 user@remote:/path/to/file ./
```

**Important:** The value is in **kilobits** (Kbit/s), not kilobytes (KB/s). To convert:

- 1000 Kbit/s = 125 KB/s
- 8000 Kbit/s = 1 MB/s
- 80000 Kbit/s = 10 MB/s

## Practical Examples

**Don’t saturate a shared office connection:**

``` bash
scp -l 4000 backup.tar.gz server:/backups/
```

This limits transfers to about 500 KB/s — enough for the transfer to complete while leaving bandwidth for other users.

**Transfer large files overnight without impacting daytime usage:**

``` bash
# Use with nohup for unattended transfers
nohup scp -l 2000 dataset.iso server:/data/ &
```

**Keep an interactive SSH session responsive during transfer:**

``` bash
scp -l 8000 bigfile user@host:/tmp/
```

## Limitations of scp -l

The `-l` flag has several limitations:

- **SFTP mode:** recent OpenSSH applies `-l` in SFTP mode too (the limit is enforced client-side); it does not affect rsync over ssh
- **Rough limiting:** The bandwidth cap is approximate, not precise
- **SCP protocol is deprecated:** OpenSSH has deprecated the SCP protocol in favor of SFTP since OpenSSH 9.0
- **No burst control:** Short transfers may exceed the limit before throttling kicks in

## Alternative: rsync with Bandwidth Limiting

`rsync` provides more precise bandwidth control and is generally preferred over SCP:

``` bash
# rsync uses KB/s (not Kbit/s like scp)
rsync -avz --progress --bwlimit=500 largefile user@remote:/path/

# --bwlimit=500 means 500 KB/s (compare to scp -l 4000 for similar speed)
rsync -avz --bwlimit=1000 --partial --progress ./data/ user@remote:/backup/data/
```

Advantages of rsync over scp:

- `--bwlimit` uses KB/s (more intuitive than Kbit/s)
- Resumable transfers with `--partial`
- Delta transfer — only sends changed portions of files
- Progress display with `--progress`
- Bandwidth shaping is more precise

## Alternative: trickle for Any Command

`trickle` is a userspace bandwidth shaper that works with any TCP application:

``` bash
sudo apt install trickle    # Ubuntu/Debian
sudo dnf install trickle    # Fedora

# Limit scp to 100 KB/s download, 100 KB/s upload
trickle -d 100 -u 100 scp file user@host:/path/

# Limit wget
trickle -d 200 wget http://example.com/largefile
```

Trickle works by intercepting socket calls, so it works with any program that uses TCP.

## Network-Level Bandwidth Control

For system-wide bandwidth management, use Linux traffic control:

``` bash
# Rate-limit outgoing SSH (port 22) to 1 Mbps
sudo tc qdisc add dev eth0 root handle 1: htb default 30
sudo tc class add dev eth0 parent 1: classid 1:10 htb rate 1mbit
sudo tc filter add dev eth0 protocol ip parent 1: prio 1 u32 match ip dport 22 0xffff flowid 1:10

# Remove the rule
sudo tc qdisc del dev eth0 root
```

This approach is useful when you want to limit all SSH transfers system-wide rather than per-command.

## Quick Reference

- `scp -l 1000` = ~125 KB/s (Kbit/s)
- `rsync --bwlimit=125` = ~125 KB/s (KB/s)
- `trickle -u 125 -d 125` = 125 KB/s each direction

For most use cases, `rsync --bwlimit` is the best choice — it’s more precise, supports resume, and uses a more intuitive unit (KB/s).
