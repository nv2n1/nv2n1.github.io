---
title: "cmap_context_set(3)"
name: "cmap_context_set"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmap_context_set/"
description: "cmap_context_set – Sets the context variable for a CMAP instance"
---

<h2 class="name">NAME</h2>
<p> cmap_context_set &#8211; Sets the context variable for a CMAP instance</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cmap.h&gt;</code> </p>
<p> <code>cs_error_t cmap_context_set (cmap_handle_t </code><i>handle</i><code>, const void *</code><i>context</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cmap_context_set</code> function is used to store the context variable for cmap instance. It has no meaning insire libcmap itself and will not be touched by the library. It can be retrieved using <code><a href="/docs/linux/man/3-cmap_context_get/">cmap_context_get</a>(3).</code> </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cmap_context_get/">cmap_context_get</a></code>(3), <code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
