---
title: "pumount(1)"
name: "pumount"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pumount/"
description: "pumount – umount arbitrary hotpluggable devices as normal user"
---

<h2 class="name">NAME</h2>
<p> pumount &#8211; umount arbitrary hotpluggable devices as normal user</p>
<h2>SYNOPSIS</h2>
<p> <code>pumount</code> [ <i>options</i> ] <i>device</i> </p>
<h2>DESCRIPTION</h2>
<p> pumount is a wrapper around the standard umount program which permits normal users to umount removable devices without a matching /etc/fstab entry. </p>
<p> pumount also supports encrypted devices which use dm-crypt and have LUKS metadata. If a LUKS-capable <code>cryptsetup</code> is installed, pumount will umount the mapped device instead and call cryptsetup to close the decrypted device afterwards. </p>
<p> <code>pumount</code> expects the <i>device</i> as its only argument. This will umount <i>device</i> from a directory below /media if policy is met (see below). </p>
<p> Please note that, as with <code>pmount</code>, you can use labels and uuids as described in <code>fstab</code> (5) for devices present in <i>/etc/fstab</i>. In this case, the device name need to match exactly the corresponding entry in <i>/etc/fstab</i>, including the <i>LABEL=</i> or <i>UUID=</i> part. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l, &#8211;lazy</code></p>
<dd> Lazy unmount. Detach the filesystem from the filesystem hierarchy now, and cleanup all references to the filesystem as soon as it is not busy anymore. (Requires kernel 2.4.11 or later.) <code>IMPORTANT NOTES</code> This option should not be used unless you <code>really</code> know what you are doing, as chances are high that it will result in data loss on the removable drive. Please run <code>pumount</code> manually and wait until it finishes. In addition, <code>pumount</code> will not <i>luksClose</i> a device which was unmounted lazily. </p>
<dt><code>&#8211;luks-force</code></p>
<dd> Normally, <code>pumount</code> will not <i>luksClose</i> (see <i><a href="/docs/linux/man/1-cryptsetup/">cryptsetup</a></i>(1)) a device <code>pmount</code> did not open. However, you can bypass this restriction with this flag. You probably will need it if you did mess around with the <i>/var/lock/pmount_luks</i> directory. </p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print a help message and exit successfully. </p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Enable verbose debug messages. </p>
<dt><code>&#8211;version</code></p>
<dd> Print the current version number and exit successfully. </p>
</dl>
<h2>POLICY</h2>
<p> The umount will succeed if all of the following conditions are met: </p>
<dl>
<dt>&bull;</p>
<dd> <i>device</i> is a block device in /dev/ (it does not need to exist if <code>-l</code> is supplied)</p>
<dt>&bull;</p>
<dd> <i>device</i> is not in /etc/fstab (if it is, pmount executes <code> umount </code><i> device</i> as the calling user to handle this transparently)</p>
<dt>&bull;</p>
<dd> <i>device</i> is mounted according to /etc/mtab and /proc/mounts with the calling user&#8217;s uid</p>
<dt>&bull;</p>
<dd> mount point is in /media </p>
</dl>
<h2>PUMOUNT AND MISSING DEVICES</h2>
<p> <code>pumount</code> now supports unmounting devices that have gone missing for some reason, such as a brutal removal of the device, or a kernel/hardware problem. Just specify the mount point as argument for <code>pumount</code>. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmount/">pmount</a></code>(1), <code><a href="/docs/linux/man/1-cryptsetup/">cryptsetup</a></code>(1), <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8) </p>
<h2>AUTHOR</h2>
<p> <code>pmount</code> is developed by Martin Pitt &lt;martin.pitt [at] canonical.com&gt;. </p>
<h2>Index</h2>
