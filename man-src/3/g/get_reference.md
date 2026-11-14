---
title: "get_reference(3)"
name: "get_reference"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_reference/"
description: "dirfile_reference, get_reference — retrieve or set the reference field for a dirfile"
---

<h2>NAME</h2>
<p> dirfile_reference, get_reference &#8212; retrieve or set the reference field for a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>const char *dirfile_reference(DIRFILE *</code><i>dirfile</i><code>, const char</code> <code>*</code><i>field_code</i><code>);</code></p>
<dt> <code>const char *get_reference(DIRFILE *</code><i>dirfile</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_reference</code>() function sets or retrieves the reference field (see <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5)) associated with the dirfile specified by <i>dirfile</i>. If the <i>field_code</i> argument is non-NULL, the reference field for the dirfile will be set to the field specified. If <i>field_code</i> is NULL, the reference field is not modified. The field code should refer to a RAW field, and may not contain a representation suffix. </p>
<p> <code>get_reference</code>() is equivalent to calling <code>dirfile_reference</code>() with <i>field_code</i> set to NULL. </p>
<h2>RETURN VALUE</h2>
<p> On success, <code>dirfile_reference</code>() and <code>get_reference</code>() return the field code of the dirfile&#8217;s reference field, which will be <i>field_code</i>, if <i>field_code</i> is non-NULL. If no <code>RAW</code> fields are defined in the dirfile, these functions will return NULL, without raising an error. On error, NULL is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></p>
<dd> The specified dirfile was opened read-only.</p>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> was not found.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_FIELD_TYPE</code></p>
<dd> The field specified by <i>field_code</i> was not a <code>RAW</code> field.</p>
<dt><code>GD_E_PROTECTED</code></p>
<dd> The metadata of the primary format file fragment (the file named <i>format</i> in the root dirfile directory) was protected from change. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
