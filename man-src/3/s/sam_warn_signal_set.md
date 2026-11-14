---
title: "sam_warn_signal_set(3)"
name: "sam_warn_signal_set"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sam_warn_signal_set/"
description: "sam_warn_signal_set – Set warn signal"
---

<p>sam_warn_signal_set &#8211; Set warn signal</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/sam.h&gt;
</code></pre>
<p> <code>cs_error_t sam_warn_signal_set (int warn_signal);</code> </p>
<h2>Description</h2>
<p>The <code>sam_warn_signal_set</code> function is used to configure warning signal sent before real killing of unresponsive application. Default value is SIGTERM. SIGKILL can be used to emulate &quot;not warning signal send&quot; behaviour. </p>
<h2>Return Value</h2>
<p>This call return CS_OK value if successful, otherwise and error is returned. </p>
<h2>Errors</h2>
<dl>
<dt>CS_ERR_BAD_HANDLE</p>
<dd>component was not initialized by calling <code><a href="/docs/linux/man/3-sam_initialize/">sam_initialize</a>(3)</code> or it was finalized. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sam_initialize/">sam_initialize</a></code>(3) <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
