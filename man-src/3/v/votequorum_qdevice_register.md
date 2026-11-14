---
title: "votequorum_qdevice_register(3)"
name: "votequorum_qdevice_register"
section: "3"
letter: "v"
url: "/docs/linux/man/3-votequorum_qdevice_register/"
description: "votequorum_qdevice_register – Registers a new quorum device"
---

<p>votequorum_qdevice_register &#8211; Registers a new quorum device</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/votequorum.h&gt;
int votequorum_qdevice_register(votequorum_handle_t handle, const char *name);</code></pre>
<h2>Description</h2>
<p>The <code>votequorum_qdevice_register</code> is used to register a new quorum device. A quorum device is an external way of adding votes to a small cluster. The quorum device is, in effect, a pseudo node in the cluster that provide votes based on some external device, usually a shared disk partition or perhaps a network router.<br />
 This call creates the device but does not mark it active. <code>votequorum_qdevice_poll</code> must be called for the votes to be included in the quorum calculation.<br />
 <code>name</code> is string containing an informative name for the quorum device. It is simply stored by votequorum and used in the display of corosync-quorumtool, it can be a maximum of 254 characters.<br />
 The number of votes contributed by the quorum device is already known to votequorum, it is set in cmap quorum.device.votes and not by the device.<br />
 Note that it is the responsibility of the quorum device subsystem (not provided as part of votequorum) to keep all nodes informed of the quorum device status.</p>
<h2>Return Value</h2>
<p>This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>Errors</h2>
<p><code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-votequorum_overview/">votequorum_overview</a></code>(8), <code><a href="/docs/linux/man/3-votequorum_initialize/">votequorum_initialize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_finalize/">votequorum_finalize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_getinfo/">votequorum_getinfo</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstart/">votequorum_trackstart</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstop/">votequorum_trackstop</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_fd_get/">votequorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_dispatch/">votequorum_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_set/">votequorum_context_set</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_get/">votequorum_context_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setexpected/">votequorum_setexpected</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setvotes/">votequorum_setvotes</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_unregister/">votequorum_qdevice_unregister</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_poll/">votequorum_qdevice_poll</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_update/">votequorum_qdevice_update</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_master_wins/">votequorum_qdevice_master_wins</a></code>(3) </p>
