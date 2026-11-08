---
title: "Optimizing SSH and SCP Performance on Linux"
date: 2018-03-24 08:22:31 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-improve-ssh-scp-performance-on-linux/
---

SSH is fast enough for most tasks, but when you’re transferring large files, running multiple commands, or managing hundreds of servers, every millisecond counts. Here’s how to squeeze real performance gains from SSH and SCP on Linux.

## Choose the Right Cipher

Cipher selection has the biggest impact on throughput. Modern CPUs have AES-NI hardware acceleration, making AES-based ciphers both secure and fast. Avoid older, slower algorithms like 3DES or arcfour.

Check available ciphers with:

``` bash
ssh -Q cipher localhost
```

Benchmark actual throughput between two hosts:

``` bash
# Host A (receiver)
iperf3 -s

# Host B (sender) - test specific cipher
ssh -c aes128-ctr user@hostA iperf3 -c hostA -t 10
```

Recommended ciphers in order of speed:

- **aes128-ctr** — fastest, hardware-accelerated, ideal for most cases
- **aes256-ctr** — still fast with AES-NI, better security margin
- **chacha20-poly1305@openssh.com** — excellent for systems without AES-NI, competitive with AES on modern CPUs

Configure in `~/.ssh/config`:

    Host *
        Ciphers aes128-ctr,aes256-ctr,chacha20-poly1305@openssh.com

## Optimize Key Exchange and Authentication

Key exchange happens at connection start and adds latency. Use modern algorithms:

    Host *
        KexAlgorithms curve25519-sha256,diffie-hellman-group16-sha512,diffie-hellman-group-exchange-sha256
        HostKeyAlgorithms ssh-ed25519,ecdsa-sha2-nistp256
        PubkeyAcceptedAlgorithms ssh-ed25519,ecdsa-sha2-nistp256

Use ed25519 keys instead of RSA for faster operations and smaller key material:

``` bash
ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519 -N ""
```

If you have older RSA keys, consider migrating to ed25519. Ed25519 is faster to verify and has been the OpenSSH default for new keys since 8.6 (2021).

## Enable Connection Multiplexing

Multiplexing reuses a single TCP connection for multiple SSH sessions, eliminating reconnection overhead. This is especially valuable when running many commands or frequent scp transfers:

    Host *
        ControlMaster auto
        ControlPath ~/.ssh/sockets/%h-%p-%r
        ControlPersist 600

Create the socket directory:

``` bash
mkdir -p ~/.ssh/sockets
chmod 700 ~/.ssh/sockets
```

Now running `ssh user@host` multiple times uses the same connection. Check active connections:

``` bash
ssh -O check user@host
```

Close multiplexed connections when done:

``` bash
ssh -O exit user@host
```

This can reduce latency from ~100ms per connection to ~5ms on subsequent sessions.

## Compression: When to Use It

SSH compression (`Compression yes`) reduces bandwidth but increases CPU usage. Only enable it for slow or high-latency links (satellite, intercontinental):

    Host slow-remote
        Compression yes
        CompressionLevel 6

For LAN transfers or modern broadband connections, compression typically hurts performance. Modern compression algorithms like zstandard (if your OpenSSH supports it) are more efficient than the legacy deflate, but avoid compression for local networks.

## Replace SCP with Faster Alternatives

SCP is single-threaded and outdated. Use rsync over SSH for large transfers:

``` bash
rsync -avz --delete -e "ssh -c aes128-ctr" user@host:/remote /local
```

For resuming interrupted transfers:

``` bash
rsync -avz --partial --progress -e ssh user@host:/remote/large.file /local
```

For parallel transfers of many files, use native SFTP batch mode:

``` bash
sftp -b batch.txt user@host
```

Or use modern alternatives like **rclone** or **restic** for large-scale data transfer with built-in parallelism and better error handling.

## Increase SSH Buffers

Larger buffers allow SSH to handle network bursts without blocking:

    Host *
        SendBuffer 262144
        ReceiveBuffer 262144

These are client-side settings. On the server side, edit `/etc/ssh/sshd_config`:

    SendBuffer 262144
    ReceiveBuffer 262144

Reload with `sudo systemctl reload sshd`.

## Tune TCP Window Scaling

At the OS level, enable TCP window scaling and increase buffer sizes:

``` bash
sudo sysctl -w net.ipv4.tcp_window_scaling=1
sudo sysctl -w net.core.rmem_max=134217728
sudo sysctl -w net.core.wmem_max=134217728
sudo sysctl -w net.ipv4.tcp_rmem="4096 87380 134217728"
sudo sysctl -w net.ipv4.tcp_wmem="4096 65536 134217728"
```

Persist these changes in `/etc/sysctl.d/99-ssh-tuning.conf`:

    net.ipv4.tcp_window_scaling=1
    net.core.rmem_max=134217728
    net.core.wmem_max=134217728
    net.ipv4.tcp_rmem=4096 87380 134217728
    net.ipv4.tcp_wmem=4096 65536 134217728

Apply with `sudo sysctl -p /etc/sysctl.d/99-ssh-tuning.conf`.

## Verify and Debug Configuration

View which algorithms are actually in use:

``` bash
ssh -G user@host | grep -E "cipher|kexalgorithm|hostkey"
```

Enable verbose output to see negotiation details:

``` bash
ssh -vv user@host
```

This shows which algorithms were selected from your preference list, helpful for diagnosing compatibility issues.

## Complete Optimized Config

Here’s a production-ready `~/.ssh/config` combining all tuning:

    Host *
        # Fast algorithms
        Ciphers aes128-ctr,aes256-ctr,chacha20-poly1305@openssh.com
        KexAlgorithms curve25519-sha256,diffie-hellman-group16-sha512,diffie-hellman-group-exchange-sha256
        HostKeyAlgorithms ssh-ed25519,ecdsa-sha2-nistp256
        PubkeyAcceptedAlgorithms ssh-ed25519,ecdsa-sha2-nistp256

        # Connection reuse
        ControlMaster auto
        ControlPath ~/.ssh/sockets/%h-%p-%r
        ControlPersist 600

        # Buffers
        SendBuffer 262144
        ReceiveBuffer 262144

## Expected Results

With these changes, expect 20–40% faster file transfers and noticeably lower latency for interactive sessions. Connection multiplexing alone provides dramatic improvements when running multiple commands.

Test changes on non-production hosts first. Some legacy servers may not support newer key exchange algorithms or ciphers; your client will fall back to secondary options in your list.
