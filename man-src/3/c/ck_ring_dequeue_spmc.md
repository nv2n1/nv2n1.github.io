---
title: "ck_ring_dequeue_spmc(3)"
name: "ck_ring_dequeue_spmc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ring_dequeue_spmc/"
description: "ck_ring_dequeue_spmc – dequeue pointer from bounded FIFO"
---

<h2>NAME</h2>
<p> <code>ck_ring_dequeue_spmc</code> &#8211; dequeue pointer from bounded FIFO</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ring.h Ft bool Fn ck_ring_dequeue_spmc ck_ring_t *ring ck_ring_buffer_t *buffer void *result</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ring_dequeue_spmc 3 function dequeues a pointer from the bounded buffer pointed to by Fa ring in FIFO fashion. The pointer is stored in the pointer pointed to by Fa result . The buffer pointed to by Fa buffer must be unique to Fa ring . The decoupling of the ring from the buffer serves to address use-cases involving multiple address spaces and DMA, among others. If you are on non-POSIX platforms or wish for strict compliance with C, then it is recommended to pass a pointer of type void ** for Fa result . This function is safe to call without locking for UINT_MAX concurrent invocations of Fn ck_ring_dequeue_spmc 3 or Fn ck_ring_trydequeue_spmc 3 and up to one concurrent Fn ck_ring_enqueue_spmc 3 or Fn ck_ring_tryenqueue_spmc 3 invocation. This function provides lock-free progress guarantees.</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_ring.h&gt;
/* This ring was previously initialized with ck_ring_init. */
ck_ring_t ring;
/* The ring was initialized for 1023 elements. */
ck_ring_buffer_t buffer[1024];
void dequeue(void)
{
    void *result;
    /* Dequeue from ring until it is empty. */
    while (ck_ring_dequeue_spmc(&amp;ring, &amp;buffer, &amp;result) == true) {
        /*
         * Results contains the oldest pointer in ring
         * since the dequeue operation returned true.
         */
        operation(result);
    }
    /* An empty ring was encountered, leave. */
    return;
}
</code></pre>
</blockquote>
<h2>RETURN VALUES</h2>
<p> The function returns true if the buffer was non-empty. The result of the dequeue operation is stored in the value pointed to by Fa result . The function will return false if the buffer was empty and the value in Fa result will be undefined.</p>
<h2>SEE ALSO</h2>
<p> ck_ring_init3, ck_ring_trydequeue_spmc3, ck_ring_enqueue_spmc3, ck_ring_enqueue_spmc_size3, ck_ring_dequeue_spsc3, ck_ring_enqueue_spsc3, ck_ring_enqueue_spsc_size3, ck_ring_capacity3, ck_ring_size3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
