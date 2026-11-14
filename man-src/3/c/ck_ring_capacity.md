---
title: "ck_ring_capacity(3)"
name: "ck_ring_capacity"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ck_ring_capacity/"
description: "ck_ring_capacity – returns number of pointer slots in bounded FIFO"
---

<h2>NAME</h2>
<p> <code>ck_ring_capacity</code> &#8211; returns number of pointer slots in bounded FIFO</p>
<h2>LIBRARY</h2>
<p> Concurrency Kit (libck, -lck)</p>
<h2>SYNOPSIS</h2>
<p> In ck_ring.h Ft unsigned int Fn ck_ring_capacity ck_ring_t *ring</p>
<h2>DESCRIPTION</h2>
<p> The Fn ck_ring_capacity 3 function returns the number of pointers that can be held in the buffer pointed to by Fa ring . Note that a ring can only hold Fn ck_ring_capacity 3 minus one entries at a time.</p>
<h2>SEE ALSO</h2>
<p> ck_ring_init3, ck_ring_enqueue_spmc3, ck_ring_dequeue_spmc3, ck_ring_trydequeue_spmc3, ck_ring_enqueue_spmc_size3, ck_ring_dequeue_spsc3, ck_ring_enqueue_spsc3, ck_ring_enqueue_spsc_size3, ck_ring_size3 </p>
<p> Additional information available at <a rel="nofollow" href="http://concurrencykit.org/">http://concurrencykit.org/</a> </p>
<h2>Index</h2>
