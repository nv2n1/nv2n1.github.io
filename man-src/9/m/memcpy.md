---
title: "memcpy(9)"
name: "memcpy"
section: "9"
letter: "m"
url: "/docs/linux/man/9-memcpy/"
description: "memcpy – Copy one area of memory to another"
---

<p>memcpy &#8211; Copy one area of memory to another</p>
<h2>Synopsis</h2>
<pre><code>void *memcpy(void *dest, const void *src, size_t count);</code></pre>
<h2>Arguments</h2>
<p><i>dest</i></p>
<dl>
<dd>
<dd>Where to copy to</dl>
<p> <i>src</i></p>
<dl>
<dd>Where to copy from</dl>
<p> <i>count</i></p>
<dl>
<dd>The size of the area.</dl>
<h2>Description</h2>
<p>You should not use this function to access IO space, use <code>memcpy_toio</code> or <code>memcpy_fromio</code> instead.</p>
<h2>Copyright</h2>
