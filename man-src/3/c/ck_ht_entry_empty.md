---
title: "ck_ht_entry_empty(3)"
name: "ck_ht_entry_empty"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_entry_empty/"
description: "ck_ht_entry_empty – determine whether entry contains a key-value pair"
---

<h2>NAME</h2>
<p> <code>ck_ht_entry_empty</code> &#8211; determine whether entry contains a key-value pair</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft bool Fn ck_ht_entry_empty ck_ht_entry_t *entry</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_entry_empty function will return <code>false</code> if Fa entry points to a valid key-value pair. If Fa entry does not point to a valid key-value pair it returns <code>true.</code> It is expected that the object pointed to by Fa entry was initialized by a preceding call to the ck_ht_entry_set family of functions, the ck_ht_get_spmc3 function or the ck_ht_set_spmc3 function.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa entry has not been initialized.</p>
<h2>SEE ALSO</h2>
<p> ck_ht_stat3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_gc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_count3, ck_ht_reset_spmc3, ck_ht_reset_size_spmc3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
