---
title: "ck_rhs_iterator_init(3)"
name: "ck_rhs_iterator_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rhs_iterator_init/"
description: "ck_rhs_iterator_init – initialize hash set iterator"
---

<h2>NAME</h2>
<p> <code>ck_rhs_iterator_init</code> &#8211; initialize hash set iterator</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rhs.h </p>
<p> <code>ck_rhs_iterator_t iterator = CK_RHS_ITERATOR_INITIALIZER</code> </p>
<p> Ft void Fn ck_rhs_iterator_init ck_rhs_iterator_t *iterator</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_rhs_iterator_init 3 function will initialize the object pointed to by the Fa iterator argument. Alternatively, an iterator may be statically initialized by assigning it to the CK_RHS_ITERATOR_INITIALIZER value. </p>
<p> An iterator is used to iterate through hash set entries with the ck_rhs_next3 function.</p>
<h2>RETURN VALUES</h2>
<p> Fn ck_rhs_iterator_init 3 has no return value.</p>
<h2>ERRORS</h2>
<p> This function will not fail.</p>
<h2>SEE ALSO</h2>
<p> ck_rhs_init3, ck_rhs_move3, ck_rhs_destroy3, CK_RHS_HASH3, ck_rhs_next3, ck_rhs_get3, ck_rhs_put3, ck_rhs_put_unique3, ck_rhs_set3, ck_rhs_fas3, ck_rhs_remove3, ck_rhs_grow3, ck_rhs_rebuild3, ck_rhs_gc3, ck_rhs_count3, ck_rhs_reset3, ck_rhs_reset_size3, ck_rhs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
