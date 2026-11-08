---
title: "Automatic Server Recovery: Handling Reboots and Panic Detection"
date: 2015-02-02 13:03:31 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /lazy-linux-admins-going-to-server-rooms-less-forced-reboot-auto-reboot-after-kernel-panic-and-email-notification-after-reboot/
---

When SSH fails but the daemon still runs, or when kernel panics strike, you need automated recovery without physical access. This guide covers three essential techniques: forcing reboots when the system is unresponsive, auto-recovery from kernel panics, and alerting you when it happens.

## Force a reboot when SSH is unresponsive

If a server stops responding to SSH commands but the daemon is still listening—usually due to memory exhaustion, runaway processes, or system load—the Linux magic SysRq interface provides kernel-level access when normal system calls fail.

Enable SysRq and trigger an immediate reboot:

``` bash
ssh root@server 'echo 1 > /proc/sys/kernel/sysrq; echo b > /proc/sysrq-trigger'
```

The `b` command forces an immediate reboot without syncing filesystems. Use this only when the system is truly unresponsive. Other useful SysRq commands:

- `s` – sync all filesystems
- `e` – terminate all processes
- `i` – kill all processes
- `u` – remount filesystems read-only

For a more graceful approach, attempt to sync data first:

``` bash
ssh root@server 'echo 1 > /proc/sys/kernel/sysrq; echo s > /proc/sysrq-trigger; sleep 5; echo b > /proc/sysrq-trigger'
```

This syncs cached writes to disk before forcing the reboot. The server will disappear from the network and return once boot completes.

Enable SysRq permanently by adding this to `/etc/sysctl.d/99-sysrq.conf`:

    kernel.sysrq = 1

Then apply it:

``` bash
sysctl -p /etc/sysctl.d/99-sysrq.conf
```

**Note:** SysRq is a security risk on systems with untrusted local users. Restrict it to `16` (enable only reboot and poweroff) if needed:

    kernel.sysrq = 16

## Automatic reboot after kernel panic

Kernel panics halt the system completely. Without automatic recovery, a panic means downtime until someone manually reboots the box. Configure the kernel to reboot automatically after a panic by setting the `kernel.panic` parameter.

Apply immediately to a running system:

``` bash
sysctl -w kernel.panic=20
```

This reboots 20 seconds after a panic, giving you time to capture console logs if they’re being recorded.

Make it persistent by adding to `/etc/sysctl.d/99-panic.conf`:

    kernel.panic = 20
    kernel.panic_on_oops = 1
    kernel.panic_on_io_nmi = 1
    kernel.panic_on_hung_task = 30

Apply immediately:

``` bash
sysctl -p /etc/sysctl.d/99-panic.conf
```

What each parameter does:

- `kernel.panic` – seconds to wait before rebooting after panic (0 disables it)
- `kernel.panic_on_oops` – reboot on kernel oops (recoverable errors that become fatal)
- `kernel.panic_on_io_nmi` – reboot on I/O-related non-maskable interrupts
- `kernel.panic_on_hung_task` – reboot if kernel detects a task stuck in D state (uninterruptible sleep)

Set different timeouts for different environments. Production might use 10 seconds, while development uses 60 to allow log capture. Use 0 to disable any parameter.

Verify the setting:

``` bash
sysctl kernel.panic
```

## Email notifications on reboot

Automatic reboots are useless if you don’t know they happened. Configure the system to notify you on startup using cron’s `@reboot` directive.

First, ensure your system can send mail. On Debian/Ubuntu:

``` bash
apt-get install nullmailer
```

Configure `/etc/nullmailer/remotes`:

    smtp.example.com smtp --port=587 --user=username --pass=password

Or if you have postfix/exim already running, mail should work out of the box.

Add this to root’s crontab (`crontab -e`):

``` bash
@reboot (sleep 30 && echo "Host $(hostname) rebooted at $(date)" | mail -s "$(hostname) reboot notification" admin@example.com) &
```

The `sleep 30` delay allows the network stack and mail system to fully initialize after boot. The trailing `&` backgrounds the command so cron doesn’t wait for mail delivery.

For better logging, also log to syslog:

``` bash
@reboot logger -t reboot-notify "System rebooted at $(date +%s)" && sleep 30 && echo "Host $(hostname) rebooted at $(date)" | mail -s "$(hostname) reboot" admin@example.com &
```

In high-volume environments, email notifications don’t scale well. Instead, send notifications to your centralized logging system or monitoring platform:

``` bash
@reboot sleep 30 && logger -t reboot-notify -p syslog.info "$(hostname) rebooted at $(date +%s)" &
```

Then configure rsyslog or syslog-ng to forward these messages to your log aggregator (ELK, Datadog, Splunk, etc.).

If mail delivery fails silently, verify with:

``` bash
echo "Test message" | mail -v -s "Test" admin@example.com
```

## Put it all together

A complete, resilient setup combines all three techniques:

``` bash
# /etc/sysctl.d/99-resilience.conf
kernel.sysrq = 1
kernel.panic = 20
kernel.panic_on_oops = 1
kernel.panic_on_io_nmi = 1
kernel.panic_on_hung_task = 30
```

``` bash
# Apply on boot and now
sysctl -p /etc/sysctl.d/99-resilience.conf
```

Add to root’s crontab:

``` bash
@reboot (sleep 30 && logger -t reboot "$(hostname) rebooted" && echo "Host $(hostname) rebooted at $(date)" | mail -s "$(hostname) reboot" admin@example.com) &
```

Keep SysRq enabled for manual intervention when needed. In your infrastructure code (Ansible, Terraform, cloud-init), deploy these settings during system initialization so every server starts with automatic recovery built in.

**Test it in a non-production environment:** Trigger a kernel panic manually and verify the reboot and notification chain work:

``` bash
# On a test system only
echo c > /proc/sysrq-trigger
```

This immediately causes a panic. Confirm your monitoring system records the reboot and receives the notification before deploying to production.
