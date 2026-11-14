---
title: "ck_ht_stat(3)"
name: "ck_ht_stat"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_stat/"
description: "ck_ht_stat – get hash table status"
---

<h2>NAME</h2>
<p> <code>ck_ht_stat</code> &#8211; get hash table status</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft void Fn ck_ht_stat ck_ht_t *ht struct ck_ht_stat *st</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_stat 3 function will store various hash set statistics in the object pointed to by Fa st . The ck_ht_stat structure is defined as follows: </p>
<blockquote>
<pre><code>
struct ck_ht_stat {
    uint64_t probe_maximum; /* Longest read-side probe sequence. */
    uint64_t n_entries;     /* Current number of keys in hash set. */
};
</code></pre>
</blockquote>
<h2>RETURN VALUES</h2>
<p> Fn ck_ht_stat 3 has no return value.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa ht has not been initialized.</p>
<h2>SEE ALSO</h2>
<p> ck_ht_count3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_reset_spmc3, ck_ht_reset_size_spmc3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
