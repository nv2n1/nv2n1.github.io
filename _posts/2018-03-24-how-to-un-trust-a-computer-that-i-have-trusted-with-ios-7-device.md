---
title: "Remove a Trusted Computer from Your iOS Device"
date: 2018-03-24 11:42:35 +0000
modified: 2026-04-12 16:11:11 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-un-trust-a-computer-that-i-have-trusted-with-ios-7-device/
---

When you connect an iPhone or iPad to a computer and tap “Trust,” iOS stores a pairing record that allows that computer to communicate with the device without asking for permission again. If you want to revoke that trust relationship, you need to delete the pairing data on both the device and the computer.

## On the iOS Device

The simplest approach is to revoke trust directly from your iPhone or iPad:

1.  Go to **Settings \> General \> Reset**
2.  Tap **Reset Location & Privacy**
3.  Tap **Reset** to confirm

This clears all location and privacy settings, including trust relationships with computers. Alternatively, you can:

1.  Go to **Settings \> Privacy \> Developer**
2.  Tap the trusted computer name and select **Forget this computer** (if available on your iOS version)

## On the Computer (macOS)

macOS stores pairing records in the lockdown directory. To remove the trust relationship:

``` bash
rm -rf ~/Library/Lockdown/*
```

This deletes all pairing records for all iOS devices. If you want to target a specific device, you can browse the lockdown directory first:

``` bash
ls -la ~/Library/Lockdown/
```

Each UUID folder corresponds to a device’s pairing record. You can delete a specific device’s folder:

``` bash
rm -rf ~/Library/Lockdown/<device_uuid>
```

After deletion, disconnect your iOS device and reconnect it. You’ll see the “Trust This Computer?” prompt again.

## On Linux

Linux systems using libimobiledevice store pairing records in:

``` bash
rm -rf ~/.local/share/libimobiledevice/
```

Or for system-wide pairings:

``` bash
sudo rm -rf /var/lib/lockdown/
```

If you’re using usbmuxd, the directory might also be under `/var/lib/usbmux/`. After clearing this directory, reconnect your device to trigger a new pairing.

## On Windows

Windows stores lockdown data in:

    C:\ProgramData\Apple\Lockdown\

or

    C:\Users\<username>\AppData\Roaming\Apple Computer\Lockdown\

You’ll need administrator privileges to delete these folders. Right-click the folder, select **Delete**, and confirm. Disconnect and reconnect your device afterward.

## Verify Trust Was Removed

After clearing the pairing data:

1.  Disconnect your iOS device from the computer
2.  Reconnect it
3.  You should see the “Trust This Computer?” prompt on your device again

If the prompt doesn’t appear, try restarting both the device and computer, then reconnecting.

## Additional Notes

- Clearing lockdown folders also revokes trust for any backup software (like iTunes or Finder) that relies on pairing
- If you’re concerned about a lost or stolen computer accessing your device remotely, also change your iCloud password and enable two-factor authentication
- On modern iOS versions (14+), you can also manage trusted devices through **Settings \> Privacy \> Bluetooth** if the device was paired as a Bluetooth accessory

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
