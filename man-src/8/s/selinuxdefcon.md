---
title: "selinuxdefcon(8)"
name: "selinuxdefcon"
section: "8"
letter: "s"
url: "/docs/linux/man/8-selinuxdefcon/"
description: "selinuxdefcon – report default SELinux context for user"
---

<p>selinuxdefcon &#8211; report default SELinux context for user </p>
<h2>Synopsis</h2>
<p><code>selinuxdefcon [-l level] user fromcon</code> </p>
<h2>Description</h2>
<p><code>selinuxdefcon</code> reports the default context for the specified user from the specified context <code>-l level</code> mcs/mls level </p>
<h2>Example</h2>
<p># selinuxdefcon jsmith system_u:system_r:sshd_t:s0<br />
 unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023</p>
<h2>AUTHOR<tt>&nbsp;<wbr>&nbsp;<wbr></tt></h2>
<p>This manual page was written by Dan Walsh &lt;dwalsh [at] redhat.com&gt;.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-secon/">secon</a>(8), <a href="/docs/linux/man/8-selinuxconlist/">selinuxconlist</a>(8) </p>
