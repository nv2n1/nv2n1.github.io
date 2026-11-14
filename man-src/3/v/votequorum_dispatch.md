---
title: "votequorum_dispatch(3)"
name: "votequorum_dispatch"
section: "3"
letter: "v"
url: "/docs/linux/man/3-votequorum_dispatch/"
description: "votequorum_dispatch – Dispatches callbacks from the votequorum service"
---

<p>votequorum_dispatch &#8211; Dispatches callbacks from the votequorum service</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/votequorum.h&gt;
int votequorum_dispatch(votequorum_handle_t handle, cs_dispatch_flags_t *dispatch_types);</code></pre>
<h2>Description</h2>
<p>The <code>votequorum_dispatch</code> function is used to dispatch configuration changes. Each application may have several connections to the votequorum API. Each application uses the <i>handle</i> argument to uniquely identify the connection. The <i>dispatch_types</i> argument is used to identify the type of dispatch to execute. The possible types are defined by the structure:  The dispatch values have the following meanings:</p>
<dl>
<dt><code>CS_DISPATCH_ONE</code></p>
<dd>Dispatch at least one callback, blocking until the callback is dispatched.</p>
<dt><code>CS_DISPATCH_ALL</code></p>
<dd>Dispatch all waiting callbacks without blocking to wait for any callbacks.</p>
<dt><code>CS_DISPATCH_BLOCKING</code></p>
<dd>Dispatch all callbacks blocking indefinitely. This is used in a threaded program where a thread is created, and then quorum_dispatch() is called immediately from the created thread to execute callbacks.</p>
<dt><code>CS_DISPATCH_ONE_NONBLOCKING</code></p>
<dd>Dispatch at most one callback. If there is no pending callback, CS_ERR_TRY_AGAIN is returned. </p>
<h2>Return Value</h2>
<p>This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>Errors</h2>
<p><code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-votequorum_overview/">votequorum_overview</a></code>(8), <code><a href="/docs/linux/man/3-votequorum_initialize/">votequorum_initialize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_finalize/">votequorum_finalize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_getinfo/">votequorum_getinfo</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstart/">votequorum_trackstart</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstop/">votequorum_trackstop</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_fd_get/">votequorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_set/">votequorum_context_set</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_get/">votequorum_context_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setexpected/">votequorum_setexpected</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setvotes/">votequorum_setvotes</a></code>(3) </p>
