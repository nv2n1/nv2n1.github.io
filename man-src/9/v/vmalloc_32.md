---
title: "vmalloc_32(9)"
name: "vmalloc_32"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vmalloc_32/"
---

vmalloc_32 - allocate virtually contiguous memory (32bit addressable)

<h2>Synopsis</h2>

<pre><code>void *vmalloc_32(unsigned long size);</code></pre>

<h2>Arguments</h2>

<i>size</i>
<dl><dd><dd>allocation size</dl>

<h2>Description</h2>

Allocate enough 32bit PA addressable pages to cover <i>size</i> from the page level allocator and map them into contiguous kernel virtual space.

<h2>Copyright</h2>


