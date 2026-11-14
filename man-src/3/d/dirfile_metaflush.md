---
title: "dirfile_metaflush(3)"
name: "dirfile_metaflush"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_metaflush/"
description: "dirfile_metaflush — close a dirfile and free associated memory."
---

<h2>NAME</h2>
<p> dirfile_metaflush &#8212; close a dirfile and free associated memory.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_metaflush(DIRFILE *</code><i>dirfile</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_metaflush</code>() function flushes all pending metadata changes in the dirfile specified by <i>dirfile </i> to disk. This is accomplished by re-writing the format file fragments containing modified metadata. Format file fragments which are unchanged are not touched. This function flushes only metadata. To flush the field data as well, call <code><a href="/docs/linux/man/3-dirfile_flush/">dirfile_flush</a></code>(3) instead.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_INTERNAL_ERROR</code></p>
<dd> An internal error occurred in the library while trying to perform the task. This indicates a bug in the library. Please report the incident to the maintainer.</p>
<dt><code>GD_E_OPEN_INCLUDE</code></p>
<dd> A temporary file could not be opened into which to write the modified metadata. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_flush/">dirfile_flush</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_close/">dirfile_close</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3) </p>
<h2>Index</h2>
