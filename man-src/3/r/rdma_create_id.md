---
title: "rdma_create_id(3)"
name: "rdma_create_id"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_create_id/"
---

rdma_create_id - Allocate a communication identifier.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_create_id

    (struct rdma_event_channel *channel,

     struct rdma_cm_id **id,

     void *context,

     enum rdma_port_space ps);</code></pre>

<h2>Arguments</h2>

<dl><dt>channel
<dd>The communication channel that events associated with the allocated rdma_cm_id will be reported on. This may be NULL.
<dt>id
<dd>A reference where the allocated communication identifier will be returned.
<dt>context
<dd>User specified context associated with the rdma_cm_id.
<dt>ps
<dd>RDMA port space.</dl>

<h2>Description</h2>

Creates an identifier that is used to track communication information.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

Rdma_cm_id's are conceptually equivalent to a socket for RDMA communication. The difference is that RDMA communication requires explicitly binding to a specified RDMA device before communication can occur, and most operations are asynchronous in nature. Asynchronous communication events on an rdma_cm_id are reported through the associated event channel. If the channel parameter is NULL, the rdma_cm_id will be placed into synchronous operation. While operating synchronously, calls that result in an event will block until the operation completes. The event will be returned to the user through the rdma_cm_id structure, and be available for access until another rdma_cm call is made. 

 Users must release the rdma_cm_id by calling rdma_destroy_id.

<h2>Port Space</h2>

Details of the services provided by the different port spaces are outlined below.
<dl><dt>RDMA_PS_TCP
<dd>Provides reliable, connection-oriented QP communication. Unlike TCP, the RDMA port space provides message, not stream, based communication.
<dt>RDMA_PS_UDP
<dd>Provides unreliable, connectionless QP communication. Supports both datagram and multicast communication.
<dt>RDMA_PS_IB
<dd>Provides for any IB services (UD, UC, RC, XRC, etc.).</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/3-rdma_create_event_channel/">rdma_create_event_channel</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_id/">rdma_destroy_id</a>(3), <a HREF="/docs/linux/man/3-rdma_get_devices/">rdma_get_devices</a>(3), <a HREF="/docs/linux/man/3-rdma_bind_addr/">rdma_bind_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_resolve_addr/">rdma_resolve_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_connect/">rdma_connect</a>(3), <a HREF="/docs/linux/man/3-rdma_listen/">rdma_listen</a>(3), <a HREF="/docs/linux/man/3-rdma_set_option/">rdma_set_option</a>(3) 
