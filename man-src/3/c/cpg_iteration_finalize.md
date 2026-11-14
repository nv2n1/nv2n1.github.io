---
title: "cpg_iteration_finalize(3)"
name: "cpg_iteration_finalize"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpg_iteration_finalize/"
description: "cpg_iteration_finalize – Finalize iterator for members of CPG"
---

<h2 class="name">NAME</h2>
<p> cpg_iteration_finalize &#8211; Finalize iterator for members of CPG</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cpg.h&gt;</code> </p>
<p> <code>cs_error_t cpg_iteration_finalize (cpg_iteration_handle_t </code><i>handle</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cpg_iteration_finalize</code> function is used to free up memory asociated with iteration obtained by calling of <code><a href="/docs/linux/man/3-cpg_iteration_initialize/">cpg_iteration_initialize</a>(3)</code> function. The <i>handle</i> argument is iterator handle obtained by <code><a href="/docs/linux/man/3-cpg_iteration_initialize/">cpg_iteration_initialize</a>(3)</code> function. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful. CS_ERR_BAD_HANDLE error is returned when handle is invalid. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cpg_iteration_initialize/">cpg_iteration_initialize</a></code>(3), <code><a href="/docs/linux/man/8-cpg_overview/">cpg_overview</a></code>(8) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
