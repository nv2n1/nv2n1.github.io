---
title: "cpg_model_initialize(3)"
name: "cpg_model_initialize"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpg_model_initialize/"
description: "cpg_model_initialize – Create a new connection to the CPG service"
---

<h2>NAME</h2>
<p> cpg_model_initialize &#8211; Create a new connection to the CPG service</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cpg.h&gt;</code> </p>
<p> <code>cs_error_t cpg_model_initialize(cpg_handle_t *</code><i>handle</i><code>, cpg_model_t </code><i>model</i><code>, cpg_model_data_t *</code><i>model_data</i><code>, void *</code><i>context</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cpg_model_initialize</code> function is used to initialize a connection to the closed process groups API. </p>
<p> Each application may have several connections to the CPG API. Each application uses the <i>handle</i> argument to uniquely identify the connection. The <i>handle</i> argument is then used in other function calls to identify the connection to be used for communication with the CPG service. </p>
<p> Argument <i>model</i> is used to explicitly choose set of callbacks and internal parameters. Currently only model <i>CPG_MODEL_V1</i> is defined. </p>
<p> Callbacks and internal parameters are passed by <i>model_data</i> argument. This is casted pointer (idea is similar as in sockaddr function) to one of structures corresponding to chosen model. Currently only <i>cpg_model_v1_data_t</i> is needed.</p>
<h2>MODEL_V1</h2>
<p> The <i>MODEL_V1</i> is backwards compatible with original callbacks initialized by <i>cpg_initialize</i> but new callback <i>cpg_totem_confchg_fn</i> is defined. </p>
<p> Every time an CPG event occurs within the joined group, one of the callbacks specified by the argument <i>callbacks</i> is called. The callback functions are described by the following type definitions: </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
typedef void (*cpg_deliver_fn_t)(
    cpg_handle_t handle,
    const struct cpg_name *group_name,
    uint32_t nodeid,
    uint32_t pid,
    const void *msg,
    size_t msg_len);
typedef void (*cpg_confchg_fn_t)(
    cpg_handle_t handle,
    const struct cpg_name *group_name,
    const struct cpg_address *member_list, size_t member_list_entries,
    const struct cpg_address *left_list, size_t left_list_entries,
    const struct cpg_address *joined_list, size_t joined_list_entries);
typedef void (*cpg_totem_confchg_fn_t)(
    cpg_handle_t handle,
    struct cpg_ring_id ring_id,
    uint32_t member_list_entries,
    const uint32_t *member_list);
</code></pre>
</dl>
<dt>
<dd></dl>
<p> The <i>cpg_model_v1_data_t</i> structure is defined as:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
typedef struct {<br />
    cpg_model_t model;<br />
    cpg_deliver_fn_t cpg_deliver_fn;<br />
    cpg_confchg_fn_t cpg_confchg_fn;<br />
    cpg_totem_confchg_fn_t cpg_totem_confchg_fn;<br />
    unsigned int flags;<br />
} cpg_model_v1_data_t;
</dl>
<dt>
<dd></dl>
<p> When a configuration change occurs or a message is to be delivered one of the callbacks is called from the <code>cpg_dispatch()</code> function. If a configuration change occurs, <i>cpg_confchg_fn</i> is called. If a delivery of a message occurs, <i>cpg_deliver_fn</i> is called. When totem membership change occurs, <i>cpg_totem_confchg_fn</i> is called. You can OR <i>CPG_MODEL_V1_DELIVER_INITIAL_TOTEM_CONF</i> constant to flags to get callback after first confchg event. </p>
<p> The <i>cpg_address</i> structure is defined</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
struct cpg_address {<br />
    unsigned int nodeid;<br />
    unsigned int pid;<br />
    unsigned int reason;<br />
};
</dl>
<dt>
<dd></dl>
<p> where nodeid is a 32 bit unique node identifier, pid is the process ID of the process that has joined/left the group or sent the message, and reason is an integer code indicating why the node joined/left the group. </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
CPG_REASON_JOIN     - the process joined a group using cpg_join().
CPG_REASON_LEAVE    - the process left a group using cpg_leave()
CPG_REASON_NODEDOWN - the process left a group because the node left the cluster.
CPG_REASON_NODEUP   - the process joined a group because it was already a member of a group on a node that has just joined the cluster
CPG_REASON_PROCDOWN - the process left a group without calling cpg_leave()
</pre>
</dl>
<dt>
<dd></dl>
<p> The <i>cpg_ring_id</i> structure is defined</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
struct cpg_ring_id {
    uint32_t nodeid;
    uint64_t seq;
};
</code></pre>
</dl>
<dt>
<dd></dl>
<p> where <i>nodeid</i> is if of node of current Totem leader and seq is increasing number. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>ERRORS</h2>
<p> The errors are undocumented.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-cpg_overview/">cpg_overview</a></code>(8), <code><a href="/docs/linux/man/3-cpg_initialize/">cpg_initialize</a></code>(3), <code><a href="/docs/linux/man/3-cpg_finalize/">cpg_finalize</a></code>(3), <code><a href="/docs/linux/man/3-cpg_fd_get/">cpg_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-cpg_dispatch/">cpg_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-cpg_join/">cpg_join</a></code>(3), <code><a href="/docs/linux/man/3-cpg_leave/">cpg_leave</a></code>(3), <code><a href="/docs/linux/man/3-cpg_mcast_joined/">cpg_mcast_joined</a></code>(3), <code><a href="/docs/linux/man/3-cpg_membership_get/">cpg_membership_get</a></code>(3) <code><a href="/docs/linux/man/3-cpg_zcb_alloc/">cpg_zcb_alloc</a></code>(3) <code><a href="/docs/linux/man/3-cpg_zcb_free/">cpg_zcb_free</a></code>(3) <code><a href="/docs/linux/man/3-cpg_zcb_mcast_joined/">cpg_zcb_mcast_joined</a></code>(3) <code><a href="/docs/linux/man/3-cpg_context_get/">cpg_context_get</a></code>(3) <code><a href="/docs/linux/man/3-cpg_context_set/">cpg_context_set</a></code>(3) <code><a href="/docs/linux/man/3-cpg_local_get/">cpg_local_get</a></code>(3) <code><a href="/docs/linux/man/3-cpg_model_initialize/">cpg_model_initialize</a></code>(3) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
