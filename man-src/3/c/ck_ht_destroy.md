---
title: "ck_ht_destroy(3)"
name: "ck_ht_destroy"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_destroy/"
description: "ck_ht_destroy – immediately destroy a hash table"
---

<h2>NAME</h2>
<p> <code>ck_ht_destroy</code> &#8211; immediately destroy a hash table</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft void Fn ck_ht_destroy ck_ht_t *ht</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_destroy function will request that the underlying allocator, as specified by the ck_ht_init3 function, immediately destroy the object pointed to by the Fa ht argument. </p>
<p> The user must guarantee that no threads are accessing the object pointed to by Fa ht when Fn ck_ht_destroy is called.</p>
<h2>RETURN VALUES</h2>
<p> Fn ck_ht_destroy has no return value.</p>
<h2>ERRORS</h2>
<dl>
<p> This function is guaranteed not to fail.</dl>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_init3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_reset_spmc3, ck_ht_reset_size_spmc3, ck_ht_count3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
