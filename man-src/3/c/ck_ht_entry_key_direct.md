---
title: "ck_ht_entry_key_direct(3)"
name: "ck_ht_entry_key_direct"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_entry_key_direct/"
description: "ck_ht_entry_key_direct – return key value as specified in hash table entry"
---

<h2>NAME</h2>
<p> <code>ck_ht_entry_key_direct</code> &#8211; return key value as specified in hash table entry</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft uintptr_t Fn ck_ht_entry_key_direct ck_ht_entry_t *entry</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_entry_key_direct function will return the key value as specified in the object pointed to by the Fa entry argument. </p>
<p> It is expected that the entry is associated with a hash table initialized with <code>CK_HT_MODE_DIRECT</code> (see ck_ht_init3 for more information).</p>
<h2>RETURN VALUES</h2>
<p> Fn ck_ht_entry_key_direct returns <code>0</code> if the entry is empty. Otherwise, it returns the key value stored in the object pointed to by the Fa entry argument.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa entry has not been initialized.</p>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_count3, ck_ht_reset_spmc3, ck_ht_reset_size_spmc3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
