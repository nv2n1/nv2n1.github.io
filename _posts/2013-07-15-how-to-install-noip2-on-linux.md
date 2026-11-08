---
title: "Installing and Configuring No-IP DynamicDNS on Linux"
date: 2013-07-15 12:48:58 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-install-noip2-on-linux/
---

The No-IP client automatically synchronizes your domain with your current public IP address. This is essential when hosting services on machines with DHCP-assigned IPs or when you need reliable DNS without paying for static IP assignments.

## Installation

### From Package Repositories

Most distributions package noip2 in their standard repos:

**Debian/Ubuntu:**

``` bash
sudo apt install noip2
```

**Fedora/RHEL/CentOS:**

``` bash
sudo dnf install noip2
```

**Arch Linux:**

``` bash
sudo pacman -S noip2
```

### Building from Source

If your distribution doesn’t package noip2, compile it directly:

``` bash
wget https://www.noip.com/client/linux/noip-duc-linux.tar.gz
tar xzf noip-duc-linux.tar.gz
cd noip-2.1.9-1/
sudo make install
```

The binary installs to `/usr/local/bin/noip2`. Some systemd unit files expect it at `/usr/bin/noip2`, so verify or create a symlink:

``` bash
sudo ln -s /usr/local/bin/noip2 /usr/bin/noip2
```

## Initial Configuration

Run the interactive setup:

``` bash
sudo noip2 -C
```

This prompts you for:

- No-IP account credentials (email and password)
- Which hostnames to update (you can select multiple)
- Update interval (30 minutes is standard; avoid intervals shorter than 15 minutes to prevent API rate-limiting)
- Whether to run as a daemon

Configuration is written to `/etc/no-ip2.conf`. Review it:

``` bash
sudo cat /etc/no-ip2.conf
```

## Running as a Systemd Service

Enable and start the service:

``` bash
sudo systemctl enable noip2
sudo systemctl start noip2
```

Check status and follow logs in real-time:

``` bash
sudo systemctl status noip2
sudo journalctl -u noip2 -n 50 -f
```

The `-f` flag streams logs, helpful for immediate troubleshooting.

## Running as a Non-Root User

If you want to avoid running a daemon as root, configure noip2 for a regular user account.

Edit `/etc/no-ip2.conf` and add:

    run_as_user=yourusername

Set permissions:

``` bash
sudo chown yourusername:yourusername /etc/no-ip2.conf
sudo chmod 600 /etc/no-ip2.conf
```

Create a user systemd service at `~/.config/systemd/user/noip2.service`:

``` ini
[Unit]
Description=No-IP Dynamic DNS Client
After=network-online.target
Wants=network-online.target

[Service]
Type=forking
ExecStart=/usr/bin/noip2 -c /etc/no-ip2.conf
Restart=on-failure
RestartSec=10

[Install]
WantedBy=default.target
```

Enable and start it for your user (no sudo):

``` bash
systemctl --user enable noip2
systemctl --user start noip2
```

## Cron-Based Updates (No Daemon)

If you prefer no long-running process, use cron instead. Add to your crontab:

``` bash
sudo crontab -e
```

Add this line:

``` bash
*/30 * * * * /usr/bin/noip2 -c /etc/no-ip2.conf
```

This updates every 30 minutes. Check syslog for activity:

``` bash
sudo grep noip2 /var/log/syslog
sudo tail -f /var/log/syslog | grep noip2
```

## Verification

Wait a few minutes after starting, then verify DNS resolution:

``` bash
dig yourdomain.ddns.net +short
nslookup yourdomain.ddns.net
```

Both should return your current public IP. Confirm your public IP independently:

``` bash
curl ifconfig.me
curl https://api.ipify.org
curl -s https://checkip.amazonaws.com
```

## Troubleshooting

**Service won’t start:**

``` bash
sudo systemctl status noip2
ls -l /usr/bin/noip2
sudo /usr/bin/noip2 -c /etc/no-ip2.conf
```

Running the binary directly shows immediate errors, whereas systemd logs may lag.

**Authentication failures:**

Review logs for “Invalid login” or “Permission denied”:

``` bash
sudo journalctl -u noip2 --since="30 minutes ago" -p err
```

Double-check credentials in `/etc/no-ip2.conf`.

**PID file permission errors (non-root user):**

When running as a non-root user, noip2 may fail to write to `/var/run/`. Override the PID location in `/etc/no-ip2.conf`:

    pid=/home/yourusername/.noip2.pid

**Rate-limiting warnings:**

The No-IP API allows one update per 30 minutes per hostname. If you see rate-limit errors, increase the update interval in `/etc/no-ip2.conf`:

    interval=30

Don’t set intervals shorter than 15 minutes unless you’re actually changing IPs that frequently.

**DNS not resolving after restart:**

Wait 2-5 minutes after restarting the service. The update may be queued. Force an immediate update:

``` bash
sudo systemctl stop noip2
sudo /usr/bin/noip2 -c /etc/no-ip2.conf
```

Then restart the service normally.

After any configuration changes, restart:

``` bash
sudo systemctl restart noip2
```
