---
title: "How to Change Your GNOME Keyring Password"
date: 2018-03-24 08:14:00 +0000
author: "Q A"
layout: post
categories: [development-best-practices]
canonical: /how-to-change-the-gnome-keyring-password/
---

GNOME Keyring stores passwords, SSH keys, and certificates. If you need to update your keyring password, you can do this through the Seahorse graphical interface or directly from the command line.

### Using Seahorse (GUI Method)

Seahorse is GNOME’s visual keyring manager. Open it with:

``` bash
seahorse
```

Once open:

1.  Go to the **View** menu and select **By Keyring**
2.  In the left sidebar, right-click on **Login** (your default keyring)
3.  Select **Change Password**
4.  Enter your current keyring password
5.  Type your new password twice to confirm
6.  Click **Change**

The password change takes effect immediately.

### Using Command Line

For headless systems or scripting, use `seahorse` with the `--help` flag to see available options, or work directly with the keyring daemon:

``` bash
seahorse --help
```

If you need to unlock your keyring from the command line (useful in scripts), you can use:

``` bash
echo -n "your-password" | gnome-keyring-daemon --unlock
```

However, for automated operations, consider using `secret-tool` from `libsecret`, which is the modern approach to keyring interaction:

``` bash
secret-tool lookup attribute value
```

### Syncing Keyring with Login Password

If your keyring password gets out of sync with your system login password, GNOME can resync them. This typically happens after a password change through system settings:

1.  Open **Settings** → **Users**
2.  Select your user and update your password
3.  GNOME will prompt you to update your keyring password to match
4.  Answer **Yes** to keep them synchronized

### If You’ve Forgotten the Keyring Password

If you forget the keyring password entirely, you’ll need to reset it:

``` bash
rm ~/.local/share/keyrings/login.keyring
```

Warning: This deletes all stored passwords in that keyring. After deletion, restart GNOME (log out and back in), and a new keyring will be created with your login password.

Alternatively, you can delete just the specific keyring database without removing the entire keyring directory:

``` bash
rm ~/.local/share/keyrings/login.keyring-*
```

### Troubleshooting

**Keyring won’t unlock after password change**: Log out completely and log back in. The keyring should automatically unlock with your new login password if they’re synchronized.

**Seahorse not installed**: Install it with:

``` bash
# Debian/Ubuntu
sudo apt install seahorse

# Fedora/RHEL
sudo dnf install seahorse

# Arch
sudo pacman -S seahorse
```

**Permission issues**: Ensure your user owns the keyring files:

``` bash
ls -la ~/.local/share/keyrings/
```

If permissions look wrong, fix them with:

``` bash
chmod 700 ~/.local/share/keyrings/
chmod 600 ~/.local/share/keyrings/*
```

The keyring system integrates tightly with your login password on modern GNOME, so keeping them synchronized prevents unlock prompts during your session.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
