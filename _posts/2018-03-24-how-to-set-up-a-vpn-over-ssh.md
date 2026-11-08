---
title: "VPN Over SSH: Using sshuttle and Alternatives"
date: 2018-03-24 11:41:26 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-set-up-a-vpn-over-ssh/
---

SSH tunneling and port forwarding work well for specific traffic, but they don’t give you a full VPN-like experience where all system traffic routes through the remote server. If you need transparent, system-wide traffic redirection over SSH, you have several solid options depending on your platform.

## sshuttle on Linux and macOS

sshuttle is the standard tool for Linux and macOS users. It creates a transparent proxy over SSH without requiring administrative access on the remote server or VPN software installation—just standard SSH access.

### Installation

On Ubuntu/Debian:

``` bash
sudo apt-get install sshuttle
```

On macOS with Homebrew:

``` bash
brew install sshuttle
```

On Fedora/RHEL:

``` bash
sudo dnf install sshuttle
```

On other distributions, install via pip:

``` bash
pip install sshuttle
```

### Basic usage

Route all traffic through your SSH server:

``` bash
sshuttle -r username@remotehost 0/0
```

The `0/0` means “all IPv4 traffic.” To include IPv6:

``` bash
sshuttle -r username@remotehost 0/0 ::/0
```

sshuttle will prompt for your SSH password (or use your SSH key automatically if configured). Once connected, your system routes all traffic through the remote host. Press Ctrl+C to disconnect.

### Selective routing

Often you don’t want everything tunneled—just specific subnets. To route only traffic destined for `10.0.0.0/8`:

``` bash
sshuttle -r username@remotehost 10.0.0.0/8
```

Multiple subnets:

``` bash
sshuttle -r username@remotehost 10.0.0.0/8 192.168.1.0/24 172.16.0.0/12
```

This is particularly useful for accessing internal corporate networks while keeping your ISP from seeing that traffic.

### Excluding traffic

Use `-x` to exclude certain IPs or subnets from the tunnel:

``` bash
sshuttle -r username@remotehost 0/0 -x 192.168.1.0/24 -x 127.0.0.1
```

This routes all traffic through the tunnel except your local network and localhost. Essential if you need local printer or NAS access while tunneled.

### Running in the background

Use `-D` to daemonize sshuttle:

``` bash
sshuttle -D -r username@remotehost 0/0
```

Stop it with:

``` bash
sshuttle --stop
```

Check active tunnels:

``` bash
ps aux | grep sshuttle
```

### Using a specific SSH key

``` bash
sshuttle -D -r username@remotehost 0/0 -e "ssh -i /path/to/key"
```

With SSH config, you can also create an alias:

``` bash
# In ~/.ssh/config
Host vpn-server
    HostName remotehost
    User username
    IdentityFile ~/.ssh/vpn_key
```

Then simply:

``` bash
sshuttle -D -r vpn-server 0/0
```

### Advanced options

Enable verbose logging to debug connection issues:

``` bash
sshuttle -r username@remotehost 0/0 -vvv
```

Change the DNS server used while tunneled:

``` bash
sshuttle -r username@remotehost 0/0 --dns
```

This forces DNS queries through the remote server, preventing DNS leaks.

Disable latency compensation (useful for testing):

``` bash
sshuttle -r username@remotehost 0/0 --no-latency-control
```

## Performance and latency considerations

sshuttle uses Python to manage routing and can add 5–20ms latency compared to native VPN software, depending on your network and the remote server’s capacity. For bandwidth-intensive work or real-time gaming, consider dedicated VPN solutions. For general browsing, accessing remote internal networks, and moderate file transfers, sshuttle performs well.

Monitor your tunnel with:

``` bash
watch -n 1 'netstat -an | grep ESTABLISHED | wc -l'
```

## Windows alternatives

Windows doesn’t have a native sshuttle equivalent, but several approaches work:

**OpenSSH with manual routing:**

Windows 10+ includes OpenSSH. You can create SSH tunnels and configure Windows routing with `netsh` commands, but this requires careful setup and isn’t as seamless as sshuttle.

``` bash
ssh -D 1080 username@remotehost
```

Then configure SOCKS5 proxy in applications or use tools like Proxifier.

**sshuttle in WSL2:**

Running sshuttle in Windows Subsystem for Linux 2 can work, but routing Windows traffic through the WSL2 tunnel requires additional configuration and isn’t straightforward.

**WireGuard over SSH:**

WireGuard is modern and fast. Some users tunnel WireGuard over SSH for additional obfuscation, though this adds complexity and overhead.

**Bitvise SSH Client:**

Third-party clients like Bitvise include SOCKS proxy support, which you can combine with a system-wide proxy tool. Less transparent than sshuttle but functional for browser traffic.

## How sshuttle differs from traditional VPN

- **No remote privileges needed:** sshuttle doesn’t require the remote server to run VPN software or have special access
- **Transparent filtering:** Traffic is redirected at the kernel level using `iptables` (Linux) or `pfctl` (macOS)
- **Python-based overhead:** Not as performant as compiled VPN solutions, but sufficient for most workloads
- **SSH authentication:** You authenticate via SSH keys or passwords, not separate VPN credentials
- **DNS handling:** sshuttle prevents DNS leaks by default when using `--dns`

## Security considerations

**SSH hardening:**

Ensure your SSH connection uses key authentication exclusively:

``` bash
# On remote server, disable password auth
PasswordAuthentication no
PubkeyAuthentication yes
```

Generate a dedicated SSH key for sshuttle:

``` bash
ssh-keygen -t ed25519 -f ~/.ssh/sshuttle_key -N "" -C "sshuttle"
ssh-copy-id -i ~/.ssh/sshuttle_key username@remotehost
```

**Traffic visibility:**

sshuttle’s traffic is encrypted end-to-end by SSH itself. However, the remote server sees all your traffic—only use servers you trust. If you’re relying on anonymity, verify the server operator’s privacy policy.

**Verify DNS leaks:**

Test with:

``` bash
curl https://dns.google/resolve?name=example.com
```

Check that the query resolves through your remote server, not your ISP.

## Testing your setup

Before routing critical traffic:

``` bash
# Verify basic connectivity
ping 8.8.8.8

# Check routing path
traceroute google.com

# Verify your public IP changed
curl icanhazip.com

# Measure throughput
iperf3 -c remotehost

# Check DNS resolution
dig google.com @8.8.8.8
```

## When to use sshuttle

- Accessing internal corporate networks from outside the office
- Securing traffic on untrusted WiFi networks
- Bypassing geographic restrictions for general browsing
- Quick VPN setup without installing additional software

For high-bandwidth streaming, real-time applications, or where latency is critical, dedicated VPN software remains superior.
