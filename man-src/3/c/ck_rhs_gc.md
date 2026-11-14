---
title: "ck_rhs_gc(3)"
name: "ck_rhs_gc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rhs_gc/"
description: "ck_rhs_gc – perform maintenance on a hash set"
---

<h2>NAME</h2>
<p> <code>ck_rhs_gc</code> &#8211; perform maintenance on a hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rhs.h Ft bool Fn ck_rhs_gc ck_rhs_t *hs</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_rhs_gc 3 function will perform various maintenance routines on the hash set pointed to by Fa hs , including recalculating the maximum number of probes.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, Fn ck_rhs_gc 3 returns true and otherwise returns false on failure due to memory allocation failure.</p>
<h2>ERRORS</h2>
<p> This function will only return false if there are internal memory allocation failures.</p>
<h2>SEE ALSO</h2>
<p> ck_rhs_init3, ck_rhs_move3, ck_rhs_destroy3, CK_RHS_HASH3, ck_rhs_iterator_init3, ck_rhs_next3, ck_rhs_get3, ck_rhs_put3, ck_rhs_put_unique3, ck_rhs_grow3, ck_rhs_rebuild3, ck_rhs_set3, ck_rhs_fas3, ck_rhs_remove3, ck_rhs_count3, ck_rhs_reset3, ck_rhs_reset_size3, ck_rhs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
