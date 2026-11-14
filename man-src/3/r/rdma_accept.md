---
title: "rdma_accept(3)"
name: "rdma_accept"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_accept/"
---

rdma_accept - Called to accept a connection request.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_accept

    (struct rdma_cm_id *id,

     struct rdma_conn_param *conn_param);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>Connection identifier associated with the request.
<dt>conn_param
<dd>Information needed to establish the connection. See CONNECTION PROPERTIES below for details.</dl>

<h2>Description</h2>

Called from the listening side to accept a connection or datagram service lookup request.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

Unlike the socket accept routine, rdma_accept is not called on a listening rdma_cm_id. Instead, after calling rdma_listen, the user waits for an RDMA_CM_EVENT_CONNECT_REQUEST event to occur. Connection request events give the user a newly created rdma_cm_id, similar to a new socket, but the rdma_cm_id is bound to a specific RDMA device. rdma_accept is called on the new rdma_cm_id.

<h2>Connection Properties</h2>

The following properties are used to configure the communication and specified by the conn_param parameter when accepting a connection or datagram communication request. Users should use the rdma_conn_param values reported in the connection request event to determine appropriate values for these fields when accepting. Users may reference the rdma_conn_param structure in the connection event directly, or can reference their own structure. If the rdma_conn_param structure from an event is referenced, the event must not be acked until after this call returns. 

 If the conn_param parameter is NULL, the values reported in the connection request event are used, adjusted down based on local hardware restrictions.
<dl><dt>private_data
<dd>References a user-controlled data buffer. The contents of the buffer are copied and transparently passed to the remote side as part of the communication request. May be NULL if private_data is not required.
<dt>private_data_len
<dd>Specifies the size of the user-controlled data buffer. Note that the actual amount of data transferred to the remote side is transport dependent and may be larger than that requested.
<dt>responder_resources
<dd>The maximum number of outstanding RDMA read and atomic operations that the local side will accept from the remote side. Applies only to RDMA_PS_TCP. This value must be less than or equal to the local RDMA device attribute max_qp_rd_atom, but preferably greater than or equal to the responder_resources value reported in the connect request event.
<dt>initiator_depth
<dd>The maximum number of outstanding RDMA read and atomic operations that the local side will have to the remote side. Applies only to RDMA_PS_TCP. This value must be less than or equal to the local RDMA device attribute max_qp_init_rd_atom and the initiator_depth value reported in the connect request event.
<dt>flow_control
<dd>Specifies if hardware flow control is available. This value is exchanged with the remote peer and is not used to configure the QP. Applies only to RDMA_PS_TCP.
<dt>retry_count
<dd>This value is ignored.
<dt>rnr_retry_count
<dd>The maximum number of times that a send operation from the remote peer should be retried on a connection after receiving a receiver not ready (RNR) error. RNR errors are generated when a send request arrives before a buffer has been posted to receive the incoming data. Applies only to RDMA_PS_TCP.
<dt>srq
<dd>Specifies if the QP associated with the connection is using a shared receive queue. This field is ignored by the library if a QP has been created on the rdma_cm_id. Applies only to RDMA_PS_TCP.
<dt>qp_num
<dd>Specifies the QP number associated with the connection. This field is ignored by the library if a QP has been created on the rdma_cm_id.</dl>

<h2>Infiniband Specific</h2>

In addition to the connection properties defined above, InfiniBand QPs are configured with minimum RNR NAK timer and local ACK timeout values. The minimum RNR NAK timer value is set to 0, for a delay of 655 ms. The local ACK timeout is calculated based on the packet lifetime and local HCA ACK delay. The packet lifetime is determined by the InfiniBand Subnet Administrator and is part of the route (path record) information obtained by the active side of the connection. The HCA ACK delay is a property of the locally used HCA. 

 The RNR retry count is a 3-bit value. 

 The length of the private data provided by the user is limited to 196 bytes for RDMA_PS_TCP, or 136 bytes for RDMA_PS_UDP.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_listen/">rdma_listen</a>(3), <a HREF="/docs/linux/man/3-rdma_reject/">rdma_reject</a>(3), <a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3) 
