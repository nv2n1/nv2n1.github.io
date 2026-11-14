---
title: "vzalloc(9)"
name: "vzalloc"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vzalloc/"
description: "vzalloc – allocate virtually contiguous memory with zero fill"
---

<p>vzalloc &#8211; allocate virtually contiguous memory with zero fill</p>
<h2>Synopsis</h2>
<pre><code>void *vzalloc(unsigned long size);</code></pre>
<h2>Arguments</h2>
<p><i>size</i></p>
<dl>
<dd>
<dd>allocation size Allocate enough pages to cover <i>size</i> from the page level allocator and map them into contiguous kernel virtual space. The memory allocated is set to zero.</dl>
<h2>Description</h2>
<p>For tight control over page level allocator and protection flags use <code>__vmalloc</code> instead.</p>
<h2>Copyright</h2>
