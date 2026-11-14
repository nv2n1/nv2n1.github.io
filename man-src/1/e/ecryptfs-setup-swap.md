---
title: "ecryptfs-setup-swap(1)"
name: "ecryptfs-setup-swap"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecryptfs-setup-swap/"
description: "ecryptfs-setup-swap – ensure that any swap space is encrypted"
---

<h2 class="name">NAME</h2>
<p> ecryptfs-setup-swap &#8211; ensure that any swap space is encrypted</p>
<h2>SYNOPSIS</h2>
<p> <code>ecryptfs-setup-swap</code> [-f|&#8211;force] </p>
<h2>DESCRIPTION</h2>
<p> This script will detect existing swap partitions or swap files, and encrypt them, using cryptsetup. </p>
<p> Encrypted swap is essential to securing any system using eCryptfs, since decrypted file contents will exist in the system&#8217;s memory, which may be swapped to disk at any time. If the system swap space is not also encrypted, it is possible that decrypted files could be written to disk in clear text. </p>
<p> Note that most Linux distributions do not yet support resuming from an encrypted swap space, and thus hibernate/resume will not work. Suspend/resume is unaffected. </p>
<p> Upon running the utility, the user will be informed of the hibernate/resume break, and asked to confirm the behavior. The -f|&#8211;force option can be used to bypass this interactive prompt. </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/8-cryptsetup/">cryptsetup</a></code>(8)</p>
<dd>
<dt><i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This manpage and the utility was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
