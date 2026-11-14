---
title: "sam_finalize(3)"
name: "sam_finalize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sam_finalize/"
description: "sam_finalize – Terminate SAM service"
---

<p>sam_finalize &#8211; Terminate SAM service</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/sam.h&gt;
</code></pre>
<p> <code>cs_error_t sam_finalize (void);</code> </p>
<h2>Description</h2>
<p>The <code>sam_finalize</code> function is used to terminate SAM API. Once the connection is finalized, the SAM may not be used again by application. Whole functionality (health checking) will be stopped and after application fail, recovery action will not be taken. </p>
<h2>Return Value</h2>
<p>This call return CS_OK value if successful, otherwise and error is returned. </p>
<h2>Errors</h2>
<dl>
<dt>CS_ERR_BAD_HANDLE</p>
<dd>library was not initialized by <code><a href="/docs/linux/man/3-sam_init/">sam_init</a>(3)</code> function or was finished already. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sam_initialize/">sam_initialize</a></code>(3) <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
