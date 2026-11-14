---
title: "rdma_notify(3)"
name: "rdma_notify"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_notify/"
---

rdma_notify - Notifies the librdmacm of an asynchronous event.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_notify

    (struct rdma_cm_id *id,

     enum ibv_event_type event);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>RDMA identifier.
<dt>event
<dd>Asynchronous event.</dl>

<h2>Description</h2>

Used to notify the librdmacm of asynchronous events that have occurred on a QP associated with the rdma_cm_id.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason. If errno is set to EISCONN (transport endpoint is already connected), this indicates that the the underlying communication manager established the connection before the call to rdma_notify could be processed. In this case, the error may safely be ignored.

<h2>Notes</h2>

Asynchronous events that occur on a QP are reported through the user's device event handler. This routine is used to notify the librdmacm of communication events. In most cases, use of this routine is not necessary, however if connection establishment is done out of band (such as done through Infiniband), it's possible to receive data on a QP that is not yet considered connected. This routine forces the connection into an established state in this case in order to handle the rare situation where the connection never forms on its own. Calling this routine ensures the delivery of the RDMA_CM_EVENT_ESTABLISHED event to the application. Events that should be reported to the CM are: IB_EVENT_COMM_EST.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_connect/">rdma_connect</a>(3), <a HREF="/docs/linux/man/3-rdma_accept/">rdma_accept</a>(3), <a HREF="/docs/linux/man/3-rdma_listen/">rdma_listen</a>(3) 
