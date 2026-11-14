---
title: "umount-ecryptfs_private(1)"
name: "umount-ecryptfs_private"
section: "1"
letter: "u"
url: "/docs/linux/man/1-umount-ecryptfs_private/"
description: "umount.ecryptfs_private – eCryptfs private unmount helper."
---

<p>umount.ecryptfs_private &#8211; eCryptfs private unmount helper.</p>
<h2>Synopsis</h2>
<p><code>umount.ecryptfs_private</code> [-f] </p>
<p> <code>NOTE:</code> This program will <code>not</code> clear the relevant keys from the user&#8217;s keyring. For this reason, it is recommended that users use <code><a href="/docs/linux/man/1-ecryptfs-umount-private/">ecryptfs-umount-private</a></code>(1) instead! </p>
<h2>Options</h2>
<p>Options available for the <code>umount.ecryptfs_private</code> command:</p>
<dl COMPACT>
<dt><code>-f</code></p>
<dd>Force the unmount, ignoring the value of the mount counter in <i>/tmp/ecryptfs-USERNAME-Private</i> </p>
</dl>
<h2>Description</h2>
<p><code>umount.ecryptfs_private</code> is a mount helper utility for non-root users to unmount a cryptographically mounted private directory, ~/Private. </p>
<p> If, and only if:<br />
&nbsp;<wbr>&nbsp;&#8211; the private mount passphrase is in their kernel keyring, and<br />
&nbsp;<wbr>&nbsp;&#8211; the current user owns both&nbsp;~/.Private and&nbsp;~/Private, and<br />
&nbsp;<wbr>&nbsp;&#8211;&nbsp;~/.Private is currently mounted on&nbsp;~/Private<br />
&nbsp;<wbr>&nbsp;&#8211; the mount counter is 0&nbsp;(counter is ignored if -f option is used) </p>
<p> This program will:<br />
&nbsp;<wbr>&nbsp;&#8211; unmount&nbsp;~/Private </p>
<p> The only setuid operationis in this program are the call to <code>umount</code> and updating <code>/etc/mtab</code>. </p>
<p> The system administrator can add the pam_ecryptfs.so module to the PAM stack and automatically perform the unmount on logout. See <code><a href="/docs/linux/man/8-pam_ecryptfs/">pam_ecryptfs</a></code>(8). </p>
<h2>Files</h2>
<p><i>~/.Private</i> &#8211; underlying directory containing encrypted data </p>
<p> <i>~/Private</i> &#8211; mountpoint containing decrypted data (when mounted) </p>
<p> <i>~/.ecryptfs/Private.sig</i> &#8211; file containing signature of mountpoint passphrase </p>
<p> <i>/tmp/ecryptfs-USERNAME-Private</i> &#8211; file containing the mount counter, incremented on each mount, decremented on each unmount </p>
<h2>See Also</h2>
<dl COMPACT>
<dt><code><a href="/docs/linux/man/7-ecryptfs/">ecryptfs</a></code>(7), <code><a href="/docs/linux/man/1-ecryptfs-setup-private/">ecryptfs-setup-private</a></code>(1), <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/1-mount-ecryptfs_private/">mount.ecryptfs_private</a></code>(1), <code><a href="/docs/linux/man/8-pam_ecryptfs/">pam_ecryptfs</a></code>(8)</p>
<dd>
<dt><i>/usr/share/doc/ecryptfs-utils/ecryptfs-faq.html</i></p>
<dd>
<dt><i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i></p>
<dd></dl>
<h2>Author</h2>
<p>This manpage and the <code>umount.ecryptfs_private</code> utility was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
