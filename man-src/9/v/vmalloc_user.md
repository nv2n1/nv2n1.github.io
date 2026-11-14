---
title: "vmalloc_user(9)"
name: "vmalloc_user"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vmalloc_user/"
---

vmalloc_user - allocate zeroed virtually contiguous memory for userspace

<h2>Synopsis</h2>

<pre><code>void *vmalloc_user(unsigned long size);</code></pre>

<h2>Arguments</h2>

<i>size</i>
<dl><dd><dd>allocation size</dl>

<h2>Description</h2>

The resulting memory area is zeroed so it can be mapped to userspace without leaking data.

<h2>Copyright</h2>


