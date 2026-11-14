---
title: "ecryptfs-mount-private(1)"
name: "ecryptfs-mount-private"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecryptfs-mount-private/"
description: "ecryptfs-mount-private – interactive eCryptfs private mount wrapper script."
---

<h2 class="name">NAME</h2>
<p> ecryptfs-mount-private &#8211; interactive eCryptfs private mount wrapper script.</p>
<h2>SYNOPSIS</h2>
<p> <code>ecryptfs-mount-private</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ecryptfs-mount-private</code> is a wrapper script for the <code>mount.ecryptfs_private</code> utility that will interactively prompt for the user&#8217;s login password, if necessary. </p>
<h2>FILES</h2>
<p> <i>~/.Private</i> &#8211; underlying directory containing encrypted data </p>
<p> <i>~/Private</i> &#8211; mountpoint containing decrypted data (when mounted) </p>
<p> <i>~/.ecryptfs/Private.sig</i> &#8211; file containing signature of mountpoint passphrase </p>
<p> <i>~/.ecryptfs/wrapped-passphrase</i> &#8211; file containing the wrapped passphrase </p>
<p> <i>~/.ecryptfs/wrapping-independent</i> &#8211; this file exists if the wrapping passphrase is independent from login passphrase </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-mount-ecryptfs_private/">mount.ecryptfs_private</a></code>(1), <code><a href="/docs/linux/man/1-ecryptfs-umount-private/">ecryptfs-umount-private</a></code>(1)</p>
<dd>
<dt><i>/usr/share/doc/ecryptfs-utils/ecryptfs-faq.html</i></p>
<dd>
<dt><i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This manpage and the <code>ecryptfs-mount-private</code> utility was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
