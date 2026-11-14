---
title: "ck_bitmap_base(3)"
name: "ck_bitmap_base"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_bitmap_base/"
description: "ck_bitmap_base – determine the size of a bit array in bytes"
---

<h2>NAME</h2>
<p> <code>ck_bitmap_base</code> &#8211; determine the size of a bit array in bytes</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_bitmap.h Ft unsigned int Fn ck_bitmap_base unsigned int n_bits</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_bitmap_base function returns the number of bytes that would be used to store the number of bits specified by Fa n_bits .</p>
<h2>RETURN VALUES</h2>
<p> This function returns a non-zero value that is guaranteed to be a multiple of <code>sizeof(CK_BITMAP_WORD)</code></p>
<h2>SEE ALSO</h2>
<p> ck_bitmap_size3, ck_bitmap_init3, ck_bitmap_set3, ck_bitmap_reset3, ck_bitmap_test3, ck_bitmap_clear3, ck_bitmap_bits3, ck_bitmap_buffer3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
