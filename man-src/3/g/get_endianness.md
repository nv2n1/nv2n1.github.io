---
title: "get_endianness(3)"
name: "get_endianness"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_endianness/"
description: "get_endianness — report the byte sex of fields in a dirfile"
---

<h2>NAME</h2>
<p> get_endianness &#8212; report the byte sex of fields in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>unsigned long get_endianness(DIRFILE *</code><i>dirfile</i><code>, int </code><i>fragment_index</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_endianness</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the byte sex for the fragment indexed by <i>fragment_index</i>. The byte sex of a fragment indicate the endianness of data stored in binary files associated with <code>RAW</code> fields defined in the specified fragment. The endianness of a fragment containing no <code>RAW</code> fields is ignored. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_endianness</code>() returns the byte sex of the specified fragment, which will be either <code>GD_BIG_ENDIAN</code> or <code>GD_LITTLE_ENDIAN</code>. On error, it returns zero and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_INDEX</code></p>
<dd> The supplied index was out of range. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_alter_endianness/">dirfile_alter_endianness</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
