---
title: "cmap_iter_finalize(3)"
name: "cmap_iter_finalize"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmap_iter_finalize/"
description: "cmap_iter_finalize – Finalize iterator for keys stored in CMAP"
---

<h2 class="name">NAME</h2>
<p> cmap_iter_finalize &#8211; Finalize iterator for keys stored in CMAP</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cmap.h&gt;</code> </p>
<p> <code>cs_error_t cmap_iter_finalize (cmap_handle_t </code><i>handle</i><code>, cmap_iter_handle_t </code><i>iter_handle</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cmap_iter_finalize</code> function is used to free up memory asociated with iteration obtained by calling of <code><a href="/docs/linux/man/3-cmap_iter_init/">cmap_iter_init</a>(3)</code> function. The <i>handle</i> argument is connection to CMAP database obtained by calling <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a>(3)</code> function. <i>iter_handle</i> argument is iterator handle obtained by <code><a href="/docs/linux/man/3-cmap_iter_init/">cmap_iter_init</a>(3)</code> function. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful. CS_ERR_BAD_HANDLE error is returned when iter_handle is invalid. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cmap_iter_init/">cmap_iter_init</a></code>(3), <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a></code>(3), <code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
