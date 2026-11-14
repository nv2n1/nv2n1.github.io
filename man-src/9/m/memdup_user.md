---
title: "memdup_user(9)"
name: "memdup_user"
section: "9"
letter: "m"
url: "/docs/linux/man/9-memdup_user/"
description: "memdup_user – duplicate memory region from user space"
---

<p>memdup_user &#8211; duplicate memory region from user space</p>
<h2>Synopsis</h2>
<pre><code>void *memdup_user(const void __user *src, size_t len);</code></pre>
<h2>Arguments</h2>
<p><i>src</i></p>
<dl>
<dd>
<dd>source address in user space</dl>
<p> <i>len</i></p>
<dl>
<dd>number of bytes to copy</dl>
<h2>Description</h2>
<p>Returns an <code>ERR_PTR</code> on failure.</p>
<h2>Copyright</h2>
