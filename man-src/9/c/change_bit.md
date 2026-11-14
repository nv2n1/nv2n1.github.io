---
title: "change_bit(9)"
name: "change_bit"
section: "9"
letter: "c"
url: "/docs/linux/man/9-change_bit/"
description: "change_bit – Toggle a bit in memory"
---

<p>change_bit &#8211; Toggle a bit in memory</p>
<h2>Synopsis</h2>
<pre><code>void change_bit(long nr, volatile unsigned long *addr);</code></pre>
<h2>Arguments</h2>
<p><i>nr</i></p>
<dl>
<dd>
<dd>Bit to change</dl>
<p> <i>addr</i></p>
<dl>
<dd>Address to start counting from</dl>
<h2>Description</h2>
<p><code>change_bit</code> is atomic and may not be reordered. Note that <i>nr</i> may be almost arbitrarily large; this function is not restricted to acting on a single-word quantity.</p>
<h2>Copyright</h2>
