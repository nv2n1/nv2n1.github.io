---
title: "Setting Date, Time, and Timezone in Linux"
date: 2013-07-12 16:32:10 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /linux-setting-date-time-and-timezone/
---

Understanding and managing system time is crucial for logging, cron jobs, SSL certificates, and system synchronization. Here’s how to handle it properly on modern Linux systems.

## Unix Time (POSIX Time)

Unix time represents seconds elapsed since 00:00:00 UTC on January 1, 1970, excluding leap seconds. Get the current Unix timestamp:

``` bash
$ date +%s
1735689600
```

This is useful for scripting, log analysis, and API interactions.

## Setting Date and Time

On modern systems, **use `timedatectl` from systemd** instead of the `date` command for permanent changes:

``` bash
$ timedatectl
               Local time: Wed 2025-01-01 14:30:45 UTC
           Universal time: Wed 2025-01-01 14:30:45 UTC
                 RTC time: Wed 2025-01-01 14:30:45
                Time zone: UTC (UTC, +0000)
```

Set the date and time using timedatectl:

``` bash
$ sudo timedatectl set-time '2025-06-22 11:28:00'
```

If your system still lacks systemd (unlikely in 2026, but possible in containers), use the `date` command:

``` bash
# date -s "22 JUN 2025 11:28:00"
```

Or with the `mmddhhmmyyyy.ss` format (month, day, hour, minute, year, second):

``` bash
# date 062211282025.00
```

## Setting Timezone

**Use `timedatectl` to manage timezones:**

List available timezones:

``` bash
$ timedatectl list-timezones
Africa/Abidjan
Africa/Accra
Africa/Addis_Ababa
...
Asia/Hong_Kong
...
```

Set your timezone:

``` bash
$ sudo timedatectl set-timezone Asia/Hong_Kong
```

Verify the change:

``` bash
$ timedatectl
               Local time: Wed 2025-01-01 22:30:45 HKT
           Universal time: Wed 2025-01-01 14:30:45 UTC
                 RTC time: Wed 2025-01-01 14:30:45
                Time zone: Asia/Hong_Kong (HKT, +0800)
```

### Manual Method (Legacy Systems)

If `timedatectl` isn’t available, manually manage `/etc/localtime`:

``` bash
$ sudo ln -sf /usr/share/zoneinfo/Asia/Hong_Kong /etc/localtime
$ date
```

The `/usr/share/zoneinfo` directory contains timezone data organized by region and city. Always verify your change with `date` or `timedatectl`.

## Hardware Clock Synchronization

The hardware clock (RTC) should be synchronized with system time, especially on machines that shut down frequently:

``` bash
$ sudo timedatectl set-local-rtc false  # Use UTC in hardware clock (recommended)
$ sudo hwclock --systohc                # Sync hardware clock to system time
```

Check hardware clock status:

``` bash
$ sudo hwclock --show
```

## NTP and Time Synchronization

Keep your system time accurate by running an NTP daemon. Most modern distros use `systemd-timesyncd` by default:

``` bash
$ timedatectl
               ...
       System clock synchronized: yes
systemd-timesyncd.service active: yes
                 RTC in local TZ: no
```

Check the NTP server being used:

``` bash
$ timedatectl show-timesync
```

For stricter requirements (databases, clusters), use full NTP servers:

``` bash
$ sudo apt install ntp          # Debian/Ubuntu
$ sudo dnf install ntp          # RHEL/Fedora/CentOS

$ sudo systemctl enable --now ntpd
$ ntpq -p                       # Check NTP peers
```

Or use Chrony (more accurate, faster sync):

``` bash
$ sudo apt install chrony
$ sudo systemctl enable --now chronyd
$ chronyc tracking
```

## Practical Examples

**Set timezone for a Docker container** (without changing the host):

``` bash
$ docker run -e TZ=Asia/Hong_Kong ubuntu date
```

**Convert Unix timestamp to human-readable format:**

``` bash
$ date -d @1735689600
Wed Jan  1 14:30:00 UTC 2025
```

**Check time difference between systems:**

``` bash
$ ssh user@remote-host date +%s
```

**Schedule a task with timezone awareness** (crontab uses system timezone):

``` bash
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
0 9 * * * /home/user/backup.sh  # Runs at 9 AM in system timezone
```

Ensure consistency across servers by keeping all machines synchronized to NTP and using UTC internally for applications, converting to local timezone only at the presentation layer.
