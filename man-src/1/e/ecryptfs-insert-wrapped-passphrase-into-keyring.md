---
title: "ecryptfs-insert-wrapped-passphrase-into-keyring(1)"
name: "ecryptfs-insert-wrapped-passphrase-into-keyring"
section: "1"
letter: "e"
url: "/docs/linux/man/1-ecryptfs-insert-wrapped-passphrase-into-keyring/"
description: "ecryptfs-insert-wrapped-passphrase-into-keyring – unwrap a wrapped passphrase from file and insert into the kernel keyring."
---

<h2 class="name">NAME</h2>
<p> ecryptfs-insert-wrapped-passphrase-into-keyring &#8211; unwrap a wrapped passphrase from file and insert into the kernel keyring.</p>
<h2>SYNOPSIS</h2>
<p> <code>ecryptfs-insert-wrapped-passphrase-into-keyring [file]</code> </p>
<p> printf &quot;%s&quot; &quot;wrapping passphrase&quot; | <code>ecryptfs-insert-wrapped-passphrase-into-keyring [file] &#8211;</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>ecryptfs-insert-wrapped-passphrase-into-keyring</code> is a utility to manually unwrap a passphrase from a file, and insert the unwrapped passphrase into the kernel keyring. </p>
<h2>SEE ALSO</h2>
<dl>
<dt><code><a href="/docs/linux/man/7-ecryptfs/">ecryptfs</a></code>(7), <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1)</p>
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
