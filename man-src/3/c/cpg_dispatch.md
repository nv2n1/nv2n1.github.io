---
title: "cpg_dispatch(3)"
name: "cpg_dispatch"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpg_dispatch/"
description: "cpg_dispatch – Dispatches callbacks from the CPG service"
---

<h2>NAME</h2>
<p> cpg_dispatch &#8211; Dispatches callbacks from the CPG service</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cpg.h&gt;</code> </p>
<p> <code>int cpg_dispatch(cpg_handle_t </code><i>handle</i><code>, cpg_dispatch_t *</code><i>dispatch_types</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>cpg_dispatch</code> function is used to dispatch configuration changes or messages from the closed process groups API. </p>
<p> Each application may have several connections to the CPG API. Each application uses the <i>handle</i> argument to uniquely identify the connection. </p>
<p> The <i>dispatch_types</i> argument is used to identify the type of dispatch to execute. The possible types are defined by the structure: </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
typedef enum {
    CS_DISPATCH_ONE,
    CS_DISPATCH_ALL,
    CS_DISPATCH_BLOCKING
} cpg_dispatch_t;
</code></pre>
</dl>
<dt>
<dd></dl>
<p> The dispatch values have the following meanings:</p>
<dl>
<dt><code>CS_DISPATCH_ONE</code></p>
<dd> Dispatch atleast one callback, blocking until the callback is dispatched.</p>
<dt><code>CS_DISPATCH_ALL</code></p>
<dd> Dispatch all waiting callbacks without blocking to wait for any callbacks.</p>
<dt><code>CS_DISPATCH_BLOCKING</code></p>
<dd> Dispatch all callbacks, blocking indefinitely. This is used in a threaded program where a thread is created, and then cpg_dispatch() is called immediately from the created thread to execute callbacks.</p>
<dt><code>CS_DISPATCH_ONE_NONBLOCKING</code></p>
<dd> Dispatch at most one callback. If there is no pending callback, CS_ERR_TRY_AGAIN is returned. </p>
</dl>
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
