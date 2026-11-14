---
title: "security_disable(3)"
name: "security_disable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-security_disable/"
description: "security_disable – disable the SELinux kernel code at runtime"
---

<p>security_disable &#8211; disable the SELinux kernel code at runtime</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;
int security_disable(void);</code></pre>
<h2>Description</h2>
<p><code>security_disable</code>() disables the SELinux kernel code, unregisters selinuxfs from <i>/proc/filesystems</i>, and then unmounts <i>/sys/fs/selinux</i>. </p>
<p> This function can only be called at runtime and prior to the initial policy load. After the initial policy load, the SELinux kernel code cannot be disabled, but only placed in &quot;permissive&quot; mode by using <code><a href="/docs/linux/man/3-security_setenforce/">security_setenforce</a>(3).</code></p>
<h2>Return Value</h2>
<p><code>security_disable</code>() returns zero on success or -1 on error.</p>
<h2>Author</h2>
<p>This manual page has been written by Guido Trentalancia &lt;guido [at] trentalancia.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8),<code> setenforce (8)</code> </p>
