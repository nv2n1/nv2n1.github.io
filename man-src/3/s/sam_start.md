---
title: "sam_start(3)"
name: "sam_start"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sam_start/"
description: "sam_start – Start health checking"
---

<p>sam_start &#8211; Start health checking</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/sam.h&gt;
</code></pre>
<p> <code>cs_error_t sam_start (void);</code> </p>
<h2>Description</h2>
<p>The <code>sam_start</code> function is used to start health checking of application. After calling this function, the active process needs to send healthchecks within the registered time interval by calling <code><a href="/docs/linux/man/3-sam_hc_send/">sam_hc_send</a>(3)</code>. If event driven healthchecking is configured by calling <code><a href="/docs/linux/man/3-sam_register/">sam_register</a>(3)</code>, an internal thread will be created and send health check confirmations four times per <i>time_interval</i>. Application must be registered by calling <code><a href="/docs/linux/man/3-sam_register/">sam_register</a>(3)</code> before this function can be called. An application can always stop health checking by calling the <code><a href="/docs/linux/man/3-sam_stop/">sam_stop</a>(3)</code> function. If SAM is initialized with quorum policy <i>SAM_RECOVERY_POLICY_QUIT</i> or <i>SAM_RECOVERY_POLICY_RESTART</i> <code>sam_start</code> will block until corosync becomes quorate. </p>
<h2>Return Value</h2>
<p>This call return CS_OK value if successful, otherwise and error is returned. If SAM is initialized with quorum policy, returned error can also be quorum error. </p>
<h2>Errors</h2>
<dl>
<dt>CS_ERR_BAD_HANDLE</p>
<dd>component was not registered by calling <code><a href="/docs/linux/man/3-sam_register/">sam_register</a>(3)</code> function. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sam_hc_send/">sam_hc_send</a></code>(3), <code><a href="/docs/linux/man/3-sam_stop/">sam_stop</a></code>(3), <code><a href="/docs/linux/man/3-sam_register/">sam_register</a></code>(3), <code><a href="/docs/linux/man/3-sam_hc_callback_register/">sam_hc_callback_register</a></code>(3) <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
