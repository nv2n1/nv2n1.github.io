---
title: "ecryptfs-wrap-passphrase(1)"
name: "ecryptfs-wrap-passphrase"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecryptfs-wrap-passphrase/"
description: "ecryptfs-wrap-passphrase – wrap an eCryptfs mount passphrase."
---

<h2 class="name">NAME</h2>
<p> ecryptfs-wrap-passphrase &#8211; wrap an eCryptfs mount passphrase.</p>
<h2>SYNOPSIS</h2>
<p> <code>ecryptfs-wrap-passphrase [file]</code> </p>
<p> printf &quot;%s
%s&quot; &quot;passphrase to wrap&quot; &quot;wrapping passphrase&quot; | <code>ecryptfs-wrap-passphrase [file] &#8211;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ecryptfs-wrap-passphrase</code> is a utility to wrap an eCryptfs mount passphrase, using a specified wrapping passphrase, and write the encrypted output to file. </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/7-ecryptfs/">ecryptfs</a></code>(7), <code><a href="/docs/linux/man/1-ecryptfs-rewrap-passphrase/">ecryptfs-rewrap-passphrase</a></code>(1), <code><a href="/docs/linux/man/1-ecryptfs-unwrap-passphrase/">ecryptfs-unwrap-passphrase</a></code>(1)</p>
<dd>
<dt><i>/usr/share/doc/ecryptfs-utils/ecryptfs-faq.html</i></p>
<dd>
<dt><i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i></p>
<dd>
</dl>
<h2>AUTHOR</h2>
<p> This manpage was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>Index</h2>
