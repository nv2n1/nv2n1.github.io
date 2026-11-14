---
title: "ck_hs_gc(3)"
name: "ck_hs_gc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_hs_gc/"
description: "ck_hs_gc – perform maintenance on a hash set"
---

<h2>NAME</h2>
<p> <code>ck_hs_gc</code> &#8211; perform maintenance on a hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_hs.h Ft bool Fn ck_hs_gc ck_hs_t *hs unsigned long cycles unsigned long seed</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_hs_gc 3 function will perform various maintenance routines on the hash set pointed to by Fa hs , including defragmentation of probe sequences with respect to tombstones and in the case that the delete workload hint has been passed, recalculation of probe sequence bounds. The Fa cycles argument is used to indicate how many hash set entries should be subject to attempted maintenance. If Fa cycles is 0, then maintenance is performed on the complete hash set. The Fa seed argument determines the start location of the maintenance process. If Fa cycles is non-zero, it is recommended that Fa seed is some random value. If the delete hint has been passed, the function will require an additional 12% of memory (with respect to existing memory usage of the set), until operation completion.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, Fn ck_hs_gc 3 returns true and otherwise returns false on failure due to memory allocation failure.</p>
<h2>ERRORS</h2>
<p> This function will only return false if there are internal memory allocation failures.</p>
<h2>SEE ALSO</h2>
<p> ck_hs_init3, ck_hs_move3, ck_hs_destroy3, CK_HS_HASH3, ck_hs_iterator_init3, ck_hs_next3, ck_hs_get3, ck_hs_put3, ck_hs_put_unique3, ck_hs_grow3, ck_hs_rebuild3, ck_hs_set3, ck_hs_fas3, ck_hs_remove3, ck_hs_count3, ck_hs_reset3, ck_hs_reset_size3, ck_hs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
