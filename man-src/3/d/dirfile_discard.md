---
title: "dirfile_discard(3)"
name: "dirfile_discard"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_discard/"
description: "dirfile_close, dirfile_discard — close a dirfile and free associated memory."
---

<h2>NAME</h2>
<p> dirfile_close, dirfile_discard &#8212; close a dirfile and free associated memory.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_close(DIRFILE *</code><i>dirfile</i><code>);</code></p>
<dt> <code>int dirfile_discard(DIRFILE *</code><i>dirfile</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_close</code>() function first calls <code><a href="/docs/linux/man/3-dirfile_flush/">dirfile_flush</a></code>(3) to flush all metadata changes to disk and to close all file handles associated with <i>dirfile</i>. It then frees memory associated with the DIRFILE object. If <i>dirfile</i> is NULL, nothing happens, and the call succeeds. </p>
<p> The <code>dirfile_discard</code>() function behaves similarly, except modified metadata is not written to disk, but simply discarded. In order to ensure that modified data files associated with <code>RAW</code> fields are properly terminated, changes to <code>RAW</code> data files are still flushed to disk by this function. If <i>dirfile</i> was opened in read-only mode, <code>dirfile_discard()</code> and <code>dirfile_close()</code> behave identically. </p>
<p> One of these functions should be called on all pointers returned by <code><a href="/docs/linux/man/3-dirfile_cbopen/">dirfile_cbopen</a></code>(3) and <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), even if the call to those function failed. After <code>dirfile_close</code>() or <code>dirfile_discard()</code> returns successfully, the pointer <i>dirfile</i> should be considered invalid.</p>
<h2>RETURN VALUE</h2>
<p> <code>dirfile_close</code>() and <code>dirfile_discard</code>() return zero on success. On error, they do not deallocate <i>dirfile</i> and set the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_RAW_IO</code></p>
<dd> An error occurred while trying to flush or close one or more open raw files. In this case, another call to <code>dirfile_close</code>() or <code>dirfile_discard</code>() may be attempted. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_flush/">dirfile_flush</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3) </p>
<h2>Index</h2>
