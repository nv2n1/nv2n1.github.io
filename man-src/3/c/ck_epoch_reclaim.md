---
title: "ck_epoch_reclaim(3)"
name: "ck_epoch_reclaim"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_epoch_reclaim/"
description: "ck_epoch_reclaim – immediately execute all deferred callbacks"
---

<h2>NAME</h2>
<p> <code>ck_epoch_reclaim</code> &#8211; immediately execute all deferred callbacks</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_epoch.h Ft void Fn ck_epoch_reclaim ck_epoch_record_t *record</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_epoch_reclaim 3 function will unconditionally execute all callbacks that have been deferred with Fn ck_epoch_call 3 .</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_epoch.h&gt;
#include &lt;ck_stack.h&gt;
#include &lt;stdlib.h&gt;
/*
 * epoch was previously initialized with ck_epoch_init.
 */
ck_epoch_t *epoch;
void function(void)
{
    ck_epoch_record_t *record;
    logically_delete(object);
    ck_epoch_call(epoch, record, &amp;object-&gt;epoch_entry, destructor);
    /*
     * Wait until no threads could possibly have a reference to the
     * object we just deleted.
     */
    ck_epoch_synchronize(epoch, record);
    /*
     * Execute all deferred callbacks.
     */
    ck_epoch_reclaim(record);
    return;
}
</code></pre>
</blockquote>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_epoch_init3, ck_epoch_register3, ck_epoch_unregister3, ck_epoch_recycle3, ck_epoch_poll3, ck_epoch_reclaim3, ck_epoch_barrier3, ck_epoch_call3, ck_epoch_begin3, ck_epoch_end3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
