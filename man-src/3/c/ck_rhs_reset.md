---
title: "ck_rhs_reset(3)"
name: "ck_rhs_reset"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_rhs_reset/"
description: "ck_rhs_reset – remove all keys from a hash set"
---

<h2>NAME</h2>
<p> <code>ck_rhs_reset</code> &#8211; remove all keys from a hash set</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_rhs.h Ft bool Fn ck_rhs_reset ck_rhs_t *hs</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_rhs_reset 3 function will remove all keys stored in the hash set pointed to by the Fa hs argument.</p>
<h2>RETURN VALUES</h2>
<p> If successful, Fn ck_rhs_reset 3 will return true and will otherwise return false on failure. This function will only fail if a replacement hash set could not be allocated internally.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if Fa hs is uninitialized. Behavior is undefined if this function is called by a non-writer thread.</p>
<h2>SEE ALSO</h2>
<p> ck_rhs_init3, ck_rhs_move3, ck_rhs_destroy3, CK_RHS_HASH3, ck_rhs_iterator_init3, ck_rhs_next3, ck_rhs_get3, ck_rhs_put3, ck_rhs_put_unique3, ck_rhs_set3, ck_rhs_fas3, ck_rhs_remove3, ck_rhs_reset_size3, ck_rhs_grow3, ck_rhs_gc3, ck_rhs_rebuild3, ck_rhs_count3, ck_rhs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
