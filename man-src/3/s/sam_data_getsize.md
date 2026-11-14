---
title: "sam_data_getsize(3)"
name: "sam_data_getsize"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sam_data_getsize/"
description: "sam_data_getsize – Return size of stored data in bytes"
---

<p>sam_data_getsize &#8211; Return size of stored data in bytes</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/sam.h&gt;
</code></pre>
<p> <code>cs_error_t sam_data_getsize (size_t *</code><i>size</i><code>);</code> </p>
<h2>Description</h2>
<p>The <code>sam_data_getsize</code> function is used to return size of stored data. Size is returned in bytes. If user data is NULL, zero is returned. Function is intended to be used before <code><a href="/docs/linux/man/3-sam_data_restore/">sam_data_restore</a>(3)</code> call to properly allocate buffer for restored data. </p>
<h2>Return Value</h2>
<p>This call return CS_OK value if successful, otherwise and error is returned. </p>
<h2>Errors</h2>
<dl>
<dt>CS_ERR_BAD_HANDLE</p>
<dd>component was not initialized by calling <code><a href="/docs/linux/man/3-sam_initialize/">sam_initialize</a>(3)</code> or it was finalized.</p>
<dt>CS_ERR_INVALID_PARAM</p>
<dd>size parameter is NULL </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sam_data_store/">sam_data_store</a></code>(3), <code><a href="/docs/linux/man/3-sam_data_restore/">sam_data_restore</a></code>(3) <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
