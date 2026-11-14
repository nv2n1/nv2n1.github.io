---
title: "memmove(9)"
name: "memmove"
section: "9"
letter: "m"
url: "/docs/linux/man/9-memmove/"
description: "memmove – Copy one area of memory to another"
---

<p>memmove &#8211; Copy one area of memory to another</p>
<h2>Synopsis</h2>
<pre><code>void *memmove(void *dest, const void *src, size_t count);</code></pre>
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
<p>Unlike <code>memcpy</code>, <code>memmove</code> copes with overlapping areas.</p>
<h2>Copyright</h2>
