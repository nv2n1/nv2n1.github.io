---
title: "cmap_delete(3)"
name: "cmap_delete"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmap_delete/"
description: "cmap_delete – Delete key/value pair from the CMAP service"
---

<h2 class="name">NAME</h2>
<p> cmap_delete &#8211; Delete key/value pair from the CMAP service</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cmap.h&gt;</code> </p>
<p> <code>cs_error_t cmap_delete(cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cmap_delete</code> function is used to delete key from cmap. Key must be previously created by <code><a href="/docs/linux/man/3-cmap_set/">cmap_set</a>(3)</code> function. The <i>handle</i> argument is connection to CMAP database obtained by calling <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a>(3)</code> function. <i>key_name</i> is name of key to delete. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful. If key_name is unspecified, CS_ERR_INVALID_PARAM is returned. For nonexisting keys, CS_ERR_NOT_EXIST error is returned. Some of keys may be tagged read-only directly in corosync and deleting such key will result in CS_ERR_ACCESS error. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a></code>(3), <code><a href="/docs/linux/man/3-cmap_set/">cmap_set</a></code>(3), <code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
