---
title: "rdma_create_event_channel(3)"
name: "rdma_create_event_channel"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_create_event_channel/"
---

rdma_create_event_channel - Open a channel used to report communication events.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
struct rdma_event_channel *rdma_create_event_channel

    (void);</code></pre>

<h2>Arguments</h2>

<dl><dt>void
<dd>no arguments</dl>

<h2>Description</h2>

Asynchronous events are reported to users through event channels.

<h2>Return Value</h2>

Returns a pointer to the created event channel, or NULL if the request fails. On failure, errno will be set to indicate the failure reason.

<h2>Notes</h2>

Event channels are used to direct all events on an rdma_cm_id. For many clients, a single event channel may be sufficient, however, when managing a large number of connections or cm_id's, users may find it useful to direct events for different cm_id's to different channels for processing. 

 All created event channels must be destroyed by calling rdma_destroy_event_channel. Users should call rdma_get_cm_event to retrieve events on an event channel. 

 Each event channel is mapped to a file descriptor. The associated file descriptor can be used and manipulated like any other fd to change its behavior. Users may make the fd non-blocking, poll or select the fd, etc.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_event_channel/">rdma_destroy_event_channel</a>(3) 
