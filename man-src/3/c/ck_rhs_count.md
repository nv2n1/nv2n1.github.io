---
title: "ck_rhs_count(3)"
name: "ck_rhs_count"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rhs_count/"
description: "ck_rhs_count – returns number of entries in hash set"
---

<h2>NAME</h2>
<p> <code>ck_rhs_count</code> &#8211; returns number of entries in hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rhs.h Ft unsigned long Fn ck_rhs_count ck_rhs_t *hs</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_rhs_count 3 function returns the number of keys currently stored in Fa hs .</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa hs is uninitialized. Behavior is undefined if this function is called by a non-writer thread.</p>
<h2>SEE ALSO</h2>
<p> ck_rhs_init3, ck_rhs_move3, ck_rhs_destroy3, CK_RHS_HASH3, ck_rhs_iterator_init3, ck_rhs_next3, ck_rhs_get3, ck_rhs_put3, ck_rhs_put_unique3, ck_rhs_set3, ck_rhs_fas3, ck_rhs_remove3, ck_rhs_grow3, ck_rhs_rebuild3, ck_rhs_gc3, ck_rhs_reset3, ck_rhs_reset_size3, ck_rhs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
