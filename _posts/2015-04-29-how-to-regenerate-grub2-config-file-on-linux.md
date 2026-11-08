---
title: "Regenerating GRUB2 Configuration Files on Linux"
date: 2015-04-29 01:20:16 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-regenerate-grub2-config-file-on-linux/
---

GRUB2 configuration needs to be regenerated when you modify boot parameters, install new kernels, or adjust default boot entries. The process varies slightly between BIOS and UEFI systems, and between distributions, but follows a consistent pattern once you understand your system layout.

## Check Your System Firmware Type

Before regenerating config, identify whether your system uses BIOS or UEFI:

``` bash
[ -d /sys/firmware/efi ] && echo "UEFI" || echo "BIOS"
```

This matters because GRUB2 stores configuration in different locations:

- **UEFI systems**: `/boot/efi/EFI/*/grub.cfg` or `/etc/grub2-efi.cfg`
- **BIOS systems**: `/boot/grub2/grub.cfg` or `/etc/grub2.cfg`

Most modern distributions prefer the `/etc/grub2.cfg` and `/etc/grub2-efi.cfg` locations for consistency.

## RPM-Based Distributions (Fedora, RHEL, CentOS, AlmaLinux, Rocky Linux)

Always back up your existing configuration first:

``` bash
sudo cp /etc/grub2.cfg /etc/grub2.cfg.backup
```

For BIOS systems:

``` bash
sudo grub2-mkconfig -o /etc/grub2.cfg
```

For UEFI systems:

``` bash
sudo grub2-mkconfig -o /etc/grub2-efi.cfg
```

If you’re unsure which to use, run the firmware check above and use the corresponding command.

## Debian and Ubuntu

Ubuntu provides `update-grub`, a wrapper script that handles both BIOS and UEFI detection automatically:

``` bash
sudo update-grub
```

This is the recommended approach on Debian/Ubuntu systems. It detects your firmware type and kernel setup, then updates the appropriate configuration file.

For manual regeneration on Debian/Ubuntu (note: no “2” in the command name):

``` bash
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

## Automated Regeneration Function

Use this shell function to handle BIOS/UEFI detection automatically on RPM-based systems:

``` bash
regenerate_grub2() {
    local grubcfg
    local backup_file

    if [ -d /sys/firmware/efi ]; then
        grubcfg="/etc/grub2-efi.cfg"
    else
        grubcfg="/etc/grub2.cfg"
    fi

    backup_file="${grubcfg}.backup.$(date +%s)"
    sudo cp "$grubcfg" "$backup_file"
    echo "Backup created: $backup_file"

    if sudo grub2-mkconfig -o "$grubcfg"; then
        echo "GRUB2 config regenerated successfully"
        return 0
    else
        echo "Error regenerating GRUB2 config" >&2
        echo "Restoring from backup..."
        sudo cp "$backup_file" "$grubcfg"
        return 1
    fi
}
```

Add this to your `~/.bashrc` or `~/.zshrc` for regular use.

## Verify the Changes

After regeneration, confirm the new config was created:

``` bash
ls -la /etc/grub2.cfg
```

Check that your kernel entries appear correctly:

``` bash
sudo grep "^menuentry" /etc/grub2.cfg | head -10
```

View more details about a specific menu entry:

``` bash
sudo grep -A 5 "^menuentry 'CentOS" /etc/grub2.cfg
```

## Troubleshooting

**“grub2-mkconfig: command not found”**

Install GRUB2 tools for your distribution:

``` bash
# Fedora/RHEL/CentOS/AlmaLinux
sudo dnf install grub2-tools grub2-common

# Debian/Ubuntu
sudo apt install grub2-common grub-pc
```

**Config file in unexpected location**

Some distributions mount `/boot` separately or use custom paths. Check `/etc/default/grub` for configuration directives:

``` bash
sudo grep -E "^GRUB_" /etc/default/grub
```

Key variables affecting config generation:

- `GRUB_DISABLE_SUBMENU`: Controls menu structure
- `GRUB_DEFAULT`: Sets default boot entry
- `GRUB_CMDLINE_LINUX`: Adds kernel parameters to all entries
- `GRUB_TIMEOUT`: Boot menu timeout in seconds

**UEFI system not detecting properly**

Verify EFI variables are accessible:

``` bash
efibootmgr -v
```

If this command fails or returns no entries, EFI support may be disabled in firmware. Reboot and check BIOS/UEFI settings.

**Regeneration hangs or fails with obscure errors**

Check for corrupt kernel images or missing device files:

``` bash
ls -la /boot/vmlinuz-* /boot/initramfs-*
sudo ls -la /dev/disk/by-uuid/
```

Remove any orphaned kernel packages before regenerating:

``` bash
# On RPM-based systems, list installed kernels
rpm -q kernel

# Remove old kernels (keep at least the current and one previous)
sudo dnf remove kernel-<old-version>
```

## When to Regenerate

Regenerate GRUB2 config in these scenarios:

- After modifying `/etc/default/grub`
- After installing new kernel packages (most distributions do this automatically)
- After manually adding entries to `/etc/grub.d/`
- When changing default boot parameters or timeout
- After updating kernel command-line arguments
- When GRUB2 packages are updated via the package manager
- After making changes to encrypted or LVM-based partitions

Most modern distributions trigger automatic regeneration during kernel installation and system updates via packaging hooks. However, manual regeneration ensures changes take effect immediately without waiting for the next system update.
