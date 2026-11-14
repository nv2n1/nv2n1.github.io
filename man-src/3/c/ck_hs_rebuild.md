---
title: "ck_hs_rebuild(3)"
name: "ck_hs_rebuild"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_hs_rebuild/"
description: "ck_hs_rebuild – rebuild a hash set"
---

<h2>NAME</h2>
<p> <code>ck_hs_rebuild</code> &#8211; rebuild a hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_hs.h Ft bool Fn ck_hs_rebuild ck_hs_t *hs</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_hs_rebuild 3 function will regenerate the hash set pointed to by Fa hs . This has the side-effect of pruning degradatory side-effects of workloads that are delete heavy. The regenerated hash set should have shorter probe sequences on average. This operation will require a significant amount of memory and is free to allocate a duplicate hash set in the rebuild process.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, Fn ck_hs_rebuild 3 returns true and otherwise returns false on failure.</p>
<h2>ERRORS</h2>
<p> This function will only return false if there are internal memory allocation failures.</p>
<h2>SEE ALSO</h2>
<p> ck_hs_init3, ck_hs_move3, ck_hs_destroy3, CK_HS_HASH3, ck_hs_iterator_init3, ck_hs_next3, ck_hs_get3, ck_hs_put3, ck_hs_put_unique3, ck_hs_set3, ck_hs_fas3, ck_hs_gc3, ck_hs_grow3, ck_hs_remove3, ck_hs_count3, ck_hs_reset3, ck_hs_reset_size3, ck_hs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
