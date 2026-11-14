---
title: "get_fragment_index(3)"
name: "get_fragment_index"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_fragment_index/"
description: "get_fragment_index — retrieve the fragment containing a dirfile field"
---

<h2>NAME</h2>
<p> get_fragment_index &#8212; retrieve the fragment containing a dirfile field</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int get_fragment_index(const DIRFILE *</code><i>dirfile</i><code>, const char</code> <code>*</code><i>field_code</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_fragment_index</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the index number of the fragment defining the field specified by <i>field_code</i>. If <i>field_code</i> contains a representation suffix, it will be ignored.</p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_fragment_index</code>() returns the requested fragment index. On error, <code>get_fragment_index</code>() returns -1 and sets the dirfile error a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> was not found in the database.</p>
<dt><code>GD_E_BAD_REPR</code></p>
<dd> The representation suffix specified in <i>field_code</i> was not recognised. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_entry/">get_entry</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_fragmentname/">get_fragmentname</a></code>(3), <code><a href="/docs/linux/man/3-get_parent_fragment/">get_parent_fragment</a></code>(3), <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5) </p>
<h2>Index</h2>
