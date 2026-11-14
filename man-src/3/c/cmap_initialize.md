---
title: "cmap_initialize(3)"
name: "cmap_initialize"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmap_initialize/"
description: "cmap_initialize – Initialize CMAP API"
---

<h2 class="name">NAME</h2>
<p> cmap_initialize &#8211; Initialize CMAP API</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cmap.h&gt;</code> </p>
<p> <code>cs_error_t cmap_initialize (cmap_handle_t </code><i>*handle</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cmap_initialize</code> function is used to initialize a connection to the Configuration Map API. Each application may have several connections to the CMAP API. Each application uses the <i>handle</i> argument to uniquely identify the connection. The <i>handle</i> argument is then used in other function calls to identify the connection to be used for communication with the CMAP service. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cmap_finalize/">cmap_finalize</a></code>(3), <code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
