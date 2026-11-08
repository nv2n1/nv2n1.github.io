---
title: "Improving SSH Performance with Faster Ciphers"
date: 2014-04-24 13:39:43 +0000
modified: 2026-04-11 16:22:43 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /improving-sshscp-performance-by-choosing-ciphers/
---

SSH performance is constrained by cipher choice, especially for large file transfers over high-bandwidth links where CPU becomes the bottleneck. Selecting the right cipher, key exchange algorithm, and compression settings can yield substantial throughput improvements.

## Current Cipher Landscape

Modern OpenSSH (7.4+) has deprecated or removed weak ciphers. Here’s what’s viable today:

**Secure and performant:**

- `chacha20-poly1305@openssh.com` — Best choice for most workloads. Software-based, no hardware dependency, ~400-600 MB/s on modern CPUs.
- `aes256-gcm@openssh.com` / `aes128-gcm@openssh.com` — Hardware-accelerated via AES-NI when available, ~300-500 MB/s.
- `aes256-ctr` / `aes128-ctr` — Fallback for systems without AES-NI support, slower but universally compatible.

**Avoid entirely:**

- `arcfour`, `rc4` — Cryptographically broken; removed from OpenSSH 7.4+.
- `blowfish-cbc` — 64-bit block size, practical security weaknesses.
- `3des` — Obsolete, too slow.

## Check Your Hardware

Before configuring, verify AES-NI support on your CPU:

``` bash
grep aes /proc/cpuinfo
```

If `aes` appears in the output, your CPU supports AES-NI, making GCM ciphers fast. On systems without it, chacha20-poly1305 or AES-CTR are better choices.

## Client Configuration

Edit `~/.ssh/config`:

    Host *
        Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr
        KexAlgorithms curve25519-sha256,curve25519-sha256@libssh.org,diffie-hellman-group16-sha512
        HostKeyAlgorithms ecdsa-sha2-nistp256,rsa-sha2-512,rsa-sha2-256
        Compression no

Modern key exchange and host key algorithms are equally important. Avoid `diffie-hellman-group1`, `group14`, and legacy RSA signatures.

## Server Configuration

Edit `/etc/ssh/sshd_config`:

    Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com,aes128-gcm@openssh.com,aes256-ctr
    KexAlgorithms curve25519-sha256,curve25519-sha256@libssh.org,diffie-hellman-group16-sha512
    HostKeyAlgorithms ecdsa-sha2-nistp256,rsa-sha2-512,rsa-sha2-256
    Compression no

Then reload SSH:

``` bash
sudo systemctl reload sshd
```

Verify the reload succeeds without breaking existing connections:

``` bash
sshd -t && sudo systemctl reload sshd
```

## Compression Tuning

Compression helps on slow WAN links but wastes CPU on fast LANs. General rules:

- **Disable for LAN/datacenter transfers** — Disk and network I/O will be the bottleneck, not encryption.
- **Enable selectively for slow links** — Useful for high-latency or bandwidth-constrained connections.

If enabling compression, set `CompressionLevel 6` for a reasonable compression-ratio-to-CPU tradeoff. Levels 7-9 add diminishing returns in compression with significant CPU cost.

Host-specific tuning in `~/.ssh/config`:

    # Fast local cluster
    Host 10.0.*
        Compression no
        Ciphers chacha20-poly1305@openssh.com,aes256-gcm@openssh.com

    # Slow remote link
    Host slow-remote.example.com
        Compression yes
        CompressionLevel 6

## Verify Cipher Negotiation

Check what cipher is actually negotiated:

``` bash
ssh -v user@host 2>&1 | grep "encrypt ciphers:"
```

Output should show:

    debug1: kex: encrypt ciphers: chacha20-poly1305@openssh.com

If an older cipher appears, check that neither client nor server config is forcing a legacy cipher, and that both have compatible algorithm lists.

## Benchmark Your Setup

Test real-world performance with a large file:

``` bash
# Compression disabled
time scp largefile.bin user@host:/tmp/

# With rsync (allows resume and skipping unchanged files)
time rsync -avz --stats largefile.bin user@host:/tmp/

# SSH with verbose timing
ssh user@host "dd if=/dev/zero bs=1M count=1000" | md5sum
```

On modern hardware with chacha20-poly1305 or AES-GCM, expect 300+ MB/s over gigabit links. Disk I/O, not encryption, typically becomes the limiting factor.

## Common Pitfalls

**Mismatched client and server ciphers** — If the server doesn’t list a cipher the client prefers, SSH falls back to the next compatible option. Always ensure both sides have overlapping algorithm lists.

**Compression enabled by default for all hosts** — Legacy configurations sometimes enable global compression. Disable it and enable only where needed.

**Using RSA key exchange** — Older systems may default to `diffie-hellman-group14-sha1` or worse. Explicitly set `KexAlgorithms` to enforce modern alternatives.

**ED25519 host keys** — Faster and stronger than RSA for authentication. If your system supports it (OpenSSH 6.3+), consider switching:

``` bash
sudo ssh-keygen -A
```

This generates ED25519 and other key types. Ensure `HostKeyAlgorithms` includes `ssh-ed25519` if available.

## Summary

Start with `chacha20-poly1305@openssh.com` as your primary cipher paired with modern key exchange algorithms. Disable compression globally and enable it only for high-latency links. Test in your environment—network conditions, hardware capabilities, and file sizes all affect real-world throughput. On current hardware, you should easily saturate gigabit links with encryption overhead below 10%.
