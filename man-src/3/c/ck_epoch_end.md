---
title: "ck_epoch_end(3)"
name: "ck_epoch_end"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_epoch_end/"
description: "ck_epoch_end – end epoch-protected segment of execution"
---

<h2>NAME</h2>
<p> <code>ck_epoch_end</code> &#8211; end epoch-protected segment of execution</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_epoch.h Ft void Fn ck_epoch_end ck_epoch_record_t *record ck_epoch_section_t *section</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_epoch_end 3 function will mark the end of an epoch-protected code section. Fa section must point to a section object initialized previously with Fn ck_epoch_begin 3 .</p>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>ERRORS</h2>
<p> The object pointed to by Fa record must have been previously registered via Fn ck_epoch_register 3 .</p>
<h2>SEE ALSO</h2>
<p> ck_epoch_init3, ck_epoch_register3, ck_epoch_unregister3, ck_epoch_recycle3, ck_epoch_poll3, ck_epoch_synchronize3, ck_epoch_reclaim3, ck_epoch_barrier3, ck_epoch_call3, ck_epoch_begin3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
