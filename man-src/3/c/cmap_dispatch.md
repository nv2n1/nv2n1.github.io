---
title: "cmap_dispatch(3)"
name: "cmap_dispatch"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmap_dispatch/"
description: "cmap_dispatch – Dispatches callbacks from the CMAP service"
---

<h2 class="name">NAME</h2>
<p> cmap_dispatch &#8211; Dispatches callbacks from the CMAP service</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cmap.h&gt;</code> </p>
<p> <code>cs_error_t cmap_dispatch (cmap_handle_t </code><i>handle</i><code>, cs_dispatch_flags_t </code><i>dispatch_types</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cmap_dispatch</code> function is used to dispatch configuration changes. </p>
<p> Each application may have several connections to the CMAP API. Each application uses the <i>handle</i> argument to uniquely identify the connection. </p>
<p> The <i>dispatch_types</i> argument is used to identify the type of dispatch to execute. The possible types are CS_DISPATCH_ONE, CS_DISPATCH_ALL and CS_DISPATCH_BLOCKING. </p>
<p> The dispatch values have the following meanings:</p>
<dl>
<dt><code>CS_DISPATCH_ONE</code></p>
<dd> Dispatch at least one callback, blocking until the callback is dispatched.</p>
<dt><code>CS_DISPATCH_ALL</code></p>
<dd> Dispatch all waiting callbacks without blocking to wait for any callbacks.</p>
<dt><code>CS_DISPATCH_BLOCKING</code></p>
<dd> Dispatch all callbacks blocking indefinitely. This is used in a threaded program where a thread is created, and then cs_dispatch() is called immediately from the created thread to execute callbacks.</p>
<dt><code>CS_DISPATCH_ONE_NONBLOCKING</code></p>
<dd> Dispatch at most one callback. If there is no pending callback, CS_ERR_TRY_AGAIN is returned.</dl>
<p> It&#8217;s needed to call <code><a href="/docs/linux/man/3-cmap_track_add/">cmap_track_add</a>(3)</code> to add tracked items and receive callbacks. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cmap_track_add/">cmap_track_add</a></code>(3), <code><a href="/docs/linux/man/3-cmap_track_delete/">cmap_track_delete</a></code>(3), <code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
