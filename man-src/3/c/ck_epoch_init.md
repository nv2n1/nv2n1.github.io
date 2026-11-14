---
title: "ck_epoch_init(3)"
name: "ck_epoch_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_epoch_init/"
description: "ck_epoch_init – initialize epoch reclamation object"
---

<h2>NAME</h2>
<p> <code>ck_epoch_init</code> &#8211; initialize epoch reclamation object</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_epoch.h Ft void Fn ck_epoch_init ck_epoch_t *epoch</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_epoch_init function initializes the epoch object pointed to by the Fa epoch pointer.</p>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>ERRORS</h2>
<dl>
<p> The behavior of Fn ck_epoch_init is undefined if Fa epoch is not a pointer to a <code>ck_epoch_t</code> object.</dl>
<h2>SEE ALSO</h2>
<p> ck_epoch_register3, ck_epoch_unregister3, ck_epoch_recycle3, ck_epoch_poll3, ck_epoch_synchronize3, ck_epoch_reclaim3, ck_epoch_barrier3, ck_epoch_call3, ck_epoch_begin3, ck_epoch_end3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
