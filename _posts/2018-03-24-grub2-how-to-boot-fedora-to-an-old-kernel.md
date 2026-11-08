---
title: "Booting Fedora with an Old Kernel in GRUB2"
date: 2018-03-24 08:16:12 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /grub2-how-to-boot-fedora-to-an-old-kernel/
---

Modern Fedora systems keep multiple kernel versions available, but older kernels are tucked in a submenu rather than appearing as top-level GRUB2 entries. This requires a slightly different approach when setting them as your default boot option.

### Understanding the GRUB2 submenu structure

When you run:

``` bash
grep menuentry /boot/grub2/grub.cfg | cut -d "'" -f2
```

You’ll see entries like “Fedora” and “Advanced options for Fedora”, but not the individual kernel versions. The older kernels live as submenu items under “Advanced options for Fedora”. The full entry name isn’t visible with that grep command alone.

To see the complete structure including submenus, use:

``` bash
grep -E "^\s*menuentry|^\s*submenu" /boot/grub2/grub.cfg | head -20
```

This shows the hierarchy more clearly.

### Setting an old kernel as default

To boot a specific older kernel, you need to reference both the submenu and the kernel entry using the `>` separator:

``` bash
grub2-set-default 'Advanced options for Fedora>Fedora, with Linux 6.x.x-xxx.fcXX.x86_64'
```

Replace the kernel version with the actual version you want. The `>` character separates the submenu name from the specific kernel entry.

### Finding the exact kernel entry name

If you’re unsure of the exact kernel version string, view the configuration directly:

``` bash
cat /boot/grub2/grub.cfg | grep -A 1 "submenu 'Advanced"
```

Or boot into GRUB2 at startup and navigate the menu with arrow keys to see the exact names of available kernels.

### Verifying your selection

After setting the default, confirm it worked:

``` bash
grub2-editenv list
```

This should show `saved_entry=Advanced options for Fedora>Fedora, with Linux X.X.X...`

### Permanent vs temporary kernel selection

If you only want to boot an old kernel once without changing the default:

1.  Reboot and hold Shift during startup to see the GRUB2 menu
2.  Navigate to “Advanced options for Fedora”
3.  Select your desired kernel version
4.  Press Enter

On EFI systems, you may need to press Escape instead of Shift to access the menu.

### Making changes persistent across updates

When Fedora updates your kernel, it automatically regenerates `/boot/grub2/grub.cfg`. If you’ve set an old kernel as default and a new kernel is installed, GRUB2 will respect your `grub2-set-default` choice, but you may want to return to booting the latest kernel eventually.

To switch back to the newest kernel:

``` bash
grub2-set-default 0
```

This boots the first entry (typically the newest kernel).

## Troubleshooting Common Issues

When encountering problems on Linux systems, follow a systematic approach. Check system logs first using journalctl for systemd-based distributions. Verify service status with systemctl before attempting restarts. For network issues, use ip addr and ss -tulpn to diagnose connectivity problems.

Package management issues often stem from stale caches. Run dnf clean all on Fedora or apt clean on Ubuntu before retrying failed installations. If a package has unmet dependencies, try resolving them with dnf autoremove or apt autoremove.

## Related System Commands

These commands are frequently used alongside the tools discussed in this article:

- systemctl status service-name – Check if a service is running
- journalctl -u service-name -f – Follow service logs in real time
- rpm -qi package-name – Query installed package information
- dnf history – View package transaction history
- top or htop – Monitor system resource usage

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
