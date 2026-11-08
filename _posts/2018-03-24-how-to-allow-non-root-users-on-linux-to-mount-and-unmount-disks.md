---
title: "Allowing Non-Root Users to Mount Disks on Linux"
date: 2018-03-24 11:45:47 +0000
modified: 2026-04-11 15:56:22 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-allow-non-root-users-on-linux-to-mount-and-unmount-disks/
---

On a Linux system, you often need to let regular users mount and unmount specific devices without requiring sudo or the root password. This is common for external drives, USB devices, or secondary internal disks. There are several approaches, each with different security and usability tradeoffs.

## Using /etc/fstab with the `user` Option

The simplest approach is to add entries to `/etc/fstab` with the `user` option. This allows any user to mount and unmount the filesystem.

First, identify your device and its UUID:

``` bash
lsblk -o NAME,UUID,FSTYPE,MOUNTPOINTS
```

Open `/etc/fstab` as root:

``` bash
sudo nano /etc/fstab
```

Add an entry like this:

    UUID=1234-5678 /mnt/external ext4 defaults,user,nofail 0 2

Key options:

- `user` — allows non-root users to mount/unmount
- `users` — allows any user to mount, but only the user who mounted it can unmount it
- `nouser` — default; only root can mount
- `nofail` — system boots normally if device is missing
- `noauto` — device won’t mount automatically at boot

After editing, test it:

``` bash
mount /mnt/external
umount /mnt/external
```

## Using sudo with NOPASSWD

For tighter control, grant specific users permission to mount specific devices via `sudo` without a password prompt.

Edit the sudoers file:

``` bash
sudo visudo
```

Add a line like this:

    alice ALL=(ALL) NOPASSWD: /usr/bin/mount /dev/sde1, /usr/bin/umount /dev/sde1

This allows user `alice` to run only those specific mount and umount commands without a password. Users can then run:

``` bash
sudo mount /dev/sde1 /mnt/external
sudo umount /mnt/external
```

## Using Polkit (Modern Desktop Systems)

On systems with Polkit (common on desktop Linux), users in the `wheel` or `sudo` group automatically get permission to mount certain removable devices without a password.

Check your Polkit configuration:

``` bash
ls -la /etc/polkit-1/rules.d/
ls -la /usr/share/polkit-1/rules.d/
```

Create a custom rule if needed:

``` bash
sudo nano /etc/polkit-1/rules.d/50-mount.rules
```

Example rule allowing mounting removable media:

``` javascript
polkit.addRule(function(action, subject) {
  if ((action.id == "org.freedesktop.udisks2.filesystem-mount" ||
       action.id == "org.freedesktop.udisks2.filesystem-unmount") &&
      subject.isInGroup("storage")) {
    return polkit.Result.YES;
  }
});
```

Then add your user to the `storage` group:

``` bash
sudo usermod -aG storage username
```

The user needs to log out and back in for group changes to take effect.

## Security Considerations

**`/etc/fstab` with `user` option**: Convenient but less restrictive. Any user can mount and unmount the device. Use for trusted systems or devices you don’t mind users accessing.

**`sudo` NOPASSWD**: More granular control. You can specify exactly which users and which devices. However, passwordless sudo should be used carefully and only for commands with limited scope.

**Polkit**: Best for desktop systems where you want automatic mounting of USB drives without prompts. Integrates with your graphical file manager and login session.

## Troubleshooting

If mounting fails with “permission denied,” check the mount point permissions:

``` bash
ls -ld /mnt/external
```

Ensure the user owns the directory or that it has appropriate group or world permissions:

``` bash
sudo chown alice:alice /mnt/external
sudo chmod 755 /mnt/external
```

If you’re using `/etc/fstab`, reload the table:

``` bash
sudo mount -a
```

For Polkit rules not taking effect, check logs:

``` bash
sudo journalctl -u polkit -f
```

Choose the method that matches your security requirements and system design. For servers, use sudo NOPASSWD. For desktops, Polkit provides the best user experience. For simple setups, `/etc/fstab` is usually sufficient.
