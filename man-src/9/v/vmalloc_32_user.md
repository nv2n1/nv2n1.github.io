---
title: "vmalloc_32_user(9)"
name: "vmalloc_32_user"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vmalloc_32_user/"
---

vmalloc_32_user - allocate zeroed virtually contiguous 32bit memory

<h2>Synopsis</h2>

<pre><code>void *vmalloc_32_user(unsigned long size);</code></pre>

<h2>Arguments</h2>

<i>size</i>
<dl><dd><dd>allocation size</dl>

<h2>Description</h2>

The resulting memory area is 32bit addressable and zeroed so it can be mapped to userspace without leaking data.

<h2>Copyright</h2>


