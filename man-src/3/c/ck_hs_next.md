---
title: "ck_hs_next(3)"
name: "ck_hs_next"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_hs_next/"
description: "ck_hs_next – iterate to next entry in hash set"
---

<h2>NAME</h2>
<p> <code>ck_hs_next</code> &#8211; iterate to next entry in hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_hs.h Ft bool Fn ck_hs_next ck_hs_t *hs ck_hs_iterator_t *iterator void **entry</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_hs_next 3 function will increment the iterator object pointed to by Fa iterator to point to the next non-empty hash set entry. If Fn ck_hs_next 3 returns true then the pointer pointed to by Fa entry is initialized to the current hash set key pointed to by the Fa iterator object. </p>
<p> It is expected that Fa iterator has been initialized using the ck_hs_iterator_init3 function or statically initialized using CK_HS_ITERATOR_INITIALIZER.</p>
<h2>RETURN VALUES</h2>
<p> If Fn ck_hs_next 3 returns true then the object pointed to by Fa entry points to a valid hash set key. If Fn ck_hs_next 3 returns false then the value of the object pointed to by Fa entry is undefined.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa iterator or Fa hs are uninitialized.</p>
<h2>SEE ALSO</h2>
<p> ck_hs_init3, ck_hs_move3, ck_hs_destroy3, CK_HS_HASH3, ck_hs_iterator_init3, ck_hs_get3, ck_hs_put3, ck_hs_put_unique3, ck_hs_set3, ck_hs_fas3, ck_hs_remove3, ck_hs_grow3, ck_hs_rebuild3, ck_hs_gc3, ck_hs_count3, ck_hs_reset3, ck_hs_reset_size3, ck_hs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
