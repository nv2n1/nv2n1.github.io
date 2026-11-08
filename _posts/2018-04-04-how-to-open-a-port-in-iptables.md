---
title: "Opening Ports with iptables: A Practical Guide"
date: 2018-04-04 02:22:34 +0000
modified: 2026-04-11 17:12:11 +0000
author: "Q A"
layout: post
categories: [databases-storage]
canonical: /how-to-open-a-port-in-iptables/
---

iptables remains the standard firewall interface across most Linux distributions, though it’s technically a compatibility layer over nftables. Whether you’re managing legacy systems or prefer the familiar syntax, here’s what you need to know.

## Basic Command to Open a Port

The fundamental syntax to allow inbound traffic on a specific port:

``` bash
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

Breaking this down:

- `-A INPUT` — append a rule to the INPUT chain
- `-p tcp` — match TCP protocol (use `udp` for UDP, or omit for both)
- `--dport 80` — match destination port 80
- `-j ACCEPT` — jump to ACCEPT target (allow the traffic)

## Common Port-Opening Scenarios

Allow HTTP traffic:

``` bash
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

Allow HTTPS traffic:

``` bash
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```

Allow SSH (test before saving to avoid locking yourself out):

``` bash
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

Allow a port range:

``` bash
sudo iptables -A INPUT -p tcp --dport 8000:8100 -j ACCEPT
```

Allow traffic from a specific source IP:

``` bash
sudo iptables -A INPUT -p tcp --dport 80 -s 192.168.1.100 -j ACCEPT
```

Allow traffic on all interfaces except one:

``` bash
sudo iptables -A INPUT -p tcp --dport 80 ! -i docker0 -j ACCEPT
```

Allow both TCP and UDP on the same port:

``` bash
sudo iptables -A INPUT -p tcp --dport 53 -j ACCEPT
sudo iptables -A INPUT -p udp --dport 53 -j ACCEPT
```

## Making Rules Persistent

iptables rules exist only in memory and flush on reboot. Choose the method that matches your distribution:

### Debian/Ubuntu with iptables-persistent

``` bash
sudo apt install iptables-persistent
sudo iptables-save > /etc/iptables/rules.v4
sudo netfilter-persistent save
```

### RHEL/CentOS/Fedora with iptables-services

``` bash
sudo dnf install iptables-services
sudo iptables-save > /etc/sysconfig/iptables
sudo systemctl enable iptables
sudo systemctl restart iptables
```

### Modern RHEL 8+/Fedora with firewalld

``` bash
sudo firewall-cmd --permanent --add-port=80/tcp
sudo firewall-cmd --reload
```

### Ubuntu 18.04+ with ufw

``` bash
sudo ufw allow 80/tcp
sudo ufw enable
```

## Viewing and Managing Rules

List all current rules:

``` bash
sudo iptables -L -n
```

List rules with line numbers:

``` bash
sudo iptables -L -n --line-numbers
```

Delete a specific rule by line number:

``` bash
sudo iptables -D INPUT 3
```

Delete a rule by specification:

``` bash
sudo iptables -D INPUT -p tcp --dport 80 -j ACCEPT
```

Show rule counts and packet statistics:

``` bash
sudo iptables -L -n -v
```

Flush all rules (dangerous on remote systems):

``` bash
sudo iptables -F
```

## Advanced Rule Management

Insert a rule at a specific position instead of appending:

``` bash
sudo iptables -I INPUT 1 -p tcp --dport 443 -j ACCEPT
```

This places the rule at position 1, pushing other rules down. Useful when you need a rule to take precedence.

Add rules with connection state tracking (more efficient):

``` bash
sudo iptables -A INPUT -p tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp --sport 80 -m state --state ESTABLISHED -j ACCEPT
```

Allow traffic from a subnet:

``` bash
sudo iptables -A INPUT -p tcp --dport 3306 -s 10.0.0.0/24 -j ACCEPT
```

Create a rule that logs before accepting:

``` bash
sudo iptables -A INPUT -p tcp --dport 22 -m limit --limit 5/min --limit-burst 10 -j LOG --log-prefix "SSH_ATTEMPT: "
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

## Modern Alternatives

For new systems or if you have flexibility:

**firewalld** offers a user-friendly zone-based system and is standard on RHEL 8+, CentOS 8+, and recent Fedora versions. Rules are persistent by default and can be modified without reloading:

``` bash
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --reload
```

**ufw** is simpler and recommended for Ubuntu/Debian systems. Install with `apt install ufw`, then enable and manage rules through straightforward commands:

``` bash
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw enable
```

**nftables** is the kernel successor to iptables, offering better performance and cleaner syntax. Most systems still ship iptables compatibility, but nftables is becoming the default:

``` bash
sudo nft add rule inet filter input tcp dport 80 accept
sudo nft list ruleset
```

## Important Considerations

Order matters — iptables processes rules top-to-bottom. A REJECT rule placed early will block traffic before a later ACCEPT rule sees it.

Always test SSH rules on remote systems before saving. Open the port, verify connectivity, then persist the rules. If you lock yourself out, console access or out-of-band management is your only option.

Use `--dport` for destination port (incoming traffic) and `--sport` for source port (less common, used for outbound filtering).

Combine `-A` to append rules or `-I` to insert at a specific line number. Use `-R` to replace an existing rule.

Check your distribution’s default policy. If INPUT is set to DROP, you need explicit ACCEPT rules. If it’s set to ACCEPT, you need explicit DROP/REJECT rules to restrict traffic.

For production systems, consider whether firewalld or ufw better matches your workflow. iptables is powerful but less forgiving than zone-based firewalls.
