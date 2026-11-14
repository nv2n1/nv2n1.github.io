---
title: "quorum_context_get(3)"
name: "quorum_context_get"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quorum_context_get/"
description: "quorum_context_get – Gets the context variable for a QUORUM instance"
---

<p>quorum_context_get &#8211; Gets the context variable for a QUORUM instance</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/quorum.h&gt;
int quorum_context_get(quorum_handle_t handle, void **context);</code></pre>
<h2>Description</h2>
<p>The <code>quorum_context_get</code> function is used to retrieve the context variable previously stored using <code><a href="/docs/linux/man/3-quorum_context_set/">quorum_context_set</a>(3)</code></p>
<h2>Return Value</h2>
<p>This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>Errors</h2>
<p><code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-quorum_overview/">quorum_overview</a></code>(8), <code><a href="/docs/linux/man/3-quorum_initialize/">quorum_initialize</a></code>(3), <code><a href="/docs/linux/man/3-quorum_finalize/">quorum_finalize</a></code>(3), <code><a href="/docs/linux/man/3-quorum_getquorate/">quorum_getquorate</a></code>(3), <code><a href="/docs/linux/man/3-quorum_trackstart/">quorum_trackstart</a></code>(3), <code><a href="/docs/linux/man/3-quorum_trackstop/">quorum_trackstop</a></code>(3), <code><a href="/docs/linux/man/3-quorum_fd_get/">quorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-quorum_dispatch/">quorum_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-quorum_context_set/">quorum_context_set</a></code>(3), </p>
