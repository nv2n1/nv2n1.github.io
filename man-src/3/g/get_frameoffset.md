---
title: "get_frameoffset(3)"
name: "get_frameoffset"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_frameoffset/"
description: "get_frameoffset — report the starting frame of fields in a dirfile"
---

<h2>NAME</h2>
<p> get_frameoffset &#8212; report the starting frame of fields in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>off_t get_frameoffset(DIRFILE *</code><i>dirfile</i><code>, int </code><i>fragment_index</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_frameoffset</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the frame offset (see <a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a>(5)) for the fragment indexed by <i>fragment_index</i>. The frame offset of a fragment indicate the frame number of the first sample of data stored in binary files associated with <code>RAW</code> fields defined in the specified fragment. The frame offset of a fragment containing no <code>RAW</code> fields is ignored. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_frameoffset</code>() returns the frame offset of the specified fragment. On error, it returns -1 and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_INDEX</code></p>
<dd> The supplied index was out of range. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_alter_frameoffset/">dirfile_alter_frameoffset</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
