---
title: "ck_bitmap_iterator_init(3)"
name: "ck_bitmap_iterator_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_bitmap_iterator_init/"
description: "ck_bitmap_iterator_init – initialize bitmap iterator"
---

<h2>NAME</h2>
<p> <code>ck_bitmap_iterator_init</code> &#8211; initialize bitmap iterator</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h </p>
<p> Ft void Fn ck_bitmap_iterator_init ck_bitmap_iterator_t *iterator ck_bitmap_t *bitmap</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_bitmap_iterator_init function will initialize the object pointed to by the Fa iterator argument for use with Fa bitmap . </p>
<p> An iterator is used to iterate through set bitmap bits with the ck_bitmap_next3 function.</p>
<h2>RETURN VALUES</h2>
<p> The Fn ck_bitmap_iterator_init function does not return a value.</p>
<h2>ERRORS</h2>
<p> This function will not fail.</p>
<h2>SEE ALSO</h2>
<p> ck_bitmap_base3, ck_bitmap_size3, ck_bitmap_init3, ck_bitmap_set3, ck_bitmap_reset3, ck_bitmap_clear3, ck_bitmap_bits3, ck_bitmap_buffer3, ck_bitmap_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
