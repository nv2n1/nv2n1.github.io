---
title: "bitmap_pos_to_ord(9)"
name: "bitmap_pos_to_ord"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_pos_to_ord/"
---

bitmap_pos_to_ord - find ordinal of set bit at given position in bitmap

<h2>Synopsis</h2>

<pre><code>int bitmap_pos_to_ord(const unsigned long *buf, unsigned int pos, unsigned int nbits);</code></pre>

<h2>Arguments</h2>

<i>buf</i>
<dl><dd><dd>pointer to a bitmap</dl>
 

 <i>pos</i>
<dl><dd>a bit position in <i>buf</i> (0 &lt;= <i>pos</i> &lt; <i>nbits</i>)</dl>
 

 <i>nbits</i>
<dl><dd>number of valid bit positions in <i>buf</i></dl>

<h2>Description</h2>

Map the bit at position <i>pos</i> in <i>buf</i> (of length <i>nbits</i>) to the ordinal of which set bit it is. If it is not set or if <i>pos</i> is not a valid bit position, map to -1. 

 If for example, just bits 4 through 7 are set in <i>buf</i>, then <i>pos</i> values 4 through 7 will get mapped to 0 through 3, respectively, and other <i>pos</i> values will get mapped to -1. When <i>pos</i> value 7 gets mapped to (returns) <i>ord</i> value 3 in this example, that means that bit 7 is the 3rd (starting with 0th) set bit in <i>buf</i>. 

 The bit positions 0 through <i>bits</i> are valid positions in <i>buf</i>.

<h2>Copyright</h2>


