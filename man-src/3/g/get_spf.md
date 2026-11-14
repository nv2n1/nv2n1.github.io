---
title: "get_spf(3)"
name: "get_spf"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_spf/"
description: "get_spf — returns the samples per frame for a field in a dirfile"
---

<h2>NAME</h2>
<p> get_spf &#8212; returns the samples per frame for a field in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>gd_spf_t get_spf(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_spf</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the number of samples per frame for the field <i>field_code</i>. If <i>field_code</i> contains a valid representation suffix, it will be ignored. The <i>gd_spf_t</i> type is an unsigned 16-bit integer type. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_spf</code>() returns the number of samples per frame for the field specified. On error, it returns zero and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> was not found in the database.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_REPR</code></p>
<dd> The representation suffix specified in <i>field_code</i> was not recognised.</p>
<dt><code>GD_E_INTERNAL_ERROR</code></p>
<dd> An internal error occurred in the library while trying to perform the task. This indicates a bug in the library. Please report the incident to the maintainer.</p>
<dt><code>GD_E_RECURSE_LEVEL</code></p>
<dd> Too many levels of recursion were encountered while trying to resolve <i>field_code</i>. This usually indicates a circular dependency in field specification in the dirfile. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3) </p>
<h2>Index</h2>
