---
title: "How to Create an Autostart Script for GNOME"
date: 2018-03-24 08:14:04 +0000
modified: 2026-04-12 16:10:47 +0000
author: "Q A"
layout: post
categories: [development-best-practices]
canonical: /how-to-write-a-autostart-script-for-gnome/
---

GNOME uses `.desktop` files in `~/.config/autostart/` to launch applications when you log in. This mechanism works across GNOME, XFCE, KDE, and most other modern desktop environments.

### Basic Setup

Create a `.desktop` file in `~/.config/autostart/`. Here’s a minimal example:

``` ini
[Desktop Entry]
Type=Application
Name=My Autostart Script
Exec=/home/user/bin/myscript.sh
```

Save this as `~/.config/autostart/myscript.desktop` and it will run on your next login.

### Real-World Example

Here’s a practical `.desktop` file for starting a Python daemon:

``` ini
[Desktop Entry]
Type=Application
Name=Dropbox
Comment=Dropbox file synchronization
Exec=/home/zma/bin/dropbox.py start
Icon=system-run
Terminal=false
StartupNotify=true
```

Key fields explained:

- **Type**: Always `Application` for executable scripts
- **Name**: Display name shown in GNOME settings
- **Exec**: Full path to your script or command. Use absolute paths only
- **Icon**: Icon name from your system’s icon theme (optional)
- **Terminal**: Set to `true` if your script needs a terminal window; `false` to run silently
- **StartupNotify**: Shows a loading indicator while the app starts
- **Comment**: Brief description (optional)

### Practical Examples

**Running a shell script:**

``` ini
[Desktop Entry]
Type=Application
Name=System Backup
Exec=/usr/local/bin/backup-daily.sh
Terminal=false
StartupNotify=true
```

**Running a Python script with delay:**

If your service takes time to initialize, add a delay:

``` ini
[Desktop Entry]
Type=Application
Name=VPN Connection
Exec=bash -c "sleep 5 && /usr/local/bin/start-vpn.py"
Terminal=false
```

**Running a command that needs output:**

``` ini
[Desktop Entry]
Type=Application
Name=System Monitor
Exec=gnome-system-monitor
Terminal=false
```

### Important Considerations

**Use absolute paths**: Never use relative paths or `~` in the `Exec` field. Always write out `/home/username/bin/script.sh`.

**Make scripts executable**: Ensure your script has execute permissions:

``` bash
chmod +x /home/user/bin/myscript.sh
```

**Use proper shebangs**: Start shell scripts with `#!/bin/bash` or `#!/usr/bin/env python3` so the system knows how to execute them.

**Logging for debugging**: Autostart scripts run without a terminal, so redirect output to a log file if needed:

``` ini
Exec=bash -c "/usr/local/bin/myscript.sh >> /tmp/autostart.log 2>&1"
```

**Environment variables**: If your script needs environment variables, set them in the Exec line:

``` ini
Exec=bash -c "export PATH=/custom/bin:$PATH && /usr/local/bin/myscript.sh"
```

### Managing Autostart Entries

List all autostart applications:

``` bash
ls ~/.config/autostart/
```

View an existing entry:

``` bash
cat ~/.config/autostart/example.desktop
```

Remove an entry:

``` bash
rm ~/.config/autostart/example.desktop
```

GNOME Settings also provides a UI to manage startup applications, though it’s typically limited. The command-line approach via `.desktop` files gives you more control.

### Testing Before Adding to Autostart

Always test your script manually first:

``` bash
/home/user/bin/myscript.sh
```

Once confirmed working, create the `.desktop` file and log out/in to verify it starts automatically.

### System-Wide Autostart

For scripts that should run for all users, place `.desktop` files in `/etc/xdg/autostart/` instead (requires root). This is useful for system services or managed deployments.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
