---
title: "memset(9)"
name: "memset"
section: "9"
letter: "m"
url: "/docs/linux/man/9-memset/"
description: "memset – Fill a region of memory with the given value"
---

<p>memset &#8211; Fill a region of memory with the given value</p>
<h2>Synopsis</h2>
<pre><code>void *memset(void *s, int c, size_t count);</code></pre>
<h2>Arguments</h2>
<p><i>s</i></p>
<dl>
<dd>
<dd>Pointer to the start of the area.</dl>
<p> <i>c</i></p>
<dl>
<dd>The byte to fill the area with</dl>
<p> <i>count</i></p>
<dl>
<dd>The size of the area.</dl>
<h2>Description</h2>
<p>Do not use <code>memset</code> to access IO space, use <code>memset_io</code> instead.</p>
<h2>Copyright</h2>
