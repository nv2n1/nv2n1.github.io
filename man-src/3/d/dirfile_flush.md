---
title: "dirfile_flush(3)"
name: "dirfile_flush"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_flush/"
description: "dirfile_flush — write all pending dirfile changes to disk."
---

<h2>NAME</h2>
<p> dirfile_flush &#8212; write all pending dirfile changes to disk.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_flush(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_flush</code>() function flushes and closes all file handles associated with <i>field_code</i>, or its input(s), in the dirfile specified by <i>dirfile</i>. If the <i>field_code</i> contains a valid representation suffix, it will be ignored. As a special case, if <i>field_code</i> is NULL, all fields in <i>dirfile</i> will be flushed and closed. In this special case, modified metadata will also be flushed to disk as if <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3) had been called.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> was not found in the database.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_REPR</code></p>
<dd> The representation suffix specified in <i>field_code</i> was not recognised.</p>
<dt><code>GD_E_RAW_IO</code></p>
<dd> An error occurred while trying to flush or close the field(s). The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_close/">dirfile_close</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3) </p>
<h2>Index</h2>
