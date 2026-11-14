---
title: "cpg_iteration_initialize(3)"
name: "cpg_iteration_initialize"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpg_iteration_initialize/"
description: "cpg_iteration_initialize – Initialize iterator for members of CPG"
---

<h2 class="name">NAME</h2>
<p> cpg_iteration_initialize &#8211; Initialize iterator for members of CPG</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cpg.h&gt;</code> </p>
<p> <code>cs_error_t cpg_iteration_initialize (cpg_handle_t </code><i>handle</i><code>, cpg_iteration_type_t </code><i>iteration_type</i><code>, const struct cpg_name *</code><i>group</i><code>, cpg_iteration_handle_t *</code><i>cpg_iteration_handle</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cpg_iteration_initialize</code> function is used to initialize iteration of CPG members. The <i>handle</i> argument is connection to CPG database obtained by calling <code><a href="/docs/linux/man/3-cpg_initialize/">cpg_initialize</a>(3)</code> function. <i>iteration_type</i> is used for limit number of returned items and can be one of: </p>
<p> <code>CPG_ITERATION_NAME_ONLY</code> &#8211; only name of used groups are returned </p>
<p> <code>CPG_ITERATION_ONE_GROUP</code> &#8211; only members group with name <i>group</i> are returned </p>
<p> <code>CPG_ITERATION_ALL</code> &#8211; all members are returned </p>
<p> The <i>group</i> parameter is used only with <code>CPG_ITERATION_ONE_GROUP</code> and it&#8217;s name of group with members to iterate. For other <i>iteration_type</i>, this parameter must be NULL. </p>
<p> <code>cpg_iteration_initialize</code> is used only for initialize context for future <code><a href="/docs/linux/man/3-cpg_iteration_next/">cpg_iteration_next</a>(3)</code> calls and handle needed for that function is returned in <i>cpg_iteration_handle</i> variable. When you have finished iteration over objects, call <code><a href="/docs/linux/man/3-cpg_iteration_finalize/">cpg_iteration_finalize</a>(3)</code> function to free up memory associated with iteration. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful. If <i>cpg_iteration_handle</i> is NULL, <code>CS_ERR_INVALID_PARAM</code> error is returned. Same error is returned when <i>iteration_type</i> is <code>CPG_ITERATION_ONE_GROUP</code>, but <i>group</i> is NULL, or when <i>group</i> is not NULL and <i>iteration_type</i> is not <code>CPG_ITERATION_ONE_GROUP</code>. If there is not enough memory for internal store of data, <code>CS_ERR_NO_MEMORY</code> is returned. <code>CS_ERR_BAD_HANDLE</code> can be returned, if <i>handle</i> is not valid handle. </p>
<h2>COMMON IPC ERRORS</h2>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cpg_iteration_next/">cpg_iteration_next</a></code>(3), <code><a href="/docs/linux/man/3-cpg_iteration_finalize/">cpg_iteration_finalize</a></code>(3), <code><a href="/docs/linux/man/3-cpg_initialize/">cpg_initialize</a></code>(3), <code><a href="/docs/linux/man/8-cpg_overview/">cpg_overview</a></code>(8) </p>
<h2>Index</h2>
