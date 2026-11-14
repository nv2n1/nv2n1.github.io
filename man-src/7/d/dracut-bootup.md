---
title: "dracut-bootup(7)"
name: "dracut-bootup"
section: "7"
letter: "d"
url: "/docs/linux/man/7-dracut-bootup/"
description: "dracut.bootup – boot ordering in the initramfs"
---

<p>dracut.bootup &#8211; boot ordering in the initramfs</p>
<h2>Description</h2>
<p>This flow chart illustrates the ordering of the services, if systemd is used in the dracut initramfs. </p>
<dl>
<dd>
<pre> systemd-journal.socket
 |
 v
 dracut-cmdline.service
 |
 v
 dracut-pre-udev.service
 |
 v
 systemd-udevd.service
 |
 v
local-fs-pre.target dracut-pre-trigger.service
 | |
 v v
 (various mounts) (various swap systemd-udev-trigger.service
 | devices...) | (various low-level (various low-level
 | | | services: seed, API VFS mounts:
 v v v tmpfiles, random mqueue, configfs,
 local-fs.target swap.target dracut-initqueue.service sysctl, ...) debugfs, ...)
 | | | | |
 \_______________|____________________ | ___________________|____________________/
 \|/
 v
 sysinit.target
 |
 _________________/|\___________________
 / | \
 | | |
 v | v
 (various | rescue.service
 sockets...) | |
 | | v
 v | rescue.target
 sockets.target |
 | |
 \_________________ | emergency.service
 \| |
 v v
 basic.target emergency.target
 |
 ______________________/|
 / |
 | v
 | dracut-pre-mount.service
 | |
 | v
 | sysroot.mount
 | |
 | v
 | initrd-root-fs.target
 (custom initrd services) |
 | v
 | dracut-mount.service
 | |
 | v
 | initrd-parse-etc.service
 | |
 | v
 | (sysroot-usr.mount and
 | various mounts marked
 | with fstab option
 | x-initrd.mount)
 | |
 | v
 | initrd-fs.target
 \______________________ |
 \|
 v
 initrd.target
 |
 v
 dracut-pre-pivot.service
 |
 v
 initrd-cleanup.service
 isolates to
 initrd-switch-root.target
 |
 v
 ______________________/|
 / |
 | initrd-udevadm-cleanup-db.service
 | |
 (custom initrd services) |
 | |
 \______________________ |
 \|
 v
 initrd-switch-root.target
 |
 v
 initrd-switch-root.service
 |
 v
 switch-root</pre>
</dl>
<h2>Author</h2>
<p>Harald Hoyer</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dracut/">dracut</a></code>(8) <code><a href="/docs/linux/man/7-bootup/">bootup</a></code>(7) </p>
