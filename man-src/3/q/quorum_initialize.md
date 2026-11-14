---
title: "quorum_initialize(3)"
name: "quorum_initialize"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quorum_initialize/"
description: "quorum_initialize – Create a new connection to the Quorum service"
---

<p>quorum_initialize &#8211; Create a new connection to the Quorum service</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/quorum.h&gt;
int quorum_initialize(quorum_handle_t *handle, quorum_callbacks_t *callbacks, uint32_t *quorum_type);</code></pre>
<h2>Description</h2>
<p>The <code>quorum_initialize</code> function is used to initialize a connection to the quorum API. Each application may have several connections to the quorum API. Each application uses the <i>handle</i> argument to uniquely identify the connection. The <i>handle</i> argument is then used in other function calls to identify the connection to be used for communication with the quorum service. Every time the voting configuraton changes (eg a node joins or leave the cluster) or the quorum status change, the callback is called. The callback function is described by the following type definitions: </p>
<pre>typedef void (*quorum_notification_fn_t) (
 quorum_handle_t handle,
 uint32_t quorate,
 uint64_t ring_seq,
 uint32_t view_list_entries,
 uint32_t *view_list
 );</pre>
<p>The <i>callbacks</i> argument is of the type: </p>
<pre>typedef struct {
 quorum_notification_fn_t quorum_notify_fn;
} quorum_callbacks_t;</pre>
<p>The <i>quorum_type</i> argument is set to:  <i>QUORUM_FREE</i> value means that no quorum algorithm is loaded and that no callbacks will take place. <i>QUORUM_SET</i> value means that one quorum algorithm is configured and that callbacks will take place. When a configuration change occurs, the callback is called from the <code>quorum_dispatch()</code> function. </p>
<h2>Return Value</h2>
<p>This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>Errors</h2>
<p><code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-quorum_overview/">quorum_overview</a></code>(8), <code><a href="/docs/linux/man/3-quorum_finalize/">quorum_finalize</a></code>(3), <code><a href="/docs/linux/man/3-quorum_getquorate/">quorum_getquorate</a></code>(3), <code><a href="/docs/linux/man/3-quorum_trackstart/">quorum_trackstart</a></code>(3), <code><a href="/docs/linux/man/3-quorum_trackstop/">quorum_trackstop</a></code>(3), <code><a href="/docs/linux/man/3-quorum_fd_get/">quorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-quorum_dispatch/">quorum_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-quorum_context_set/">quorum_context_set</a></code>(3), <code><a href="/docs/linux/man/3-quorum_context_get/">quorum_context_get</a></code>(3) </p>
