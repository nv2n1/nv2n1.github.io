---
title: "ck_ht_hash(3)"
name: "ck_ht_hash"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_hash/"
description: "ck_ht_hash – generate a hash value for a hash table"
---

<h2>NAME</h2>
<p> <code>ck_ht_hash</code> &#8211; generate a hash value for a hash table</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft void Fn ck_ht_hash ck_ht_hash_t *h ck_ht_t *ht const void *key uint16_t key_length</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_hash function will generate a hash value in the object pointed to by the Fa h argument. The hash value is valid for use in the hash table pointed to by the Fa ht argument for the key (of bytestring type) specified by the Fa key argument. The length of the key is specified by the Fa key_length argument.</p>
<h2>RETURN VALUES</h2>
<p> Fn ck_ht_hash has no return value.</p>
<h2>ERRORS</h2>
<dl>
<p> Behavior is undefined if Fa key is <code>NULL</code> or if Fa ht is uninitialized.</dl>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_reset_spmc3, ck_ht_reset_size_spmc3, ck_ht_count3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
