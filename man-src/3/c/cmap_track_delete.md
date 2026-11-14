---
title: "cmap_track_delete(3)"
name: "cmap_track_delete"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmap_track_delete/"
description: "cmap_track_delete – Remove tracking of values in CMAP"
---

<h2 class="name">NAME</h2>
<p> cmap_track_delete &#8211; Remove tracking of values in CMAP</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cmap.h&gt;</code> </p>
<p> <code>cs_error_t cmap_track_delete (cmap_handle_t </code><i>handle</i><code>, cmap_track_handle_t </code><i>track_handle</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cmap_track_delte</code> function is used to remove tracking of values changed in CMAP. The <i>handle</i> argument is connection to CMAP database obtained by calling <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a>(3)</code> function. <i>track_handle</i> argument is iterator handle obtained by <code><a href="/docs/linux/man/3-cmap_track_add/">cmap_track_add</a>(3)</code> function. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful. CS_ERR_BAD_HANDLE error is returned when track_handle is invalid. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cmap_track_add/">cmap_track_add</a></code>(3), <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a></code>(3), <code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
