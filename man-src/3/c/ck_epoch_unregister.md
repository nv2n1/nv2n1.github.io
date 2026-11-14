---
title: "ck_epoch_unregister(3)"
name: "ck_epoch_unregister"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_epoch_unregister/"
description: "ck_epoch_unregister – unregister a thread for epoch reclamation"
---

<h2>NAME</h2>
<p> <code>ck_epoch_unregister</code> &#8211; unregister a thread for epoch reclamation</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_epoch.h Ft void Fn ck_epoch_unregister ck_epoch_record_t *record</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_epoch_unregister 3 function allows for the record pointed by the Fa record pointer to be used as a return value by the Fn ck_epoch_recycle 3 function. This record can now be used by another thread of execution. Behavior is undefined if the object pointed by Fa record is modified in any way, even after a call is made to the Fn ck_epoch_unregister 3 function.</p>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_epoch_init3, ck_epoch_register3, ck_epoch_recycle3, ck_epoch_poll3, ck_epoch_synchronize3, ck_epoch_reclaim3, ck_epoch_barrier3, ck_epoch_call3, ck_epoch_begin3, ck_epoch_end3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
