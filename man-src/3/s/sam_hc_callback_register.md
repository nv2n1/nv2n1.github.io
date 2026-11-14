---
title: "sam_hc_callback_register(3)"
name: "sam_hc_callback_register"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sam_hc_callback_register/"
description: "sam_hc_callback_register – Register health check callback"
---

<p>sam_hc_callback_register &#8211; Register health check callback</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/sam.h&gt;
</code></pre>
<p> <code>cs_error_t sam_hc_callback_register (sam_hc_callback_t cb);</code> </p>
<h2>Description</h2>
<p>The <code>sam_hc_callback_register</code> function is used to register a user provided healthcheck callback. After calling of this function, the SAM is switched from application driven healthchecking to event driven healthchecking. In this mode, <code><a href="/docs/linux/man/3-sam_hc_send/">sam_hc_send</a>(3)</code> does not need to be executed. The parameter <i>cb</i> is callback function of type <i>sam_hc_callback_t</i> defined as: </p>
<pre> typedef int (*sam_hc_callback_t)(void);</pre>
<p>This function will be regulargly called and must return 0 if the process is functioning normally, or -1 if the process is executing abnormally. When -1 is returned, the SAM server execute the registered recovery policy. A value of NULL can be passed into this function to switch into application driven healthchecking. <i>cb</i> to NULL. </p>
<h2>Return Value</h2>
<p>This call return CS_OK value if successful, otherwise and error is returned. </p>
<h2>Errors</h2>
<dl>
<dt>CS_ERR_BAD_HANDLE</p>
<dd>SAM was not initialized and registered or health checking is in running state</p>
<dt>CS_ERR_LIBRARY</p>
<dd>internal library call failed. This can occur during fork() or pipe () system calls and the errno variable can be read to retrieve more information. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sam_start/">sam_start</a></code>(3), <code><a href="/docs/linux/man/3-sam_stop/">sam_stop</a></code>(3), <code><a href="/docs/linux/man/3-sam_hc_send/">sam_hc_send</a></code>(3), <code><a href="/docs/linux/man/3-sam_register/">sam_register</a></code>(3), <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
