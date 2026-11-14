---
title: "ck_ht_count(3)"
name: "ck_ht_count"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_count/"
description: "ck_ht_count – return count of key-value pairs in hash table"
---

<h2>NAME</h2>
<p> <code>ck_ht_count</code> &#8211; return count of key-value pairs in hash table</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft uint64_t Fn ck_ht_count ck_ht_t *ht</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_count function will return the number of entries in the hash table pointed to be the Fa ht argument. The function may only be called without the presence of concurrent write operations.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa ht has not been initialized.</p>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_reset_size_spmc3, ck_ht_reset_spmc3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
