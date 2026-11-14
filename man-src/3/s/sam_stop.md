---
title: "sam_stop(3)"
name: "sam_stop"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sam_stop/"
description: "sam_stop – Stop health checking"
---

<p>sam_stop &#8211; Stop health checking</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/sam.h&gt;
</code></pre>
<p> <code>cs_error_t sam_stop (void);</code> </p>
<h2>Description</h2>
<p>The <code>sam_stop</code> function is used to stop health checking of an active process. After calling this function, the application no longer should send helathchecks. In the case of event driven healthchecking, the healthchecking thread will be stopped. A process can always start health checking again by calling <code><a href="/docs/linux/man/3-sam_start/">sam_start</a>(3)</code> function. </p>
<h2>Return Value</h2>
<p>This call return CS_OK value if successful, otherwise and error is returned. </p>
<h2>Errors</h2>
<dl>
<dt>CS_ERR_BAD_HANDLE</p>
<dd>health checking was not started by calling <code><a href="/docs/linux/man/3-sam_start/">sam_start</a>(3)</code> function. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sam_start/">sam_start</a></code>(3) <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
