---
title: "bitmap_bitremap(9)"
name: "bitmap_bitremap"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_bitremap/"
---

bitmap_bitremap - Apply map defined by a pair of bitmaps to a single bit

<h2>Synopsis</h2>

<pre><code>int bitmap_bitremap(int oldbit, const unsigned long *old, const unsigned long *new, int bits);</code></pre>

<h2>Arguments</h2>

<i>oldbit</i>
<dl><dd><dd>bit position to be mapped</dl>
 

 <i>old</i>
<dl><dd>defines domain of map</dl>
 

 <i>new</i>
<dl><dd>defines range of map</dl>
 

 <i>bits</i>
<dl><dd>number of bits in each of these bitmaps</dl>

<h2>Description</h2>

Let <i>old</i> and <i>new</i> define a mapping of bit positions, such that whatever position is held by the n-th set bit in <i>old</i> is mapped to the n-th set bit in <i>new</i>. In the more general case, allowing for the possibility that the weight 'w' of <i>new</i> is less than the weight of <i>old</i>, map the position of the n-th set bit in <i>old</i> to the position of the m-th set bit in <i>new</i>, where m == n % w. 

 The positions of unset bits in <i>old</i> are mapped to themselves (the identify map). 

 Apply the above specified mapping to bit position <i>oldbit</i>, returning the new bit position. 

 For example, lets say that <i>old</i> has bits 4 through 7 set, and <i>new</i> has bits 12 through 15 set. This defines the mapping of bit position 4 to 12, 5 to 13, 6 to 14 and 7 to 15, and of all other bit positions unchanged. So if say <i>oldbit</i> is 5, then this routine returns 13.

<h2>Copyright</h2>


