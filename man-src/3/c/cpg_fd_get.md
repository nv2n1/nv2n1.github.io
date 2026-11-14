---
title: "cpg_fd_get(3)"
name: "cpg_fd_get"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpg_fd_get/"
description: "cpg_fd_get – Dispatches callbacks from the CPG service"
---

<h2>NAME</h2>
<p> cpg_fd_get &#8211; Dispatches callbacks from the CPG service</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cpg.h&gt;</code> </p>
<p> <code>int cpg_fd_get(cpg_handle_t </code><i>handle</i><code>, int *</code><i>fd</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>cpg_fd_get</code> function is used to retrieve the file descriptor that may be used with the poll system call to determine when <code><a href="/docs/linux/man/3-cpg_dispatch/">cpg_dispatch</a>(3)</code> won&#8217;t block. The <i>handle</i> argument may not be used directly with <code>poll</code> because it is not the file descriptor, but instead an internal identifier used by the CPG library.</p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>ERRORS</h2>
<p> The errors are undocumented.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-cpg_overview/">cpg_overview</a></code>(8), <code><a href="/docs/linux/man/3-cpg_initialize/">cpg_initialize</a></code>(3), <code><a href="/docs/linux/man/3-cpg_finalize/">cpg_finalize</a></code>(3), <code><a href="/docs/linux/man/3-cpg_fd_get/">cpg_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-cpg_dispatch/">cpg_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-cpg_join/">cpg_join</a></code>(3), <code><a href="/docs/linux/man/3-cpg_leave/">cpg_leave</a></code>(3), <code><a href="/docs/linux/man/3-cpg_mcast_joined/">cpg_mcast_joined</a></code>(3), <code><a href="/docs/linux/man/3-cpg_membership_get/">cpg_membership_get</a></code>(3) <code><a href="/docs/linux/man/3-cpg_zcb_alloc/">cpg_zcb_alloc</a></code>(3) <code><a href="/docs/linux/man/3-cpg_zcb_free/">cpg_zcb_free</a></code>(3) <code><a href="/docs/linux/man/3-cpg_zcb_mcast_joined/">cpg_zcb_mcast_joined</a></code>(3) <code><a href="/docs/linux/man/3-cpg_context_get/">cpg_context_get</a></code>(3) <code><a href="/docs/linux/man/3-cpg_context_set/">cpg_context_set</a></code>(3) <code><a href="/docs/linux/man/3-cpg_local_get/">cpg_local_get</a></code>(3) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
