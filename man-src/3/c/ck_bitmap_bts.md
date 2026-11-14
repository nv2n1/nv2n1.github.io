---
title: "ck_bitmap_bts(3)"
name: "ck_bitmap_bts"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_bitmap_bts/"
description: "ck_bitmap_bts – set the bit at the specified index and fetch its original value"
---

<h2>NAME</h2>
<p> <code>ck_bitmap_bts</code> &#8211; set the bit at the specified index and fetch its original value</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_bitmap.h Ft bool Fn ck_bitmap_bts ck_bitmap_t *bitmap unsigned int n</p>
<h2>DESCRIPTION</h2>
<p> Fn ck_bitmap_bts sets the bit at the offset specified by the argument Fa n to <code>1</code> and fetches its original value.</p>
<h2>RETURN VALUES</h2>
<p> This function returns the original value of the bit at offset Fa n in Fa bitmap .</p>
<h2>SEE ALSO</h2>
<p> ck_bitmap_base3, ck_bitmap_size3, ck_bitmap_init3, ck_bitmap_reset3, ck_bitmap_clear3, ck_bitmap_set3, ck_bitmap_test3, ck_bitmap_bits3, ck_bitmap_buffer3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
