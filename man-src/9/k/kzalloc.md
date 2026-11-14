---
title: "kzalloc(9)"
name: "kzalloc"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kzalloc/"
---

kzalloc - allocate memory. The memory is set to zero.

<h2>Synopsis</h2>

<pre><code>void *kzalloc(size_t size, gfp_t flags);</code></pre>

<h2>Arguments</h2>

<i>size</i>
<dl><dd><dd>how many bytes of memory are required.</dl>
 

 <i>flags</i>
<dl><dd>the type of memory to allocate (see kmalloc).</dl>

<h2>Copyright</h2>


