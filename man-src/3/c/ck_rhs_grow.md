---
title: "ck_rhs_grow(3)"
name: "ck_rhs_grow"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rhs_grow/"
description: "ck_rhs_grow – enlarge hash set capacity"
---

<h2>NAME</h2>
<p> <code>ck_rhs_grow</code> &#8211; enlarge hash set capacity</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rhs.h Ft bool Fn ck_rhs_grow ck_rhs_t *hs unsigned long capacity</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_rhs_grow 3 function will resize the hash set in order to be able to store at least the number of entries specified by Fa capacity at a load factor of one. The default hash set load factor is 0.5. If you wish to minimize the likelihood of memory allocations for a hash set meant to store n entries, then specify a Fa capacity of 2n. The default behavior of ck_rhs is to round Fa capacity to the next power of two if it is not already a power of two.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, Fn ck_rhs_grow 3 returns true and otherwise returns false on failure.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa hs is uninitialized. This function will only return false if there are internal memory allocation failures.</p>
<h2>SEE ALSO</h2>
<p> ck_rhs_init3, ck_rhs_move3, ck_rhs_destroy3, CK_RHS_HASH3, ck_rhs_iterator_init3, ck_rhs_next3, ck_rhs_get3, ck_rhs_put3, ck_rhs_put_unique3, ck_rhs_set3, ck_rhs_fas3, ck_rhs_remove3, ck_rhs_rebuild3, ck_rhs_gc3, ck_rhs_count3, ck_rhs_reset3, ck_rhs_reset_size3, ck_rhs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
