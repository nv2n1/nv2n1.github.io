---
title: "ck_bitmap_size(3)"
name: "ck_bitmap_size"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_bitmap_size/"
description: "ck_bitmap_size – returns necessary number of bytes for bitmap"
---

<h2>NAME</h2>
<p> <code>ck_bitmap_size</code> &#8211; returns necessary number of bytes for bitmap</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_bitmap.h Ft unsigned int Fn ck_bitmap_size unsigned int n_bits</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_bitmap_size function returns the number of bytes that are necessary to allocate for a bitmap that will contain the number of bits specified by Fa n_bits . </p>
<p> This function is used to determine how many bytes to allocate for dynamically created bitmap objects. The allocated object must still be initialized using ck_bitmap_init3.</p>
<h2>RETURN VALUES</h2>
<p> This function returns a non-zero value.</p>
<h2>SEE ALSO</h2>
<p> ck_bitmap_base3, ck_bitmap_init3, ck_bitmap_set_mpmc3, ck_bitmap_reset_mpmc3, ck_bitmap_test3, ck_bitmap_clear3, ck_bitmap_bits3, ck_bitmap_buffer3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
