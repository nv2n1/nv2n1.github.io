---
title: "vmalloc(9)"
name: "vmalloc"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vmalloc/"
description: "vmalloc – allocate virtually contiguous memory"
---

<p>vmalloc &#8211; allocate virtually contiguous memory</p>
<h2>Synopsis</h2>
<pre><code>void *vmalloc(unsigned long size);</code></pre>
<h2>Arguments</h2>
<p><i>size</i></p>
<dl>
<dd>
<dd>allocation size Allocate enough pages to cover <i>size</i> from the page level allocator and map them into contiguous kernel virtual space.</dl>
<h2>Description</h2>
<p>For tight control over page level allocator and protection flags use <code>__vmalloc</code> instead.</p>
<h2>Copyright</h2>
