---
title: "grub-mount(1)"
name: "grub-mount"
section: "1"
letter: "g"
url: "/docs/linux/man/1-grub-mount/"
description: "grub-mount – export GRUB filesystem with FUSE"
---

<h2 class="name">NAME</h2>
<p> grub-mount &#8211; export GRUB filesystem with FUSE </p>
<h2>SYNOPSIS</h2>
<p> <code>grub-mount</code> [<i>,OPTION/</i>&#8230;] <i>,IMAGE1 /</i>[<i>,IMAGE2 /</i>&#8230;] <i>,MOUNTPOINT/</i></p>
<h2>DESCRIPTION</h2>
<p> Debug tool for filesystem driver.</p>
<dl>
<dt><code>-C</code>, <code>&#8211;crypto</code></dt>
<dd> Mount crypto devices.</dd>
<dt><code>-d</code>, <code>&#8211;debug</code>=<i>,STRING/</i></dt>
<dd> Set debug environment variable.</dd>
<dt><code>-K</code>, <code>&#8211;zfs-key</code>=<i>,FILE/</i>|prompt</dt>
<dd> Load zfs crypto key.</dd>
<dt><code>-r</code>, <code>&#8211;root</code>=<i>,DEVICE_NAME/</i></dt>
<dd> Set root device.</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> print verbose messages.</dd>
<dt>-?, <code>&#8211;help</code></dt>
<dd> give this help list</dd>
<dt><code>&#8211;usage</code></dt>
<dd> give a short usage message</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> print program version</dd></dl>
<p> Mandatory or optional arguments to long options are also mandatory or optional for any corresponding short options.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>grub-mount</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>grub-mount</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info grub-mount</code></dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
