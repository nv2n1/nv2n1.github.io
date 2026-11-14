---
title: "sam_data_restore(3)"
name: "sam_data_restore"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sam_data_restore/"
description: "sam_data_restore – Restore previously saved user data"
---

<p>sam_data_restore &#8211; Restore previously saved user data</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/sam.h&gt;
</code></pre>
<p> <code>cs_error_t sam_data_restore (void *</code><i>data</i><code>, size_t </code><i>size</i><code>);</code> </p>
<h2>Description</h2>
<p>The <code>sam_data_restore</code> function is used to restore data, previously saved by calling <code><a href="/docs/linux/man/3-sam_data_store/">sam_data_store</a>(3)</code>. Such data survives between instances. The <i>data</i> parameter is pointer to memory initialized by caller. Stored data are copied there. This also means, that caller is responsible for freeing memory. The <i>size</i> parameter is length of <i>data</i>. This one must be at least same length as previously stored data otherwise error is returned. Parameter can be larger but only stored data size bytes are changed. Use <code><a href="/docs/linux/man/3-sam_data_getsize/">sam_data_getsize</a>(3)</code> to find out length of stored data. </p>
<h2>Return Value</h2>
<p>This call return CS_OK value if successful, otherwise and error is returned. </p>
<h2>Errors</h2>
<dl>
<dt>CS_ERR_BAD_HANDLE</p>
<dd>component was not initialized by calling <code><a href="/docs/linux/man/3-sam_initialize/">sam_initialize</a>(3)</code> or it was finalized.</p>
<dt>CS_ERR_INVALID_PARAM</p>
<dd>data parameter is NULL or size is less then currently stored data length </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sam_data_getsize/">sam_data_getsize</a></code>(3), <code><a href="/docs/linux/man/3-sam_data_store/">sam_data_store</a></code>(3) <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
