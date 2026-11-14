---
title: "ecryptfs-find(1)"
name: "ecryptfs-find"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecryptfs-find/"
description: "ecryptfs-find – use inode numbers to match encrypted/decrypted filenames"
---

<h2 class="name">NAME</h2>
<p> ecryptfs-find &#8211; use inode numbers to match encrypted/decrypted filenames</p>
<h2>SYNOPSIS</h2>
<p> <code>ecryptfs-find</code> cleartext-filename <code>ecryptfs-find</code> ECRYPTFS_FNEK_ENCRYPTED.fwBGx18a.UcYl18CF7VKLMSDuEadV </p>
<h2>DESCRIPTION</h2>
<p> This program will attempt to match encrypted filenames to their decrypted counterpart, and attempt to match decrypted filenames to their encrypted counterpart. </p>
<p> Notes:<br />
&nbsp;&#8211; the eCryptfs filesystem must be mounted in order to work<br />
&nbsp;&#8211; it uses&nbsp;<code><a href="/docs/linux/man/1-ls/">ls</a></code>(1)&nbsp;in order to determine the inode<br />
&nbsp;&#8211; it uses&nbsp;<code><a href="/docs/linux/man/1-find/">find</a></code>(1)&nbsp;in order to locate the inode </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) </p>
<p> <i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i> </p>
<h2>AUTHOR</h2>
<p> This manpage was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
