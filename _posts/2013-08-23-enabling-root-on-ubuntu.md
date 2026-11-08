---
title: "Using Root Access Safely on Ubuntu"
date: 2013-08-23 06:35:00 +0000
author: "Thirumal Venkat"
layout: post
canonical: https://www.systutorials.com/enabling-root-on-ubuntu/
---

Ubuntu locks the root account by default as a safety measure—it prevents accidental system damage and enforces audit trails through `sudo`. If you genuinely need direct root access, here’s how to enable it and the security tradeoffs involved.

## Set a root password

The simplest approach:

``` bash
sudo passwd root
```

You’ll be prompted to enter and confirm a new password. Once set, switch to the root user with:

``` bash
su -
```

The `-` flag ensures you get a login shell with root’s environment variables properly configured. You’ll need to enter the root password you just set.

Exit the root shell with `exit` or `Ctrl+D`.

## Understanding the security cost

Enabling the root account directly means losing Ubuntu’s protection against accidental system damage and losing command logging. Every action as root becomes harder to audit. Consider whether you actually need this, or if `sudo` for specific commands is sufficient. Most modern workflows don’t require a persistent root shell.

If you only need root occasionally, `sudo -i` gives you a root shell without permanently enabling the account:

``` bash
sudo -i
```

This is almost always the better choice. You retain `sudo` logging, maintain the security boundary, and can exit immediately when done.

## Configure passwordless sudo for specific commands

If you need to run certain commands frequently as root without entering a password each time, use `visudo` to edit the sudoers file:

``` bash
sudo visudo
```

Add a line like:

``` bash
username ALL=(ALL) NOPASSWD: /usr/bin/systemctl
```

This allows the user to run `systemctl` without a password prompt. Always use `visudo`—it validates syntax before saving and prevents lockouts. Never edit `/etc/sudoers` directly.

For multiple commands:

``` bash
username ALL=(ALL) NOPASSWD: /usr/bin/systemctl, /usr/bin/journalctl, /bin/systemctl
```

For all commands (dangerous, but sometimes necessary in automated contexts):

``` bash
username ALL=(ALL) NOPASSWD: ALL
```

## Grant sudo access to a user

If a user doesn’t have sudo access at all, add them to the sudo group:

``` bash
sudo usermod -aG sudo username
```

They’ll need to enter their own password (not the root password) when using `sudo`. This is safer than enabling root directly.

## Disable root access again

If you decide you don’t need direct root access:

``` bash
sudo passwd -dl root
```

The `-d` flag removes the password, and `-l` locks the account. This prevents any login attempts via `su -` or SSH.

## When to enable root, and when not to

**Don’t enable root if:**

- You’re setting up a general-purpose system or workstation
- You’re managing a production server (audit trails matter)
- You’re the only user or one of a few users (sudo handles privileges fine)
- You’re running Ubuntu on a system others can access

**Consider enabling root if:**

- You’re performing intensive sysadmin work and constantly typing `sudo` (though `sudo -i` is usually better)
- You’re running legacy scripts or tools that demand root and won’t work with sudo
- You’re in a lab or isolated environment with no security requirements

**Better alternatives in almost all cases:**

- Use `sudo` for individual commands requiring elevated privileges
- Create a dedicated administrative user account with passwordless sudo access for specific operations
- Use `sudo -u` to run commands as other users without switching shells
- Configure granular sudoers rules for fine-grained permissions by role or command

If you find yourself constantly switching to root, you likely have a workflow problem that’s better solved with better sudo configuration or shell aliases. A single typo as root can destroy your system with no protection; sudo’s inherent friction exists for a reason.
