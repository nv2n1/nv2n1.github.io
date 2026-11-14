---
title: "mount-ecryptfs(8)"
name: "mount-ecryptfs"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mount-ecryptfs/"
description: "mount.ecryptfs – eCryptfs mount helper."
---

<p>mount.ecryptfs &#8211; eCryptfs mount helper.</p>
<h2>Synopsis</h2>
<p><code>mount -t ecryptfs</code> [<i>lower directory</i>] [<i>ecryptfs mount point</i>] </p>
<h2>Description</h2>
<p><code>mount.ecryptfs</code> is eCryptfs mount helper. The mount utility will defer to the mount helper to perform various configuration tasks; use the -i option to bypass the mount helper if you would rather manually specify your mount options. To mount eCryptfs, specify the lower directory (i.e., /root/crypt) for the encrypted files and the eCryptfs mountpoint (i.e., /mnt/crypt) for the decrypted view of the files: <i>mount -t ecryptfs /root/crypt /mnt/crypt</i> </p>
<h2>See Also</h2>
<dl>
<dt><code><a href="/docs/linux/man/7-ecryptfs/">ecryptfs</a></code>(7), <code><a href="/docs/linux/man/8-ecryptfsd/">ecryptfsd</a></code>(8), <code><a href="/docs/linux/man/8-ecryptfs-manager/">ecryptfs-manager</a></code>(8), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8)</p>
<dd>
<dt><i>/usr/share/doc/ecryptfs-utils/ecryptfs-faq.html</i></p>
<dd>
<dt><i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i></p>
<dd>
<h2>Author</h2>
<p>This manpage was written by William Lima &lt;wlima.amadeus [at] gmail.com&gt; for the Ubuntu system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
