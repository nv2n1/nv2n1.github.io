---
title: "selinux_check_securetty_context(3)"
name: "selinux_check_securetty_context"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selinux_check_securetty_context/"
description: "selinux_check_securetty_context – check whether a SELinux tty security context is defined as a securetty context"
---

<p>selinux_check_securetty_context &#8211; check whether a SELinux tty security context is defined as a securetty context</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int selinux_check_securetty_context(char *tty_context);</code></pre>
<h2>Description</h2>
<p><code>selinux_check_securetty_context</code>() returns 0 if tty_context is a securetty context, returns &lt; 0 otherwise.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
