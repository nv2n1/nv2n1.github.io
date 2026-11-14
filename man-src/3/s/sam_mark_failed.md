---
title: "sam_mark_failed(3)"
name: "sam_mark_failed"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sam_mark_failed/"
description: "sam_mark_failed – Mark process failed"
---

<p>sam_mark_failed &#8211; Mark process failed</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/sam.h&gt;
</code></pre>
<p> <code>cs_error_t sam_mark_failed (void);</code> </p>
<h2>Description</h2>
<p>The <code>sam_mark_failed</code> function is used with SAM_RECOVERY_POLICY_CMAP mostly together with SAM_RECOVERY_POLICY_RESTART to mark process failed. Process marked failed is killed without sending warn signal and control process will exit as with SAM_RECOVERY_POLICY_QUIT policy. Condb key state will be set to failed so corosync watchdog can take required action. </p>
<h2>Return Value</h2>
<p>This call return CS_OK value if successful, otherwise and error is returned. </p>
<h2>Errors</h2>
<dl>
<dt>CS_ERR_BAD_HANDLE</p>
<dd>library was not initialized by calling <code><a href="/docs/linux/man/3-sam_initialize/">sam_initialize</a>(3)</code> or was already finalized</p>
<dt>CS_ERR_INVALID_PARAM</p>
<dd>recovery policy doesn&#8217;t has SAM_RECOVERY_POLICY_CMAP flag set</p>
<dt>CS_ERR_LIBRARY</p>
<dd>some internal error appeared (communication with parent process) </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sam_initialize/">sam_initialize</a></code>(3) <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
