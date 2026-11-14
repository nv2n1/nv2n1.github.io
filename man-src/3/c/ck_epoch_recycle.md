---
title: "ck_epoch_recycle(3)"
name: "ck_epoch_recycle"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_epoch_recycle/"
description: "ck_epoch_recycle – return an epoch record that may be used by caller"
---

<h2>NAME</h2>
<p> <code>ck_epoch_recycle</code> &#8211; return an epoch record that may be used by caller</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_epoch.h Ft ck_epoch_record_t * Fn ck_epoch_recycle ck_epoch_t *epoch</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_epoch_recycle 3 function attempts to return an unused epoch record object for use by the caller. These epoch records were associated with previous calls to the Fn ck_epoch_unregister 3 function.</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_epoch.h&gt;
#include &lt;stdlib.h&gt;
/*
 * epoch was previously initialized with ck_epoch_init.
 */
ck_epoch_t *epoch;
void function(void)
{
    ck_epoch_record_t *record;
    record = ck_epoch_recycle(&amp;epoch);
    if (record == NULL) {
        record = malloc(sizeof *record);
        if (record == NULL)
            return;
        ck_epoch_register(&amp;epoch, record);
    }
    /*
     * After we are done, we will unregister the record so it
     * can be used by other new participants in the epoch system
     * provided by the object pointed to by "epoch".
     */
    ck_epoch_unregister(&amp;epoch, record);
    return;
}
</code></pre>
</blockquote>
<h2>RETURN VALUES</h2>
<p> This function returns a pointer to a <code>ck_epoch_record_t</code> object. If no unused record was found to be associated with the object pointed to by Fa epoch , then the function will return NULL.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if the object pointed to by Fa epoch is not a valid epoch object.</p>
<h2>SEE ALSO</h2>
<p> ck_epoch_init3, ck_epoch_register3, ck_epoch_unregister3, ck_epoch_poll3, ck_epoch_synchronize3, ck_epoch_reclaim3, ck_epoch_barrier3, ck_epoch_call3, ck_epoch_begin3, ck_epoch_end3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
