---
title: "qbipcc-h(3)"
name: "qbipcc-h"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qbipcc-h/"
description: "qbipcc.h –"
---

<p>qbipcc.h &#8211; </p>
<p> Client IPC API.</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;qb/qbconfig.h&gt;

#include &lt;pthread.h&gt;

#include &lt;sys/poll.h&gt;

#include &lt;sys/socket.h&gt;

#include &lt;qb/qbhdb.h&gt;

#include &lt;qb/qbipc_common.h&gt;</code></pre>
<h3>Typedefs</h3>
<p>typedef struct qb_ipcc_connection <code>qb_ipcc_connection_t</code></p>
<h3>Functions</h3>
<p><code>qb_ipcc_connection_t</code> * <code>qb_ipcc_connect</code> (const char *name, size_t max_msg_size)<br />
 <i>Create a connection to an IPC service. </i><br />
 int32_t <code>qb_ipcc_verify_dgram_max_msg_size</code> (size_t max_msg_size)<br />
 <i>Test kernel dgram socket buffers to verify the largest size up to the max_msg_size value a single msg can be. </i><br />
 void <code>qb_ipcc_disconnect</code> (<code>qb_ipcc_connection_t</code> *c)<br />
 <i>Disconnect an IPC connection. </i><br />
 int32_t <code>qb_ipcc_fd_get</code> (<code>qb_ipcc_connection_t</code> *c, int32_t *fd)<br />
 <i>Get the file descriptor to poll. </i><br />
 int32_t <code>qb_ipcc_fc_enable_max_set</code> (<code>qb_ipcc_connection_t</code> *c, uint32_t max)<br />
 <i>Set the maximum allowable flowcontrol value. </i><br />
 ssize_t <code>qb_ipcc_send</code> (<code>qb_ipcc_connection_t</code> *c, const void *msg_ptr, size_t msg_len)<br />
 <i>Send a message. </i><br />
 ssize_t <code>qb_ipcc_sendv</code> (<code>qb_ipcc_connection_t</code> *c, const struct iovec *iov, size_t iov_len)<br />
 <i>Send a message (iovec). </i><br />
 ssize_t <code>qb_ipcc_recv</code> (<code>qb_ipcc_connection_t</code> *c, void *msg_ptr, size_t msg_len, int32_t ms_timeout)<br />
 <i>Receive a response. </i><br />
 ssize_t <code>qb_ipcc_sendv_recv</code> (<code>qb_ipcc_connection_t</code> *c, const struct iovec *iov, uint32_t iov_len, void *msg_ptr, size_t msg_len, int32_t ms_timeout)<br />
 <i>This is a convenience function that simply sends and then recvs. </i><br />
 ssize_t <code>qb_ipcc_event_recv</code> (<code>qb_ipcc_connection_t</code> *c, void *msg_ptr, size_t msg_len, int32_t ms_timeout)<br />
 <i>Receive an event. </i><br />
 void <code>qb_ipcc_context_set</code> (<code>qb_ipcc_connection_t</code> *c, void *context)<br />
 <i>Associate a &#8216;user&#8217; pointer with this connection. </i><br />
 void * <code>qb_ipcc_context_get</code> (<code>qb_ipcc_connection_t</code> *c)<br />
 <i>Get the context (set previously) </i><br />
 int32_t <code>qb_ipcc_is_connected</code> (<code>qb_ipcc_connection_t</code> *c)<br />
 <i>Is the connection connected? </i><br />
 int32_t <code>qb_ipcc_get_buffer_size</code> (<code>qb_ipcc_connection_t</code> *c)<br />
 <i>What is the actual buffer size used after the connection. </i></p>
<h2>Detailed Description</h2>
<p>Client IPC API. </p>
<p> <code>Lifecycle of an IPC connection.</code></p>
<dl>
<dd>An IPC connection is made to the server with <code>qb_ipcc_connect()</code>. This function connects to the server and requests channels be created for communication. To disconnect, the client either exits or executes the function <code>qb_ipcc_disconnect()</code>.</dl>
<p> <code>Synchronous communication</code></p>
<dl>
<dd>The function <code>qb_ipcc_sendv_recv()</code> sends an iovector request and receives a response.</dl>
<p> <code>Asynchronous requests from the client</code></p>
<dl>
<dd>The function <code>qb_ipcc_sendv()</code> sends an iovector request. The function <code>qb_ipcc_send()</code> sends an message buffer request.</dl>
<p> <code>Asynchronous events from the server</code></p>
<dl>
<dd>The <code>qb_ipcc_event_recv()</code> function receives an out-of-band asyncronous message. The asynchronous messages are queued and can provide very high out-of-band performance. To determine when to call <code>qb_ipcc_event_recv()</code> the <code>qb_ipcc_fd_get()</code> call is used to obtain a file descriptor used in the poll() or select() system calls.</dl>
<h2>Typedef Documentation</h2>
<h3>typedef struct qb_ipcc_connection <code>qb_ipcc_connection_t</code></h3>
<h2>Function Documentation</h2>
<h3><code>qb_ipcc_connection_t</code>* qb_ipcc_connect (const char *name, size_tmax_msg_size)</h3>
<p>Create a connection to an IPC service. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>name</i> name of the service.<br />
 <i>max_msg_size</i> biggest msg size.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>NULL (error: see errno) or a connection object.</dl>
<p> <code>Note:</code></p>
<dl>
<dd>It is recommended to do a one time check on the max_msg_size value using qb_ipcc_verify_dgram_max_msg_size <i>BEFORE</i> calling the connect function when IPC_SOCKET is in use. Some distributions while allow large message buffers to be set on the socket, but not actually honor them because of kernel state values. The qb_ipcc_verify_dgram_max_msg_size function both sets the socket buffer size and verifies it by doing a send/recv.</dl>
<h3>void* qb_ipcc_context_get (<code>qb_ipcc_connection_t</code> *c)</h3>
<p>Get the context (set previously) </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the context</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_ipcc_context_set()</code></dl>
<h3>void qb_ipcc_context_set (<code>qb_ipcc_connection_t</code> *c, void *context)</h3>
<p>Associate a &#8216;user&#8217; pointer with this connection. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> the point to associate with this connection.<br />
 <i>c</i> connection instance</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_ipcc_context_get()</code></dl>
<h3>void qb_ipcc_disconnect (<code>qb_ipcc_connection_t</code> *c)</h3>
<p>Disconnect an IPC connection. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance</dl>
<h3>ssize_t qb_ipcc_event_recv (<code>qb_ipcc_connection_t</code> *c, void *msg_ptr, size_tmsg_len, int32_tms_timeout)</h3>
<p>Receive an event. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance<br />
 <i>msg_ptr</i> pointer to a message buffer to receive into<br />
 <i>msg_len</i> the size of the buffer<br />
 <i>ms_timeout</i> time in milli seconds to wait for a message 0 == no wait, negative == block, positive == wait X ms.<br />
 <i>ms_timeout</i> max time to wait for a response</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>size of the message or error (-errno)</dl>
<p> <code>Note:</code></p>
<dl>
<dd>that msg_ptr will include a <code>qb_ipc_response_header</code> at the top of the message.</dl>
<h3>int32_t qb_ipcc_fc_enable_max_set (<code>qb_ipcc_connection_t</code> *c, uint32_tmax)</h3>
<p>Set the maximum allowable flowcontrol value. </p>
<p> <code>Note:</code></p>
<dl>
<dd>the default is 1</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance<br />
 <i>max</i> the max allowable flowcontrol value (1 or 2)</dl>
<h3>int32_t qb_ipcc_fd_get (<code>qb_ipcc_connection_t</code> *c, int32_t *fd)</h3>
<p>Get the file descriptor to poll. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance<br />
 <i>fd</i> (out) file descriptor to poll</dl>
<h3>int32_t qb_ipcc_get_buffer_size (<code>qb_ipcc_connection_t</code> *c)</h3>
<p>What is the actual buffer size used after the connection. </p>
<p> <code>Note:</code></p>
<dl>
<dd>The buffer size is guaranteed to be at least the size of the value given in qb_ipcc_connect, but it is possible the server will enforce a larger size depending on the implementation. If the server side is known to enforce a buffer size, use this function after the client connection is established to retrieve the buffer size in use. It is important for the client side to know the buffer size in use so the client can successfully retrieve large server events.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>connection</i> size in bytes or -error code</dl>
<h3>int32_t qb_ipcc_is_connected (<code>qb_ipcc_connection_t</code> *c)</h3>
<p>Is the connection connected? </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>QB_TRUE</i> when connected<br />
 <i>QB_FALSE</i> when not connected</dl>
<h3>ssize_t qb_ipcc_recv (<code>qb_ipcc_connection_t</code> *c, void *msg_ptr, size_tmsg_len, int32_tms_timeout)</h3>
<p>Receive a response. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance<br />
 <i>msg_ptr</i> pointer to a message buffer to receive into<br />
 <i>msg_len</i> the size of the buffer<br />
 <i>ms_timeout</i> max time to wait for a response</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(size recv&#8217;ed, -errno == error)</dl>
<p> <code>Note:</code></p>
<dl>
<dd>that msg_ptr will include a <code>qb_ipc_response_header</code> at the top of the message.</dl>
<h3>ssize_t qb_ipcc_send (<code>qb_ipcc_connection_t</code> *c, const void *msg_ptr, size_tmsg_len)</h3>
<p>Send a message. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance<br />
 <i>msg_ptr</i> pointer to a message to send<br />
 <i>msg_len</i> the size of the message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(size sent, -errno == error)</dl>
<p> <code>Note:</code></p>
<dl>
<dd>the msg_ptr must include a <code>qb_ipc_request_header</code> at the top of the message. The server will read the size field to determine how much to recv.</dl>
<h3>ssize_t qb_ipcc_sendv (<code>qb_ipcc_connection_t</code> *c, const struct iovec *iov, size_tiov_len)</h3>
<p>Send a message (iovec). </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance<br />
 <i>iov</i> pointer to an iovec struct to send<br />
 <i>iov_len</i> the number of iovecs used</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>(size sent, -errno == error)</dl>
<p> <code>Note:</code></p>
<dl>
<dd>the iov[0] must be a <code>qb_ipc_request_header</code>. The server will read the size field to determine how much to recv.</dl>
<h3>ssize_t qb_ipcc_sendv_recv (<code>qb_ipcc_connection_t</code> *c, const struct iovec *iov, uint32_tiov_len, void *msg_ptr, size_tmsg_len, int32_tms_timeout)</h3>
<p>This is a convenience function that simply sends and then recvs. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance<br />
 <i>iov</i> pointer to an iovec struct to send<br />
 <i>iov_len</i> the number of iovecs used<br />
 <i>msg_ptr</i> pointer to a message buffer to receive into<br />
 <i>msg_len</i> the size of the buffer<br />
 <i>ms_timeout</i> max time to wait for a response</dl>
<p> <code>Note:</code></p>
<dl>
<dd>the iov[0] must include a <code>qb_ipc_request_header</code> at the top of the message. The server will read the size field to determine how much to recv. </p>
<p> that msg_ptr will include a <code>qb_ipc_response_header</code> at the top of the message.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_ipcc_sendv()</code> <code>qb_ipcc_recv()</code></dl>
<h3>int32_t qb_ipcc_verify_dgram_max_msg_size (size_tmax_msg_size)</h3>
<p>Test kernel dgram socket buffers to verify the largest size up to the max_msg_size value a single msg can be. Rounds down to the nearest 1k. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>max_msg_size</i> biggest msg size.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>-1 if max size can not be detected, positive value representing the largest single msg up to max_msg_size that can successfully be sent over a unix dgram socket.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libqb from the source code.</p>
