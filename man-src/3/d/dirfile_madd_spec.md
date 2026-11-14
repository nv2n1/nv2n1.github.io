---
title: "dirfile_madd_spec(3)"
name: "dirfile_madd_spec"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_madd_spec/"
description: "dirfile_add_spec, dirfile_madd_spec — add a field to a dirfile"
---

<h2>NAME</h2>
<p> dirfile_add_spec, dirfile_madd_spec &#8212; add a field to a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_add_spec(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>line</i><code>,</code> <code>int </code><i>fragment_index</i><code>);</code></p>
<dt> <code>int dirfile_madd_spec(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>line</i><code>,</code> <code>const char *</code><i>parent</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_add_spec</code>() function adds the field described by the field specification line in <i>line</i> to the dirfile specified by <i>dirfile</i>. The <code>dirfile_madd_spec</code>() function behaves similarly, but adds the field as a metafield under the field indicated by the field <i>parent</i>. Field specification lines are described in detail in <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5). Since Standards Version 7 (see <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5)) permits specifying metafield without the use of the <code>/META</code> directive, <code>dirfile_add_spec</code>() may also be used to add metafields, by specifying the metafield&#8217;s full field code. See <a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a>(5) for full details. </p>
<p> When using <code>dirfile_madd_spec</code>(), <i>line</i> should only contain a field specification, and not a <code>/META</code> directive. </p>
<p> Passing these functions a directive line instead of a field specification line will result in a syntax error. These functions never call the registered parser callback function, even if <i>line</i> contains a syntax error. </p>
<h2>RETURN VALUE</h2>
<p> On success, <code>dirfile_add_spec</code>() and <code>dirfile_madd_spec</code>() return zero. On error, -1 is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></p>
<dd> The specified dirfile was opened read-only.</p>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The <i>parent</i> field code was not found, or was already a metafield.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_INDEX</code></p>
<dd> The <i>fragment_index</i> argument was out of range.</p>
<dt><code>GD_E_FORMAT</code></p>
<dd> A syntax error was encountered in <i>line</i>.</p>
<dt><code>GD_E_PROTECTED</code></p>
<dd> The metadata of the fragment was protected from change. Or, the creation of a <code>RAW</code> field was attempted and the data of the fragment was protected.</p>
<dt><code>GD_E_RAW_IO</code></p>
<dd> An I/O error occurred while creating an empty binary file to be associated with a newly added <code>RAW</code> field.</p>
<dt><code>GD_E_UNKNOWN_ENCODING</code></p>
<dd> The encoding scheme of the specified format file fragment is not known to the library. As a result, the library was unable to create an empty binary file to be associated with a newly added <code>RAW</code> field.</p>
<dt><code>GD_E_UNSUPPORTED</code></p>
<dd> The encoding scheme of the specified format file fragment does not support creating an empty binary file to be associated with a newly added <code>RAW</code> field. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_add/">dirfile_add</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_bit/">dirfile_add_bit</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_const/">dirfile_add_const</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_lincom/">dirfile_add_lincom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_linterp/">dirfile_add_linterp</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_multiply/">dirfile_add_multiply</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_phase/">dirfile_add_phase</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_raw/">dirfile_add_raw</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd/">dirfile_madd</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_bit/">dirfile_madd_bit</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_const/">dirfile_madd_const</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_lincom/">dirfile_madd_lincom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_linterp/">dirfile_madd_linterp</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_multiply/">dirfile_madd_multiply</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_phase/">dirfile_madd_phase</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_string/">dirfile_madd_string</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
