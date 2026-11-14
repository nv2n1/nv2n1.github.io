---
title: "votequorum_initialize(3)"
name: "votequorum_initialize"
section: "3"
letter: "v"
url: "/docs/linux/man/3-votequorum_initialize/"
description: "votequorum_initialize – Create a new connection to the VoteQuorum service"
---

<p>votequorum_initialize &#8211; Create a new connection to the VoteQuorum service</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/votequorum.h&gt;
int votequorum_initialize(votequorum_handle_t *handle, votequorum_callbacks_t *callbacks);</code></pre>
<h2>Description</h2>
<p>The <code>votequorum_initialize</code> function is used to initialize a connection to the vote-based quorum database API. Each application may have several connections to the votequorum API. Each application uses the <i>handle</i> argument to uniquely identify the connection. The <i>handle</i> argument is then used in other function calls to identify the connection to be used for communication with the votequorum service. Every time the voting configuration is about to change (eg a node joins or leave the cluster), the callback is called. The callback function is described by the following type definitions: </p>
<pre>typedef void (*votequorum_nodelist_notification_fn_t) (
 votequorum_handle_t handle,
 uint64_t context,
 uint32_t node_list_entries,
 uint32_t node_list[]
 );</pre>
<p>Current ring_id (one get in votequorum_quorum_notification_fn) must be passed to <code>votequorum_qdevice_poll</code> to make qdevice voting valid. Every time the quorum state changes (eg a node joins or leave the cluster), the callback is called. The callback function is described by the following type definitions: </p>
<pre>typedef void (*votequorum_quorum_notification_fn_t) (
 votequorum_handle_t handle,
 uint64_t context,
 uint32_t quorate,
 uint32_t node_list_entries,
 votequorum_node_t node_list[]
 );</pre>
<p>The difference between votequorum_nodelist_notification_t and votequorum_quorum_notification_t is subtle but important. The &#8216;nodelist&#8217; callback is sent at the start of a cluster state transition and contains the new ring_id and only the list of nodes that are included in the sync state &#8211; ie only active nodes. No quorum information is included this callback because it is not available at that time. The &#8216;quorum&#8217; callback is sent after the cluster state transition has completed and does contain quorum information. In addition, the nodelist contains a list of all nodes known to votequorum (whether up or down) and their state as well as information about the quorum device attached (if any). quorum callbacks will not be sent for qdevice up and down events unless they affect quorum. Every time the expected votes are changed, the callback is called. The expected votes callback function is described by the following type definitions: </p>
<pre>typedef void (*votequorum_expectedvotes_notification_fn_t) (
 votequorum_handle_t handle,
 uint64_t context,
 uint32_t expected_votes);</pre>
<p>The <i>callbacks</i> argument is of the type: </p>
<pre>typedef struct {
 votequorum_quorum_notification_fn_t votequorum_quorum_notify_fn;
 votequorum_expectedvotes_notification_fn_t votequorum_expectedvotes_notify_fn;
 votequorum_nodelist_notification_fn_t votequorum_nodelist_notify_fn;
} votequorum_callbacks_t;</pre>
<p>When a configuration change occurs, the callback is called from the <code>votequorum_dispatch()</code> function. </p>
<h2>Return Value</h2>
<p>This call returns the CS_OK value if successful, otherwise an error is returned.</p>
<h2>Errors</h2>
<p><code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-votequorum_overview/">votequorum_overview</a></code>(8), <code><a href="/docs/linux/man/3-votequorum_finalize/">votequorum_finalize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_getinfo/">votequorum_getinfo</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstart/">votequorum_trackstart</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstop/">votequorum_trackstop</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_fd_get/">votequorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_dispatch/">votequorum_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_set/">votequorum_context_set</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_get/">votequorum_context_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setexpected/">votequorum_setexpected</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setvotes/">votequorum_setvotes</a></code>(3) </p>
