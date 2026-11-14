---
title: "kmalloc_array(9)"
name: "kmalloc_array"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kmalloc_array/"
---

kmalloc_array - allocate memory for an array.

<h2>Synopsis</h2>

<pre><code>void *kmalloc_array(size_t n, size_t size, gfp_t flags);</code></pre>

<h2>Arguments</h2>

<i>n</i>
<dl><dd><dd>number of elements.</dl>
 

 <i>size</i>
<dl><dd>element size.</dl>
 

 <i>flags</i>
<dl><dd>the type of memory to allocate (see kmalloc).</dl>

<h2>Copyright</h2>


