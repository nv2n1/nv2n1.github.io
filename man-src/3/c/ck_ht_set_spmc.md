---
title: "ck_ht_set_spmc(3)"
name: "ck_ht_set_spmc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_set_spmc/"
description: "ck_ht_set_spmc – store key-value pair into hash table"
---

<h2>NAME</h2>
<p> <code>ck_ht_set_spmc</code> &#8211; store key-value pair into hash table</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft bool Fn ck_ht_set_spmc ck_ht_t *ht ck_ht_hash_t h ck_ht_entry_t *entry</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_set_spmc function will store the key-value pair specified in the Fa entry argument in the hash table pointed to by the Fa ht argument. The key specified in Fa entry is expected to have the hash value specified by the Fa h argument. </p>
<p> If Fa ht was created with CK_HT_MODE_BYTESTRING then Fa entry must have been initialized with the ck_ht_entry_set3 function. If Fa ht was created with CK_HT_MODE_DIRECT then Fa entry must have been initialized with the ck_ht_entry_set_direct3 function. </p>
<p> It is expected that Fa h was initialized with ck_ht_hash3 if Fa ht was created with CK_HT_MODE_BYTESTRING. If Fa ht was initialized with CK_HT_MODE_DIRECT then it is expected that Fa h was initialized with the ck_ht_hash_direct3 function. </p>
<p> If the call to Fn ck_ht_set_spmc was successful then the key-value pair in Fa entry will contain the previous key-value pair associated with the key originally contained in the Fa entry argument. If the operation was unsuccessful then Fa entry is unmodified. </p>
<p> This function is safe to call in the presence of concurrent ck_ht_get_spmc operations.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion Fn ck_ht_set_spmc returns <code>true</code> and otherwise returns <code>false</code> on failure.</p>
<h2>ERRORS</h2>
<dl>
<p> Behavior is undefined if Fa entry or Fa ht are uninitialized. The function will return <code>false</code> if the hash table required to be grown but failed while attempting to grow.</dl>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_reset_spmc3, ck_ht_reset_size_spmc3, ck_ht_count3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
