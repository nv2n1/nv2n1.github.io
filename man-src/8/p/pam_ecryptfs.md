---
title: "pam_ecryptfs(8)"
name: "pam_ecryptfs"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pam_ecryptfs/"
description: "pam_ecryptfs – PAM module for eCryptfs"
---

<p>pam_ecryptfs &#8211; PAM module for eCryptfs</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>pam_ecryptfs.so</code> [unwrap]</dl>
<h2>Description</h2>
<dd>pam_ecryptfs is a PAM module that can use the login password to unwrap an ecryptfs mount passphrase stored in ~/.ecryptfs/wrapped-passphrase, and automatically mount a private cryptographic directory.</p>
<h2>Options</h2>
<dl>
<dt><code>unwrap</code></p>
<dd>Use the login passphrase to unwrap an eCryptfs mount passphrase.</p>
<dt></dl>
<h2>Module Services Provided</h2>
<dd>The services <code>auth</code>, and <code>session</code> are supported.</p>
<h2>Examples</h2>
<p>To unwrap a mount passphrase and automatically mount a private directory on login, add the following lines to <i>/etc/pam.d/common-auth</i>:</p>
<dl>
<dd>
<pre> auth required pam_ecryptfs.so unwrap</pre>
</dl>
<p> <i>/etc/pam.d/common-session</i>:</p>
<dl>
<dd>
<pre> session optional pam_ecryptfs.so unwrap</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-ecryptfs/">ecryptfs</a></code>(7), <code><a href="/docs/linux/man/5-pam-conf/">pam.conf</a></code>(5), <code><a href="/docs/linux/man/8-pam-d/">pam.d</a></code>(8), <code><a href="/docs/linux/man/8-pam/">pam</a></code>(8)</p>
<dl>
<dt><i>/usr/share/doc/ecryptfs-utils/ecryptfs-faq.html</i></p>
<dd>
<dt><i><a rel="nofollow" href="http://ecryptfs.org/">http://ecryptfs.org/</a></i></p>
<dd>
<h2>Author</h2>
<p>This manpage was written by Dustin Kirkland &lt;kirkland [at] ubuntu.com&gt; for Ubuntu systems (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation. </p>
<p> On Debian and Ubuntu systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
