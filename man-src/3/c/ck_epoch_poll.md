---
title: "ck_epoch_poll(3)"
name: "ck_epoch_poll"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_epoch_poll/"
description: "ck_epoch_poll – non-blocking poll of epoch object for dispatch cycles"
---

<h2>NAME</h2>
<p> <code>ck_epoch_poll</code> &#8211; non-blocking poll of epoch object for dispatch cycles</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_epoch.h Ft bool Fn ck_epoch_poll ck_epoch_record_t *record</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_epoch_poll 3 function will attempt to dispatch any functions associated with the object pointed to by Fa epoch via Fn ck_epoch_call 3 if deemed safe. This function is meant to be used in cases epoch reclamation cost must be amortized over time in a manner that does not affect caller progress.</p>
<h2>RETURN VALUES</h2>
<p> This function will return true if at least one function was dispatched. This function will return false if it has determined not all threads have observed the latest generation of epoch-protected objects. Neither value indicates an error.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if the object pointed to by Fa record has not have been previously registered via Fn ck_epoch_register 3 .</p>
<h2>SEE ALSO</h2>
<p> ck_epoch_init3, ck_epoch_register3, ck_epoch_unregister3, ck_epoch_recycle3, ck_epoch_synchronize3, ck_epoch_reclaim3, ck_epoch_barrier3, ck_epoch_call3, ck_epoch_begin3, ck_epoch_end3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
