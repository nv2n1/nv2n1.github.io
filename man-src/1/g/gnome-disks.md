---
title: "gnome-disks(1)"
name: "gnome-disks"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-disks/"
description: "gnome-disks – the GNOME Disks application"
---

<h2 class="name">NAME</h2>
<p> gnome-disks &#8211; the GNOME Disks application </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gnome-disks</code> [OPTIONS]</dl>
<h2>DESCRIPTION</h2>
<p> <code>gnome-disks</code></p>
<dd>is the command to launch the GNOME Disks application. Disks provides a way to inspect, format, partition and configure disks and block devices. </p>
<p> The Disks application is <i>single-instance</i>. What this means is that if the application is not already running when the <code>gnome-disks</code> command is invoked, it will get launched and the command invocation will block until the application exits. Otherwise the existing application instance will be used and the <code>gnome-disks</code> command will exit immediately.</p>
<h2>OPTIONS</h2>
<p> The following options are understood: </p>
<p> <code>&#8211;block-device </code><i>DEVICE</i></p>
<dl>
<dt>
<dd> Switches to the Disks application and selects the block device given by <i>DEVICE</i> (for example, /dev/sda).</dl>
<p> <code>&#8211;block-device </code><i>DEVICE</i> <code>&#8211;format-device</code> [<code>&#8211;xid </code><i>WINDOW-ID</i>]</p>
<dl>
<dt>
<dd> Shows the &#8220;Format Volume&#8221; dialog for the block device given by <i>DEVICE</i> (for example, /dev/sdb1). If <i>WINDOW-ID</i> is given, makes the dialog transient to the given XID.</dl>
<p> <code>&#8211;restore-disk-image </code><i>FILE</i></p>
<dl>
<dt>
<dd> Shows the &#8220;Restore Disk Image&#8221; dialog for the file given by <i>FILE</i> (for example, /home/user/Downloads/SuperOS.iso) and prompts the user to choose a disk to restore the image unto.</dl>
<p> <code>-h, &#8211;help</code></p>
<dl>
<dt>
<dd> Prints a short help text and exits.</dl>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;zeuthen [at] gmail.com&gt; with a lot of help from many others.</p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://gitlab.gnome.org/GNOME/gnome-disk-utility/-/issues/">https://gitlab.gnome.org/GNOME/gnome-disk-utility/-/issues/</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gnome-disk-image-mounter/">gnome-disk-image-mounter</a></code>(1), <code><a href="/docs/linux/man/8-udisks/">udisks</a></code>(8) </p>
<h2>Index</h2>
