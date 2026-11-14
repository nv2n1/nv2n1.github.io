---
title: "quorum_trackstop(3)"
name: "quorum_trackstop"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quorum_trackstop/"
description: "quorum_trackstop – Disable callbacks notification."
---

<p>quorum_trackstop &#8211; Disable callbacks notification.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/quorum.h&gt;
int quorum_trackstart(quorum_handle_t *handle);</code></pre>
<h2>Description</h2>
<p>The <code>quorum_trackstop</code> function is used to disable callbacks notification from the quorum API. </p>
<h2>Return Value</h2>
<p>This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>Errors</h2>
<p><code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-quorum_overview/">quorum_overview</a></code>(8), <code><a href="/docs/linux/man/3-quorum_initialize/">quorum_initialize</a></code>(3), <code><a href="/docs/linux/man/3-quorum_finalize/">quorum_finalize</a></code>(3), <code><a href="/docs/linux/man/3-quorum_getquorate/">quorum_getquorate</a></code>(3), <code><a href="/docs/linux/man/3-quorum_trackstart/">quorum_trackstart</a></code>(3), <code><a href="/docs/linux/man/3-quorum_fd_get/">quorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-quorum_dispatch/">quorum_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-quorum_context_set/">quorum_context_set</a></code>(3), <code><a href="/docs/linux/man/3-quorum_context_get/">quorum_context_get</a></code>(3) </p>
