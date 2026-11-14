---
title: "cmap_iter_init(3)"
name: "cmap_iter_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmap_iter_init/"
description: "cmap_iter_init – Initialize iterator for keys stored in CMAP"
---

<h2 class="name">NAME</h2>
<p> cmap_iter_init &#8211; Initialize iterator for keys stored in CMAP</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cmap.h&gt;</code> </p>
<p> <code>cs_error_t cmap_iter_init (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>prefix</i><code>, cmap_iter_handle_t *</code><i>cmap_iter_handle</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cmap_iter_init</code> function is used to initialize iteration of all keys with given <i>prefix.</i> The <i>handle</i> argument is connection to CMAP database obtained by calling <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a>(3)</code> function. <i>prefix</i> is string, and every returned key must have name with given prefix. This variable can also be NULL (or empty string) and then all keys are iterated. </p>
<p> <code>cmap_iter_init</code> is used only for initialize context for future <code><a href="/docs/linux/man/3-cmap_iter_next/">cmap_iter_next</a>(3)</code> calls and handle needed for that function is returned in <i>cmap_iter_handle</i> variable. When you have finished iteration over objects, call <code><a href="/docs/linux/man/3-cmap_iter_finalize/">cmap_iter_finalize</a>(3)</code> function to free up memory associated with iteration. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful. If there are no items with given prefixes, CS_ERR_NO_SECTIONS is returned. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cmap_iter_next/">cmap_iter_next</a></code>(3), <code><a href="/docs/linux/man/3-cmap_iter_finalize/">cmap_iter_finalize</a></code>(3), <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a></code>(3), <code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
