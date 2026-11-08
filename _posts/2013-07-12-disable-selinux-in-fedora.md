---
title: "Managing SELinux in Fedora and CentOS"
date: 2013-07-12 16:31:57 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /disable-selinux-in-fedora/
---

SELinux provides mandatory access controls that catch security violations most firewall and file permission rules miss. Before disabling it, exhaust other options — SELinux warnings often reveal real security problems worth understanding.

That said, there are legitimate reasons to adjust SELinux: testing application behavior without policy violations, troubleshooting misbehaving software, or running systems where the overhead isn’t justified. You have three practical options: permissive mode (log without blocking), temporary disable, and permanent disable.

## Switch to Permissive Mode

Permissive mode logs policy violations without blocking operations. This is the safest approach if you’re troubleshooting because you get visibility into what SELinux would reject.

Edit `/etc/selinux/config`:

``` bash
sudo vi /etc/selinux/config
```

Find this line:

    SELINUX=enforcing

Change it to:

    SELINUX=permissive

Reboot for the change to take effect:

``` bash
sudo reboot
```

You can also verify the change before rebooting by checking what will be applied:

``` bash
sudo getenforce
```

This shows the current mode; reboot will move you to what’s configured in `/etc/selinux/config`.

## Temporarily Disable SELinux Without Rebooting

For testing or quick troubleshooting, disable SELinux at runtime:

``` bash
sudo setenforce 0
```

The return value tells you the operation succeeded (0 means success as a command exit code, not SELinux status). Verify the change:

``` bash
sudo getenforce
Permissive
```

Re-enable enforcement with:

``` bash
sudo setenforce 1
```

This persists only until reboot. If you reboot without changing `/etc/selinux/config`, SELinux returns to whatever mode is configured there.

## Permanently Disable SELinux

If you’re certain you don’t need SELinux, disable it permanently:

``` bash
sudo vi /etc/selinux/config
```

Change:

    SELINUX=enforcing

To:

    SELINUX=disabled

Reboot for the change to apply. Disabling SELinux completely removes the kernel module from enforcement — it’s different from permissive mode, which still performs checks and logging.

**Warning:** Some packages and systemd services expect SELinux to be available. Fully disabling it can cause unexpected behavior. Permissive mode is almost always preferable.

## Check SELinux Status

Use `getenforce` for a quick status check:

``` bash
sudo getenforce
Enforcing
```

For more detailed information, use `sestatus`:

``` bash
sudo sestatus
SELinux status:                 enabled
Current mode:                   enforcing
Mode from config file:          enforcing
Policy name:                    targeted
Policy from config file:        targeted
```

For scripts, use `selinuxenabled` to test if SELinux is active:

``` bash
selinuxenabled && echo "SELinux is enabled" || echo "SELinux is disabled"
```

The command returns exit code 0 if SELinux is enabled (mode is not disabled), so the exit code is useful for conditionals, not a status value.

## Working with SELinux Policies

Rather than disabling SELinux entirely, you can adjust the policy level. The `targeted` policy is the default and covers common processes. Switch to `mls` (Multi-Level Security) for stricter controls, or create custom policies:

``` bash
sudo vi /etc/selinux/config
```

Change the `SELINUXTYPE` line:

    SELINUXTYPE=targeted

After reboot, verify with:

``` bash
sudo sestatus | grep "Policy name"
Policy name:                    targeted
```

## Reviewing SELinux Denials

Before disabling SELinux, check what it’s actually blocking. Set it to permissive and examine the audit log:

``` bash
sudo grep -i denied /var/log/audit/audit.log | tail -20
```

Or use `ausearch`:

``` bash
sudo ausearch -m AVC -ts recent
```

This shows recent access control violations. Many are harmless, but some reveal genuine misconfigurations in your application’s file permissions or process isolation. Understanding these denials often leads to a solution that doesn’t require disabling SELinux entirely.
