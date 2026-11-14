---
title: "ck_bitmap_next(3)"
name: "ck_bitmap_next"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_bitmap_next/"
description: "ck_bitmap_next – iterate to the next set bit in bitmap"
---

<h2>NAME</h2>
<p> <code>ck_bitmap_next</code> &#8211; iterate to the next set bit in bitmap</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_bitmap.h Ft bool Fn ck_bitmap_next ck_bitmap_t *bitmap ck_bitmap_iterator_t iterator unsigned int *bit</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_bitmap_next function will increment the iterator object pointed to by Fa iterator to point to the next set bit in the bitmap. If Fn ck_bitmap_next returns <code>true</code> then the pointer pointed to by Fa bit is initialized to the number of the current set bit pointed to by the Fa iterator object. </p>
<p> It is expected that Fa iterator has been initialized using the ck_bitmap_iterator_init3 function.</p>
<h2>RETURN VALUES</h2>
<p> If Fn ck_bitmap_next returns <code>true</code> then the object pointed to by Fa bit contains a set bit. If Fn ck_bitmap_next returns <code>false</code> then value of the object pointed to by Fa bit is undefined.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa iterator or Fa bitmap are uninitialized.</p>
<h2>SEE ALSO</h2>
<p> ck_bitmap_base3, ck_bitmap_size3, ck_bitmap_init3, ck_bitmap_set3, ck_bitmap_reset3, ck_bitmap_clear3, ck_bitmap_bits3, ck_bitmap_buffer3, ck_bitmap_iterator_init3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
