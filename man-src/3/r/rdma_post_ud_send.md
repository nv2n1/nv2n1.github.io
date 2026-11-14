---
title: "rdma_post_ud_send(3)"
name: "rdma_post_ud_send"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_post_ud_send/"
---

rdma_post_ud_send - post a work request to send a datagram.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_verbs.h&gt;
int rdma_post_ud_send

    (struct rdma_cm_id *id,

     void *context,

     void *addr,

     size_t length,

     struct ibv_mr *mr,

     int flags,

     struct ibv_ah *ah,

     uint32_t remote_qpn);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>A reference to a communication identifier where the message buffer will be posted.
<dt>context
<dd>User-defined context associated with the request.
<dt>addr
<dd>The address of the memory buffer to post.
<dt>length
<dd>The length of the memory buffer.
<dt>mr
<dd>Optional registered memory region associated with the posted buffer.
<dt>flags
<dd>Optional flags used to control the send operation.
<dt>ah
<dd>An address handle describing the address of the remote node.
<dt>remote_qpn
<dd>The number of the destination queue pair.</dl>

<h2>Description</h2>

Posts a work request to the send queue of the queue pair associated with the rdma_cm_id. The contents of the posted buffer will be sent to the specified destination queue pair.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

The user is responsible for ensuring that the destination queue pair has queued a receive request before issuing the send operations. For a list of supported flags, see ibv_post_send. Unless the send request is using inline data, the message buffer must have been registered before being posted, with the mr parameter referencing the registration. The buffer must remain registered until the send completes. 

 The user-defined context associated with the send request will be returned to the user through the work completion wr_id, work request identifier, field.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/3-rdma_connect/">rdma_connect</a>(3), <a HREF="/docs/linux/man/3-rdma_accept/">rdma_accept</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_msgs/">rdma_reg_msgs</a>(3) <a HREF="/docs/linux/man/3-ibv_post_send/">ibv_post_send</a>(3), <a HREF="/docs/linux/man/3-rdma_post_recv/">rdma_post_recv</a>(3) 
