---
title: "ck_hs_apply(3)"
name: "ck_hs_apply"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_hs_apply/"
description: "ck_hs_apply – apply a function to hash set value"
---

<h2>NAME</h2>
<p> <code>ck_hs_apply</code> &#8211; apply a function to hash set value</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_hs.h Ft void * Fn ck_hs_apply_fn_t void *key void *closure Ft bool Fn ck_hs_apply ck_hs_t *hs unsigned long hash const void *key ck_hs_apply_fn_t *function void *argument</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_hs_apply 3 function will lookup the hash set slot associated with Fa key and pass it to function pointed to by Fa function for further action. This callback may remove or replace the value by respectively returning NULL or a pointer to another object with an identical key. The first argument passed to Fa function is a pointer to the object found in the hash set and the second argument is the Fa argument pointer passed to Fn ck_hs_apply 3 . If the pointer returned by Fa function is equivalent to the first argument then no modification is made to the hash set.</p>
<h2>RETURN VALUES</h2>
<p> Upon successful completion, Fn ck_hs_apply 3 returns true and otherwise returns false on failure.</p>
<h2>SEE ALSO</h2>
<p> ck_hs_init3, ck_hs_move3, ck_hs_destroy3, ck_hs_fas3, CK_HS_HASH3, ck_hs_iterator_init3, ck_hs_next3, ck_hs_get3, ck_hs_put3, ck_hs_put_unique3, ck_hs_remove3, ck_hs_grow3, ck_hs_rebuild3, ck_hs_gc3, ck_hs_count3, ck_hs_reset3, ck_hs_reset_size3, ck_hs_stat3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
