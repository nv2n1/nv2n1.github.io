---
title: "ck_hs_get(3)"
name: "ck_hs_get"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_hs_get/"
description: "ck_hs_get – load a key from a hash set"
---

<h2>NAME</h2>
<p> <code>ck_hs_get</code> &#8211; load a key from a hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_hs.h Ft void * Fn ck_hs_get ck_hs_t *hs unsigned long hash const void *key</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_hs_get 3 function will return a pointer to a key in the hash set Fa hs that is of equivalent value to the object pointed to by Fa key . The key specified by Fa key is expected to have the hash value specified by the Fa hash argument (which is to have been previously generated using the CK_HS_HASH3 macro).</p>
<h2>RETURN VALUES</h2>
<p> If the provided key is a member of Fa hs then a pointer to the key as stored in Fa hs is returned. If the key was not found in Fa hs then a value of <code>NULL</code> is returned.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa entry or Fa hs are uninitialized.</p>
<h2>SEE ALSO</h2>
<p> ck_hs_init3, ck_hs_move3, ck_hs_destroy3, CK_HS_HASH3, ck_hs_iterator_init3, ck_hs_next3, ck_hs_put3, ck_hs_put_unique3, ck_hs_set3, ck_hs_fas3, ck_hs_remove3, ck_hs_grow3, ck_hs_rebuild3, ck_hs_gc3, ck_hs_count3, ck_hs_reset3, ck_hs_reset_size3, ck_hs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
