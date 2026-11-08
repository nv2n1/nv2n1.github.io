---
title: "Installing noip2 on Linux: A Setup Guide"
date: 2018-03-24 08:04:25 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-install-noip2-on-linux-2/
---

No-IP provides dynamic DNS service for systems that don’t have static IP addresses. The `noip2` client daemon monitors your system’s IP and automatically updates your No-IP domain when changes occur. Here’s how to set it up properly.

## Prerequisites

You’ll need:

- A No-IP account with at least one hostname configured
- Root or sudo access
- A Linux system with `systemd` or init.d support
- Basic familiarity with the command line

## Download and Compile noip2

Start by downloading the latest source from No-IP:

``` bash
cd /tmp
wget https://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
tar xzf noip-duc-linux.tar.gz
cd noip-2.1.9-1
```

Check the No-IP website for the latest version number, as the version may differ. Compile the source:

``` bash
make
sudo make install
```

The installer will prompt you for your No-IP credentials and configuration options. Keep track of the installation path—it typically installs to `/usr/local/bin/noip2`.

## Configuration

After installation, configure noip2 with your account details:

``` bash
sudo /usr/local/bin/noip2 -c /etc/noip2.conf
```

This interactive setup will ask for:

- Your No-IP username
- Your password
- Which hostnames to update
- Update interval (default is 30 minutes)
- Whether to run in the foreground or background

## Running as a Systemd Service

Modern Linux distributions use `systemd`. Create a service file:

``` bash
sudo nano /etc/systemd/system/noip2.service
```

Add the following:

``` ini
[Unit]
Description=No-IP Dynamic DNS Update Client
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/bin/noip2
ExecStop=/usr/local/bin/noip2 -k
Restart=on-failure
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

``` bash
sudo systemctl daemon-reload
sudo systemctl enable noip2
sudo systemctl start noip2
```

Verify it’s running:

``` bash
sudo systemctl status noip2
```

## Running as a Traditional Service (init.d)

For systems without `systemd`, create an init script:

``` bash
sudo nano /etc/init.d/noip2
```

``` bash
#!/bin/bash
### BEGIN INIT INFO
# Provides:          noip2
# Required-Start:    $network
# Required-Stop:     $network
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Description:       No-IP Dynamic DNS Update Client
### END INIT INFO

DAEMON=/usr/local/bin/noip2

case "$1" in
    start)
        echo "Starting noip2..."
        $DAEMON
        ;;
    stop)
        echo "Stopping noip2..."
        $DAEMON -k
        ;;
    restart)
        echo "Restarting noip2..."
        $DAEMON -k
        sleep 1
        $DAEMON
        ;;
    *)
        echo "Usage: $0 {start|stop|restart}"
        exit 1
        ;;
esac

exit 0
```

Make it executable and enable it:

``` bash
sudo chmod +x /etc/init.d/noip2
sudo update-rc.d noip2 defaults
sudo service noip2 start
```

## Cron-Based Approach (Alternative)

If you prefer not to run a daemon, use cron to periodically restart noip2. Add this to root’s crontab:

``` bash
sudo crontab -e
```

Add the line:

    0 */5 * * * /usr/local/bin/noip2 -k && sleep 2 && /usr/local/bin/noip2

This restarts noip2 every 5 minutes. The `-k` flag kills the existing process, then the daemon restarts. This approach is less elegant than a service but works reliably on older systems.

## Monitoring and Verification

Check if noip2 is running:

``` bash
ps aux | grep noip2
```

View the update history:

``` bash
sudo tail -f /var/log/noip2.log
```

On some systems, logs may be in `/var/run/noip2.log` or viewed via journalctl:

``` bash
sudo journalctl -u noip2 -f
```

## Troubleshooting

**Service won’t start**: Verify the configuration file exists and has correct permissions:

``` bash
sudo ls -la /etc/noip2.conf
```

**Authentication failures**: Confirm your No-IP username and password in the configuration. Regenerate the config:

``` bash
sudo /usr/local/bin/noip2 -c /etc/noip2.conf
```

**IP not updating**: Check your No-IP account for login anomalies. Some ISPs block port 8245. Test connectivity:

``` bash
curl -I https://updates.noip.com/
```

**Log file permissions**: Ensure noip2 can write to its log location. Check ownership and permissions if you encounter permission denied errors.

## Additional Options

Review all available flags:

``` bash
/usr/local/bin/noip2 -h
```

Common options:

- `-c`: Specify configuration file path
- `-k`: Kill running daemon
- `-d`: Run in foreground (useful for debugging)
- `-n`: Run once without exiting
- `-i`: Specify IP address manually

Using the systemd service approach is recommended for most modern distributions, as it integrates better with system logging and restart policies.
