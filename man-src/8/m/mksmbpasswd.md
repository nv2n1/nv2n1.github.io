---
title: "mksmbpasswd(8)"
name: "mksmbpasswd"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mksmbpasswd/"
description: "mksmbpasswd – formats a /etc/passwd entry for a smbpasswd file"
---

<p>mksmbpasswd &#8211; formats a /etc/passwd entry for a smbpasswd file</p>
<h2>Synopsis</h2>
<p>mksmbpasswd cat /etc/passwd | /usr/sbin/mksmbpasswd &gt; /etc/samba/smbpasswd</p>
<h2>Description</h2>
<p><code>mksmbpasswd</code> should be used only once, the first time Samba is installed. The idea is to ease accounts creation by transferring all user accounts from /etc/passwd to /etc/samba/smbpasswd. </p>
<p> Please note that passwords are not transferred automatically from /etc/passwd to the new /etc/samba/smbpasswd file. After running <code>mksmbpasswd</code> all accounts are disabled so the system administrator must run smbpasswd for each account that needs to be enable.</p>
<h2>Files</h2>
<dl>
<dt>/etc/passwd</p>
<dd>System wide accounts file</p>
<dt>/etc/samba/smbpasswd</p>
<dd>Encrypted passwords file for the Samba daemons</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/7-samba/">samba</a>(7), <a href="/docs/linux/man/8-nmbd/">nmbd</a>(8), <a href="/docs/linux/man/8-smbd/">smbd</a>(8)</p>
<h2>Author</h2>
<p>Eloy A. Paris &lt;peloy [at] debian.org&gt; (man page based on sendmailconfig&#8217;s man page by Robert Leslie &lt;rob [at] mars.org&gt;)</p>
