---
title: "get_protection(3)"
name: "get_protection"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_protection/"
description: "get_protection — report the protection level of a dirfile fragment"
---

<h2>NAME</h2>
<p> get_protection &#8212; report the protection level of a dirfile fragment</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int get_protection(DIRFILE *</code><i>dirfile</i><code>, int </code><i>fragment_index</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_protection</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the advisory protection level for the fragment indexed by <i>fragment_index</i>. </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_protection</code>() returns the advisory protection level of the specified fragment, which will be one of the following symbols.</p>
<dl>
<dt>
<dd> <code>GD_PROTECT_NONE</code>,~<code>GD_PROTECT_FORMAT</code>,~<code>GD_PROTECT_DATA</code>,~ <code>GD_PROTECT_ALL</code>. The meaning of these symbols are explained in the <code><a href="/docs/linux/man/3-dirfile_protect/">dirfile_protect</a></code>(3) man page. On error, it returns -1 and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_INDEX</code></p>
<dd> The supplied index was out of range. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_protect/">dirfile_protect</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
