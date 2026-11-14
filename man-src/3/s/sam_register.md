---
title: "sam_register(3)"
name: "sam_register"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sam_register/"
description: "sam_rehister – Register component for health checking"
---

<p>sam_rehister &#8211; Register component for health checking</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/sam.h&gt;
</code></pre>
<p> <code>cs_error_t sam_register (unsigned int *</code><i>instance_id</i>); </p>
<h2>Description</h2>
<p>The <code>sam_register</code> function is used to register a process for healthchecking. If recovery policy is set to <i>SAM_RECOVERY_POLICY_RESTART</i> and recovery action will be taken, the new process instance will begin execution at the next code line after this function is called. This function can be called only once and SAM must be initialized by <code><a href="/docs/linux/man/3-sam_initialize/">sam_initialize</a>(3)</code> function. The <i>instance_id</i> argument is a pointer to a value storing the current iteration instance. If this parameter is NULL, no <i>instance_id</i> is returned. and then, no <i>instance_id</i> will be returned. This value starts at 0 for the first iteration instance, and increases by 1 each time a recovery restart is executed. After reaching MAX_INT, the instance_id will reset to 0. The placement of this function is important because after it is called, the process id will change. After registration, event driven health checking is not running. </p>
<h2>Return Value</h2>
<p>This call return CS_OK value if successful, otherwise and error is returned. </p>
<h2>Errors</h2>
<dl>
<dt>CS_ERR_BAD_HANDLE</p>
<dd>health checking was not started by calling <code><a href="/docs/linux/man/3-sam_start/">sam_start</a>(3)</code> function.</p>
<dt>CS_ERR_LIBRARY</p>
<dd>internal library call failed. This can be one of pipe creation or fork. It&#8217;s possible to get more information from errno. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sam_start/">sam_start</a></code>(3), <code><a href="/docs/linux/man/3-sam_initialize/">sam_initialize</a></code>(3), <code><a href="/docs/linux/man/3-sam_hc_callback_register/">sam_hc_callback_register</a></code>(3) <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
