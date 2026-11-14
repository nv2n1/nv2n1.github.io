---
title: "rdma_ack_cm_event(3)"
name: "rdma_ack_cm_event"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_ack_cm_event/"
---

rdma_ack_cm_event - Free a communication event.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_ack_cm_event

    (struct rdma_cm_event *event);</code></pre>

<h2>Arguments</h2>

<dl><dt>event
<dd>Event to be released.</dl>

<h2>Description</h2>

All events which are allocated by rdma_get_cm_event must be released, there should be a one-to-one correspondence between successful gets and acks. This call frees the event structure and any memory that it references.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_id/">rdma_destroy_id</a>(3) 
