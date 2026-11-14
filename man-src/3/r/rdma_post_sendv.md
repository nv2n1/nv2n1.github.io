---
title: "rdma_post_sendv(3)"
name: "rdma_post_sendv"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_post_sendv/"
---

rdma_post_sendv - post a work request to send a message.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_verbs.h&gt;
int rdma_post_sendv

    (struct rdma_cm_id *id,

     void *context,

     struct ibv_sge *slg,

     int nsge,

     int flags);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>A reference to a communication identifier where the message buffer will be posted.
<dt>context
<dd>User-defined context associated with the request.
<dt>slg
<dd>A scatter-gather list of memory buffers posted as a single request.
<dt>nsge
<dd>The number of scatter-gather entries in the slg array.
<dt>flags
<dd>Optional flags used to control the send operation.</dl>

<h2>Description</h2>

Posts a work request to the send queue of the queue pair associated with the rdma_cm_id. The contents of the posted buffers will be sent to the remote peer of a connection.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

The user is responsible for ensuring that the remote peer has queued a receive request before issuing the send operations. For a list of supported flags, see ibv_post_send. Unless the send request is using inline data, the message buffers must have been registered before being posted, and the buffers must remain registered until the send completes. 

 Send operations may not be posted to an rdma_cm_id or the corresponding queue pair until it has been connected. 

 The user-defined context associated with the send request will be returned to the user through the work completion wr_id, work request identifier, field.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/3-rdma_connect/">rdma_connect</a>(3), <a HREF="/docs/linux/man/3-rdma_accept/">rdma_accept</a>(3), <a HREF="/docs/linux/man/3-ibv_post_send/">ibv_post_send</a>(3), <a HREF="/docs/linux/man/3-rdma_post_send/">rdma_post_send</a>(3), <a HREF="/docs/linux/man/3-rdma_post_recv/">rdma_post_recv</a>(3) 
