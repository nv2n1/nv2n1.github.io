---
title: "cmap_set(3)"
name: "cmap_set"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmap_set/"
description: "cmap_set – Store value in CMAP"
---

<h2 class="name">NAME</h2>
<p> cmap_set &#8211; Store value in CMAP</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cmap.h&gt;</code> </p>
<p> <code>cs_error_t cmap_set (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, const void *</code><i>value</i><code>, size_t </code><i>value_len</i><code>, cmap_value_types_t </code><i>type</i><code>);</code> </p>
<p> Also shortcuts for different types are defined </p>
<p> <code>cs_error_t cmap_set_int8(cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, int8_t </code><i>value</i><code>);</code> </p>
<p> <code>cs_error_t cmap_set_uint8(cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, uint8_t </code><i>value</i><code>);</code> </p>
<p> <code>cs_error_t cmap_set_int16(cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, int16_t </code><i>value</i><code>);</code> </p>
<p> <code>cs_error_t cmap_set_uint16(cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, uint16_t </code><i>value</i><code>);</code> </p>
<p> <code>cs_error_t cmap_set_int32(cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, int32_t </code><i>value</i><code>);</code> </p>
<p> <code>cs_error_t cmap_set_uint32(cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, uint32_t </code><i>value</i><code>);</code> </p>
<p> <code>cs_error_t cmap_set_int64(cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, int64_t </code><i>value</i><code>);</code> </p>
<p> <code>cs_error_t cmap_set_uint64(cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, uint64_t </code><i>value</i><code>);</code> </p>
<p> <code>cs_error_t cmap_set_float(cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, float </code><i>value</i><code>);</code> </p>
<p> <code>cs_error_t cmap_set_double(cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, double </code><i>value</i><code>);</code> </p>
<p> <code>cs_error_t cmap_set_string(cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, const char *</code><i>value</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cmap_set</code> function is used to store key inside cmap. The <i>handle</i> argument is connection to CMAP database obtained by calling <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a>(3)</code> function. <i>key_name</i> is name of key to set value. Key name is limited by minimal (CMAP_KEYNAME_MINLEN, currently 3) and maximal (CMAP_KEYNAME_MAXLEN, currently 255) length. Also key can contain only limited set of characters expressed by regexp [a-zA-Z0-9._-/:]*. <i>value</i> is pointer to allocated data which will be stored inside CMAP. Length of value (number of bytes) is supplied as <i>value_len</i> parameter. Last parameter is <i>type</i> which gives type of value. It may be one of: </p>
<p> <code>CMAP_VALUETYPE_INT8</code> &#8211; 8-bit signed integer </p>
<p> <code>CMAP_VALUETYPE_UINT8</code> &#8211; 8-bit unsigned integer </p>
<p> <code>CMAP_VALUETYPE_INT16</code> &#8211; 16-bit signed integer </p>
<p> <code>CMAP_VALUETYPE_UINT16</code> &#8211; 16-bit unsigned integer </p>
<p> <code>CMAP_VALUETYPE_INT32</code> &#8211; 32-bit signed integer </p>
<p> <code>CMAP_VALUETYPE_UINT32</code> &#8211; 32-bit unsigned integer </p>
<p> <code>CMAP_VALUETYPE_INT64</code> &#8211; 64-bit signed integer </p>
<p> <code>CMAP_VALUETYPE_UINT64</code> &#8211; 64-bit unsigned integer </p>
<p> <code>CMAP_VALUETYPE_FLOAT</code> &#8211; Float value </p>
<p> <code>CMAP_VALUETYPE_DOUBLE</code> &#8211; Double value </p>
<p> <code>CMAP_VALUETYPE_STRING</code> &#8211; C-style string </p>
<p> <code>CMAP_VALUETYPE_BINARY</code> &#8211; Binary data, byte with zero value has no special meaning </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful. If value or key_name are unspecified, CS_ERR_INVALID_PARAM is returned. Too short or too long key_name returns CS_ERR_NAME_TOO_LONG error code. Some of keys may be tagged read-only directly in corosync and seting such key will result in CS_ERR_ACCESS error. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cmap_get/">cmap_get</a></code>(3), <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a></code>(3), <code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
