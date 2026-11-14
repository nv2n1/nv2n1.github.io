---
title: "kfree_const(9)"
name: "kfree_const"
section: "9"
letter: "k"
url: "/docs/linux/man/9-kfree_const/"
---

kfree_const - conditionally free memory

<h2>Synopsis</h2>

<pre><code>void kfree_const(const void *x);</code></pre>

<h2>Arguments</h2>

<i>x</i>
<dl><dd><dd>pointer to the memory</dl>

<h2>Description</h2>

Function calls kfree only if <i>x</i> is not in .rodata section.

<h2>Copyright</h2>


