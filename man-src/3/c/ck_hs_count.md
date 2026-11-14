---
title: "ck_hs_count(3)"
name: "ck_hs_count"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_hs_count/"
description: "ck_hs_count – returns number of entries in hash set"
---

<h2>NAME</h2>
<p> <code>ck_hs_count</code> &#8211; returns number of entries in hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_hs.h Ft unsigned long Fn ck_hs_count ck_hs_t *hs</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_hs_count 3 function returns the number of keys currently stored in Fa hs .</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa hs is uninitialized. Behavior is undefined if this function is called by a non-writer thread.</p>
<h2>SEE ALSO</h2>
<p> ck_hs_init3, ck_hs_move3, ck_hs_destroy3, CK_HS_HASH3, ck_hs_iterator_init3, ck_hs_next3, ck_hs_get3, ck_hs_put3, ck_hs_put_unique3, ck_hs_set3, ck_hs_fas3, ck_hs_remove3, ck_hs_grow3, ck_hs_rebuild3, ck_hs_gc3, ck_hs_reset3, ck_hs_reset_size3, ck_hs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
