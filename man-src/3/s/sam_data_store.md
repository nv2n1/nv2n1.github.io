---
title: "sam_data_store(3)"
name: "sam_data_store"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sam_data_store/"
description: "sam_data_store – Store user data"
---

<p>sam_data_store &#8211; Store user data</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;corosync/sam.h&gt;
</code></pre>
<p> <code>cs_error_t sam_data_store (const void *</code><i>data</i><code>, size_t </code><i>size</i><code>);</code> </p>
<h2>Description</h2>
<p>The <code>sam_data_store</code> function is used to store data, which survives between instances. The <i>data</i> parameter is pointer to memory with data to store. Data are stored in newly allocated memory inside library, so caller can safely remove them after call of function. You can use NULL as parameter to remove and free previously saved data. In this case <i>size</i> argument is ignored. The <i>size</i> parameter is length of <i>data</i>. Use <code><a href="/docs/linux/man/3-sam_data_getsize/">sam_data_getsize</a>(3)</code> to find out length of stored data and <code><a href="/docs/linux/man/3-sam_data_restore/">sam_data_restore</a>(3)</code> to restore stored data. </p>
<h2>Return Value</h2>
<p>This call return CS_OK value if successful, otherwise and error is returned. </p>
<h2>Errors</h2>
<dl>
<dt>CS_ERR_BAD_HANDLE</p>
<dd>component was not initialized by calling <code><a href="/docs/linux/man/3-sam_initialize/">sam_initialize</a>(3)</code> or it was finalized.</p>
<dt>CS_ERR_NO_MEMORY</p>
<dd>internal malloc/realloc failed because data are too large</p>
<dt>CS_ERR_LIBRARY</p>
<dd>some internal error appeared (mostly because communication with parent process failed) </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-sam_data_getsize/">sam_data_getsize</a></code>(3), <code><a href="/docs/linux/man/3-sam_data_restore/">sam_data_restore</a></code>(3) <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable <code>CS_ERR_INVALID_PARAM</code> Invalid argument <code>CS_ERR_ACCESS</code> Permission denied <code>CS_ERR_LIBRARY</code> The connection failed <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
