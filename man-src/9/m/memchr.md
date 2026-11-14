---
title: "memchr(9)"
name: "memchr"
section: "9"
letter: "m"
url: "/docs/linux/man/9-memchr/"
description: "memchr – Find a character in an area of memory."
---

<p>memchr &#8211; Find a character in an area of memory.</p>
<h2>Synopsis</h2>
<pre><code>void *memchr(const void *s, int c, size_t n);</code></pre>
<h2>Arguments</h2>
<p><i>s</i></p>
<dl>
<dd>
<dd>The memory area</dl>
<p> <i>c</i></p>
<dl>
<dd>The byte to search for</dl>
<p> <i>n</i></p>
<dl>
<dd>The size of the area.</dl>
<h2>Description</h2>
<p>returns the address of the first occurrence of <i>c</i>, or <code>NULL</code> if <i>c</i> is not found</p>
<h2>Copyright</h2>
