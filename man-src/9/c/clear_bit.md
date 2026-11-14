---
title: "clear_bit(9)"
name: "clear_bit"
section: "9"
letter: "c"
url: "/docs/linux/man/9-clear_bit/"
description: "clear_bit – Clears a bit in memory"
---

<p>clear_bit &#8211; Clears a bit in memory</p>
<h2>Synopsis</h2>
<pre><code>void clear_bit(long nr, volatile unsigned long *addr);</code></pre>
<h2>Arguments</h2>
<p><i>nr</i></p>
<dl>
<dd>
<dd>Bit to clear</dl>
<p> <i>addr</i></p>
<dl>
<dd>Address to start counting from</dl>
<h2>Description</h2>
<p><code>clear_bit</code> is atomic and may not be reordered. However, it does not contain a memory barrier, so if it is used for locking purposes, you should call <code>smp_mb__before_atomic</code> and/or <code>smp_mb__after_atomic</code> in order to ensure changes are visible on other processors.</p>
<h2>Copyright</h2>
