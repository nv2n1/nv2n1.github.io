---
title: "Rate-Limiting SSH Connections with iptables and firewalld"
date: 2018-03-24 11:44:52 +0000
author: "Eric Ma"
layout: post
categories: [scripting-utilities]
canonical: /how-to-use-iptables-to-limit-rates-new-ssh-incoming-connections-from-each-ip-on-linux/
---

Rate-limiting SSH brute-force attempts is essential for any server exposed to the internet. Using iptables with the `recent` module, you can drop connections from IPs that exceed a threshold in a given time window—for example, blocking IPs that attempt more than 6 connections in 60 seconds.

## Using iptables

The `recent` module tracks connection attempts by source IP and allows you to set thresholds. Here’s a practical ruleset:

``` bash
for tables in iptables ip6tables ; do
    # Allow established inbound connections
    $tables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT
    # Drop if 6+ new connections in 60 seconds
    $tables -A INPUT -p tcp --dport 22 -m recent --update --seconds 60 --hitcount 6 --name SSH --rsource -j DROP
    # Record and allow new connections
    $tables -A INPUT -p tcp --dport 22 -m recent --set --name SSH --rsource -j ACCEPT
    # Reject other connections
    $tables -A INPUT -j REJECT
    $tables -A FORWARD -j REJECT
done
```

**How it works:**

1.  The first rule allows traffic for established connections, so legitimate users won’t be affected mid-session.
2.  The second rule drops packets from IPs that have hit the threshold (6 connections within 60 seconds). The `--rsource` flag tracks by source IP only (ignoring destination ports).
3.  The third rule records each new SSH connection attempt and allows it through—this is how the `recent` module counts attempts.
4.  The final rules reject everything else.

The `recent` module maintains state in `/proc/net/xt_recent/SSH` on most systems. You can check active entries:

``` bash
cat /proc/net/xt_recent/SSH
```

To clear the list manually (useful for testing or unblocking IPs):

``` bash
echo / > /proc/net/xt_recent/SSH
```

## Adjusting the threshold

Change the `--hitcount` and `--seconds` values to match your needs:

``` bash
# Allow 10 attempts per 120 seconds
$tables -A INPUT -p tcp --dport 22 -m recent --update --seconds 120 --hitcount 10 --name SSH --rsource -j DROP
```

## Using firewalld

If you’re running firewalld, add equivalent rules via direct rules:

``` bash
firewall-cmd --permanent --direct --add-rule ipv4 filter INPUT_direct 0 -p tcp --dport 22 -m state --state NEW -m recent --set
firewall-cmd --permanent --direct --add-rule ipv4 filter INPUT_direct 1 -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 6 -j REJECT --reject-with tcp-reset
firewall-cmd --reload
```

For IPv6, replace `ipv4` with `ipv6`:

``` bash
firewall-cmd --permanent --direct --add-rule ipv6 filter INPUT_direct 0 -p tcp --dport 22 -m state --state NEW -m recent --set
firewall-cmd --permanent --direct --add-rule ipv6 filter INPUT_direct 1 -p tcp --dport 22 -m state --state NEW -m recent --update --seconds 60 --hitcount 6 -j REJECT --reject-with tcp-reset
firewall-cmd --reload
```

The rule numbers (0, 1) determine execution order—lower numbers run first.

## Important considerations

**Stateful inspection:** The `--state NEW` flag (in firewalld rules) or implicit state tracking (in iptables) ensures only new connection attempts are counted, not established traffic.

**Whitelist trusted IPs:** If you have administrators or CI/CD systems connecting frequently, whitelist them before rate-limit rules:

``` bash
iptables -A INPUT -p tcp --dport 22 -s 203.0.113.50 -j ACCEPT
```

**Monitor for false positives:** Legitimate users behind NAT or proxies share IPs. A 6-per-60-second limit is reasonable for most deployments, but adjust based on your traffic patterns.

**Combine with other defenses:** Rate-limiting works best alongside SSH key authentication (disable password auth), non-standard ports, and tools like `fail2ban` or `sshguard` for adaptive blocking.

**Persistence:** These rules won’t survive reboot. Use `iptables-save` / `iptables-restore` or a persistence tool like `iptables-persistent` (Debian/Ubuntu) to make changes permanent.
