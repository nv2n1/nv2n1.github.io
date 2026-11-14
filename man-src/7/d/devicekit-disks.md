---
title: "devicekit-disks(7)"
name: "devicekit-disks"
section: "7"
letter: "d"
url: "/docs/linux/man/7-devicekit-disks/"
description: "DeviceKit-disks – Disk Management"
---

<p>DeviceKit-disks &#8211; Disk Management</p>
<h2>Description</h2>
<p>DeviceKit-disks provides an interface to enumerate block devices and perform operations on them. Any application can access the <i>org.freedesktop.DeviceKit.Disks</i> service on the system message bus. Some operations (such as formatting disks etc.) is restricted using PolicyKit.</p>
<h2>Device Information</h2>
<p>On Linux, DeviceKit-disks relies on recent versions of <code><a href="/docs/linux/man/7-udev/">udev</a></code>(7) and the kernel. Influential device properties in the udev database include: </p>
<p> <code>DKD_PRESENTATION_HIDE</code></p>
<dl>
<dd>If set to 1 this is a hint to presentation level software that the device should not be shown to the user.</dl>
<p> <code>DKD_PRESENTATION_NOPOLICY</code></p>
<dl>
<dd>If set to 1 this is a hint to presentation level software that the device should not be automounted or autoassembled (for e.g. components of a multi-disk device).</dl>
<p> <code>DKD_PRESENTATION_NAME</code></p>
<dl>
<dd>The name to user for the device when presenting it to the user.</dl>
<p> <code>DKD_PRESENTATION_ICON_NAME</code></p>
<dl>
<dd>The icon to use when presenting the device to the user. If set, the name must follow the freedesktop.org icon theme specification.</dl>
<p> The <code>ID_DRIVE_*</code> properties are used to describe what kind of physical media can be used in a device. These are typically set on the main block device (e.g. /dev/sdb) and more than one these properties can be set if the device supports multiple kinds of media. </p>
<p> <code>ID_DRIVE_EJECTABLE</code></p>
<dl>
<dd>Whether the media in the drive is physically ejectable. Only set this to 1 (or 0) if the drive truly uses (or doesn&#8217;t) ejectable media. In particular, it is not necessary to set this for e.g. iPod or Kindle devices where it is necessary to send a command via <code><a href="/docs/linux/man/1-eject/">eject</a></code>(1) since the desktop user session will offer this option for removable devices regardless of whether they are ejectable. If this property is not set, a heuristic will be used to determine if the media is ejectable (drives using optical, Zip or Jaz media are considered ejectable).</dl>
<p> <code>ID_DRIVE_DETACHABLE</code></p>
<dl>
<dd>Whether the device is detachable. It is only meaningful to set this to 0 (to avoid marking a device as detachable) since the code for detaching the device is part of DeviceKit-disks itself. If this property is not set, a heuristic will be used to determine if the drive is detachable (currently only devices connected through USB are detachable).</dl>
<p> <code>ID_DRIVE_CAN_SPINDOWN</code></p>
<dl>
<dd>Whether the device can spin down. It is only meaningful to set this to 0 (to avoid marking a device as being capable of spinning down) since the code for spinning down the device is part of DeviceKit-disks itself. If this property is not set, a heuristic will be used to determine if the drive can spin down (currently only ATA devices, including those USB devices with a SAT layer) can be spun down).</dl>
<p> <code>ID_DRIVE_FLASH</code></p>
<dl>
<dd>The device is compatible with flash.</dl>
<p> <code>ID_DRIVE_FLASH_CF</code></p>
<dl>
<dd>The device is compatible with Compact Flash.</dl>
<p> <code>ID_DRIVE_FLASH_MS</code></p>
<dl>
<dd>The device is compatible with Memory Stick.</dl>
<p> <code>ID_DRIVE_FLASH_SM</code></p>
<dl>
<dd>The device is compatible with SmartMedia.</dl>
<p> <code>ID_DRIVE_FLASH_SD</code></p>
<dl>
<dd>The device is compatible with SecureDigital.</dl>
<p> <code>ID_DRIVE_FLASH_SDHC</code></p>
<dl>
<dd>The device is compatible with High-Capicity SecureDigital.</dl>
<p> <code>ID_DRIVE_FLASH_MMC</code></p>
<dl>
<dd>The device is compatible with MultiMediaCard.</dl>
<p> <code>ID_DRIVE_FLOPPY</code></p>
<dl>
<dd>The device is compatible with floppy disk.</dl>
<p> <code>ID_DRIVE_FLOPPY_ZIP</code></p>
<dl>
<dd>The device is compatible with Zip.</dl>
<p> <code>ID_DRIVE_FLOPPY_JAZ</code></p>
<dl>
<dd>The device is compatible with Jaz.</dl>
<p> The <code>ID_DRIVE_MEDIA_*</code> properties describe the current media in a device. As with the <code>ID_DRIVE_*</code> properties, these properties are typically set on the main block device (e.g. /dev/sdb). Typically only one of these properties are set. </p>
<p> <code>ID_DRIVE_MEDIA_FLASH</code></p>
<dl>
<dd>The physical media currently inserted into the device is flash.</dl>
<p> <code>ID_DRIVE_MEDIA_FLASH_CF</code></p>
<dl>
<dd>The physical media currently inserted into the device is Compact Flash.</dl>
<p> <code>ID_DRIVE_MEDIA_FLASH_MS</code></p>
<dl>
<dd>The physical media currently inserted into the device is Memory Stick.</dl>
<p> <code>ID_DRIVE_MEDIA_FLASH_SM</code></p>
<dl>
<dd>The physical media currently inserted into the device is SmartMedia.</dl>
<p> <code>ID_DRIVE_MEDIA_FLASH_SD</code></p>
<dl>
<dd>The physical media currently inserted into the device is SecureDigital.</dl>
<p> <code>ID_DRIVE_MEDIA_FLASH_SDHC</code></p>
<dl>
<dd>The physical media currently inserted into the device is High-Capicity SecureDigital.</dl>
<p> <code>ID_DRIVE_MEDIA_FLASH_MMC</code></p>
<dl>
<dd>The physical media currently inserted into the device is MultiMediaCard.</dl>
<p> <code>ID_DRIVE_MEDIA_FLOPPY</code></p>
<dl>
<dd>The physical media currently inserted into the device is floppy disk.</dl>
<p> <code>ID_DRIVE_MEDIA_FLOPPY_ZIP</code></p>
<dl>
<dd>The physical media currently inserted into the device is Zip.</dl>
<p> <code>ID_DRIVE_MEDIA_FLOPPY_JAZ</code></p>
<dl>
<dd>The physical media currently inserted into the device is Jaz.</dl>
<h2>Author</h2>
<p>Written by David Zeuthen david [at] fubar.dk with a lot of help from many others.</p>
<h2>Bugs</h2>
<p>Please send bug reports to either the distribution or the hal mailing list, see m[blue]<code><a rel="nofollow" href="http://lists.freedesktop.org/mailman/listinfo/hal">http://lists.freedesktop.org/mailman/listinfo/hal</a></code>m[]. to subscribe.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-devicekit/">DeviceKit</a></code>(7), <code><a href="/docs/linux/man/8-policykit/">PolicyKit</a></code>(8), <code><a href="/docs/linux/man/8-devkit-disks-daemon/">devkit-disks-daemon</a></code>(8), <code><a href="/docs/linux/man/1-devkit-disks/">devkit-disks</a></code>(1) </p>
