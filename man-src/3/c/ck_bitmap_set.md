---
title: "ck_bitmap_set(3)"
name: "ck_bitmap_set"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_bitmap_set/"
description: "ck_bitmap_set – set the bit at the specified index"
---

<h2>NAME</h2>
<p> <code>ck_bitmap_set</code> &#8211; set the bit at the specified index</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_bitmap.h Ft void Fn ck_bitmap_set ck_bitmap_t *bitmap unsigned int n</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_bitmap_set sets the bit at offset specified by the argument Fa n to <code>1</code></p>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_bitmap_base3, ck_bitmap_size3, ck_bitmap_init3, ck_bitmap_reset3, ck_bitmap_clear3, ck_bitmap_test3, ck_bitmap_bits3, ck_bitmap_buffer3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
