---
title: "get_native_type(3)"
name: "get_native_type"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_native_type/"
description: "get_native_type — returns the native data type of a field in a dirfile"
---

<h2>NAME</h2>
<p> get_native_type &#8212; returns the native data type of a field in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>gd_type_t get_native_type(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_native_type</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the native data type of the field <i>field_code</i>, which may contain a representation suffix. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<p> The native data type of a field of a given entry type is calculated as:</p>
<dl>
<dt><code>BIT</code>~or~<code>INDEX</code>~Entry:</p>
<dd> <code>GD_UINT64</code>;</p>
<dt><code>CONST</code>~Entry:</p>
<dd> the data type of the constant;</p>
<dt><code>LINCOM</code>~or~<code>POLYNOM</code>~Entry:</p>
<dd> if any of the scalar parameters is complex valued, or if the native data type of any of the input fields is complex valued: <code>GD_COMPLEX128</code>, otherwise: <code>GD_FLOAT64</code>;</p>
<dt><code>LINTERP</code>~Entry:</p>
<dd> if the look-up table is complex valued: <code>GD_COMPLEX128</code>, otherwise: <code>GD_FLOAT64</code>;</p>
<dt><code>MULTIPLY</code>~Entry:</p>
<dd> if either input field is complex valued: <code>GD_COMPLEX128</code>, otherwise: <code>GD_FLOAT64</code>; <code>.TP</code> <code>PHASE</code>~Entry: the native data type of the input field;</p>
<dt><code>RAW</code>~Entry:</p>
<dd> the data type of the raw data on disk;</p>
<dt><code>SBIT</code>~Entry:</p>
<dd> <code>GD_INT64</code>;</p>
<dt><code>STRING</code>~Entry:</p>
<dd> <code>GD_NULL</code>.</dl>
<p> Furthermore, if the supplied <i>field_code</i> contains a representation suffix, and the native data type of the field is complex valued, the native type returned will be the corresponding real valued type. </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_native_type</code>() returns the native data type of the field code specified. This will be one of the symbols:</p>
<dl>
<dt>
<dd> <code>GD_NULL</code>,~<code>GD_UINT8</code>,~<code>GD_INT8</code>,~<code>GD_UINT16</code>,~<code>GD_INT16</code>,~<code>GD_UINT32</code>, <code>GD_INT32</code>,~<code>GD_FLOAT32</code>,~<code>GD_FLOAT64</code>,~<code>GD_COMPLEX64</code>,~<code>GD_COMPLEX128</code>. The meanings of these symbols are explained in the <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3) manual page. On error, it returns <code>GD_UNKNOWN</code> and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> or one of the fields it uses as input was not found in the database.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_REPR</code></p>
<dd> The representation suffix specified in <i>field_code</i>, or in one of its input fields, was not recognised.</p>
<dt><code>GD_E_BAD_SCALAR</code></p>
<dd> A non-literal scalar used in the definition of the field or one of its inputs was not found, or was not a <code>CONST</code> field.</p>
<dt><code>GD_E_DIMENSION</code></p>
<dd> A scalar field was found where a vector field was expected.</p>
<dt><code>GD_E_OPEN_LINFILE</code></p>
<dd> An error occurred while trying to read a LINTERP table from disk.</p>
<dt><code>GD_E_RECURSE_LEVEL</code></p>
<dd> Too many levels of recursion were encountered while trying to resolve <i>field_code</i>. This usually indicates a circular dependency in field specification in the dirfile. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3) </p>
<h2>Index</h2>
