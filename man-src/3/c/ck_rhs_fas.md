---
title: "ck_rhs_fas(3)"
name: "ck_rhs_fas"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rhs_fas/"
description: "ck_rhs_fas – fetch and store key in hash set"
---

<h2>NAME</h2>
<p> <code>ck_rhs_fas</code> &#8211; fetch and store key in hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rhs.h Ft bool Fn ck_rhs_fas ck_rhs_t *hs unsigned long hash const void *key void **previous</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_rhs_fas 3 function will fetch and store the key specified by the Fa key argument in the hash set pointed to by the Fa hs argument. The key specified by Fa key is expected to have the hash value specified by the Fa hash argument (which was previously generated using the CK_RHS_HASH3 macro). </p>
<p> If the call to Fn ck_rhs_fas 3 was successful then the key specified by Fa key was successfully stored in the hash set pointed to by Fa hs . The key must already exist in the hash set, and is replaced by Fa key and the previous value is stored into the void pointer pointed to by the Fa previous argument. If the key does not exist in the hash set then the function will return false and the hash set is unchanged. This function is guaranteed to be stable with respect to memory usage.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, Fn ck_rhs_fas 3 returns true and otherwise returns false on failure.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa key or Fa hs are uninitialized.</p>
<h2>SEE ALSO</h2>
<p> ck_rhs_init3, ck_rhs_move3, ck_rhs_destroy3, CK_RHS_HASH3, ck_rhs_iterator_init3, ck_rhs_next3, ck_rhs_get3, ck_rhs_put3, ck_rhs_put_unique3, ck_rhs_remove3, ck_rhs_grow3, ck_rhs_rebuild3, ck_rhs_gc3, ck_rhs_count3, ck_rhs_reset3, ck_rhs_reset_size3, ck_rhs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
