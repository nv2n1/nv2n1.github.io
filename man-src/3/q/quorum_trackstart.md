---
title: "quorum_trackstart(3)"
name: "quorum_trackstart"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quorum_trackstart/"
description: "quorum_trackstart – Enable callbacks notification."
---

<p>quorum_trackstart &#8211; Enable callbacks notification.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/quorum.h&gt;
int quorum_trackstart(quorum_handle_t *handle, unsigned int flags);</code></pre>
<h2>Description</h2>
<p>The <code>quorum_trackstart</code> function is used to enable callbacks notification from the quorum API. Every time the voting configuraton changes (eg a node joins or leave the cluster) or the quorum status change, the notification is queued. The notification is dispatched via <code>quorum_dispatch()</code> function that will execute the callback. The <i>flags</i> argument is defined by one or more of the following values and values can be bitwise-or&#8217;d </p>
<pre><code>#define CS_TRACK_CURRENT      0x01
#define CS_TRACK_CHANGES      0x02
#define CS_TRACK_CHANGES_ONLY 0x04</code></pre>
<h2>Return Value</h2>
<p>This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>Errors</h2>
<p><code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-quorum_overview/">quorum_overview</a></code>(8), <code><a href="/docs/linux/man/3-quorum_initialize/">quorum_initialize</a></code>(3), <code><a href="/docs/linux/man/3-quorum_finalize/">quorum_finalize</a></code>(3), <code><a href="/docs/linux/man/3-quorum_getquorate/">quorum_getquorate</a></code>(3), <code><a href="/docs/linux/man/3-quorum_trackstop/">quorum_trackstop</a></code>(3), <code><a href="/docs/linux/man/3-quorum_fd_get/">quorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-quorum_dispatch/">quorum_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-quorum_context_set/">quorum_context_set</a></code>(3), <code><a href="/docs/linux/man/3-quorum_context_get/">quorum_context_get</a></code>(3) </p>
