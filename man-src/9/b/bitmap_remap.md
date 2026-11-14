---
title: "bitmap_remap(9)"
name: "bitmap_remap"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_remap/"
---

bitmap_remap - Apply map defined by a pair of bitmaps to another bitmap

<h2>Synopsis</h2>

<pre><code>void bitmap_remap(unsigned long *dst, const unsigned long *src, const unsigned long *old, const unsigned long *new, unsigned int nbits);</code></pre>

<h2>Arguments</h2>

<i>dst</i>
<dl><dd><dd>remapped result</dl>
 

 <i>src</i>
<dl><dd>subset to be remapped</dl>
 

 <i>old</i>
<dl><dd>defines domain of map</dl>
 

 <i>new</i>
<dl><dd>defines range of map</dl>
 

 <i>nbits</i>
<dl><dd>number of bits in each of these bitmaps</dl>

<h2>Description</h2>

Let <i>old</i> and <i>new</i> define a mapping of bit positions, such that whatever position is held by the n-th set bit in <i>old</i> is mapped to the n-th set bit in <i>new</i>. In the more general case, allowing for the possibility that the weight 'w' of <i>new</i> is less than the weight of <i>old</i>, map the position of the n-th set bit in <i>old</i> to the position of the m-th set bit in <i>new</i>, where m == n % w. 

 If either of the <i>old</i> and <i>new</i> bitmaps are empty, or if <i>src</i> and <i>dst</i> point to the same location, then this routine copies <i>src</i> to <i>dst</i>. 

 The positions of unset bits in <i>old</i> are mapped to themselves (the identify map). 

 Apply the above specified mapping to <i>src</i>, placing the result in <i>dst</i>, clearing any bits previously set in <i>dst</i>. 

 For example, lets say that <i>old</i> has bits 4 through 7 set, and <i>new</i> has bits 12 through 15 set. This defines the mapping of bit position 4 to 12, 5 to 13, 6 to 14 and 7 to 15, and of all other bit positions unchanged. So if say <i>src</i> comes into this routine with bits 1, 5 and 7 set, then <i>dst</i> should leave with bits 1, 13 and 15 set.

<h2>Copyright</h2>


