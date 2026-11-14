---
title: "ck_ht_iterator_init(3)"
name: "ck_ht_iterator_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_iterator_init/"
description: "ck_ht_iterator_init – initialize hash table iterator"
---

<h2>NAME</h2>
<p> <code>ck_ht_iterator_init</code> &#8211; initialize hash table iterator</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h </p>
<p> <code>ck_ht_iterator_t iterator = CK_HT_ITERATOR_INITIALIZER</code> </p>
<p> Ft void Fn ck_ht_iterator_init ck_ht_iterator_t *iterator</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_iterator_init function will initialize the object pointed to by the Fa iterator argument. Alternatively, an iterator may be statically initialized by assigning it the <code>CK_HT_ITERATOR_INITIALIZER</code> value. </p>
<p> An iterator is used to iterate through hash table entries with the ck_ht_next3 function.</p>
<h2>RETURN VALUES</h2>
<p> The Fn ck_ht_iterator_init function does not return a value.</p>
<h2>ERRORS</h2>
<p> This function will not fail.</p>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_count3, ck_ht_reset_size_spmc3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key_length3, ck_ht_entry_key3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value3, ck_ht_entry_value_direct3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
