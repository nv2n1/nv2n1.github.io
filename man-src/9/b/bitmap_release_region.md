---
title: "bitmap_release_region(9)"
name: "bitmap_release_region"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_release_region/"
description: "bitmap_release_region – release allocated bitmap region"
---

<p>bitmap_release_region &#8211; release allocated bitmap region</p>
<h2>Synopsis</h2>
<pre><code>void bitmap_release_region(unsigned long *bitmap, unsigned int pos, int order);</code></pre>
<h2>Arguments</h2>
<p><i>bitmap</i></p>
<dl>
<dd>
<dd>array of unsigned longs corresponding to the bitmap</dl>
<p> <i>pos</i></p>
<dl>
<dd>beginning of bit region to release</dl>
<p> <i>order</i></p>
<dl>
<dd>region size (log base 2 of number of bits) to release</dl>
<h2>Description</h2>
<p>This is the complement to <code>__bitmap_find_free_region</code> and releases the found region (by clearing it in the bitmap). </p>
<p> No return value.</p>
<h2>Copyright</h2>
