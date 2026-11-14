---
title: "cmap_iter_next(3)"
name: "cmap_iter_next"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmap_iter_next/"
description: "cmap_iter_next – Return next item in iteration in CMAP"
---

<h2 class="name">NAME</h2>
<p> cmap_iter_next &#8211; Return next item in iteration in CMAP</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cmap.h&gt;</code> </p>
<p> <code>cs_error_t cmap_iter_next(cmap_handle_t </code><i>handle</i><code>, cmap_iter_handle_t </code><i>iter_handle</i><code>, char </code><i>key_name[]</i><code>, size_t *</code><i>value_len</i><code>, cmap_value_types_t *</code><i>type</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cmap_iter_next</code> function is used to get next value in iteration. The <i>handle</i> argument is connection to CMAP database obtained by calling <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a>(3)</code> function. <i>iter_handle</i> argument is iterator handle obtained by <code><a href="/docs/linux/man/3-cmap_iter_init/">cmap_iter_init</a>(3)</code> function. Following key name is stored inside <i>key_name</i> argument, which must be preallocated by caller and its quaranted maximum size is CMAP_KEYNAME_MAXLEN (urrently 255). <i>value_len</i> is pointer where length of value is stored, but can be NULL. <i>type</i> is also optional argument (can be NULL) and here type of value is stored (type is one of types described in <code><a href="/docs/linux/man/3-cmap_get/">cmap_get</a>(3)</code> function). </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful. If there are no more items to iterate, CS_NO_SECTION error code is returned. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cmap_iter_init/">cmap_iter_init</a></code>(3), <code><a href="/docs/linux/man/3-cmap_iter_finalize/">cmap_iter_finalize</a></code>(3), <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a></code>(3), <code><a href="/docs/linux/man/3-cmap_get/">cmap_get</a></code>(3), <code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
