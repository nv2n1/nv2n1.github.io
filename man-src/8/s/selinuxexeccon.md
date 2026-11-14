---
title: "selinuxexeccon(8)"
name: "selinuxexeccon"
section: "8"
letter: "s"
url: "/docs/linux/man/8-selinuxexeccon/"
description: "selinuxexeccon – report SELinux context used for this executable"
---

<p>selinuxexeccon &#8211; report SELinux context used for this executable</p>
<h2>Synopsis</h2>
<p><code>selinuxexeccon</code> <i>command</i> [<i>fromcon</i>]</p>
<h2>Description</h2>
<p><code>selinuxexeccon</code> reports the SELinux process context for the specified command from the specified context or the current context.</p>
<h2>Example</h2>
<pre># selinuxexeccon /usr/bin/passwd 
staff_u:staff_r:passwd_t:s0-s0:c0.c1023
# selinuxexeccon /usr/sbin/sendmail system_u:system_r:httpd_t:s0
system_u:system_r:system_mail_t:s0</pre>
<h2>Author</h2>
<p>This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-secon/">secon</a></code>(8) </p>
