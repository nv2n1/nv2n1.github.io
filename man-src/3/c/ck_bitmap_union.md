---
title: "ck_bitmap_union(3)"
name: "ck_bitmap_union"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_bitmap_union/"
description: "ck_bitmap_union – generates union of two bitmaps"
---

<h2>NAME</h2>
<p> <code>ck_bitmap_union</code> &#8211; generates union of two bitmaps</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_bitmap.h Ft void Fn ck_bitmap_union ck_bitmap_t *dst ck_bitmap_t *src</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_bitmap_union function sets all bits in the bitmap pointed to by Fa src in the bitmap pointed to by Fa dst .</p>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_bitmap_base3, ck_bitmap_size3, ck_bitmap_init3, ck_bitmap_reset3, ck_bitmap_set3, ck_bitmap_clear3, ck_bitmap_test3, ck_bitmap_bits3, ck_bitmap_buffer3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
