---
title: "get_raw_filename(3)"
name: "get_raw_filename"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_raw_filename/"
description: "get_raw_filename — retrieve the pathname of a binary file in a dirfile"
---

<h2>NAME</h2>
<p> get_raw_filename &#8212; retrieve the pathname of a binary file in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>const char *get_raw_filename(DIRFILE *</code><i>dirfile</i><code>, const char</code> <code>*</code><i>field_code</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_raw_filename</code>() function retrieves the pathname of the file backing the <code>RAW</code> field specified by <i>field_code</i> in the dirfile specified by <i>dirfile</i>. If <i>field_code</i> contains a valid representation suffix, it will be ignored. </p>
<h2>RETURN VALUE</h2>
<p> On success, <code>get_raw_filename</code>() returns the full pathname of the binary file associated with the specified field. On error, NULL is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> was not found.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_FIELD_TYPE</code></p>
<dd> The field specified by <i>field_code</i> was not a <code>RAW</code> field.</p>
<dt><code>GD_E_BAD_REPR</code></p>
<dd> The representation suffix specified in <i>field_code</i> was not recognised.</p>
<dt><code>GD_E_UNKNOWN_ENCODING</code></p>
<dd> The encoding scheme of the specified field could not be determined or was not understood by GetData. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_entry/">get_entry</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
