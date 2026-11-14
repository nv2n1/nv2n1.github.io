---
title: "ck_rhs_stat(3)"
name: "ck_rhs_stat"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rhs_stat/"
description: "ck_rhs_stat – get hash set status"
---

<h2>NAME</h2>
<p> <code>ck_rhs_stat</code> &#8211; get hash set status</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rhs.h Ft void Fn ck_rhs_stat ck_rhs_t *hs struct ck_rhs_stat *st</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_rhs_stat 3 function will store various hash set statistics in the object pointed to by Fa st . The ck_rhs_stat structure is defined as follows: </p>
<blockquote>
<pre><code>
struct ck_rhs_stat {
    unsigned long n_entries;    /* Current number of keys in hash set. */
    unsigned int probe_maximum; /* Longest read-side probe sequence. */
};
</code></pre>
</blockquote>
<h2>RETURN VALUES</h2>
<p> Fn ck_rhs_stat 3 has no return value.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa hs is uninitialized. Behavior is undefined if this function is called by a non-writer thread.</p>
<h2>SEE ALSO</h2>
<p> ck_rhs_init3, ck_rhs_move3, ck_rhs_destroy3, CK_RHS_HASH3, ck_rhs_iterator_init3, ck_rhs_next3, ck_rhs_get3, ck_rhs_put3, ck_rhs_put_unique3, ck_rhs_set3, ck_rhs_fas3, ck_rhs_remove3, ck_rhs_grow3, ck_rhs_gc3, ck_rhs_rebuild3, ck_rhs_count3, ck_rhs_reset3, ck_rhs_reset_size3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
