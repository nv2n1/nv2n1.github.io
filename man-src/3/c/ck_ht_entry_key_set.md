---
title: "ck_ht_entry_key_set(3)"
name: "ck_ht_entry_key_set"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_entry_key_set/"
description: "ck_ht_entry_key_set – initialize pointer to key in hash table entry"
---

<h2>NAME</h2>
<p> <code>ck_ht_entry_key_set</code> &#8211; initialize pointer to key in hash table entry</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft void Fn ck_ht_entry_key_set ck_ht_entry_t *entry const void *key uint16_t key_length</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_entry_key_set function will initialize the object pointed to by Fa entry with a key pointed to by the Fa key argument. The length of the key is specified by Fa key_length. The maximum value of Fa key_length is defined by the CK_HT_KEY_LENGTH macro. This function is typically used to initialize an entry for ck_ht_get_spmc3 and ck_ht_remove_spmc3 operations. It is expected that the entry will be associated with a hash table initialized with <code>CK_HT_MODE_BYTESTRING</code> (see ck_ht_init3 for more information).</p>
<h2>RETURN VALUES</h2>
<p> Fn ck_ht_entry_key_set has no return value.</p>
<h2>ERRORS</h2>
<p> This function will never fail.</p>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_count3, ck_ht_reset_spmc3, ck_ht_reset_size_spmc3, ck_ht_entry_empty3, ck_ht_entry_key_set_direct3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
