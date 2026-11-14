---
title: "get_error(3)"
name: "get_error"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_error/"
description: "get_error — report a getdata library error"
---

<h2>NAME</h2>
<p> get_error &#8212; report a getdata library error</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int get_error(const DIRFILE *</code><i>dirfile</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_error</code>() function returns the numeric dirfile error associated with the dirfile <i>dirfile</i> which is set by many GetData library functions. </p>
<p> The <i>dirfile</i> argument should point to a DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<p> A textual description of the error may be obtained by calling <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3). </p>
<h2>RETURN VALUE</h2>
<p> The <code>get_error</code>() function always returns the dirfile error corresponding to the error state of the last library call on the supplied DIRFILE object.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3) </p>
<h2>Index</h2>
