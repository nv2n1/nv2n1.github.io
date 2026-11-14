---
title: "qbipcs-h(3)"
name: "qbipcs-h"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qbipcs-h/"
description: "qbipcs.h –"
---

<p>qbipcs.h &#8211; </p>
<p> Server IPC API.</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;stdlib.h&gt;

#include &lt;sys/uio.h&gt;

#include &lt;qb/qbipc_common.h&gt;

#include &lt;qb/qbhdb.h&gt;

#include &lt;qb/qbloop.h&gt;</code></pre>
<h3>Data Structures</h3>
<pre><code>struct qb_ipcs_stats



struct qb_ipcs_connection_stats



struct qb_ipcs_connection_stats_2



struct qb_ipcs_poll_handlers



struct qb_ipcs_service_handlers



Typedefs</code></pre>
<p> typedef struct qb_ipcs_connection <code>qb_ipcs_connection_t</code> </p>
<p> typedef struct qb_ipcs_service <code>qb_ipcs_service_t</code> </p>
<p> typedef int32_t(* <code>qb_ipcs_dispatch_fn_t</code> )(int32_t fd, int32_t revents, void *data) </p>
<p> typedef int32_t(* <code>qb_ipcs_dispatch_add_fn</code> )(enum <code>qb_loop_priority</code> p, int32_t fd, int32_t events, void *data, <code>qb_ipcs_dispatch_fn_t</code> fn) </p>
<p> typedef int32_t(* <code>qb_ipcs_dispatch_mod_fn</code> )(enum <code>qb_loop_priority</code> p, int32_t fd, int32_t events, void *data, <code>qb_ipcs_dispatch_fn_t</code> fn) </p>
<p> typedef int32_t(* <code>qb_ipcs_dispatch_del_fn</code> )(int32_t fd) </p>
<p> typedef int32_t(* <code>qb_ipcs_job_add_fn</code> )(enum <code>qb_loop_priority</code> p, void *data, <code>qb_loop_job_dispatch_fn</code> dispatch_fn) </p>
<p> typedef int32_t(* <code>qb_ipcs_connection_accept_fn</code> )(<code>qb_ipcs_connection_t</code> *c, uid_t uid, gid_t gid)<br />
 <i>This callback is to check whether you want to accept a new connection. </i><br />
 typedef void(* <code>qb_ipcs_connection_created_fn</code> )(<code>qb_ipcs_connection_t</code> *c)<br />
 <i>This is called after a new connection has been created. </i><br />
 typedef int32_t(* <code>qb_ipcs_connection_closed_fn</code> )(<code>qb_ipcs_connection_t</code> *c)<br />
 <i>This is called after a connection has been disconnected. </i><br />
 typedef void(* <code>qb_ipcs_connection_destroyed_fn</code> )(<code>qb_ipcs_connection_t</code> *c)<br />
 <i>This is called just before a connection is freed. </i><br />
 typedef int32_t(* <code>qb_ipcs_msg_process_fn</code> )(<code>qb_ipcs_connection_t</code> *c, void *data, size_t size)<br />
 <i>This is the message processing calback. </i></p>
<h3>Enumerations</h3>
<p>enum <code>qb_ipcs_rate_limit</code> { <code>QB_IPCS_RATE_FAST</code>, <code>QB_IPCS_RATE_NORMAL</code>, <code>QB_IPCS_RATE_SLOW</code>, <code>QB_IPCS_RATE_OFF</code>, <code>QB_IPCS_RATE_OFF_2</code> }</p>
<h3>Functions</h3>
<p><code>qb_ipcs_service_t</code> * <code>qb_ipcs_create</code> (const char *name, int32_t service_id, enum <code>qb_ipc_type</code> type, struct <code>qb_ipcs_service_handlers</code> *handlers)<br />
 <i>Create a new IPC server. </i><br />
 void <code>qb_ipcs_ref</code> (<code>qb_ipcs_service_t</code> *s)<br />
 <i>Increase the reference counter on the service object. </i><br />
 void <code>qb_ipcs_unref</code> (<code>qb_ipcs_service_t</code> *s)<br />
 <i>Decrease the reference counter on the service object. </i><br />
 void <code>qb_ipcs_poll_handlers_set</code> (<code>qb_ipcs_service_t</code> *s, struct <code>qb_ipcs_poll_handlers</code> *handlers)<br />
 <i>Set your poll callbacks. </i><br />
 void <code>qb_ipcs_service_context_set</code> (<code>qb_ipcs_service_t</code> *s, void *context)<br />
 <i>Associate a &#8216;user&#8217; pointer with this service. </i><br />
 void * <code>qb_ipcs_service_context_get</code> (<code>qb_ipcs_service_t</code> *s)<br />
 <i>Get the context (set previously) </i><br />
 int32_t <code>qb_ipcs_run</code> (<code>qb_ipcs_service_t</code> *s)<br />
 <i>run the new IPC server. </i><br />
 void <code>qb_ipcs_destroy</code> (<code>qb_ipcs_service_t</code> *s)<br />
 <i>Destroy the IPC server. </i><br />
 void <code>qb_ipcs_request_rate_limit</code> (<code>qb_ipcs_service_t</code> *s, enum <code>qb_ipcs_rate_limit</code> rl)<br />
 <i>Limit the incoming request rate. </i><br />
 ssize_t <code>qb_ipcs_response_send</code> (<code>qb_ipcs_connection_t</code> *c, const void *data, size_t size)<br />
 <i>Send a response to a incoming request. </i><br />
 ssize_t <code>qb_ipcs_response_sendv</code> (<code>qb_ipcs_connection_t</code> *c, const struct iovec *iov, size_t iov_len)<br />
 <i>Send a response to a incoming request. </i><br />
 ssize_t <code>qb_ipcs_event_send</code> (<code>qb_ipcs_connection_t</code> *c, const void *data, size_t size)<br />
 <i>Send an asyncronous event message to the client. </i><br />
 ssize_t <code>qb_ipcs_event_sendv</code> (<code>qb_ipcs_connection_t</code> *c, const struct iovec *iov, size_t iov_len)<br />
 <i>Send an asyncronous event message to the client. </i><br />
 void <code>qb_ipcs_connection_ref</code> (<code>qb_ipcs_connection_t</code> *c)<br />
 <i>Increment the connection&#8217;s reference counter. </i><br />
 void <code>qb_ipcs_connection_unref</code> (<code>qb_ipcs_connection_t</code> *c)<br />
 <i>Decrement the connection&#8217;s reference counter. </i><br />
 void <code>qb_ipcs_disconnect</code> (<code>qb_ipcs_connection_t</code> *c)<br />
 <i>Disconnect from this client. </i><br />
 int32_t <code>qb_ipcs_service_id_get</code> (<code>qb_ipcs_connection_t</code> *c)<br />
 <i>Get the service id related to this connection&#8217;s service. </i><br />
 void <code>qb_ipcs_context_set</code> (<code>qb_ipcs_connection_t</code> *c, void *context)<br />
 <i>Associate a &#8216;user&#8217; pointer with this connection. </i><br />
 void * <code>qb_ipcs_context_get</code> (<code>qb_ipcs_connection_t</code> *c)<br />
 <i>Get the context (set previously) </i><br />
 void * <code>qb_ipcs_connection_service_context_get</code> (<code>qb_ipcs_connection_t</code> *c)<br />
 <i>Get the context previously set on the service backing this connection. </i><br />
 int32_t <code>qb_ipcs_connection_stats_get</code> (<code>qb_ipcs_connection_t</code> *c, struct <code>qb_ipcs_connection_stats</code> *stats, int32_t clear_after_read)<br />
 <i>Get the connection statistics. </i><br />
 struct <code>qb_ipcs_connection_stats_2</code> * <code>qb_ipcs_connection_stats_get_2</code> (<code>qb_ipcs_connection_t</code> *c, int32_t clear_after_read)<br />
 <i>Get (and allocate) the connection statistics. </i><br />
 int32_t <code>qb_ipcs_stats_get</code> (<code>qb_ipcs_service_t</code> *pt, struct <code>qb_ipcs_stats</code> *stats, int32_t clear_after_read)<br />
 <i>Get the service statistics. </i><br />
 <code>qb_ipcs_connection_t</code> * <code>qb_ipcs_connection_first_get</code> (<code>qb_ipcs_service_t</code> *pt)<br />
 <i>Get the first connection. </i><br />
 <code>qb_ipcs_connection_t</code> * <code>qb_ipcs_connection_next_get</code> (<code>qb_ipcs_service_t</code> *pt, <code>qb_ipcs_connection_t</code> *current)<br />
 <i>Get the next connection. </i><br />
 void <code>qb_ipcs_connection_auth_set</code> (<code>qb_ipcs_connection_t</code> *conn, uid_t uid, gid_t gid, mode_t mode)<br />
 <i>Set the permissions on and shared memory files so that both processes can read and write to them. </i><br />
 int32_t <code>qb_ipcs_connection_get_buffer_size</code> (<code>qb_ipcs_connection_t</code> *conn)<br />
 <i>Retrieve the connection ipc buffer size. </i><br />
 void <code>qb_ipcs_enforce_buffer_size</code> (<code>qb_ipcs_service_t</code> *s, uint32_t max_buf_size)<br />
 <i>Enforce the max buffer size clients must use from the server side. </i></p>
<h2>Detailed Description</h2>
<p>Server IPC API.</p>
<h2>Typedef Documentation</h2>
<h3>typedef int32_t(* qb_ipcs_connection_accept_fn)(<code>qb_ipcs_connection_t</code> *c, uid_t uid, gid_t gid)</h3>
<p>This callback is to check whether you want to accept a new connection. The type of checks you should do are authentication, service availabilty or process resource constraints. </p>
<p> <code>Returns:</code></p>
<dl>
<dd>0 to accept or -errno to indicate a failure (sent back to the client)</dl>
<p> <code>Note:</code></p>
<dl>
<dd>If connection state data is allocated as a result of this callback being invoked, that data must be freed in the destroy callback. Just because the accept callback returns 0, that does not guarantee the create and closed callback functions will follow. </p>
<p> you can call <code>qb_ipcs_connection_auth_set()</code> within this function.</dl>
<h3>typedef int32_t(* qb_ipcs_connection_closed_fn)(<code>qb_ipcs_connection_t</code> *c)</h3>
<p>This is called after a connection has been disconnected. </p>
<p> <code>Note:</code></p>
<dl>
<dd>This callback will only be invoked if the connection is successfully created. </p>
<p> if you return anything but 0 this function will be repeativily called (until 0 is returned).</dl>
<h3>typedef void(* qb_ipcs_connection_created_fn)(<code>qb_ipcs_connection_t</code> *c)</h3>
<p>This is called after a new connection has been created. </p>
<p> <code>Note:</code></p>
<dl>
<dd>A client connection is not considered connected until this callback is invoked.</dl>
<h3>typedef void(* qb_ipcs_connection_destroyed_fn)(<code>qb_ipcs_connection_t</code> *c)</h3>
<p>This is called just before a connection is freed.</p>
<h3>typedef struct qb_ipcs_connection <code>qb_ipcs_connection_t</code></h3>
<h3>typedef int32_t(* qb_ipcs_dispatch_add_fn)(enum <code>qb_loop_priority</code> p, int32_t fd, int32_t events, void *data, <code>qb_ipcs_dispatch_fn_t</code> fn)</h3>
<h3>typedef int32_t(* qb_ipcs_dispatch_del_fn)(int32_t fd)</h3>
<h3>typedef int32_t(* qb_ipcs_dispatch_fn_t)(int32_t fd, int32_t revents, void *data)</h3>
<h3>typedef int32_t(* qb_ipcs_dispatch_mod_fn)(enum <code>qb_loop_priority</code> p, int32_t fd, int32_t events, void *data, <code>qb_ipcs_dispatch_fn_t</code> fn)</h3>
<h3>typedef int32_t(* qb_ipcs_job_add_fn)(enum <code>qb_loop_priority</code> p, void *data, <code>qb_loop_job_dispatch_fn</code> dispatch_fn)</h3>
<h3>typedef int32_t(* qb_ipcs_msg_process_fn)(<code>qb_ipcs_connection_t</code> *c, void *data, size_t size)</h3>
<p>This is the message processing calback. It is called with the message data.</p>
<h3>typedef struct qb_ipcs_service <code>qb_ipcs_service_t</code></h3>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>qb_ipcs_rate_limit</code></h3>
<p><code>Enumerator</code></p>
<dl>
<dt><i>QB_IPCS_RATE_FAST </i></p>
<dd>
<dt><i>QB_IPCS_RATE_NORMAL </i></p>
<dd>
<dt><i>QB_IPCS_RATE_SLOW </i></p>
<dd>
<dt><i>QB_IPCS_RATE_OFF </i></p>
<dd>
<dt><i>QB_IPCS_RATE_OFF_2 </i></p>
<dd></dl>
<h2>Function Documentation</h2>
<h3>void qb_ipcs_connection_auth_set (<code>qb_ipcs_connection_t</code> *conn, uid_tuid, gid_tgid, mode_tmode)</h3>
<p>Set the permissions on and shared memory files so that both processes can read and write to them. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>conn</i> connection instance<br />
 <i>uid</i> the user id to set.<br />
 <i>gid</i> the group id to set.<br />
 <i>mode</i> the mode to set.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd>chmod() chown()</dl>
<p> <code>Note:</code></p>
<dl>
<dd>this must be called within the <code>qb_ipcs_connection_accept_fn()</code> callback.</dl>
<h3><code>qb_ipcs_connection_t</code>* qb_ipcs_connection_first_get (<code>qb_ipcs_service_t</code> *pt)</h3>
<p>Get the first connection. </p>
<p> <code>Note:</code></p>
<dl>
<dd>call <code>qb_ipcs_connection_unref()</code> after using the connection.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>pt</i> service instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>first connection</dl>
<h3>int32_t qb_ipcs_connection_get_buffer_size (<code>qb_ipcs_connection_t</code> *conn)</h3>
<p>Retrieve the connection ipc buffer size. This reflects the largest size msg that can be sent or received. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>conn</i> connection instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>msg size in bytes, negative value on error.</dl>
<h3><code>qb_ipcs_connection_t</code>* qb_ipcs_connection_next_get (<code>qb_ipcs_service_t</code> *pt, <code>qb_ipcs_connection_t</code> *current)</h3>
<p>Get the next connection. </p>
<p> <code>Note:</code></p>
<dl>
<dd>call <code>qb_ipcs_connection_unref()</code> after using the connection.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>pt</i> service instance<br />
 <i>current</i> current connection</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>next connection</dl>
<h3>void qb_ipcs_connection_ref (<code>qb_ipcs_connection_t</code> *c)</h3>
<p>Increment the connection&#8217;s reference counter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance</dl>
<h3>void* qb_ipcs_connection_service_context_get (<code>qb_ipcs_connection_t</code> *c)</h3>
<p>Get the context previously set on the service backing this connection. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the context</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_ipcs_service_context_set</code></dl>
<h3>int32_t qb_ipcs_connection_stats_get (<code>qb_ipcs_connection_t</code> *c, struct <code>qb_ipcs_connection_stats</code> *stats, int32_tclear_after_read)</h3>
<p>Get the connection statistics. </p>
<p> <code>Deprecated</code></p>
<dl>
<dd>from v0.13.0 onwards, use qb_ipcs_connection_stats_get_2</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>stats</i> (out) the statistics structure<br />
 <i>clear_after_read</i> clear stats after copying them into stats<br />
 <i>c</i> connection instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 == ok; -errno to indicate a failure</dl>
<h3>struct <code>qb_ipcs_connection_stats_2</code>* qb_ipcs_connection_stats_get_2 (<code>qb_ipcs_connection_t</code> *c, int32_tclear_after_read)</h3>
<p>Get (and allocate) the connection statistics. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>clear_after_read</i> clear stats after copying them into stats<br />
 <i>c</i> connection instance</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>NULL</i> if no memory or invalid connection<br />
 <i>allocated</i> statistics structure (user must free it).</dl>
<h3>void qb_ipcs_connection_unref (<code>qb_ipcs_connection_t</code> *c)</h3>
<p>Decrement the connection&#8217;s reference counter. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance</dl>
<h3>void* qb_ipcs_context_get (<code>qb_ipcs_connection_t</code> *c)</h3>
<p>Get the context (set previously) </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the context</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_ipcs_context_set()</code></dl>
<h3>void qb_ipcs_context_set (<code>qb_ipcs_connection_t</code> *c, void *context)</h3>
<p>Associate a &#8216;user&#8217; pointer with this connection. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>context</i> the point to associate with this connection.<br />
 <i>c</i> connection instance</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_ipcs_context_get()</code></dl>
<h3><code>qb_ipcs_service_t</code>* qb_ipcs_create (const char *name, int32_tservice_id, enum <code>qb_ipc_type</code>type, struct <code>qb_ipcs_service_handlers</code> *handlers)</h3>
<p>Create a new IPC server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>name</i> for clients to connect to.<br />
 <i>service_id</i> an integer to associate with the service<br />
 <i>type</i> transport type.<br />
 <i>handlers</i> callbacks.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the new service instance.</dl>
<h3>void qb_ipcs_destroy (<code>qb_ipcs_service_t</code> *s)</h3>
<p>Destroy the IPC server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> service instance to destroy</dl>
<h3>void qb_ipcs_disconnect (<code>qb_ipcs_connection_t</code> *c)</h3>
<p>Disconnect from this client. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance</dl>
<h3>void qb_ipcs_enforce_buffer_size (<code>qb_ipcs_service_t</code> *s, uint32_tmax_buf_size)</h3>
<p>Enforce the max buffer size clients must use from the server side. </p>
<p> <code>Note:</code></p>
<dl>
<dd>Setting this will force client connections to use at least max_buf_size bytes as their buffer size. If this value is not set on the server, the clients enforce their own buffer sizes.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> ipc server instance<br />
 <i>max_buf_size</i> represented in bytes</dl>
<h3>ssize_t qb_ipcs_event_send (<code>qb_ipcs_connection_t</code> *c, const void *data, size_tsize)</h3>
<p>Send an asyncronous event message to the client. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance<br />
 <i>data</i> the message to send<br />
 <i>size</i> the size of the message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>size sent or -errno for errors</dl>
<p> <code>Note:</code></p>
<dl>
<dd>the data must include a <code>qb_ipc_response_header</code> at the top of the message. The client will read the size field to determine how much to recv. </p>
<p> When send returns -EMSGSIZE, this means the msg is too large and will never succeed. To determine the max msg size a client can be sent, use <code>qb_ipcs_connection_get_buffer_size()</code></dl>
<h3>ssize_t qb_ipcs_event_sendv (<code>qb_ipcs_connection_t</code> *c, const struct iovec *iov, size_tiov_len)</h3>
<p>Send an asyncronous event message to the client. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance<br />
 <i>iov</i> the iovec struct that points to the message to send<br />
 <i>iov_len</i> the number of iovecs.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>size sent or -errno for errors</dl>
<p> <code>Note:</code></p>
<dl>
<dd>the iov[0] must be a <code>qb_ipc_response_header</code>. The client will read the size field to determine how much to recv. </p>
<p> When send returns -EMSGSIZE, this means the msg is too large and will never succeed. To determine the max msg size a client can be sent, use <code>qb_ipcs_connection_get_buffer_size()</code></dl>
<h3>void qb_ipcs_poll_handlers_set (<code>qb_ipcs_service_t</code> *s, struct <code>qb_ipcs_poll_handlers</code> *handlers)</h3>
<p>Set your poll callbacks. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> service instance<br />
 <i>handlers</i> the handlers that you want ipcs to use.</dl>
<h3>void qb_ipcs_ref (<code>qb_ipcs_service_t</code> *s)</h3>
<p>Increase the reference counter on the service object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> service instance</dl>
<h3>void qb_ipcs_request_rate_limit (<code>qb_ipcs_service_t</code> *s, enum <code>qb_ipcs_rate_limit</code>rl)</h3>
<p>Limit the incoming request rate. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> service instance<br />
 <i>rl</i> the new rate</dl>
<h3>ssize_t qb_ipcs_response_send (<code>qb_ipcs_connection_t</code> *c, const void *data, size_tsize)</h3>
<p>Send a response to a incoming request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance<br />
 <i>data</i> the message to send<br />
 <i>size</i> the size of the message</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>size sent or -errno for errors</dl>
<p> <code>Note:</code></p>
<dl>
<dd>the data must include a <code>qb_ipc_response_header</code> at the top of the message. The client will read the size field to determine how much to recv.</dl>
<h3>ssize_t qb_ipcs_response_sendv (<code>qb_ipcs_connection_t</code> *c, const struct iovec *iov, size_tiov_len)</h3>
<p>Send a response to a incoming request. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>c</i> connection instance<br />
 <i>iov</i> the iovec struct that points to the message to send<br />
 <i>iov_len</i> the number of iovecs.</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>size sent or -errno for errors</dl>
<p> <code>Note:</code></p>
<dl>
<dd>the iov[0] must be a <code>qb_ipc_response_header</code>. The client will read the size field to determine how much to recv. </p>
<p> When send returns -EMSGSIZE, this means the msg is too large and will never succeed. To determine the max msg size a client can be sent, use <code>qb_ipcs_connection_get_buffer_size()</code></dl>
<h3>int32_t qb_ipcs_run (<code>qb_ipcs_service_t</code> *s)</h3>
<p>run the new IPC server. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> service instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 == ok; -errno to indicate a failure. Service is destroyed on failure.</dl>
<h3>void* qb_ipcs_service_context_get (<code>qb_ipcs_service_t</code> *s)</h3>
<p>Get the context (set previously) </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> service instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>the context</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_ipcs_service_context_set()</code></dl>
<h3>void qb_ipcs_service_context_set (<code>qb_ipcs_service_t</code> *s, void *context)</h3>
<p>Associate a &#8216;user&#8217; pointer with this service. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> service instance<br />
 <i>context</i> the pointer to associate with this service.</dl>
<p> <code>See Also:</code></p>
<dl>
<dd><code>qb_ipcs_service_context_get()</code></dl>
<h3>int32_t qb_ipcs_service_id_get (<code>qb_ipcs_connection_t</code> *c)</h3>
<p>Get the service id related to this connection&#8217;s service. (as passed into <code>qb_ipcs_create()</code> </p>
<p> <code>Returns:</code></p>
<dl>
<dd>service id.</dl>
<h3>int32_t qb_ipcs_stats_get (<code>qb_ipcs_service_t</code> *pt, struct <code>qb_ipcs_stats</code> *stats, int32_tclear_after_read)</h3>
<p>Get the service statistics. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>stats</i> (out) the statistics structure<br />
 <i>clear_after_read</i> clear stats after copying them into stats<br />
 <i>pt</i> service instance</dl>
<p> <code>Returns:</code></p>
<dl>
<dd>0 == ok; -errno to indicate a failure</dl>
<h3>void qb_ipcs_unref (<code>qb_ipcs_service_t</code> *s)</h3>
<p>Decrease the reference counter on the service object. </p>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>s</i> service instance</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libqb from the source code.</p>
