---
title: "gnome-disk-image-mounter(1)"
name: "gnome-disk-image-mounter"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-disk-image-mounter/"
description: "gnome-disk-image-mounter – Attach and mount disk images"
---

<h2 class="name">NAME</h2>
<p> gnome-disk-image-mounter &#8211; Attach and mount disk images </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>gnome-disk-image-mounter</code> [&#8211;writable] [<i>URI</i>&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>gnome-disk-image-mounter</code></p>
<dd>can be used to set up disk images. Both regular files and <i>GVfs</i> URIs (such as <a href="smb://filer/media/file.iso)">smb://filer/media/file.iso)</a> can be used in the <i>URI</i> parameter. If no <i>URI</i>s are given and a window server is running, a graphical file chooser will be presented. </p>
<p> Note that <code>gnome-disk-image-mounter</code> will not mount filesystems or unlock encrypted volumes in the disk image &#8211; this responsibility is left to the automounter in GNOME Shell to ensure that the same interactions happen as if the disk image was a regular physical device or disc. </p>
<p> By default the disk images are attached read-only, use the option <code>&#8211;writable</code> to change this.</p>
<h2>RETURN VALUE</h2>
<p> <code>gnome-disk-image-mounter</code> returns 0 on success and non-zero on failure.</p>
<h2>AUTHOR</h2>
<p> Written by David Zeuthen &lt;zeuthen [at] gmail.com&gt; with a lot of help from many others.</p>
<h2>BUGS</h2>
<p> Please send bug reports to either the distribution bug tracker or the upstream bug tracker at m[blue]<code><a rel="nofollow" href="https://gitlab.gnome.org/GNOME/gnome-disk-utility/-/issues/">https://gitlab.gnome.org/GNOME/gnome-disk-utility/-/issues/</a></code>m[].</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gnome-shell/">gnome-shell</a></code>(1), <code><a href="/docs/linux/man/1-gnome-disks/">gnome-disks</a></code>(1), <code><a href="/docs/linux/man/8-udisks/">udisks</a></code>(8), <code><a href="/docs/linux/man/8-losetup/">losetup</a></code>(8) </p>
<h2>Index</h2>
