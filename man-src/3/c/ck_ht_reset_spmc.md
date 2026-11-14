---
title: "ck_ht_reset_spmc(3)"
name: "ck_ht_reset_spmc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_reset_spmc/"
description: "ck_ht_reset_spmc – remove all entries from a hash table"
---

<h2>NAME</h2>
<p> <code>ck_ht_reset_spmc</code> &#8211; remove all entries from a hash table</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft bool Fn ck_ht_reset_spmc ck_ht_t *ht</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_reset_spmc function will remove all key-value pairs stored in the hash table pointed to by the Fa ht argument.</p>
<h2>RETURN VALUES</h2>
<p> If successful, Fn ck_ht_reset_spmc will return <code>true</code> and will otherwise return <code>false.</code> This function will only fail if a replacement hash table could not be allocated internally.</p>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_reset_size_spmc3, ck_ht_count3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
