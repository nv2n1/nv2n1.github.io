---
title: "rdma_connect(3)"
name: "rdma_connect"
section: "3"
letter: "r"
url: "/docs/linux/man/3-rdma_connect/"
---

rdma_connect - Initiate an active connection request.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;
int rdma_connect

    (struct rdma_cm_id *id,

     struct rdma_conn_param *conn_param);</code></pre>

<h2>Arguments</h2>

<dl><dt>id
<dd>RDMA identifier.
<dt>conn_param
<dd>connection parameters. See CONNECTION PROPERTIES below for details.</dl>

<h2>Description</h2>

For an rdma_cm_id of type RDMA_PS_TCP, this call initiates a connection request to a remote destination. For an rdma_cm_id of type RDMA_PS_UDP, it initiates a lookup of the remote QP providing the datagram service.

<h2>Return Value</h2>

Returns 0 on success, or -1 on error. If an error occurs, errno will be set to indicate the failure reason.

<h2>Notes</h2>

Users must have resolved a route to the destination address by having called rdma_resolve_route or rdma_create_ep before calling this routine.

<h2>Connection Properties</h2>

The following properties are used to configure the communication and specified by the conn_param parameter when connecting or establishing datagram communication.
<dl><dt>private_data
<dd>References a user-controlled data buffer. The contents of the buffer are copied and transparently passed to the remote side as part of the communication request. May be NULL if private_data is not required.
<dt>private_data_len
<dd>Specifies the size of the user-controlled data buffer. Note that the actual amount of data transferred to the remote side is transport dependent and may be larger than that requested.
<dt>responder_resources
<dd>The maximum number of outstanding RDMA read and atomic operations that the local side will accept from the remote side. Applies only to RDMA_PS_TCP. This value must be less than or equal to the local RDMA device attribute max_qp_rd_atom and remote RDMA device attribute max_qp_init_rd_atom. The remote endpoint can adjust this value when accepting the connection.
<dt>initiator_depth
<dd>The maximum number of outstanding RDMA read and atomic operations that the local side will have to the remote side. Applies only to RDMA_PS_TCP. This value must be less than or equal to the local RDMA device attribute max_qp_init_rd_atom and remote RDMA device attribute max_qp_rd_atom. The remote endpoint can adjust this value when accepting the connection.
<dt>flow_control
<dd>Specifies if hardware flow control is available. This value is exchanged with the remote peer and is not used to configure the QP. Applies only to RDMA_PS_TCP.
<dt>retry_count
<dd>The maximum number of times that a data transfer operation should be retried on the connection when an error occurs. This setting controls the number of times to retry send, RDMA, and atomic operations when timeouts occur. Applies only to RDMA_PS_TCP.
<dt>rnr_retry_count
<dd>The maximum number of times that a send operation from the remote peer should be retried on a connection after receiving a receiver not ready (RNR) error. RNR errors are generated when a send request arrives before a buffer has been posted to receive the incoming data. Applies only to RDMA_PS_TCP.
<dt>srq
<dd>Specifies if the QP associated with the connection is using a shared receive queue. This field is ignored by the library if a QP has been created on the rdma_cm_id. Applies only to RDMA_PS_TCP.
<dt>qp_num
<dd>Specifies the QP number associated with the connection. This field is ignored by the library if a QP has been created on the rdma_cm_id. Applies only to RDMA_PS_TCP.</dl>

<h2>Infiniband Specific</h2>

In addition to the connection properties defined above, InfiniBand QPs are configured with minimum RNR NAK timer and local ACK timeout values. The minimum RNR NAK timer value is set to 0, for a delay of 655 ms. The local ACK timeout is calculated based on the packet lifetime and local HCA ACK delay. The packet lifetime is determined by the InfiniBand Subnet Administrator and is part of the resolved route (path record) information. The HCA ACK delay is a property of the locally used HCA. 

 Retry count and RNR retry count values are 3-bit values. 

 The length of the private data provided by the user is limited to 56 bytes for RDMA_PS_TCP, or 180 bytes for RDMA_PS_UDP.

<h2>Iwarp Specific</h2>

Connections established over iWarp RDMA devices currently require that the active side of the connection send the first message.

<h2>See Also</h2>

<a HREF="/docs/linux/man/7-rdma_cm/">rdma_cm</a>(7), <a HREF="/docs/linux/man/3-rdma_create_id/">rdma_create_id</a>(3), <a HREF="/docs/linux/man/3-rdma_resolve_route/">rdma_resolve_route</a>(3), <a HREF="/docs/linux/man/3-rdma_disconnect/">rdma_disconnect</a>(3), <a HREF="/docs/linux/man/3-rdma_listen/">rdma_listen</a>(3), <a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3) 
