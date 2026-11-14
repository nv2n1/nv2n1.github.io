---
title: "ck_ring_init(3)"
name: "ck_ring_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ring_init/"
description: "ck_ring_init – initialize bounded FIFO"
---

<h2>NAME</h2>
<p> <code>ck_ring_init</code> &#8211; initialize bounded FIFO</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ring.h Ft void Fn ck_ring_init ck_ring_t *ring unsigned int size</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ring_init function initializes a bounded FIFO buffer pointed to by Fa ring for the storage of up to Fa size number of pointers. The Fa size argument must be a power-of-two greater than or equal to 4.</p>
<h2>RETURN VALUES</h2>
<p> This function has no return value.</p>
<h2>SEE ALSO</h2>
<p> ck_ring_dequeue_spmc3, ck_ring_trydequeue_spmc3, ck_ring_enqueue_spmc3, ck_ring_enqueue_spmc_size3, ck_ring_dequeue_spsc3, ck_ring_enqueue_spsc3, ck_ring_enqueue_spsc_size3, ck_ring_capacity3, ck_ring_size3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
