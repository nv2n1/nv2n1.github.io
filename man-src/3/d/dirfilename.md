---
title: "dirfilename(3)"
name: "dirfilename"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfilename/"
description: "dirfilename — retrieve the name of a dirfile"
---

<h2>NAME</h2>
<p> dirfilename &#8212; retrieve the name of a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>const char *dirfilename(const DIRFILE *</code><i>dirfile</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfilename</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns its name. The name of a dirfile is the pathname passed to <code>dirfile_cbopen</code>() or <code>dirfile_open</code>() when the dirfile was opened. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>dirfilename</code>() returns a pointer to a constant string containing the pathname of the dirfile. On error, <code>dirfilename</code>() returns NULL and sets the dirfile error to a non-zero value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_cbopen/">dirfile_cbopen</a></code>(3) </p>
<h2>Index</h2>
