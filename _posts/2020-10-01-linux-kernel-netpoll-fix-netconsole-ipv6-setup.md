---
title: "Fix netconsole IPv6 configuration in Linux kernel netpoll"
date: 2020-10-01 01:30:11 +0000
layout: post
canonical: https://www.systutorials.com/linux-kernel-netpoll-fix-netconsole-ipv6-setup/
---

The `netconsole` kernel module allows logging kernel messages over the network to a remote syslog server. A bug in the IPv6 configuration handling within the netpoll subsystem could cause incorrect addressing or kernel warnings when using IPv6 targets.

## The Bug

When configuring netconsole with an IPv6 target address, the netpoll subsystem didn’t properly validate or handle IPv6-specific parameters. This could result in:

- Kernel warnings about invalid network configurations
- Netconsole failing to initialize with IPv6 targets
- Incorrect source or destination IPv6 addresses in log packets
- Stack traces in dmesg referencing netpoll or netconsole functions

## Configuring Netconsole with IPv6

Netconsole sends kernel messages over UDP. For IPv6, the configuration syntax is:

```wp-block-code
# Load the netconsole module with IPv6 target
sudo modprobe netconsole \
    src_ip=2001:db8::1 \
    dst_ip=2001:db8::2 \
    dst_port=514 \
    dev_name=eth0
```

Or configure it at boot via kernel parameters:

```wp-block-code
netconsole=2001:db8::1/eth0,514,2001:db8::2,514
```

## The Fix

The patch corrects IPv6 address validation and handling in the netpoll configuration path. The key changes include:

```wp-block-code
/* Before fix (simplified) */
static int netpoll_parse_ip_addr(const char *str, struct in6_addr *addr)
{
    /* Only handled IPv4, IPv6 paths fell through without validation */
    return in4_pton(str, -1, (u8 *)addr, -1, NULL);
}

/* After fix */
static int netpoll_parse_ip_addr(const char *str, struct in6_addr *addr)
{
    if (strchr(str, ':')) {
        /* IPv6 address */
        return in6_pton(str, -1, (u8 *)addr, -1, NULL);
    } else {
        /* IPv4 address - map to IPv6-mapped IPv4 */
        return in4_pton(str, -1, (u8 *)addr, -1, NULL);
    }
}
```

## Setting Up a Remote Log Receiver

To receive netconsole messages on a remote machine:

```wp-block-code
# On the receiving server, listen for UDP syslog
sudo dnf install rsyslog     # Fedora/RHEL
sudo apt install rsyslog     # Ubuntu/Debian

# Enable UDP reception in /etc/rsyslog.conf
module(load="imudp")
input(type="imudp" port="514")

# Restart rsyslog
sudo systemctl restart rsyslog
```

Configure the firewall:

```wp-block-code
sudo firewall-cmd --permanent --add-port=514/udp
sudo firewall-cmd --reload
```

## Testing Netconsole

```wp-block-code
# On the sending machine, configure netconsole
sudo modprobe netconsole src_ip=192.168.1.10/eth0,6666,192.168.1.20,514

# Generate a test kernel message
echo "Test netconsole message" | sudo tee /dev/kmsg

# On the receiving machine, check for the message
sudo tail -f /var/log/messages | grep netconsole
```

## Netconsole for Kernel Debugging

Netconsole is especially valuable for debugging kernel panics and oops messages that don’t reach disk. Configure it early in boot:

```wp-block-code
# Add to kernel boot parameters in /etc/default/grub
GRUB_CMDLINE_LINUX="netconsole=192.168.1.10/eth0,6666,192.168.1.20,514"

# Rebuild GRUB
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

## Dynamic Netconsole Configuration

You can add and remove netconsole targets at runtime:

```wp-block-code
# Add a target dynamically
echo "192.168.1.10" > /sys/module/netconsole/parameters/ip
echo "514" > /sys/module/netconsole/parameters/port

# Or use the configfs interface (newer kernels)
mkdir /sys/kernel/config/netconsole/target1
cd /sys/kernel/config/netconsole/target1
echo "192.168.1.20" > remote_ip
echo "514" > remote_port
echo "eth0" > dev_name
echo 1 > enabled
```

## Verifying the Fix

Check your kernel version against the patch:

```wp-block-code
uname -r
# Check if the fix is applied
grep -r "netpoll_parse_ip\|netconsole_ipv6" /usr/src/linux/
```

Most modern distributions include this fix in their kernel updates. If you’re running an older kernel and experiencing netconsole IPv6 issues, upgrading to the latest stable kernel for your distribution should resolve them.

## Netconsole Security Considerations

Netconsole sends kernel messages in **plaintext** over UDP. There is no encryption or authentication. This means:

- Anyone on the same network segment can read your kernel logs
- Messages can be spoofed or intercepted
- Never use netconsole across untrusted networks without additional encryption (e.g., a VPN or SSH tunnel)

For secure remote logging, consider using `journalctl --remote` or `rsyslog` with TLS instead of netconsole. Netconsole is best suited for local network debugging scenarios where encryption isn’t required.

## Monitoring Netconsole Traffic

Capture and inspect netconsole packets:

```wp-block-code
# Capture netconsole traffic on the receiver
sudo tcpdump -i eth0 udp port 514 -A -s 0 | tee kernel-messages.log

# Filter for specific message levels
sudo tcpdump -i eth0 udp port 514 -A | grep -E 'emerg|alert|crit|err'
```

This is useful for verifying that netconsole messages are actually reaching the receiving server during troubleshooting.
