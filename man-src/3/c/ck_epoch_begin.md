---
title: "ck_epoch_begin(3)"
name: "ck_epoch_begin"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_epoch_begin/"
description: "ck_epoch_begin – begin epoch-protected segment of execution"
---

<h2>NAME</h2>
<p> <code>ck_epoch_begin</code> &#8211; begin epoch-protected segment of execution</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_epoch.h Ft void Fn ck_epoch_begin ck_epoch_record_t *record ck_epoch_section_t *section</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_epoch_begin 3 function will mark the beginning of an epoch-protected code section. An epoch-protected code section is delimited by a call to the Fn ck_epoch_end 3 function. Though recursion is allowed for epoch-protected sections, recursive calls will be associated with the Fn ck_epoch_begin 3 that is at the top of the call stack. If a section is passed, then recursion on a record will cause the epoch to be refreshed on entry of every protected section.</p>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>ERRORS</h2>
<p> The object pointed to by Fa epoch must have been previously initiated via Fn ck_epoch_init 3 . The object pointed to by Fa record must have been previously registered via Fn ck_epoch_register 3 .</p>
<h2>SEE ALSO</h2>
<p> ck_epoch_init3, ck_epoch_register3, ck_epoch_unregister3, ck_epoch_recycle3, ck_epoch_poll3, ck_epoch_synchronize3, ck_epoch_reclaim3, ck_epoch_barrier3, ck_epoch_call3, ck_epoch_end3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
