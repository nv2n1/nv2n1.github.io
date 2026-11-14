---
title: "ck_bitmap_test(3)"
name: "ck_bitmap_test"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_bitmap_test/"
description: "ck_bitmap_test – determine if the bit at the specified index is set"
---

<h2>NAME</h2>
<p> <code>ck_bitmap_test</code> &#8211; determine if the bit at the specified index is set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_bitmap.h Ft bool Fn ck_bitmap_test ck_bitmap_t *bitmap unsigned int n</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_bitmap_test determines if the bit at the offset specified by the argument Fa n is set to <code>1</code></p>
<h2>RETURN VALUES</h2>
<p> This function returns <code>true</code> if the bit at the specified offset is set to <code>1</code> and otherwise returns <code>false</code></p>
<h2>SEE ALSO</h2>
<p> ck_bitmap_base3, ck_bitmap_size3, ck_bitmap_init3, ck_bitmap_set_mpmc3, ck_bitmap_reset_mpmc3, ck_bitmap_clear3, ck_bitmap_bits3, ck_bitmap_buffer3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
