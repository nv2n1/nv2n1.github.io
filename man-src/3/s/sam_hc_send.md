---
title: "sam_hc_send(3)"
name: "sam_hc_send"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sam_hc_send/"
description: "sam_hc_send – Send health check confirmation"
---

<p>sam_hc_send &#8211; Send health check confirmation</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/sam.h&gt;
</code></pre>
<p> <code>cs_error_t sam_hc_send (void);</code> </p>
<h2>Description</h2>
<p>The <code>sam_hc_send</code> function is used to send healthcheck confirmation from the applicatoin. This function should be called reguarly when configured for application driven healthchecking, otherwise recovery actoin will be taken. When using event driven healthchecking, this function should not be used. </p>
<h2>Return Value</h2>
<p>This call return CS_OK value if successful, otherwise and error is returned. </p>
<h2>Errors</h2>
<dl>
<dt>CS_ERR_BAD_HANDLE</p>
<dd>health checking is not in running state (<code><a href="/docs/linux/man/3-sam_start/">sam_start</a>(3)</code> has not been executed) or function is called after stop/finalization of SAM. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sam_start/">sam_start</a></code>(3), <code><a href="/docs/linux/man/3-sam_stop/">sam_stop</a></code>(3), <code><a href="/docs/linux/man/3-sam_hc_callback_register/">sam_hc_callback_register</a></code>(3) <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
