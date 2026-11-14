---
title: "ck_ring_enqueue_spsc_size(3)"
name: "ck_ring_enqueue_spsc_size"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ring_enqueue_spsc_size/"
description: "ck_ring_enqueue_spsc_size – enqueue pointer into bounded FIFO and return size of buffer"
---

<h2>NAME</h2>
<p> <code>ck_ring_enqueue_spsc_size</code> &#8211; enqueue pointer into bounded FIFO and return size of buffer</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ring.h Ft bool Fn ck_ring_enqueue_spsc_size ck_ring_t *ring ck_ring_buffer_t *buffer void *entry unsigned int *size</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ring_enqueue_spsc_size 3 function enqueues the pointer Fa entry into the bounded buffer pointed to by Fa ring in FIFO fashion. The buffer pointed to by Fa buffer must be unique to Fa ring and point to an array of ck_ring_buffer_t of sufficient length (according to the power-of-2 elements in the buffer). The decoupling of the ring from the buffer serves to address use-cases involving multiple address spaces and DMA, among others. If you are on non-POSIX platforms or wish for strict compliance with C, then it is recommended to pass a pointer of type void ** for Fa entry . This function is safe to call without locking for up to one concurrent invocation of Fn ck_ring_dequeue_spsc 3 . This function provides wait-free progress guarantees.</p>
<h2>EXAMPLE</h2>
<blockquote>
<pre><code>
#include &lt;ck_ring.h&gt;
/* This ring was previously initialized with ck_ring_init. */
ck_ring_t ring;
/* The ring was initialized for 1023 elements. */
ck_ring_buffer_t buffer[1024];
void enqueue(void)
{
    void *entry = some_object;
    unsigned int length;
    /* Attempt to enqueue pointer to some_object into buffer. */
    if (ck_ring_enqueue_spsc(&amp;ring, &amp;buffer, &amp;entry, &amp;length) == false) {
        /*
         * The buffer was full and the enqueue operation
         * has failed.
         */
        return;
    }
    /*
     * If buffer length was 100 items or more at the time entry was
     * enqueued, do something.
     */
    if (length &gt; 100) {
        do_something;
    }
    return;
}
</code></pre>
</blockquote>
<h2>RETURN VALUES</h2>
<p> The function returns true if the value of Fa entry was successfully enqueued into Fa ring . This function will return the number of items in Fa ring with respect to the linearization point (the point in item that Fa entry is enqueued). The function will return false if the value of Fa entry could not be enqueued which only occurs if Fa ring was full.</p>
<h2>SEE ALSO</h2>
<p> ck_ring_init3, ck_ring_dequeue_spmc3, ck_ring_trydequeue_spmc3, ck_ring_enqueue_spmc3, ck_ring_enqueue_spmc_size3, ck_ring_dequeue_spsc3, ck_ring_enqueue_spsc3, ck_ring_capacity3, ck_ring_size3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
