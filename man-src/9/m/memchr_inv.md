---
title: "memchr_inv(9)"
name: "memchr_inv"
section: "9"
letter: "m"
url: "/docs/linux/man/9-memchr_inv/"
description: "memchr_inv – Find an unmatching character in an area of memory."
---

<p>memchr_inv &#8211; Find an unmatching character in an area of memory.</p>
<h2>Synopsis</h2>
<pre><code>void *memchr_inv(const void *start, int c, size_t bytes);</code></pre>
<h2>Arguments</h2>
<p><i>start</i></p>
<dl>
<dd>
<dd>The memory area</dl>
<p> <i>c</i></p>
<dl>
<dd>Find a character other than c</dl>
<p> <i>bytes</i></p>
<dl>
<dd>The size of the area.</dl>
<h2>Description</h2>
<p>returns the address of the first character other than <i>c</i>, or <code>NULL</code> if the whole buffer contains just <i>c</i>.</p>
<h2>Copyright</h2>
