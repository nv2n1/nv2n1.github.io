---
title: "rdma_post_recv(3)"
name: "rdma_post_recv"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_post_recv/"
---

rdma_post_recv - post a work request to receive an incoming message.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_verbs.h&gt;
int rdma_post_recv

    (struct rdma_cm_id *id,

     void *context,

     void *addr,

     size_t length,

     struct ibv_mr *mr);</code></pre>

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
<dd>A registered memory region associated with the posted buffer.</dl>

<h2>Description</h2>

Posts a work request to the receive queue of the queue pair associated with the rdma_cm_id. The posted buffer will be queued to receive an incoming message sent by the remote peer.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

The user is responsible for ensuring that a receive buffer is posted and large enough to contain all sent data before the peer posts the corresponding send message. The message buffer must have been registered before being posted, with the mr parameter referencing the registration. The buffer must remain registered until the receive completes. 

 Messages may be posted to an rdma_cm_id only after a queue pair has been associated with it. A queue pair is bound to an rdma_cm_id after calling rdma_create_ep or rdma_create_qp, if the rdma_cm_id is allocated using rdma_create_id. 

 The user-defined context associated with the receive request will be returned to the user through the work completion wr_id, work request identifier, field.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/3-rdma_create_id/">rdma_create_id</a>(3), <a HREF="/docs/linux/man/3-rdma_create_ep/">rdma_create_ep</a>(3), <a HREF="/docs/linux/man/3-rdma_create_qp/">rdma_create_qp</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_read/">rdma_reg_read</a>(3), <a HREF="/docs/linux/man/3-ibv_reg_mr/">ibv_reg_mr</a>(3), <a HREF="/docs/linux/man/3-ibv_dereg_mr/">ibv_dereg_mr</a>(3), <a HREF="/docs/linux/man/3-rdma_post_recvv/">rdma_post_recvv</a>(3), <a HREF="/docs/linux/man/3-rdma_post_send/">rdma_post_send</a>(3) 
