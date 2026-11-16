---
title: "kzalloc_node(9)"
name: "kzalloc_node"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kzalloc_node/"
---

kzalloc_node - allocate zeroed memory from a particular memory node.

<h2>Synopsis</h2>

<pre><code>void *kzalloc_node(size_t size, gfp_t flags, int node);</code></pre>

<h2>Arguments</h2>

<i>size</i>
<dl><dd></dd><dd>how many bytes of memory are required.</dd></dl>
 

 <i>flags</i>
<dl><dd>the type of memory to allocate (see kmalloc).</dd></dl>
 

 <i>node</i>
<dl><dd>memory node from which to allocate</dd></dl>

<h2>Copyright</h2>


