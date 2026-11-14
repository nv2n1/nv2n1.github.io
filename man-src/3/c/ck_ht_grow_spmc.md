---
title: "ck_ht_grow_spmc(3)"
name: "ck_ht_grow_spmc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_grow_spmc/"
description: "ck_ht_grow_spmc – resize a hash table if necessary"
---

<h2>NAME</h2>
<p> <code>ck_ht_grow_spmc</code> &#8211; resize a hash table if necessary</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft bool Fn ck_ht_grow_spmc ck_ht_t *ht uint64_t capacity</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_grow_spmc function will resize the hash table in order to be able to at least store the number of entries specified by Fa capacity at a load factor of one. The default load hash table load factor is 0.5. If you wish to minimize the likelihood of memory allocations for a hash table meant to store n entries then specify a capacity of 2n. The default behavior of ck_ht is to round Fa capacity to the next available power of two if it is not already a power of two. </p>
<p> This function is safe to call in the presence of concurrent ck_ht_get_spmc3 operations.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion Fn ck_ht_grow_spmc returns <code>true</code> and otherwise returns a <code>false</code> value.</p>
<h2>ERRORS</h2>
<dl>
<p> Behavior is undefined if Fa ht is uninitialized. The function will only return <code>false</code> if there are internal memory allocation failures.</dl>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_remove_spmc3, ck_ht_reset_spmc3, ck_ht_reset_size_spmc3, ck_ht_count3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
