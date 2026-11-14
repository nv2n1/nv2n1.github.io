---
title: "ck_ht_get_spmc(3)"
name: "ck_ht_get_spmc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_get_spmc/"
description: "ck_ht_get_spmc – load a key-value pair from a hash table"
---

<h2>NAME</h2>
<p> <code>ck_ht_get_spmc</code> &#8211; load a key-value pair from a hash table</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft bool Fn ck_ht_get_spmc ck_ht_t *ht ck_ht_hash_t h ck_ht_entry_t *entry</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_get_spmc function will return the value associated with the key specified in the Fa entry argument in the hash table pointed to by the Fa ht argument. The key specified in Fa entry is expected to have the hash value specified by the Fa h argument. </p>
<p> If Fa ht was created with CK_HT_MODE_BYTESTRING then Fa entry must have been initialized with the ck_ht_entry_set_key3 or ck_ht_entry_set3 functions. If Fa ht was created with CK_HT_MODE_DIRECT then Fa entry must have been initialized with the ck_ht_entry_key_set_direct3 or ck_ht_entry_set_direct3 functions. </p>
<p> It is expected that Fa h was initialized with ck_ht_hash3 if Fa ht was created with CK_HT_MODE_BYTESTRING. If Fa ht was initialized with CK_HT_MODE_DIRECT then it is expected that Fa h was initialized with the ck_ht_hash_direct3 function. </p>
<p> If the call to Fn ck_ht_get_spmc was successful then the key-value pair in Fa entry was successfully found in the hash table pointed to by Fa h and will fail if the key specified in Fa entry does not exist in the hash table. If successful Fa entry will contain the key-value pair found in the hash table pointed to by the Fa ht argument. </p>
<p> If Fa ht was initialized with CK_HT_MODE_BYTESTRING then the key/value pair in Fa entry may be extracted using the ck_ht_entry_key3 and ck_ht_entry_value3 functions. The length of the key may be extracted using the ck_ht_entry_key_length3 function. </p>
<p> If Fa ht was initialized with CK_HT_MODE_DIRECT then the key/value pair in Fa entry may be extracted using the ck_ht_entry_key_direct3 and ck_ht_entry_value_direct3 functions. </p>
<p> This function is safe to call in the presence of a concurrent writer.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion Fn ck_ht_get_spmc returns <code>true.</code> If successful, Fa entry will contain the key/value pair as found in the hash table. Otherwise the function returns <code>false</code> on failure.</p>
<h2>ERRORS</h2>
<dl>
<p> Behavior is undefined if Fa entry or Fa ht are uninitialized. The function will return <code>false</code> if the key as specified in Fa entry was not found in the hash table.</dl>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_reset_spmc3, ck_ht_reset_size_spmc3, ck_ht_count3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
