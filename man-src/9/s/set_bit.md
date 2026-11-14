---
title: "set_bit(9)"
name: "set_bit"
section: "9"
letter: "s"
url: "/docs/linux/man/9-set_bit/"
description: "set_bit – Atomically set a bit in memory"
---

<p>set_bit &#8211; Atomically set a bit in memory</p>
<h2>Synopsis</h2>
<pre><code>void set_bit(long nr, volatile unsigned long *addr);</code></pre>
<h2>Arguments</h2>
<p><i>nr</i></p>
<dl>
<dd>
<dd>the bit to set</dl>
<p> <i>addr</i></p>
<dl>
<dd>the address to start counting from</dl>
<h2>Description</h2>
<p>This function is atomic and may not be reordered. See <code>__set_bit</code> if you do not require the atomic guarantees.</p>
<h2>Note</h2>
<p>there are no guarantees that this function will not be reordered on non x86 architectures, so if you are writing portable code, make sure not to rely on its reordering guarantees. </p>
<p> Note that <i>nr</i> may be almost arbitrarily large; this function is not restricted to acting on a single-word quantity.</p>
<h2>Copyright</h2>
