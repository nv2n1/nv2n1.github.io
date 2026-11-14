---
title: "bitmap_from_u32array(9)"
name: "bitmap_from_u32array"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_from_u32array/"
---

bitmap_from_u32array - copy the contents of a u32 array of bits to bitmap

<h2>Synopsis</h2>

<pre><code>unsigned int bitmap_from_u32array(unsigned long *bitmap, unsigned int nbits, const u32 *buf, unsigned int nwords);</code></pre>

<h2>Arguments</h2>

<i>bitmap</i>
<dl><dd><dd>array of unsigned longs, the destination bitmap, non NULL</dl>
 

 <i>nbits</i>
<dl><dd>number of bits in <i>bitmap</i></dl>
 

 <i>buf</i>
<dl><dd>array of u32 (in host byte order), the source bitmap, non NULL</dl>
 

 <i>nwords</i>
<dl><dd>number of u32 words in <i>buf</i></dl>

<h2>Description</h2>

copy min(nbits, 32*nwords) bits from <i>buf</i> to <i>bitmap</i>, remaining bits between nword and nbits in <i>bitmap</i> (if any) are cleared. In last word of <i>bitmap</i>, the bits beyond nbits (if any) are kept unchanged. 

 Return the number of bits effectively copied.

<h2>Copyright</h2>


