---
title: "bitmap_to_u32array(9)"
name: "bitmap_to_u32array"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_to_u32array/"
---

bitmap_to_u32array - copy the contents of bitmap to a u32 array of bits

<h2>Synopsis</h2>

<pre><code>unsigned int bitmap_to_u32array(u32 *buf, unsigned int nwords, const unsigned long *bitmap, unsigned int nbits);</code></pre>

<h2>Arguments</h2>

<i>buf</i>
<dl><dd><dd>array of u32 (in host byte order), the dest bitmap, non NULL</dl>
 

 <i>nwords</i>
<dl><dd>number of u32 words in <i>buf</i></dl>
 

 <i>bitmap</i>
<dl><dd>array of unsigned longs, the source bitmap, non NULL</dl>
 

 <i>nbits</i>
<dl><dd>number of bits in <i>bitmap</i></dl>

<h2>Description</h2>

copy min(nbits, 32*nwords) bits from <i>bitmap</i> to <i>buf</i>. Remaining bits after nbits in <i>buf</i> (if any) are cleared. 

 Return the number of bits effectively copied.

<h2>Copyright</h2>


