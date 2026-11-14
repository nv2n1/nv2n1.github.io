---
title: "cpg_join(3)"
name: "cpg_join"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cpg_join/"
description: "cpg_join – Joins one or more groups in the CPG library"
---

<h2>NAME</h2>
<p> cpg_join &#8211; Joins one or more groups in the CPG library</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cpg.h&gt;</code> </p>
<p> <code>int cpg_join(cpg_handle_t </code><i>handle</i><code>, struct cpg_name *</code><i>group</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>cpg_join</code> function is used to join one group. When a group is joined, the <code><a href="/docs/linux/man/3-cpg_mcast_joined/">cpg_mcast_joined</a>(3)</code> is called internally to multicast to the groups joined in the argument <i>handle.</i> The process will also get notifications of other processes joining and leaving the group. Messages that are sent to any of the groups joined to the parameter <i>handle</i> will be delivered by <code><a href="/docs/linux/man/3-cpg_dispatch/">cpg_dispatch</a>(3).</code> </p>
<p> This function may be only be called once for each handle. When a group has been joined the process will start to receive callbacks relating to messages sent from members of the group or notifications of processes joining or leaving the group. </p>
<p> Note that more than one process on each node can join a CPG group and each will receive its own copy of any messages sent using <i>cpg_mcast_joined()</i> and its own confchg callback. </p>
<p> The argument <i>group</i> is used to specify the group to join. </p>
<p> The <i>groups</i> argument is of the type struct cpg_name which is defined by the structure: </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre><code>
struct cpg_name {
    int length;
    char value[128];
};
</code></pre>
</dl>
<dt>
<dd></dl>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful, CS_ERR_INVALID_PARAM if the handle is already joined to a group. </p>
<h2>ERRORS</h2>
<p> Not all errors are documented.</p>
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
