---
title: "ck_rhs_destroy(3)"
name: "ck_rhs_destroy"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rhs_destroy/"
description: "ck_rhs_destroy – destroy hash set"
---

<h2>NAME</h2>
<p> <code>ck_rhs_destroy</code> &#8211; destroy hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rhs.h Ft void Fn ck_rhs_destroy ck_rhs_t *hs</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_rhs_destroy 3 function will request that the underlying allocator, as specified by the ck_rhs_init3 function, immediately destroy the object pointed to by the Fa hs argument. The user must guarantee that no threads are accessing the object pointed to by Fa hs when Fn ck_rhs_destroy 3 is called.</p>
<h2>RETURN VALUES</h2>
<p> Fn ck_rhs_destroy 3 has no return value.</p>
<h2>ERRORS</h2>
<p> This function is guaranteed not to fail.</p>
<h2>SEE ALSO</h2>
<p> ck_rhs_init3, ck_rhs_move3, CK_RHS_HASH3, ck_rhs_iterator_init3, ck_rhs_next3, ck_rhs_get3, ck_rhs_put3, ck_rhs_put_unique3, ck_rhs_set3, ck_rhs_fas3, ck_rhs_remove3, ck_rhs_grow3, ck_rhs_rebuild3, ck_rhs_gc3, ck_rhs_count3, ck_rhs_reset3, ck_rhs_reset_size3, ck_rhs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
