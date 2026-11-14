---
title: "get_fragmentname(3)"
name: "get_fragmentname"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_fragmentname/"
description: "get_fragmentname — retrieve a dirfile format file fragment name"
---

<h2>NAME</h2>
<p> get_fragmentname &#8212; retrieve a dirfile format file fragment name</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>const char* get_fragmentname(const DIRFILE *</code><i>dirfile</i><code>, int </code><i>index</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_fragmentname</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the filename of the format file fragment indexed by the non-negative <i>index</i>. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<p> The format file fragment with <i>index</i> equal to zero is always the primary format file for the database (the file called <code>format</code> in the root dirfile directory). The largest valid value of <i>index</i> is one less than the total number of format file fragments, which may be obtained from a call to <code><a href="/docs/linux/man/3-get_nfragments/">get_nfragments</a></code>(3).</p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_fragmentname</code>() returns a pointer to a read-only character string containing the file name of the specified format file fragment. On error, <code>get_fragmentname</code>() returns NULL and sets the dirfile error a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_INDEX</code></p>
<dd> The supplied index was out of range. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3). </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_include/">dirfile_include</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_nfragments/">get_nfragments</a></code>(3), <code><a href="/docs/linux/man/3-get_parent_fragment/">get_parent_fragment</a></code>(3) </p>
<h2>Index</h2>
