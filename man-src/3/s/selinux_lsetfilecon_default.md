---
title: "selinux_lsetfilecon_default(3)"
name: "selinux_lsetfilecon_default"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_lsetfilecon_default/"
description: "selinux_lsetfilecon_default – set the file context to the system defaults"
---

<p>selinux_lsetfilecon_default &#8211; set the file context to the system defaults</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int selinux_lsetfilecon_default(const char *path);</code></pre>
<h2>Description</h2>
<p><code>selinux_lsetfilecon_default</code>() sets the file context to the system defaults.</p>
<h2>Return Value</h2>
<p>Returns zero on success or -1 otherwise.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8), <code><a href="/docs/linux/man/3-selinux_file_context_cmp/">selinux_file_context_cmp</a></code>(3), <code><a href="/docs/linux/man/3-selinux_file_context_verify/">selinux_file_context_verify</a></code>(3), <code><a href="/docs/linux/man/3-matchpathcon/">matchpathcon</a></code>(3), <code><a href="/docs/linux/man/3-freecon/">freecon</a></code>(3), <code><a href="/docs/linux/man/3-setfilecon/">setfilecon</a></code>(3), <code><a href="/docs/linux/man/3-setfscreatecon/">setfscreatecon</a></code>(3) </p>
