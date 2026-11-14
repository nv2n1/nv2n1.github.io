---
title: "mount-ecryptfs_private(1)"
name: "mount-ecryptfs_private"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mount-ecryptfs_private/"
description: "mount.ecryptfs_private – eCryptfs private mount helper."
---

<p>mount.ecryptfs_private &#8211; eCryptfs private mount helper.</p>
<h2>Synopsis</h2>
<p><code>mount.ecryptfs_private [ALIAS]</code> </p>
<p> <code>NOTE:</code> This program will <code>not</code> dynamically load the relevant keys. For this reason, it is recommended that users use <code><a href="/docs/linux/man/1-ecryptfs-mount-private/">ecryptfs-mount-private</a></code>(1) instead! </p>
<h2>Description</h2>
<p><code>mount.ecryptfs_private</code> is a mount helper utility for non-root users to cryptographically mount a private directory, ~/Private by default. </p>
<p> This program optionally takes one argument, ALIAS. If ALIAS is omitted, the program will default to using &quot;Private&quot; using:<br />
&nbsp;&#8211;&nbsp;$HOME/.Private as the SOURCE<br />
&nbsp;&#8211;&nbsp;$HOME/Private as the DESTINATION<br />
&nbsp;&#8211;&nbsp;$HOME/.ecryptfs/Private.sig for the key signatures. </p>
<p> If ALIAS is specified, then the program will look for an <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5) style configuration in:<br />
&nbsp;&#8211;&nbsp;$HOME/.ecryptfs/ALIAS.conf and for key signature(s) in:<br />
&nbsp;&#8211;&nbsp;$HOME/.ecryptfs/ALIAS.sig </p>
<p> The mounting will proceed if, and only if:<br />
&nbsp;<wbr>&nbsp;&#8211; the required passphrase is in their kernel keyring, and<br />
&nbsp;<wbr>&nbsp;&#8211; the current user owns both the SOURCE and DESTINATION mount points<br />
&nbsp;<wbr>&nbsp;&#8211; the DESTINATION is not already mounted </p>
<p> This program will:<br />
&nbsp;<wbr>&nbsp;&#8211; mount SOURCE onto DESTINATION<br />
&nbsp;<wbr>&nbsp;&#8211; as an ecryptfs filesystem<br />
&nbsp;<wbr>&nbsp;&#8211; using the AES cipher<br />
&nbsp;<wbr>&nbsp;&#8211; with a key length of 16 bytes<br />
&nbsp;<wbr>&nbsp;&#8211; using the passphrase whose signature is in&nbsp;~/.ecryptfs/Private.sig </p>
<p> The only setuid operation in this program is the call to <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8) or <code><a href="/docs/linux/man/8-umount/">umount</a></code>(8). </p>
<p> The <code><a href="/docs/linux/man/1-ecryptfs-setup-private/">ecryptfs-setup-private</a></code>(1) utility will create the ~/.Private and ~/Private directories, generate a mount passphrase, wrap the passphrase, and write the ~/.ecryptfs/Private.sig. </p>
<p> The system administrator can add the pam_ecryptfs.so module to the PAM stack which will automatically use the login passphrase to unwrap the mount passphrase, add the passphrase to the user&#8217;s kernel keyring, and automatically perform the mount. See <code><a href="/docs/linux/man/8-pam_ecryptfs/">pam_ecryptfs</a></code>(8). </p>
<h2>Files</h2>
<p><i>~/.Private</i> &#8211; underlying directory containing encrypted data </p>
<p> <i>~/Private</i> &#8211; mountpoint containing decrypted data (when mounted) </p>
<p> <i>~/.ecryptfs/Private.sig</i> &#8211; file containing signature of mountpoint passphrase </p>
<p> <i>~/.ecryptfs/wrapped-passphrase</i> &#8211; mount passphrase, encrypted with the login passphrase </p>
<h2>See Also</h2>
<dl COMPACT>
<dt><code><a href="/docs/linux/man/7-ecryptfs/">ecryptfs</a></code>(7), <code><a href="/docs/linux/man/1-ecryptfs-rewrap-passphrase/">ecryptfs-rewrap-passphrase</a></code>(1), <code><a href="/docs/linux/man/1-ecryptfs-setup-private/">ecryptfs-setup-private</a></code>(1), <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/8-mount/">mount</a></code>(8), <code><a href="/docs/linux/man/1-umount-ecryptfs_private/">umount.ecryptfs_private</a></code>(1), <code><a href="/docs/linux/man/8-pam_ecryptfs/">pam_ecryptfs</a></code>(8), <code><a href="/docs/linux/man/5-fstab/">fstab</a></code>(5)</p>
<dd>
<dt><i>/usr/share/doc/ecryptfs-utils/ecryptfs-faq.html</i></p>
<dd>
<dt><i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i></p>
<dd></dl>
<h2>Author</h2>
<p>This manpage and the <code>mount.ecryptfs_private</code> utility was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
