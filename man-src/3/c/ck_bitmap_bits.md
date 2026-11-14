---
title: "ck_bitmap_bits(3)"
name: "ck_bitmap_bits"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_bitmap_bits/"
description: "ck_bitmap_bits – return number of addressable bits in bitmap"
---

<h2>NAME</h2>
<p> <code>ck_bitmap_bits</code> &#8211; return number of addressable bits in bitmap</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_bitmap.h Ft unsigned int Fn ck_bitmap_bits ck_bitmap_t *bitmap</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_bitmap_bits function returns the maximum number of addressable bits in the object pointed to by Fa bitmap .</p>
<h2>RETURN VALUES</h2>
<p> This function returns a non-zero value.</p>
<h2>SEE ALSO</h2>
<p> ck_bitmap_base3, ck_bitmap_size3, ck_bitmap_init3, ck_bitmap_set3, ck_bitmap_reset3, ck_bitmap_test3, ck_bitmap_clear3, ck_bitmap_buffer3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
