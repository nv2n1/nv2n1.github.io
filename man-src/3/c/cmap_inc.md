---
title: "cmap_inc(3)"
name: "cmap_inc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmap_inc/"
description: "cmap_inc – Increase already stored value in CMAP"
---

<h2 class="name">NAME</h2>
<p> cmap_inc &#8211; Increase already stored value in CMAP</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cmap.h&gt;</code> </p>
<p> <code>cs_error_t cmap_inc (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cmap_inc</code> function is used to increase integer value of already stored key inside cmap. The <i>handle</i> argument is connection to CMAP database obtained by calling <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a>(3)</code> function. <i>key_name</i> is name of key to increase value of. </p>
<p> Function is defined only on values where increase makes sense and is well defined, so it can be one of: </p>
<p> <code>CMAP_VALUETYPE_INT8</code> &#8211; 8-bit signed integer </p>
<p> <code>CMAP_VALUETYPE_UINT8</code> &#8211; 8-bit unsigned integer </p>
<p> <code>CMAP_VALUETYPE_INT16</code> &#8211; 16-bit signed integer </p>
<p> <code>CMAP_VALUETYPE_UINT16</code> &#8211; 16-bit unsigned integer </p>
<p> <code>CMAP_VALUETYPE_INT32</code> &#8211; 32-bit signed integer </p>
<p> <code>CMAP_VALUETYPE_UINT32</code> &#8211; 32-bit unsigned integer </p>
<p> <code>CMAP_VALUETYPE_INT64</code> &#8211; 64-bit signed integer </p>
<p> <code>CMAP_VALUETYPE_UINT64</code> &#8211; 64-bit unsigned integer </p>
<p> Overflow/underflow is not detected and it&#8217;s ignored. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful. If value or key_name are unspecified, CS_ERR_INVALID_PARAM is returned. CS_ERR_NOT_EXIST error is returned if key doesn&#8217;t exist (wasn&#8217;t created by calling <code><a href="/docs/linux/man/3-cmap_set/">cmap_set</a>(3)</code> first). Some of keys may be tagged read-only directly in corosync and seting such key will result in CS_ERR_ACCESS error. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cmap_get/">cmap_get</a></code>(3), <code><a href="/docs/linux/man/3-cmap_set/">cmap_set</a></code>(3), <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a></code>(3), <code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
