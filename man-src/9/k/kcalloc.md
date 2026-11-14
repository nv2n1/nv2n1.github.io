---
title: "kcalloc(9)"
name: "kcalloc"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kcalloc/"
---

kcalloc - allocate memory for an array. The memory is set to zero.

<h2>Synopsis</h2>

<pre><code>void *kcalloc(size_t n, size_t size, gfp_t flags);</code></pre>

<h2>Arguments</h2>

<i>n</i>
<dl><dd><dd>number of elements.</dl>
 

 <i>size</i>
<dl><dd>element size.</dl>
 

 <i>flags</i>
<dl><dd>the type of memory to allocate (see kmalloc).</dl>

<h2>Copyright</h2>


