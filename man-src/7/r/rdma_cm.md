---
title: "rdma_cm(7)"
name: "rdma_cm"
section: "7"
letter: "r"
url: "/docs/linux/man/7-rdma_cm/"
---

rdma_cm - RDMA communication manager.

<h2>Synopsis</h2>

<pre><code>#include &lt;rdma/rdma_cma.h&gt;</code></pre>

<h2>Description</h2>

Used to establish communication over RDMA transports.

<h2>Notes</h2>

The RDMA CM is a communication manager used to setup reliable, connected and unreliable datagram data transfers. It provides an RDMA transport neutral interface for establishing connections. The API concepts are based on sockets, but adapted for queue pair (QP) based semantics: communication must be over a specific RDMA device, and data transfers are message based. 

 The RDMA CM can control both the QP and communication management (connection setup / teardown) portions of an RDMA API, or only the communication management piece. It works in conjunction with the verbs API defined by the libibverbs library. The libibverbs library provides the underlying interfaces needed to send and receive data. 

 The RDMA CM can operate asynchronously or synchronously. The mode of operation is controlled by the user through the use of the rdma_cm event channel parameter in specific calls. If an event channel is provided, an rdma_cm identifier will report its event data (results of connecting, for example), on that channel. If a channel is not provided, then all rdma_cm operations for the selected rdma_cm identifier will block until they complete.

<h2>Rdma Verbs</h2>

The rdma_cm supports the full range of verbs available through the libibverbs library and interfaces. However, it also provides wrapper functions for some of the more commonly used verbs funcationality. The full set of abstracted verb calls are: 

 rdma_reg_msgs - register an array of buffers for sending and receiving 

 rdma_reg_read - registers a buffer for RDMA read operations 

 rdma_reg_write - registers a buffer for RDMA write operations 

 rdma_dereg_mr - deregisters a memory region 

 rdma_post_recv - post a buffer to receive a message 

 rdma_post_send - post a buffer to send a message 

 rdma_post_read - post an RDMA to read data into a buffer 

 rdma_post_write - post an RDMA to send data from a buffer 

 rdma_post_recvv - post a vector of buffers to receive a message 

 rdma_post_sendv - post a vector of buffers to send a message 

 rdma_post_readv - post a vector of buffers to receive an RDMA read 

 rdma_post_writev - post a vector of buffers to send an RDMA write 

 rdma_post_ud_send - post a buffer to send a message on a UD QP 

 rdma_get_send_comp - get completion status for a send or RDMA operation 

 rdma_get_recv_comp - get information about a completed receive

<h2>Client Operation</h2>

This section provides a general overview of the basic operation for the active, or client, side of communication. This flow assume asynchronous operation with low level call details shown. For synchronous operation, calls to rdma_create_event_channel, rdma_get_cm_event, rdma_ack_cm_event, and rdma_destroy_event_channel would be eliminated. Abstracted calls, such as rdma_create_ep encapsulate serveral of these calls under a single API. Users may also refer to the example applications for code samples. A general connection flow would be:
<dl><dt>rdma_getaddrinfo
<dd>retrieve address information of the destination
<dt>rdma_create_event_channel
<dd>create channel to receive events
<dt>rdma_create_id
<dd>allocate an rdma_cm_id, this is conceptually similar to a socket
<dt>rdma_resolve_addr
<dd>obtain a local RDMA device to reach the remote address
<dt>rdma_get_cm_event
<dd>wait for RDMA_CM_EVENT_ADDR_RESOLVED event
<dt>rdma_ack_cm_event
<dd>ack event
<dt>rdma_create_qp
<dd>allocate a QP for the communication
<dt>rdma_resolve_route
<dd>determine the route to the remote address
<dt>rdma_get_cm_event
<dd>wait for RDMA_CM_EVENT_ROUTE_RESOLVED event
<dt>rdma_ack_cm_event
<dd>ack event
<dt>rdma_connect
<dd>connect to the remote server
<dt>rdma_get_cm_event
<dd>wait for RDMA_CM_EVENT_ESTABLISHED event
<dt>rdma_ack_cm_event
<dd>ack event</dl>
 

 Perform data transfers over connection
<dl><dt>rdma_disconnect
<dd>tear-down connection
<dt>rdma_get_cm_event
<dd>wait for RDMA_CM_EVENT_DISCONNECTED event
<dt>rdma_ack_cm_event
<dd>ack event
<dt>rdma_destroy_qp
<dd>destroy the QP
<dt>rdma_destroy_id
<dd>release the rdma_cm_id
<dt>rdma_destroy_event_channel
<dd>release the event channel</dl>
 

 An almost identical process is used to setup unreliable datagram (UD) communication between nodes. No actual connection is formed between QPs however, so disconnection is not needed. 

 Although this example shows the client initiating the disconnect, either side of a connection may initiate the disconnect.

<h2>Server Operation</h2>

This section provides a general overview of the basic operation for the passive, or server, side of communication. A general connection flow would be:
<dl><dt>rdma_create_event_channel
<dd>create channel to receive events
<dt>rdma_create_id
<dd>allocate an rdma_cm_id, this is conceptually similar to a socket
<dt>rdma_bind_addr
<dd>set the local port number to listen on
<dt>rdma_listen
<dd>begin listening for connection requests
<dt>rdma_get_cm_event
<dd>wait for RDMA_CM_EVENT_CONNECT_REQUEST event with a new rdma_cm_id
<dt>rdma_create_qp
<dd>allocate a QP for the communication on the new rdma_cm_id
<dt>rdma_accept
<dd>accept the connection request
<dt>rdma_ack_cm_event
<dd>ack event
<dt>rdma_get_cm_event
<dd>wait for RDMA_CM_EVENT_ESTABLISHED event
<dt>rdma_ack_cm_event
<dd>ack event</dl>
 

 Perform data transfers over connection
<dl><dt>rdma_get_cm_event
<dd>wait for RDMA_CM_EVENT_DISCONNECTED event
<dt>rdma_ack_cm_event
<dd>ack event
<dt>rdma_disconnect
<dd>tear-down connection
<dt>rdma_destroy_qp
<dd>destroy the QP
<dt>rdma_destroy_id
<dd>release the connected rdma_cm_id
<dt>rdma_destroy_id
<dd>release the listening rdma_cm_id
<dt>rdma_destroy_event_channel
<dd>release the event channel</dl>

<h2>Return Codes</h2>

<dl><dt>= 0
<dd>success
<dt>= -1
<dd>error - see errno for more details</dl>
 

 Most librdmacm functions return 0 to indicate success, and a -1 return value to indicate failure. If a function operates asynchronously, a return value of 0 means that the operation was successfully started. The operation could still complete in error; users should check the status of the related event. If the return value is -1, then errno will contain additional information regarding the reason for the failure. 

 Prior versions of the library would return -errno and not set errno for some cases related to ENOMEM, ENODEV, ENODATA, EINVAL, and EADDRNOTAVAIL codes. Applications that want to check these codes and have compatability with prior library versions must manually set errno to the negative of the return code if it is &lt; -1.

<h2>See Also</h2>

<a HREF="/docs/linux/man/3-rdma_accept/">rdma_accept</a>(3), <a HREF="/docs/linux/man/3-rdma_ack_cm_event/">rdma_ack_cm_event</a>(3), <a HREF="/docs/linux/man/3-rdma_bind_addr/">rdma_bind_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_connect/">rdma_connect</a>(3), <a HREF="/docs/linux/man/3-rdma_create_ep/">rdma_create_ep</a>(3), <a HREF="/docs/linux/man/3-rdma_create_event_channel/">rdma_create_event_channel</a>(3), <a HREF="/docs/linux/man/3-rdma_create_id/">rdma_create_id</a>(3), <a HREF="/docs/linux/man/3-rdma_create_qp/">rdma_create_qp</a>(3), <a HREF="/docs/linux/man/3-rdma_dereg_mr/">rdma_dereg_mr</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_ep/">rdma_destroy_ep</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_event_channel/">rdma_destroy_event_channel</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_id/">rdma_destroy_id</a>(3), <a HREF="/docs/linux/man/3-rdma_destroy_qp/">rdma_destroy_qp</a>(3), <a HREF="/docs/linux/man/3-rdma_disconnect/">rdma_disconnect</a>(3), <a HREF="/docs/linux/man/3-rdma_event_str/">rdma_event_str</a>(3), <a HREF="/docs/linux/man/3-rdma_free_devices/">rdma_free_devices</a>(3), <a HREF="/docs/linux/man/3-rdma_getaddrinfo/">rdma_getaddrinfo</a>(3), <a HREF="/docs/linux/man/3-rdma_get_cm_event/">rdma_get_cm_event</a>(3), <a HREF="/docs/linux/man/3-rdma_get_devices/">rdma_get_devices</a>(3), <a HREF="/docs/linux/man/3-rdma_get_dst_port/">rdma_get_dst_port</a>(3), <a HREF="/docs/linux/man/3-rdma_get_local_addr/">rdma_get_local_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_get_peer_addr/">rdma_get_peer_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_get_recv_comp/">rdma_get_recv_comp</a>(3), <a HREF="/docs/linux/man/3-rdma_get_request/">rdma_get_request</a>(3), <a HREF="/docs/linux/man/3-rdma_get_send_comp/">rdma_get_send_comp</a>(3), <a HREF="/docs/linux/man/3-rdma_get_src_port/">rdma_get_src_port</a>(3), <a HREF="/docs/linux/man/3-rdma_join_multicast/">rdma_join_multicast</a>(3), <a HREF="/docs/linux/man/3-rdma_leave_multicast/">rdma_leave_multicast</a>(3), <a HREF="/docs/linux/man/3-rdma_listen/">rdma_listen</a>(3), <a HREF="/docs/linux/man/3-rdma_migrate_id/">rdma_migrate_id</a>(3), <a HREF="/docs/linux/man/3-rdma_notify/">rdma_notify</a>(3), <a HREF="/docs/linux/man/3-rdma_post_read/">rdma_post_read</a>(3) <a HREF="/docs/linux/man/3-rdma_post_readv/">rdma_post_readv</a>(3), <a HREF="/docs/linux/man/3-rdma_post_recv/">rdma_post_recv</a>(3), <a HREF="/docs/linux/man/3-rdma_post_recvv/">rdma_post_recvv</a>(3), <a HREF="/docs/linux/man/3-rdma_post_send/">rdma_post_send</a>(3), <a HREF="/docs/linux/man/3-rdma_post_sendv/">rdma_post_sendv</a>(3), <a HREF="/docs/linux/man/3-rdma_post_ud_send/">rdma_post_ud_send</a>(3), <a HREF="/docs/linux/man/3-rdma_post_write/">rdma_post_write</a>(3), <a HREF="/docs/linux/man/3-rdma_post_writev/">rdma_post_writev</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_msgs/">rdma_reg_msgs</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_read/">rdma_reg_read</a>(3), <a HREF="/docs/linux/man/3-rdma_reg_write/">rdma_reg_write</a>(3), <a HREF="/docs/linux/man/3-rdma_reject/">rdma_reject</a>(3), <a HREF="/docs/linux/man/3-rdma_resolve_addr/">rdma_resolve_addr</a>(3), <a HREF="/docs/linux/man/3-rdma_resolve_route/">rdma_resolve_route</a>(3), <a HREF="/docs/linux/man/3-rdma_set_option/">rdma_set_option</a>(3) <a HREF="/docs/linux/man/1-mckey/">mckey</a>(1), <a HREF="/docs/linux/man/1-rdma_client/">rdma_client</a>(1), <a HREF="/docs/linux/man/1-rdma_server/">rdma_server</a>(1), <a HREF="/docs/linux/man/1-rping/">rping</a>(1), <a HREF="/docs/linux/man/1-ucmatose/">ucmatose</a>(1), <a HREF="/docs/linux/man/1-udaddy/">udaddy</a>(1) 
