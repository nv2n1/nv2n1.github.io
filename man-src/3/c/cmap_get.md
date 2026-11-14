---
title: "cmap_get(3)"
name: "cmap_get"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cmap_get/"
description: "cmap_get – Retrieve value from CMAP"
---

<h2 class="name">NAME</h2>
<p> cmap_get &#8211; Retrieve value from CMAP</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;corosync/cmap.h&gt;</code> </p>
<p> <code>cs_error_t cmap_get (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, void *</code><i>value</i><code>, size_t *</code><i>value_len</i><code>, cmap_value_types_t *</code><i>type</i><code>);</code> </p>
<p> Also shortcuts for different types are defined </p>
<p> <code>cs_error_t cmap_get_int8 (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, int8_t *</code><i>i8</i><code>);</code> </p>
<p> <code>cs_error_t cmap_get_uint8 (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, uint8_t *</code><i>u8</i><code>);</code> </p>
<p> <code>cs_error_t cmap_get_int16 (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, int16_t *</code><i>i16</i><code>);</code> </p>
<p> <code>cs_error_t cmap_get_uint16 (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, uint16_t *</code><i>u16</i><code>);</code> </p>
<p> <code>cs_error_t cmap_get_int32 (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, int32_t *</code><i>i32</i><code>);</code> </p>
<p> <code>cs_error_t cmap_get_uint32 (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, uint32_t *</code><i>u32</i><code>);</code> </p>
<p> <code>cs_error_t cmap_get_int64 (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, int64_t *</code><i>i64</i><code>);</code> </p>
<p> <code>cs_error_t cmap_get_uint64 (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, uint64_t *</code><i>u64</i><code>);</code> </p>
<p> <code>cs_error_t cmap_get_float (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, float *</code><i>flt</i><code>);</code> </p>
<p> <code>cs_error_t cmap_get_double (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, double *</code><i>dbl</i><code>);</code> </p>
<p> <code>cs_error_t cmap_get_string (cmap_handle_t </code><i>handle</i><code>, const char *</code><i>key_name</i><code>, char **</code><i>str</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>cmap_get</code> function is used to retrieve key from cmap previously set by <code><a href="/docs/linux/man/3-cmap_set/">cmap_set</a>(3)</code> function. The <i>handle</i> argument is connection to CMAP database obtained by calling <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a>(3)</code> function. <i>key_name</i> is name of key to get value from. <i>value</i> is pointer to preallocated data used as storage for data, but can be also NULL, and then only <i>value_len</i> and/or <i>type</i> is returned (both of them can also be NULL, allowing function to be used only for test of existence of key). If <i>value</i> is not NULL, actual length of value in map is checked against <i>*value_len.</i> If <i>*value_len</i> is shorter then length of value in map, error CS_ERR_INVALID_PARAM is returned. After successful copy of value, <i>*value_len</i> is set to actual length of value in map. Parameter <i>type</i> is pointer to memory, where type of value is stored after successful return. Pointer can also be NULL and then nothing is stored. Type can be one of: </p>
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
<p> Sortcut functions tests cmap type with it&#8217;s own type. If type didn&#8217;t match, CS_ERR_INVALID_PARAM error is returned. No conversions are done, so for example <code>cmap_get_int16</code> is not able to return value with <code>CMAP_VALUETYPE_INT8</code> type. </p>
<p> String shortcut function returns newly allocated memory and caller is responsible for freeing that. </p>
<h2>RETURN VALUE</h2>
<p> This call returns the CS_OK value if successful. If value or key_name are unspecified, CS_ERR_INVALID_PARAM is returned. Same error is also returned if <i>value</i> is specified, and <i>*value_len</i> is too short for store of data. If key doesn&#8217;t exists (it was not set by calling <code><a href="/docs/linux/man/3-cmap_set/">cmap_set</a>(3)</code> function first) CS_ERR_NOT_EXIST error is returned. For helper functions, CS_ERR_INVALID_PARAM is returned if type stored in cmap doesn&#8217;t match with type of helper function. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-cmap_set/">cmap_set</a></code>(3), <code><a href="/docs/linux/man/3-cmap_initialize/">cmap_initialize</a></code>(3), <code><a href="/docs/linux/man/8-cmap_overview/">cmap_overview</a></code>(8) </p>
<p> <code>CS_ERR_TRY_AGAIN</code> Resource temporarily unavailable </p>
<p> <code>CS_ERR_INVALID_PARAM</code> Invalid argument </p>
<p> <code>CS_ERR_ACCESS</code> Permission denied </p>
<p> <code>CS_ERR_LIBRARY</code> The connection failed </p>
<p> <code>CS_ERR_INTERRUPT</code> System call inturrupted by a signal </p>
<p> <code>CS_ERR_NOT_SUPPORTED</code> The requested protocol/functuality not supported </p>
<p> <code>CS_ERR_MESSAGE_ERROR</code> Incorrect auth message received </p>
<p> <code>CS_ERR_NO_MEMORY</code> Not enough memory to completed the requested task </p>
<h2>Index</h2>
