---
title: "get_error_string(3)"
name: "get_error_string"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_error_string/"
description: "get_error_string — report a getdata library error"
---

<h2>NAME</h2>
<p> get_error_string &#8212; report a getdata library error</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>char *get_error_string(const DIRFILE *</code><i>dirfile</i><code>, char *</code><i>buffer</i><code>, size_t</code> <i>buflen</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_error_string</code>() function returns a string describing the last dirfile error encountered while operating on <i>dirfile</i>. The string is written to the user-supplied buffer <i>buffer</i>. At most <i>buflen</i> characters will be written. This always includes a terminating null byte, even if the error string was truncated. The numeric dirfile error itself may be obtained by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). </p>
<p> The <i>dirfile</i> argument should point to a DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<h2>RETURN VALUE</h2>
<p> The <code>get_error_string</code>() function returns <i>buffer</i>, or NULL if buflen is less than one. The error state of <i>dirfile</i> is unchanged.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). </p>
<h2>Index</h2>
