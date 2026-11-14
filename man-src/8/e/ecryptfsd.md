---
title: "ecryptfsd(8)"
name: "ecryptfsd"
section: "8"
letter: "e"
url: "/docs/linux/man/8-ecryptfsd/"
description: "ecryptfsd – user-space eCryptfs daemon."
---

<p>ecryptfsd &#8211; user-space eCryptfs daemon.</p>
<h2>Description</h2>
<p><code>ecryptfsd</code> is a userspace daemon that runs as the user performing file operations under the eCryptfs mount point. It services public key requests from the eCryptfs kernel module; these requests are sent via /dev/ecryptfs on file open events. ecryptfsd only needs to be run when a mount is done with a public key module. The daemon can be started simply by running <i>ecryptfsd</i>. ecryptfsd will register itself with the kernel as the daemon that should service all eCryptfs filesystem requests done under the context of the user who runs the daemon. </p>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/7-ecryptfs/">ecryptfs</a></code>(7), <code><a href="/docs/linux/man/8-ecryptfs-manager/">ecryptfs-manager</a></code>(8), <code><a href="/docs/linux/man/8-mount-ecryptfs/">mount.ecryptfs</a></code>(8)</p>
<dd>
<dt><i>/usr/share/doc/ecryptfs-utils/ecryptfs-faq.html</i></p>
<dd>
<dt><i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i></p>
<dd>
<h2>Author</h2>
<p>This manpage was written by William Lima &lt;wlima.amadeus [at] gmail.com&gt; for the Ubuntu system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
