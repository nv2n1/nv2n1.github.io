---
title: "votequorum_qdevice_unregister(3)"
name: "votequorum_qdevice_unregister"
section: "3"
letter: "v"
url: "/docs/linux/man/3-votequorum_qdevice_unregister/"
description: "votequorum_qdevice_unregister – Unregisters a new quorum device"
---

<p>votequorum_qdevice_unregister &#8211; Unregisters a new quorum device</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/votequorum.h&gt;
int votequorum_qdevice_unregister(votequorum_handle_t handle, const char *name);</code></pre>
<h2>Description</h2>
<p>The <code>votequorum_qdevice_unregister</code> unregisters a quorum device. Any votes it had will be removed from the cluster. NOTE that this could make the cluster inquorate.</p>
<h2>Return Value</h2>
<p>This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>Errors</h2>
<p><code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-votequorum_overview/">votequorum_overview</a></code>(8), <code><a href="/docs/linux/man/3-votequorum_initialize/">votequorum_initialize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_finalize/">votequorum_finalize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_getinfo/">votequorum_getinfo</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstart/">votequorum_trackstart</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstop/">votequorum_trackstop</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_fd_get/">votequorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_dispatch/">votequorum_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_set/">votequorum_context_set</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_get/">votequorum_context_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setexpected/">votequorum_setexpected</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setvotes/">votequorum_setvotes</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_register/">votequorum_qdevice_register</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_poll/">votequorum_qdevice_poll</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_update/">votequorum_qdevice_update</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_master_wins/">votequorum_qdevice_master_wins</a></code>(3) </p>
