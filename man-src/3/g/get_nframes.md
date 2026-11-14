---
title: "get_nframes(3)"
name: "get_nframes"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_nframes/"
description: "get_nframes — report the size of a dirfile"
---

<h2>NAME</h2>
<p> get_nframes &#8212; report the size of a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>off_t get_nframes(DIRFILE *</code><i>dirfile</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_nframes</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the number of frames in the database. Since different fields may have differing number of frames, the Dirfile Standards (see <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5)) dictate that the number of frames in the database is defined to be equal to the number of frames in the first raw field specified in the format file. </p>
<p> If no vector fields are defined in the database, <code>get_nframes</code>() returns zero and succeeds. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_nframes</code>() returns the number of frames in the dirfile. On error, it returns zero and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_RAW_IO</code></p>
<dd> An attempt to <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) the file associated with first raw field defined in the format failed.</p>
<dt><code>GD_E_UNSUPPORTED</code></p>
<dd> Reading from dirfiles with the encoding scheme of the specified dirfile is not supported by the library. See <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5) for details on dirfile encoding schemes. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3) </p>
<h2>Index</h2>
