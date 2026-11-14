---
title: "fusermount3(1)"
name: "fusermount3"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fusermount3/"
description: "fusermount3 – mount and unmount FUSE filesystems"
---

<h2 class="name">NAME</h2>
<p> <code>fusermount3</code> &#8211; mount and unmount FUSE filesystems</p>
<h2>SYNOPSIS</h2>
<p> <code>fusermount3</code> [<i>OPTIONS</i>] <i>MOUNTPOINT</i> </p>
<h2>DESCRIPTION</h2>
<p> Filesystem in Userspace (FUSE) is a simple interface for userspace programs to export a virtual filesystem to the Linux kernel. It also aims to provide a secure method for non privileged users to create and mount their own filesystem implementations. </p>
<p> <code>fusermount3</code> is a program to mount and unmount FUSE filesystems. It should be called directly only for unmounting FUSE file systems. To allow mounting and unmounting by unprivileged users, <code>fusermount3</code> needs to be installed set-uid root.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-h</p>
<dd> print help.</p>
<dt>-V</p>
<dd> print version.</p>
<dt>-o <i>OPTION</i>[,<i>OPTION</i>&#8230;]</p>
<dd> mount options.</p>
<dt>-u</p>
<dd> unmount.</p>
<dt>-q</p>
<dd> quiet.</p>
<dt>-z</p>
<dd> lazy unmount. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-mount/">mount</a></i>(8), <i><a href="/docs/linux/man/8-mount-fuse3/">mount.fuse3</a></i>(8), <i><a href="/docs/linux/man/4-fuse/">fuse</a></i>(4), </p>
<h2>HOMEPAGE</h2>
<p> More information about fusermount3 and the FUSE project can be found at &lt;<i><a rel="nofollow" href="http://fuse.sourceforge.net/">http://fuse.sourceforge.net/</a></i>&gt;. </p>
<h2>AUTHORS</h2>
<p> FUSE is currently maintained by Nikolaus Rath &lt;Nikolaus [at] rath.org&gt; </p>
<p> The original author of FUSE is Miklos Szeredi &lt;<i>miklos [at] szeredi.hu</i>&gt;. </p>
<p> This manual page was originally written by Daniel Baumann &lt;<i>daniel.baumann [at] progress-technologies.net</i>&gt;. </p>
<h2>Index</h2>
