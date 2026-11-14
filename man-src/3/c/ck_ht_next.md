---
title: "ck_ht_next(3)"
name: "ck_ht_next"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_next/"
description: "ck_ht_next – iterate to next entry in hash table"
---

<h2>NAME</h2>
<p> <code>ck_ht_next</code> &#8211; iterate to next entry in hash table</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft bool Fn ck_ht_next ck_ht_t *ht ck_ht_iterator_t *iterator ck_ht_entry_t **entry</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_next function will increment the iterator object pointed to by Fa iterator to point to the next non-empty hash table entry. If Fn ck_ht_next returns <code>true</code> then the pointer pointed to by Fa entry is initialized to the current hash table entry pointed to by the Fa iterator object. </p>
<p> It is expected that Fa iterator has been initialized using the ck_ht_iterator_init3 function or statically initialized using <code>CK_HT_ITERATOR_INITIALIZER.</code></p>
<h2>RETURN VALUES</h2>
<p> If Fn ck_ht_next returns <code>true</code> then the object pointed to by Fa entry points to a valid hash table entry. If Fn ck_ht_next returns <code>false</code> then value of the object pointed to by Fa entry is undefined.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa iterator or Fa ht are uninitialized.</p>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_count3, ck_ht_reset_spmc3, ck_ht_reset_size_spmc3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key_length3, ck_ht_entry_key3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value3, ck_ht_entry_value_direct3, ck_ht_iterator_init3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
