---
title: "votequorum_qdevice_master_wins(3)"
name: "votequorum_qdevice_master_wins"
section: "3"
letter: "v"
url: "/docs/linux/man/3-votequorum_qdevice_master_wins/"
description: "votequorum_qdevice_master_wins – Sets or clears quorum device master_wins flag"
---

<p>votequorum_qdevice_master_wins &#8211; Sets or clears quorum device master_wins flag</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/votequorum.h&gt;
int votequorum_qdevice_master_wins(votequorum_handle_t handle const char name, unsigned int allow);</code></pre>
<h2>Description</h2>
<p>The <code>votequorum_qdevice_master_wins</code> informs votequorum whether or not the currently registered qdevice subsystem supports &#8216;master_wins&#8217; mode (default 0). This mode allows the qdevice to effectively take over the quorum calculations of votequorum. Any node with an active qdevice that also has master_wins set becomes quorate regardless of the node votes of the cluster. It is left up to the qdevice subsystem itself (not part of votequorum) to communicate across the nodes or otherwise provide some system of deciding which nodes will be part of the quorate cluster, if any. eg They may be the set of nodes that has access to a quorum disk.<br />
 <code>name</code> The name of the currently registered quorum device on this node. This must match the existing name known to votequorum.<br />
 <code>allow</code> 0 (the default) means that master_wins is not active on this node. 1 means that master_wins is active on this node.</p>
<h2>Return Value</h2>
<p>This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>Errors</h2>
<p><code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-votequorum_overview/">votequorum_overview</a></code>(8), <code><a href="/docs/linux/man/3-votequorum_initialize/">votequorum_initialize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_finalize/">votequorum_finalize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_getinfo/">votequorum_getinfo</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstart/">votequorum_trackstart</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstop/">votequorum_trackstop</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_fd_get/">votequorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_dispatch/">votequorum_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_set/">votequorum_context_set</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_get/">votequorum_context_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setexpected/">votequorum_setexpected</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setvotes/">votequorum_setvotes</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_register/">votequorum_qdevice_register</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_poll/">votequorum_qdevice_poll</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_update/">votequorum_qdevice_update</a></code>(3), </p>
