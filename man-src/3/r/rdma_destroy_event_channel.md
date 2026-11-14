---
title: "rdma_destroy_event_channel(3)"
name: "rdma_destroy_event_channel"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_destroy_event_channel/"
---

rdma_destroy_event_channel - Close an event communication channel.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
void rdma_destroy_event_channel

    (struct rdma_event_channel *channel);</code></pre>

<h2>Arguments</h2>

<dl><dt>channel
<dd>The communication channel to destroy.</dl>

<h2>Description</h2>

Release all resources associated with an event channel and closes the associated file descriptor.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

All rdma_cm_id's associated with the event channel must be destroyed, and all returned events must be acked before calling this function.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_create_event_channel/">rdma_create_event_channel</a>(3), <a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3), <a HREF="/docs/linux/man/3-rdma_ack_cm_event/">rdma_ack_cm_event</a>(3) 
