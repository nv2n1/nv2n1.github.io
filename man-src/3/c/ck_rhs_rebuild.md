---
title: "ck_rhs_rebuild(3)"
name: "ck_rhs_rebuild"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rhs_rebuild/"
description: "ck_rhs_rebuild – rebuild a hash set"
---

<h2>NAME</h2>
<p> <code>ck_rhs_rebuild</code> &#8211; rebuild a hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rhs.h Ft bool Fn ck_rhs_rebuild ck_rhs_t *hs</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_rhs_rebuild 3 function will regenerate the hash set pointed to by Fa hs . This has the side-effect of pruning degradatory side-effects of workloads that are delete heavy. The regenerated hash set should have shorter probe sequences on average. This operation will require a significant amount of memory and is free to allocate a duplicate hash set in the rebuild process.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, Fn ck_rhs_rebuild 3 returns true and otherwise returns false on failure.</p>
<h2>ERRORS</h2>
<p> This function will only return false if there are internal memory allocation failures.</p>
<h2>SEE ALSO</h2>
<p> ck_rhs_init3, ck_rhs_move3, ck_rhs_destroy3, CK_RHS_HASH3, ck_rhs_iterator_init3, ck_rhs_next3, ck_rhs_get3, ck_rhs_put3, ck_rhs_put_unique3, ck_rhs_set3, ck_rhs_fas3, ck_rhs_gc3, ck_rhs_grow3, ck_rhs_remove3, ck_rhs_count3, ck_rhs_reset3, ck_rhs_reset_size3, ck_rhs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
