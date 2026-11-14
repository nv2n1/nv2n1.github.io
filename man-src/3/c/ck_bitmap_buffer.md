---
title: "ck_bitmap_buffer(3)"
name: "ck_bitmap_buffer"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_bitmap_buffer/"
description: "ck_bitmap_buffer – returns pointer to bit array"
---

<h2>NAME</h2>
<p> <code>ck_bitmap_buffer</code> &#8211; returns pointer to bit array</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_bitmap.h Ft void * Fn ck_bitmap_buffer ck_bitmap_t *bitmap</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_bitmap_buffer functions returns a pointer to the actual bit array. For ck_bitmap pointers, the bit array is of type CK_BITMAP_WORD[] and consists of ck_bitmap_base(bitmap) / sizeof(CK_BITMAP_WORD) elements. On currently supported 64-bit platforms <code>CK_BITMAP_WORD</code> is <code>uint64_t</code> On currently supported 32-bit platforms <code>CK_BITMAP_WORD</code> is <code>uint32_t</code></p>
<h2>RETURN VALUES</h2>
<p> This function returns a non-NULL value.</p>
<h2>SEE ALSO</h2>
<p> ck_bitmap_base3, ck_bitmap_size3, ck_bitmap_init3, ck_bitmap_set3, ck_bitmap_reset3, ck_bitmap_test3, ck_bitmap_clear3, ck_bitmap_bits3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
