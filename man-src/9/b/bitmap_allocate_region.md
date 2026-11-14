---
title: "bitmap_allocate_region(9)"
name: "bitmap_allocate_region"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_allocate_region/"
description: "bitmap_allocate_region – allocate bitmap region"
---

<p>bitmap_allocate_region &#8211; allocate bitmap region</p>
<h2>Synopsis</h2>
<pre><code>int bitmap_allocate_region(unsigned long *bitmap, unsigned int pos, int order);</code></pre>
<h2>Arguments</h2>
<p><i>bitmap</i></p>
<dl>
<dd>
<dd>array of unsigned longs corresponding to the bitmap</dl>
<p> <i>pos</i></p>
<dl>
<dd>beginning of bit region to allocate</dl>
<p> <i>order</i></p>
<dl>
<dd>region size (log base 2 of number of bits) to allocate</dl>
<h2>Description</h2>
<p>Allocate (set bits in) a specified region of a bitmap. </p>
<p> Return 0 on success, or <code>-EBUSY</code> if specified region wasn&#8217;t free (not all bits were zero).</p>
<h2>Copyright</h2>
