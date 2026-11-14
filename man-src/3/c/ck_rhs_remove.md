---
title: "ck_rhs_remove(3)"
name: "ck_rhs_remove"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rhs_remove/"
description: "ck_rhs_remove – remove key from a hash set"
---

<h2>NAME</h2>
<p> <code>ck_rhs_remove</code> &#8211; remove key from a hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rhs.h Ft void * Fn ck_rhs_remove ck_rhs_t *hs unsigned long hash const void *key</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_rhs_remove 3 function will attempt to remove the key specified by the Fa key argument in the hash set pointed to by the Fa hs argument. The key specified by Fa key is expected to have the hash value specified by the Fa hash argument (which was previously generated using the CK_RHS_HASH3 macro). </p>
<p> If the call to Fn ck_rhs_remove 3 was successful then the key contained in the hash set is returned. If the key was not a member of the hash set then <code>NULL</code> is returned.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, Fn ck_rhs_remove 3 returns a pointer to a key and otherwise returns <code>NULL</code> on failure.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa key or Fa hs are uninitialized.</p>
<h2>SEE ALSO</h2>
<p> ck_rhs_init3, ck_rhs_move3, ck_rhs_destroy3, CK_RHS_HASH3, ck_rhs_iterator_init3, ck_rhs_next3, ck_rhs_get3, ck_rhs_put3, ck_rhs_put_unique3, ck_rhs_set3, ck_rhs_fas3, ck_rhs_grow3, ck_rhs_gc3, ck_rhs_rebuild3, ck_rhs_count3, ck_rhs_reset3, ck_rhs_reset_size3, ck_rhs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
