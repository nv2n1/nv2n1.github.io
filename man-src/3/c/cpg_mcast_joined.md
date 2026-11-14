---
title: "cpg_mcast_joined(3)"
name: "cpg_mcast_joined"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpg_mcast_joined/"
description: "cpg_mcast_joined – Multicasts to all groups joined to a handle"
---

<h2>NAME</h2>
<p> cpg_mcast_joined &#8211; Multicasts to all groups joined to a handle</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/uio.h&gt;</code> <code>#include &lt;corosync/cpg.h&gt;</code> </p>
<p> <code>int cpg_mcast_joined(cpg_handle_t </code><i>handle</i><code>, cpg_guarantee_t </code><i>guarantee</i><code>, struct iovec *</code><i>iovec</i><code>, int </code><i>iov_len</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>cpg_mcast_joined</code> function will multicast a message to all the processes that have been joined with the <code><a href="/docs/linux/man/3-cpg_join/">cpg_join</a>(3)</code> function for the same group name. Messages that are sent to any of the groups joined to the parameter <i>handle</i> will be delivered to all subscribed processes in the system. </p>
<p> The argument <i>guarantee</i> requests a delivery guarantee for the message to be sent. The cpg_guarantee_t type is defined by:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
typedef enum {
    CPG_TYPE_UNORDERED, /* not implemented */
    CPG_TYPE_FIFO,      /* same as agreed */
    CPG_TYPE_AGREED,    /* implemented */
    CPG_TYPE_SAFE       /* not implemented */
} cpg_guarantee_t;
</code></pre>
</dl>
<dt>
<dd></dl>
<p> The meanings of the cpg_guarantee_t typedef are:</p>
<dl>
<dt><code>CPG_TYPE_UNORDERED</code></p>
<dd> Messages are guaranteed to be delivered, but with no particular order. This mode is unimplemented in the CPG library.</p>
<dt><code>CPG_TYPE_FIFO</code></p>
<dd> Messages are guaranteed to be delivered in first sent first delivery order. In fact, this guarantee is equivalent to the CPG_TYPE_AGREED guarantee.</p>
<dt><code>CPG_TYPE_AGREED</code></p>
<dd> All processors must agree on the order of delivery. If a message is sent from two or more processes at about the same time, the delivery will occur in the same order to all processes.</p>
<dt><code>CPG_TYPE_SAFE</code></p>
<dd> All processes must agree on the order of delivery. Further all processes must have a copy of the message before any delivery takes place. This mode is unimplemented in the CPG library.</dl>
<p> The <i>iovec</i> argument describes the scatter/gather list which is used to transmit a message. This is a iovec described by:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
struct iovec {
    void *iov_base;       /* Pointer to data.  */
    unsigned int iov_len; /* Length of data.  */
};
</code></pre>
</dl>
<dt>
<dd></dl>
<p> The <i>iov_len</i> argument describes the number of entires in the <i>iovec</i> argument. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>ERRORS</h2>
<p> The errors are undocumented.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-cpg_overview/">cpg_overview</a></code>(8), <code><a href="/docs/linux/man/3-cpg_initialize/">cpg_initialize</a></code>(3), <code><a href="/docs/linux/man/3-cpg_finalize/">cpg_finalize</a></code>(3), <code><a href="/docs/linux/man/3-cpg_fd_get/">cpg_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-cpg_dispatch/">cpg_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-cpg_join/">cpg_join</a></code>(3), <code><a href="/docs/linux/man/3-cpg_leave/">cpg_leave</a></code>(3), <code><a href="/docs/linux/man/3-cpg_mcast_joined/">cpg_mcast_joined</a></code>(3), <code><a href="/docs/linux/man/3-cpg_membership_get/">cpg_membership_get</a></code>(3) <code><a href="/docs/linux/man/3-cpg_zcb_alloc/">cpg_zcb_alloc</a></code>(3) <code><a href="/docs/linux/man/3-cpg_zcb_free/">cpg_zcb_free</a></code>(3) <code><a href="/docs/linux/man/3-cpg_zcb_mcast_joined/">cpg_zcb_mcast_joined</a></code>(3) <code><a href="/docs/linux/man/3-cpg_context_get/">cpg_context_get</a></code>(3) <code><a href="/docs/linux/man/3-cpg_context_set/">cpg_context_set</a></code>(3) <code><a href="/docs/linux/man/3-cpg_local_get/">cpg_local_get</a></code>(3) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
