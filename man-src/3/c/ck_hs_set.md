---
title: "ck_hs_set(3)"
name: "ck_hs_set"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_hs_set/"
description: "ck_hs_set – store key into a hash set"
---

<h2>NAME</h2>
<p> <code>ck_hs_set</code> &#8211; store key into a hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_hs.h Ft bool Fn ck_hs_set ck_hs_t *hs unsigned long hash const void *key void **previous</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_hs_set 3 function will store the key specified by the Fa key argument in the hash set pointed to by the Fa hs argument. The key specified by Fa key is expected to have the hash value specified by the Fa hash argument (which was previously generated using the CK_HS_HASH3 macro). </p>
<p> If the call to Fn ck_hs_set 3 was successful then the key specified by Fa key was successfully stored in the hash set pointed to by Fa hs . If the key already exists in the hash set, then it is replaced by Fa key and the previous value is stored into the void pointer pointed to by the Fa previous argument. If previous is set to <code>NULL</code> then Fa key was not a replacement for an existing entry in the hash set.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, Fn ck_hs_set 3 returns true and otherwise returns false on failure.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa key or Fa hs are uninitialized. The function will also return false if the hash set could not be enlarged to accomodate key insertion.</p>
<h2>SEE ALSO</h2>
<p> ck_hs_init3, ck_hs_move3, ck_hs_destroy3, CK_HS_HASH3, ck_hs_iterator_init3, ck_hs_next3, ck_hs_get3, ck_hs_put3, ck_hs_put_unique3, ck_hs_fas3, ck_hs_remove3, ck_hs_grow3, ck_hs_gc3, ck_hs_rebuild3, ck_hs_count3, ck_hs_reset3, ck_hs_reset_size3, ck_hs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
