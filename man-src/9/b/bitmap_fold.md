---
title: "bitmap_fold(9)"
name: "bitmap_fold"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_fold/"
description: "bitmap_fold – fold larger bitmap into smaller, modulo specified size"
---

<p>bitmap_fold &#8211; fold larger bitmap into smaller, modulo specified size</p>
<h2>Synopsis</h2>
<pre><code>void bitmap_fold(unsigned long *dst, const unsigned long *orig, unsigned int sz, unsigned int nbits);</code></pre>
<h2>Arguments</h2>
<p><i>dst</i></p>
<dl>
<dd>
<dd>resulting smaller bitmap</dl>
<p> <i>orig</i></p>
<dl>
<dd>original larger bitmap</dl>
<p> <i>sz</i></p>
<dl>
<dd>specified size</dl>
<p> <i>nbits</i></p>
<dl>
<dd>number of bits in each of these bitmaps</dl>
<h2>Description</h2>
<p>For each bit oldbit in <i>orig</i>, set bit oldbit mod <i>sz</i> in <i>dst</i>. Clear all other bits in <i>dst</i>. See further the comment and Example [2] for <code>bitmap_onto</code> for why and how to use this.</p>
<h2>Copyright</h2>
