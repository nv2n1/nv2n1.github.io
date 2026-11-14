---
title: "quorum_finalize(3)"
name: "quorum_finalize"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quorum_finalize/"
description: "quorum_finalize – Terminate a connection to the quorum service"
---

<p>quorum_finalize &#8211; Terminate a connection to the quorum service</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/quorum.h&gt;
int quorum_finalize(quorum_handle_t handle);</code></pre>
<h2>Description</h2>
<p>The <code>quorum_finalize</code> function is used to close a connection to the quorum API. Once the connection is finalized, the handle may not be used again by applications. No more callbacks will be dispatched from the <code>quorum_dispatch</code> function. </p>
<h2>Return Value</h2>
<p>This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>Errors</h2>
<p><code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-quorum_overview/">quorum_overview</a></code>(8), <code><a href="/docs/linux/man/3-quorum_initialize/">quorum_initialize</a></code>(3), <code><a href="/docs/linux/man/3-quorum_getquorate/">quorum_getquorate</a></code>(3), <code><a href="/docs/linux/man/3-quorum_trackstart/">quorum_trackstart</a></code>(3), <code><a href="/docs/linux/man/3-quorum_trackstop/">quorum_trackstop</a></code>(3), <code><a href="/docs/linux/man/3-quorum_fd_get/">quorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-quorum_dispatch/">quorum_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-quorum_context_set/">quorum_context_set</a></code>(3), <code><a href="/docs/linux/man/3-quorum_context_get/">quorum_context_get</a></code>(3) </p>
