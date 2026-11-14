---
title: "ck_ht_gc(3)"
name: "ck_ht_gc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ht_gc/"
description: "ck_ht_gc – perform maintenance on a hash table"
---

<h2>NAME</h2>
<p> <code>ck_ht_gc</code> &#8211; perform maintenance on a hash table</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ht.h Ft bool Fn ck_ht_gc ck_ht_t *ht unsigned long cycles unsigned long seed</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ht_gc function will perform various maintenance routines on the hash table pointed to by Fa ht , including defragmentation of probe sequences with respect to tombstones and in the case that the delete workload hint has been passed, recalculation of probe sequence bounds. The Fa cycles argument is used to indicate how many hash table entries should be subject to attempted maintenance. If Fa cycles is 0, then maintenance is performed on the complete hash table. The Fa seed argument determines the start location of the maintenance process. If Fa cycles is non-zero, it is recommended that Fa seed is some random value. If the delete hint has been passed, the function will require an additional 12% of memory (with respect to existing memory usage of the set), until operation completion.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, Fn ck_ht_gc 3 returns true and otherwise returns false on failure due to memory allocation failure.</p>
<h2>ERRORS</h2>
<p> This function will only return false if there are internal memory allocation failures.</p>
<h2>SEE ALSO</h2>
<p> ck_ht_count3, ck_ht_stat3, ck_ht_init3, ck_ht_destroy3, ck_ht_hash3, ck_ht_hash_direct3, ck_ht_set_spmc3, ck_ht_put_spmc3, ck_ht_get_spmc3, ck_ht_grow_spmc3, ck_ht_remove_spmc3, ck_ht_reset_size_spmc3, ck_ht_reset_spmc3, ck_ht_entry_empty3, ck_ht_entry_key_set3, ck_ht_entry_key_set_direct3, ck_ht_entry_key3, ck_ht_entry_key_length3, ck_ht_entry_value3, ck_ht_entry_set3, ck_ht_entry_set_direct3, ck_ht_entry_key_direct3, ck_ht_entry_value_direct3, ck_ht_iterator_init3, ck_ht_next3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
