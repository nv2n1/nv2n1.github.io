---
title: "vmalloc_node(9)"
name: "vmalloc_node"
section: "9"
letter: "v"
url: "/docs/linux/man/9-vmalloc_node/"
description: "vmalloc_node – allocate memory on a specific node"
---

<p>vmalloc_node &#8211; allocate memory on a specific node</p>
<h2>Synopsis</h2>
<pre><code>void *vmalloc_node(unsigned long size, int node);</code></pre>
<h2>Arguments</h2>
<p><i>size</i></p>
<dl>
<dd>
<dd>allocation size</dl>
<p> <i>node</i></p>
<dl>
<dd>numa node</dl>
<h2>Description</h2>
<p>Allocate enough pages to cover <i>size</i> from the page level allocator and map them into contiguous kernel virtual space. </p>
<p> For tight control over page level allocator and protection flags use <code>__vmalloc</code> instead.</p>
<h2>Copyright</h2>
