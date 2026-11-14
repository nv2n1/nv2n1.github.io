---
title: "get_constant(3)"
name: "get_constant"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_constant/"
description: "get_constant — retrieve a scalar constant from a dirfile database"
---

<h2>NAME</h2>
<p> get_constant &#8212; retrieve a scalar constant from a dirfile database</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int get_constant(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>gd_type_t </code><i>return_type</i><code>, void *</code><i>data_out</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_constant</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> for the <code>CONST</code> scalar <i>field_code</i>, which may contain a representation suffix. The constant is converted to the data type specified by <i>return_type</i>, and stored in the user-supplied buffer <i>data_out</i>. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). The argument <i>data_out</i> must point to a valid memory location of sufficient size to hold a value of the return type specified. </p>
<p> The <i>return_type</i> argument should be one of the following symbols, which indicates the desired return type of the data:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>GD_UINT8</i></p>
<dd> unsigned 8-bit integer</p>
<dt><i>GD_INT8</i></p>
<dd> signed (two&#8217;s complement) 8-bit integer</p>
<dt><i>GD_UINT16</i></p>
<dd> unsigned 16-bit integer</p>
<dt><i>GD_INT16</i></p>
<dd> signed (two&#8217;s complement) 16-bit integer</p>
<dt><i>GD_UINT32</i></p>
<dd> unsigned 32-bit integer</p>
<dt><i>GD_INT32</i></p>
<dd> signed (two&#8217;s complement) 32-bit integer</p>
<dt><i>GD_UINT64</i></p>
<dd> unsigned 64-bit integer</p>
<dt><i>GD_INT64</i></p>
<dd> signed (two&#8217;s complement) 64-bit integer</p>
<dt><i>GD_FLOAT32</i></p>
<dd> IEEE-754 standard 32-bit single precision floating point number</p>
<dt><i>GD_FLOAT64</i></p>
<dd> IEEE-754 standard 64-bit double precision floating point number</p>
<dt><i>GD_COMPLEX64</i></p>
<dd> C99-conformant 64-bit single precision complex number</p>
<dt><i>GD_COMPLEX128</i></p>
<dd> C99-conformant 128-bit double precision complex number</p>
<dt><i>GD_NULL</i></p>
<dd> the null type: the database is queried as usual, but no data is returned. In this case, <i>data_out</i> is ignored and may be NULL.</dl>
</dl>
<p> The return type of the constant need not be the same as the type of the data stored in the database. Type conversion will be performed as necessary to return the requested type. If the <i>field_code</i> does not indicate a representation, but conversion from a complex value to a purely real one is required, only the real portion of the requested vector will be returned.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>get_constant</code>() returns zero. On error, it returns -1 and sets the dirfile error to a non-zero value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> was not found in the database.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> An invalid <i>dirfile</i> was supplied.</p>
<dt><code>GD_E_BAD_FIELD_TYPE</code></p>
<dd> The supplied <i>field_code</i> referred to a field of a type other than <code>CONST</code>. The caller should use <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), or <code><a href="/docs/linux/man/3-get_string/">get_string</a></code>(3) instead.</p>
<dt><code>GD_E_BAD_REPR</code></p>
<dd> The representation suffix specified in <i>field</i>code<i>,</i> or in one of the field codes it uses for input, was invalid.</p>
<dt><code>GD_E_BAD_TYPE</code></p>
<dd> An invalid <i>return_type</i> was specified.</p>
<dt><code>GD_E_INTERNAL_ERROR</code></p>
<dd> An internal error occurred in the library while trying to perform the task. This indicates a bug in the library. Please report the incident to the maintainer. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered may be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_constants/">get_constants</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-put_constant/">put_constant</a></code>(3) </p>
<h2>Index</h2>
