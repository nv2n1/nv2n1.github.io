---
title: "ck_ht_remove_spmc(3)"
name: "ck_ht_remove_spmc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_remove_spmc/"
description: "ck_ht_remove_spmc – resize a hash table if necessary"
---

<h2>NAME</h2>
<p> <code>ck_ht_remove_spmc</code> &#8211; resize a hash table if necessary</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft bool Fn ck_ht_remove_spmc ck_ht_t *ht ck_ht_hash_t h ck_ht_entry_t *entry</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_remove_spmc function will remove the key-value pair associated with the key specified by the Fa entry argument. </p>
<p> If Fa ht was created with CK_HT_MODE_BYTESTRING then Fa entry must have been initialized with the ck_ht_entry_set_key3 or ck_ht_entry_set3 functions. If Fa ht was created with CK_HT_MODE_DIRECT then Fa entry must have been initialized with the ck_ht_entry_key_set_direct3 or ck_ht_entry_set_direct3 functions. </p>
<p> It is expected that Fa h was initialized with ck_ht_hash3 if Fa ht was created with CK_HT_MODE_BYTESTRING. If Fa ht was initialized with CK_HT_MODE_DIRECT then it is expected that Fa h was initialized with the ck_ht_hash_direct3 function.</p>
<h2>RETURN VALUES</h2>
<p> If successful, Fa entry will contain the key-value pair that was found in the hash table and Fn ck_ht_remove_spmc will return <code>true.</code> If the entry could not be found then Fn ck_ht_remove_spmc will return <code>false.</code></p>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_reset_spmc3, ck_ht_reset_size_spmc3, ck_ht_count3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
