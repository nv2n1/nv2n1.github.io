---
title: "bitmap_find_next_zero_area_off(9)"
name: "bitmap_find_next_zero_area_off"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bitmap_find_next_zero_area_off/"
---

bitmap_find_next_zero_area_off - find a contiguous aligned zero area

<h2>Synopsis</h2>

<pre><code>unsigned long bitmap_find_next_zero_area_off(unsigned long *map, unsigned long size, unsigned long start, unsigned int nr, unsigned long align_mask, unsigned long align_offset);</code></pre>

<h2>Arguments</h2>

<i>map</i>
<dl><dd><dd>The address to base the search on</dl>
 

 <i>size</i>
<dl><dd>The bitmap size in bits</dl>
 

 <i>start</i>
<dl><dd>The bitnumber to start searching at</dl>
 

 <i>nr</i>
<dl><dd>The number of zeroed bits we're looking for</dl>
 

 <i>align_mask</i>
<dl><dd>Alignment mask for zero area</dl>
 

 <i>align_offset</i>
<dl><dd>Alignment offset for zero area.</dl>

<h2>Description</h2>

The <i>align_mask</i> should be one less than a power of 2; the effect is that the bit offset of all zero areas this function finds plus <i>align_offset</i> is multiple of that power of 2.

<h2>Copyright</h2>


