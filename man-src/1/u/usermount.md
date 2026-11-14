---
title: "usermount(1)"
name: "usermount"
section: "1"
letter: "u"
url: "/docs/linux/man/1-usermount/"
description: "usermount – A graphical tool to mount, unmount and format filesystems."
---

<h2>NAME</h2>
<p> usermount &#8211; A graphical tool to mount, unmount and format filesystems.</p>
<h2>SYNOPSIS</h2>
<p> <code>usermount</code> [ <i>options</i> ] </p>
<p> <code>userformat</code> [ <i>options</i> ] <i>device</i></p>
<h2>DESCRIPTION</h2>
<p> <code>usermount</code> is a graphical tool to allow users to easily manage removable media, such as floppy disks or zip disks. When the tool starts up, it scans <i>/etc/fstab</i> for all filesystems that have been configured to allow users to mount and unmount them. The filesystem can be mounted or unmounted by pressing the toggle button labeled <i>Mount</i>. </p>
<p> Also, if the user has the appropriate permissions for the device, the <i>Format</i> button will be active. This allows the user to format disks using <code>fdformat</code> and create a new filesystem of the type listed (using <code>mkfs</code> with the appropriate option). Naturally, the user will be prompted for confirmation before actually destroying data on the device. </p>
<p> Note that if a device is already mounted, the format button is inactive for all entries that share the same device. </p>
<p> When run as root, <code>usermount</code> displays all of the entries in <i>/etc/fstab</i> rather than just the ones with the <i>user</i> option. </p>
<p> Invoking <code>userformat</code> <i>device</i> allows formatting <i>device</i>, as if by selecting <i>device</i> in the <code>userformat</code> window, and by clicking the <i>Format</i> button.</p>
<h2>OPTIONS</h2>
<p> This program has no command line options of it&#8217;s own, but it does take the standard X program options like <code>-display</code> and such. See the <i><a href="/docs/linux/man/1-x/">X</a></i>(1) man page for some of the common options.</p>
<h2>FILES</h2>
<dl>
<dt><i>/etc/fstab</i></p>
<dd> The system file describing the mountable filesystems.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-mount/">mount</a></i>(8), <i><a href="/docs/linux/man/8-fdformat/">fdformat</a></i>(8), <i><a href="/docs/linux/man/8-mkfs/">mkfs</a></i>(8), <i><a href="/docs/linux/man/5-fstab/">fstab</a></i>(5) <i><a href="/docs/linux/man/1-x/">X</a></i>(1)</p>
<h2>BUGS</h2>
<p> Mount entries with a filesystem type of iso9660 are outright considered CD-ROMs and the format button is always disabled. </p>
<p> Mount entries for swap files or partitions are also ignored. A nice feature might be to allow root to turn swap on and off for swap partitions.</p>
<h2>AUTHOR</h2>
<p> Otto Hammersmith &lt;otto [at] redhat.com&gt; </p>
<h2>Index</h2>
