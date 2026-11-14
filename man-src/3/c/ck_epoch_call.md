---
title: "ck_epoch_call(3)"
name: "ck_epoch_call"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_epoch_call/"
description: "ck_epoch_call – defer function execution until a grace period"
---

<h2>NAME</h2>
<p> <code>ck_epoch_call</code> &#8211; defer function execution until a grace period</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_epoch.h typedef struct ck_epoch_entry ck_epoch_entry_t;<br />
 typedef void ck_epoch_cb_t(ck_epoch_entry_t *); Ft void Fn ck_epoch_call ck_epoch_record_t *record ck_epoch_entry_t *entry ck_epoch_cb_t *function</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_epoch_call 3 function will defer the execution of the function pointed to by Fa function until a grace-period has been detected in Fa epoch . The function will be provided the pointer specified by Fa entry . The function will execute at some time in the future via calls to Fn ck_epoch_reclaim 3 , Fn ck_epoch_barrier 3 or Fn ck_epoch_poll 3 .</p>
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
struct object {
    int value;
    ck_epoch_entry_t epoch_entry;
};
static struct object *global;
CK_EPOCH_CONTAINER(struct object, epoch_entry, object_container)
void destroy_object(ck_epoch_entry_t *e)
{
    struct object *o = object_container(e);
    free(o);
    return;
}
void function(void)
{
    ck_epoch_record_t *record;
    struct object *n;
    record = malloc(sizeof *record);
    ck_epoch_register(&amp;epoch, record);
    n = malloc(sizeof *n);
    if (n == NULL)
        return;
    n-&gt;value = 1;
    /*
     * We are using an epoch section here because there are multiple
     * writers. It is also an option to use other forms of blocking
     * write-side synchronization such as mutexes.
     */
    ck_epoch_begin(record);
    n = ck_pr_fas_ptr(&amp;global, n);
    ck_epoch_end(record);
    /* Defer destruction of previous object. */
    ck_epoch_call(record, &amp;n-&gt;epoch_entry, destroy_object);
    /* Poll epoch sub-system in non-blocking manner. */
    ck_epoch_poll(record);
    return;
}
</code></pre>
</blockquote>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>ERRORS</h2>
<p> The object pointed to by Fa record must have been previously registered via Fn ck_epoch_register 3 .</p>
<h2>SEE ALSO</h2>
<p> ck_epoch_init3, ck_epoch_register3, ck_epoch_unregister3, ck_epoch_recycle3, ck_epoch_poll3, ck_epoch_synchronize3, ck_epoch_reclaim3, ck_epoch_barrier3, ck_epoch_begin3, ck_epoch_end3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
