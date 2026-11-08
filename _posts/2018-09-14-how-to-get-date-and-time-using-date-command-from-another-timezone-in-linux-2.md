---
title: "Display Date and Time Across Multiple Timezones on Linux"
date: 2018-09-14 09:29:53 +0000
layout: post
canonical: https://www.systutorials.com/how-to-get-date-and-time-using-date-command-from-another-timezone-in-linux-2/
---

The simplest way to display the date and time in a different timezone is with the TZ environment variable:

``` bash
TZ='America/New_York' date
```

This temporarily sets the timezone for that single command execution without affecting your system settings. The change applies only to that invocation.

Chain multiple timezone checks easily:

``` bash
TZ='America/New_York' date
TZ='Europe/London' date
TZ='Asia/Tokyo' date
```

## Custom Format Strings with Timezones

Combine TZ with custom format strings for logs, scripts, or API integration:

``` bash
TZ='Asia/Shanghai' date +"%Y-%m-%d %H:%M:%S"
TZ='Europe/Berlin' date +"%A, %B %d, %Y at %H:%M:%S %Z"
TZ='UTC' date +"%Y-%m-%dT%H:%M:%SZ"
```

Common format specifiers:

- `%Y`: 4-digit year
- `%m`: 2-digit month (01-12)
- `%d`: 2-digit day of month
- `%H`: Hour (00-23)
- `%M`: Minute (00-59)
- `%S`: Second (00-59)
- `%Z`: Timezone abbreviation (e.g., EST, IST)
- `%z`: UTC offset as ±HHMM (e.g., -0500, +0530)
- `%a`: Abbreviated weekday name
- `%A`: Full weekday name

Format specifiers work identically regardless of timezone.

## ISO 8601 Output (Recommended for Logs and APIs)

Modern date implementations support ISO 8601 formatting natively, which is essential for logs, APIs, and databases:

``` bash
TZ='America/Los_Angeles' date -Iseconds
```

Output: `2026-03-15T14:30:45-07:00`

The `-I` flag accepts precision levels:

- `-Idate`: `2026-03-15`
- `-Iminutes`: `2026-03-15T14:30-07:00`
- `-Iseconds`: `2026-03-15T14:30:45-07:00`
- `-Inanoseconds`: Full nanosecond precision

This is preferred over custom format strings for machine-readable output because it includes the timezone offset automatically and avoids ambiguity.

## Finding and Validating Timezone Names

List available timezones on your system:

``` bash
timedatectl list-timezones
```

Or browse the timezone database directly:

``` bash
ls /usr/share/zoneinfo/
```

Timezone names follow the `Region/City` pattern. Explore by region:

``` bash
ls /usr/share/zoneinfo/America/
ls /usr/share/zoneinfo/Europe/
ls /usr/share/zoneinfo/Asia/
```

Validate a timezone before using it in scripts:

``` bash
TZ='Australia/Sydney' date && echo "Valid timezone" || echo "Invalid timezone"
```

## Using TZ in Bash Scripts

Set TZ for individual commands within a script:

``` bash
#!/bin/bash

echo "Sydney time: $(TZ='Australia/Sydney' date +"%Y-%m-%d %H:%M:%S")"
echo "UTC time: $(TZ='UTC' date -Iseconds)"
echo "New York time: $(TZ='America/New_York' date -Iseconds)"
```

Or export TZ to affect all subsequent date commands in a script:

``` bash
#!/bin/bash

export TZ='Europe/Paris'
date +"%Y-%m-%d %H:%M:%S"  # Uses Europe/Paris
```

For temporary scope in a single command without affecting the rest of your script:

``` bash
#!/bin/bash

TZ='Asia/Kolkata' date -Iseconds
# TZ is back to the parent shell's timezone after this line
```

## Cron Jobs with Timezone Handling

Set TZ at the top of your crontab file to apply it to all jobs:

``` bash
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
TZ=America/Chicago
0 9 * * * /path/to/script.sh
30 14 * * * /path/to/backup.sh
```

Or set TZ within individual script invocations:

``` bash
0 9 * * * TZ='America/Denver' /path/to/script.sh >> /var/log/script.log 2>&1
```

For systemd timers (a modern alternative to cron), set the timezone in the service file or use absolute UTC times in the timer unit.

## Converting Between Timezones

Convert a known UTC timestamp to a different timezone:

``` bash
TZ='America/Denver' date -d "2026-03-15T18:30:45Z" +"%Y-%m-%d %H:%M:%S %Z"
```

Convert current time across multiple timezones:

``` bash
for tz in 'UTC' 'America/New_York' 'Europe/London' 'Asia/Shanghai'; do
  echo "$tz: $(TZ="$tz" date -Iseconds)"
done
```

## Checking and Updating System Timezone

View your system’s current timezone:

``` bash
timedatectl status
```

Check the localtime symlink:

``` bash
ls -l /etc/localtime
```

Change the system timezone:

``` bash
sudo timedatectl set-timezone 'America/Los_Angeles'
```

## Keeping Timezone Data Current

The `tzdata` package contains timezone definitions and gets updated several times yearly as countries change daylight saving time rules or modify UTC offsets. Stale timezone data causes inaccurate timestamps for affected regions.

Check your current tzdata version:

``` bash
# Debian/Ubuntu
dpkg -s tzdata | grep Version

# RHEL/Fedora/CentOS
rpm -q tzdata
```

Update timezone data:

``` bash
# Debian/Ubuntu
apt update && apt upgrade tzdata

# RHEL/Fedora/CentOS
dnf upgrade tzdata

# Alpine
apk update && apk upgrade tzdata
```

After updating tzdata, running processes may need to restart to pick up new timezone rules. This is particularly important for long-running services (databases, application servers, log aggregators) that cache timezone offsets at startup.

## Practical Example: Multi-Region Log Aggregation

When aggregating logs from servers in different regions, standardize timestamps on UTC:

``` bash
#!/bin/bash

# Log with UTC timestamp
{
  echo "[$(TZ='UTC' date -Iseconds)] User login detected"
  echo "[$(TZ='UTC' date -Iseconds)] Processing request"
} >> /var/log/app.log

# Later, convert UTC timestamp for local review
TIMESTAMP="2026-03-15T18:30:45Z"
echo "UTC: $TIMESTAMP"
echo "Denver: $(TZ='America/Denver' date -d "$TIMESTAMP" -Iseconds)"
echo "Sydney: $(TZ='Australia/Sydney' date -d "$TIMESTAMP" -Iseconds)"
```

## Why TZ Over Other Approaches

The TZ environment variable is the standard POSIX approach and offers these advantages:

- Available on every POSIX-compliant system without additional dependencies
- No performance overhead compared to other tools
- Works in shell scripts, cron jobs, and systemd services
- Easy to debug — timezone is explicit in each command
- Portable across distributions
