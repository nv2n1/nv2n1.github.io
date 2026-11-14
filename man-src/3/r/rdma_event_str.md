---
title: "rdma_event_str(3)"
name: "rdma_event_str"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_event_str/"
---

rdma_event_str - Returns a string representation of an rdma cm event.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
char *rdma_event_str

    (enumrdma_cm_event_type event);</code></pre>

<h2>Arguments</h2>

<dl><dt>event
<dd>Asynchronous event.</dl>

<h2>Description</h2>

Returns a string representation of an asynchronous event.

<h2>Return Value</h2>

Returns a pointer to a static character string corresponding to the event.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3) 
