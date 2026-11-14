---
title: "security_check_context_raw(3)"
name: "security_check_context_raw"
section: "3"
letter: "s"
url: "/docs/linux/man/3-security_check_context_raw/"
description: "security_check_context – check the validity of a SELinux context"
---

<p>security_check_context &#8211; check the validity of a SELinux context</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int security_check_context(char *con);
int security_check_context_raw(char *con);</code></pre>
<h2>Description</h2>
<p><code>security_check_context</code>() returns 0 if SELinux is running and the context is valid, otherwise it returns -1. </p>
<p> <code>security_check_context_raw</code>() behaves identically to <code>security_check_context</code>() but does not perform context translation.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
