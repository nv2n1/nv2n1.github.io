---
title: "ck_rhs_hash(3)"
name: "ck_rhs_hash"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rhs_hash/"
description: "CK_RHS_HASH – invoke hash function with hash set seed"
---

<p><code>CK_RHS_HASH</code> &#8211; invoke hash function with hash set seed</p>
<h2>Library</h2>
<p>Concurrency Kit (libck, -lck)</p>
<h2>Synopsis</h2>
<p>In ck_rhs.h Ft unsigned long Fn CK_RHS_HASH ck_rhs_t *hs ck_rhs_hash_cb_t *hf const void *key</p>
<h2>Description</h2>
<p>The Fn CK_RHS_HASH 3 macro will invoke the hash function pointed to by the Fa hf argument with the seed value associated with Fa hs and the key pointer specified by the Fa key argument.</p>
<h2>Return Values</h2>
<p>This function will return the value returned by the Fa hf function.</p>
<h2>Errors</h2>
<p>It is expected Fa hs was previously initialized via Fn ck_rhs_init 3 .</p>
<h2>See Also</h2>
<p>ck_rhs_init3, ck_rhs_destroy3, ck_rhs_iterator_init3, ck_rhs_next3, ck_rhs_get3, ck_rhs_put3, ck_rhs_set3, ck_rhs_remove3, ck_rhs_grow3, ck_rhs_count3, ck_rhs_reset3, ck_rhs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a></p>
