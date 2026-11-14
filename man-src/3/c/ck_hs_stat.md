---
title: "ck_hs_stat(3)"
name: "ck_hs_stat"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_hs_stat/"
description: "ck_hs_stat – get hash set status"
---

<h2>NAME</h2>
<p> <code>ck_hs_stat</code> &#8211; get hash set status</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_hs.h Ft void Fn ck_hs_stat ck_hs_t *hs struct ck_hs_stat *st</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_hs_stat 3 function will store various hash set statistics in the object pointed to by Fa st . The ck_hs_stat structure is defined as follows: </p>
<blockquote>
<pre><code>
struct ck_hs_stat {
    unsigned long tombstones;   /* Current number of tombstones in hash set. */
    unsigned long n_entries;    /* Current number of keys in hash set. */
    unsigned int probe_maximum; /* Longest read-side probe sequence. */
};
</code></pre>
</blockquote>
<h2>RETURN VALUES</h2>
<p> Fn ck_hs_stat 3 has no return value.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa hs is uninitialized. Behavior is undefined if this function is called by a non-writer thread.</p>
<h2>SEE ALSO</h2>
<p> ck_hs_init3, ck_hs_move3, ck_hs_destroy3, CK_HS_HASH3, ck_hs_iterator_init3, ck_hs_next3, ck_hs_get3, ck_hs_put3, ck_hs_put_unique3, ck_hs_set3, ck_hs_fas3, ck_hs_remove3, ck_hs_grow3, ck_hs_gc3, ck_hs_rebuild3, ck_hs_count3, ck_hs_reset3, ck_hs_reset_size3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
