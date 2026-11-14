---
title: "ecryptfs-rewrite-file(1)"
name: "ecryptfs-rewrite-file"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecryptfs-rewrite-file/"
description: "ecryptfs-rewrite-file – force a file to be rewritten (reencrypted) in the lower filesystem"
---

<h2 class="name">NAME</h2>
<p> ecryptfs-rewrite-file &#8211; force a file to be rewritten (reencrypted) in the lower filesystem</p>
<h2>SYNOPSIS</h2>
<p> <code>ecryptfs-rewrite-file [file1] [file2] [file3] &#8230;</code> </p>
<h2>DESCRIPTION</h2>
<p> This script takes one or more files/directories/symlinks as arguments, moves each of them to a temporary file, and then moves them back to the original name. This causes the file to be rewritten (and reencrypted) in the lower filesystem. </p>
<p> This script may be combined with <code><a href="/docs/linux/man/1-find/">find</a></code>(1) and <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1) to rewrite an entire eCryptfs mountpoint, unmount, and sync: </p>
<p>&nbsp;<wbr>&nbsp;find . -xdev -print0 | xargs -r -0&nbsp;/usr/bin/ecryptfs-rewrite-file<br />
&nbsp;<wbr>&nbsp;ecryptfs-umount-private<br />
&nbsp;<wbr>&nbsp;sync </p>
<p> It is advised that this script is executed in runlevel 1 or 3, to avoid simultanteous writes and race conditions with targeted files. </p>
<p> <code>USING THIS SCRIPT WHILE GNOME, KDE, OR OTHER APPLICATIONS ARE RUNNING MAY CAUSE DATA LOSS.</code> </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1), <code><a href="/docs/linux/man/1-ecryptfs-umount-private/">ecryptfs-umount-private</a></code>(1), <code><a href="/docs/linux/man/1-sync/">sync</a></code>(1)</p>
<dd>
<dt><i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This manpage was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
