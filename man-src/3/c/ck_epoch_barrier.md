---
title: "ck_epoch_barrier(3)"
name: "ck_epoch_barrier"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_epoch_barrier/"
description: "ck_epoch_barrier – block until a grace period and all callbacks have been dispatched"
---

<h2>NAME</h2>
<p> <code>ck_epoch_barrier</code> &#8211; block until a grace period and all callbacks have been dispatched</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_epoch.h Ft void Fn ck_epoch_barrier ck_epoch_record_t *record</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_epoch_barrier 3 function will block the caller until a grace period has been detected, according to the semantics of epoch reclamation. Any objects requiring safe memory reclamation which are logically deleted are safe for physical deletion following a call to Fn ck_epoch_barrier 3 . This function will also dispatch all callbacks associated with Fa epoch that were previously scheduled via Fn ck_epoch_call 3 .</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_epoch.h&gt;
#include &lt;ck_stack.h&gt;
#include &lt;stdlib.h&gt;
/*
 * epoch was previously initialized with ck_epoch_init.
 * stack was previously initialized with ck_stack_init.
 */
ck_epoch_t *epoch;
ck_stack_t *stack;
void function(void)
{
    ck_epoch_record_t *record;
    ck_stack_entry_t *s;
    record = malloc(sizeof *record);
    ck_epoch_register(&amp;epoch, record);
    /*
     * We are using an epoch section here to guarantee no
     * nodes in the stack are deleted while we are dereferencing
     * them. This is needed here because there are multiple writers.
     * If there was only one thread popping from the this stack,
     * then there is no need to ck_epoch_begin/ck_epoch_end.
     */
    ck_epoch_begin(record);
    /* Logically delete an object. */
    s = ck_stack_pop_upmc(stack);
    ck_epoch_end(record);
    /*
     * Wait until no threads could possibly have a reference to the
     * object we just popped (assume all threads are simply executing
     * ck_stack_pop_upmc).
     */
    ck_epoch_barrier(record);
    /* It is now safe to physically delete the object. */
    free(s);
    return;
}
</code></pre>
</blockquote>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>ERRORS</h2>
<p> Behavior is undefined if the object pointed to by Fa epoch is not a valid epoch object. The object pointed to by Fa record must have been previously registered via Fn ck_epoch_register 3 .</p>
<h2>SEE ALSO</h2>
<p> ck_epoch_init3, ck_epoch_register3, ck_epoch_unregister3, ck_epoch_recycle3, ck_epoch_poll3, ck_epoch_synchronize3, ck_epoch_reclaim3, ck_epoch_call3, ck_epoch_begin3, ck_epoch_end3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
