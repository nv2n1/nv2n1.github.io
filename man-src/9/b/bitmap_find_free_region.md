---
title: "bitmap_find_free_region(9)"
name: "bitmap_find_free_region"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_find_free_region/"
---

bitmap_find_free_region - find a contiguous aligned mem region

<h2>Synopsis</h2>

<pre><code>int bitmap_find_free_region(unsigned long *bitmap, unsigned int bits, int order);</code></pre>

<h2>Arguments</h2>

<i>bitmap</i>
<dl><dd><dd>array of unsigned longs corresponding to the bitmap</dl>
 

 <i>bits</i>
<dl><dd>number of bits in the bitmap</dl>
 

 <i>order</i>
<dl><dd>region size (log base 2 of number of bits) to find</dl>

<h2>Description</h2>

Find a region of free (zero) bits in a <i>bitmap</i> of <i>bits</i> bits and allocate them (set them to one). Only consider regions of length a power (<i>order</i>) of two, aligned to that power of two, which makes the search algorithm much faster. 

 Return the bit offset in bitmap of the allocated region, or -errno on failure.

<h2>Copyright</h2>


