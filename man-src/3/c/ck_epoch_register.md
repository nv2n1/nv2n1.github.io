---
title: "ck_epoch_register(3)"
name: "ck_epoch_register"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_epoch_register/"
description: "ck_epoch_register – register a thread for epoch reclamation"
---

<h2>NAME</h2>
<p> <code>ck_epoch_register</code> &#8211; register a thread for epoch reclamation</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_epoch.h Ft void Fn ck_epoch_register ck_epoch_t *epoch ck_epoch_record_t *record</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_epoch_register 3 function associates a record object specified by the Fa record pointer with the epoch object pointed to by Fa epoch . Any thread or processor that will require safe memory reclamation guarantees must register a unique record object. After registration, the object pointed to by the Fa record argument will have lifetime managed by the underlying epoch sub-system. The record object must not be destroyed after it is associated with a Fn ck_epoch_register 3 call.</p>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_epoch_init3, ck_epoch_unregister3, ck_epoch_recycle3, ck_epoch_poll3, ck_epoch_synchronize3, ck_epoch_reclaim3, ck_epoch_barrier3, ck_epoch_call3, ck_epoch_begin3, ck_epoch_end3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
