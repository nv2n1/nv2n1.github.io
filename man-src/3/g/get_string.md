---
title: "get_string(3)"
name: "get_string"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_string/"
description: "get_string — retrieve a string from a dirfile database"
---

<h2>NAME</h2>
<p> get_string &#8212; retrieve a string from a dirfile database</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>size_t get_string(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>size_t </code><i>len</i><code>, char *</code><i>data_out</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_string</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> for the string scalar <i>field_code</i>, which should not contain a representation suffix. The first <i>len</i> characters of the string scalar are stored in the user-supplied buffer <i>data_out</i>. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<p> If <i>len</i> equals zero, or if <i>data_out</i> equals NULL, no data will be copied to <i>data_out</i>, but the length of the string scalar will still be returned by <code>get_string</code>(). Otherwise, the argument <i>data_out</i> must point to a valid memory location of sufficient size to hold at least <i>len</i> characters. If the length of the string scalar is greater than <i>len</i>, <i>data_out</i> will not be NULL-terminated.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>get_string</code>() returns the actual length of the specified string scalar, including the trailing NULL character. A return value greater than <i>len</i> indicates that the output string is not null terminated. </p>
<p> On error, it returns 0 and sets the dirfile error to a non-zero value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> was not found in the database.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> An invalid <i>dirfile</i> was supplied.</p>
<dt><code>GD_E_BAD_FIELD_TYPE</code></p>
<dd> The supplied <i>field_code</i> referred to a field of type other than <code>STRING</code>. The caller should use <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), or <code><a href="/docs/linux/man/3-get_constant/">get_constant</a></code>(3) instead.</p>
<dt><code>GD_E_BAD_TYPE</code></p>
<dd> An invalid <i>return_type</i> was specified.</p>
<dt><code>GD_E_INTERNAL_ERROR</code></p>
<dd> An internal error occurred in the library while trying to perform the task. This indicates a bug in the library. Please report the incident to the maintainer. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered may be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-put_string/">put_string</a></code>(3) </p>
<h2>Index</h2>
