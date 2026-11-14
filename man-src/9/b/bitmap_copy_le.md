---
title: "bitmap_copy_le(9)"
name: "bitmap_copy_le"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_copy_le/"
---

bitmap_copy_le - copy a bitmap, putting the bits into little-endian order.

<h2>Synopsis</h2>

<pre><code>void bitmap_copy_le(unsigned long *dst, const unsigned long *src, unsigned int nbits);</code></pre>

<h2>Arguments</h2>

<i>dst</i>
<dl><dd><dd>destination buffer</dl>
 

 <i>src</i>
<dl><dd>bitmap to copy</dl>
 

 <i>nbits</i>
<dl><dd>number of bits in the bitmap</dl>

<h2>Description</h2>

Require nbits % BITS_PER_LONG == 0.

<h2>Copyright</h2>


