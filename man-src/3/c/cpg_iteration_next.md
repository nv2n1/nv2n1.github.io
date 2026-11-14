---
title: "cpg_iteration_next(3)"
name: "cpg_iteration_next"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpg_iteration_next/"
description: "cpg_iteration_next – Return next item in iteration of CPG"
---

<h2 class="name">NAME</h2>
<p> cpg_iteration_next &#8211; Return next item in iteration of CPG</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cpg.h&gt;</code> </p>
<p> <code>cs_error_t cpg_iteration_next (cpg_iteration_handle_t </code><i>handle</i><code>, struct cpg_iteration_description_t *</code><i>description</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cpg_iter_next</code> function is used to get next value in iteration. The <i>handle</i> argument is iterator handle obtained by <code><a href="/docs/linux/man/3-cpg_iteration_initalize/">cpg_iteration_initalize</a>(3)</code> function. <i>description</i> is pointer to structure with following definition:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
struct cpg_iteration_description_t {
    struct cpg_name group;
    uint32_t nodeid;
    uint32_t pid;
};
</code></pre>
</dl>
<dt>
<dd></dl>
<p> where <code>group</code> is name of group, <code>nodeid</code> is ID of connected node and <code>pid</code> is pid of connected process. If iteration was initialized with <code>CPG_ITERATION_NAME_ONLY</code> iteration type, both <code>nodeid</code> and <code>pid</code> are 0. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful. If there are no more items to iterate, CS_NO_SECTION error code is returned. </p>
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
