---
title: "bitmap_ord_to_pos(9)"
name: "bitmap_ord_to_pos"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_ord_to_pos/"
---

bitmap_ord_to_pos - find position of n-th set bit in bitmap

<h2>Synopsis</h2>

<pre><code>unsigned int bitmap_ord_to_pos(const unsigned long *buf, unsigned int ord, unsigned int nbits);</code></pre>

<h2>Arguments</h2>

<i>buf</i>
<dl><dd><dd>pointer to bitmap</dl>
 

 <i>ord</i>
<dl><dd>ordinal bit position (n-th set bit, n &gt;= 0)</dl>
 

 <i>nbits</i>
<dl><dd>number of valid bit positions in <i>buf</i></dl>

<h2>Description</h2>

Map the ordinal offset of bit <i>ord</i> in <i>buf</i> to its position in <i>buf</i>. Value of <i>ord</i> should be in range 0 &lt;= <i>ord</i> &lt; weight(buf). If <i>ord</i> &gt;= weight(buf), returns <i>nbits</i>. 

 If for example, just bits 4 through 7 are set in <i>buf</i>, then <i>ord</i> values 0 through 3 will get mapped to 4 through 7, respectively, and all other <i>ord</i> values returns <i>nbits</i>. When <i>ord</i> value 3 gets mapped to (returns) <i>pos</i> value 7 in this example, that means that the 3rd set bit (starting with 0th) is at position 7 in <i>buf</i>. 

 The bit positions 0 through <i>nbits</i>-1 are valid positions in <i>buf</i>.

<h2>Copyright</h2>


