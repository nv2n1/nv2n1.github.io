---
title: "selinux_getpolicytype(3)"
name: "selinux_getpolicytype"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_getpolicytype/"
description: "selinux_getpolicytype – get the type of SELinux policy running on the system"
---

<p>selinux_getpolicytype &#8211; get the type of SELinux policy running on the system</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int selinux_getpolicytype(char **policytype);</code></pre>
<h2>Description</h2>
<p><code>selinux_getpolicytype</code>() Reads the contents of the <i>/etc/selinux/config</i> file to determine the SELinux policy used on the system, and sets <i>policytype</i> accordingly. Free <i>policytype</i> with <code><a href="/docs/linux/man/3-free/">free</a></code>(3).</p>
<h2>Return Value</h2>
<p>On success, zero is returned. On failure, -1 is returned.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
