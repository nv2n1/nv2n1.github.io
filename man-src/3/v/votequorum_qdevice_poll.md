---
title: "votequorum_qdevice_poll(3)"
name: "votequorum_qdevice_poll"
section: "3"
letter: "v"
url: "/docs/linux/man/3-votequorum_qdevice_poll/"
description: "votequorum_qdevice_poll – Tells votequorum the result of the quorum device poll"
---

<p>votequorum_qdevice_poll &#8211; Tells votequorum the result of the quorum device poll</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/votequorum.h&gt;
int votequorum_qdevice_poll(votequorum_handle_t handle, const char *name, unsigned int cast_vote, votequorum_ring_id_t ring_id);</code></pre>
<h2>Description</h2>
<p>The <code>votequorum_qdevice_poll</code> is called by the quorum device subsystem (not provided as part of votequorum) to tell the voting system if the quorum device is present/active or not. If <code>cast_vote</code> is 1 then the votes for the device are included in the quorum calculation, otherwise not. Current <code>ring_id</code> must be set (one get in votequorum_notification_fn callback) otherwise poll is ignored. This routine should be called at regular intervals to ensure that the device status is always known to votequorum. If <code>votequorum_qdevice_poll</code> is not called for (default) 10 seconds (or 30 seconds for sync phase) then the device will be deemed to be dead and its votes removed from the cluster. This does not unregister the device. The default poll time can be changed by setting the cmap variable <code>quorum.device.timeout</code> for normal operation or <code>quorum.device.sync_timeout</code> for synchronization phase.</p>
<h2>Return Value</h2>
<p>This call returns the CS_OK value if successful, otherwise an error is returned. </p>
<h2>Errors</h2>
<p><code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-votequorum_overview/">votequorum_overview</a></code>(8), <code><a href="/docs/linux/man/3-votequorum_initialize/">votequorum_initialize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_finalize/">votequorum_finalize</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_getinfo/">votequorum_getinfo</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstart/">votequorum_trackstart</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_trackstop/">votequorum_trackstop</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_fd_get/">votequorum_fd_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_dispatch/">votequorum_dispatch</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_set/">votequorum_context_set</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_context_get/">votequorum_context_get</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setexpected/">votequorum_setexpected</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_setvotes/">votequorum_setvotes</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_register/">votequorum_qdevice_register</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_unregister/">votequorum_qdevice_unregister</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_update/">votequorum_qdevice_update</a></code>(3), <code><a href="/docs/linux/man/3-votequorum_qdevice_master_wins/">votequorum_qdevice_master_wins</a></code>(3), </p>
