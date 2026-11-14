---
title: "get_nfragments(3)"
name: "get_nfragments"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_nfragments/"
description: "get_nfragments — retrieve the number of format file fragments in a dirfile"
---

<h2>NAME</h2>
<p> get_nfragments &#8212; retrieve the number of format file fragments in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int get_nfragments(const DIRFILE *</code><i>dirfile</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_nfragments</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the total number of parsed format file fragments in the database. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_nfragments</code>() returns the total number of format file fragments which are present in the dirfile. On error, <code>get_nfragments</code>() returns zero and sets the dirfile error to a non-zero value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_include/">dirfile_include</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_fragmentname/">get_fragmentname</a></code>(3), <code><a href="/docs/linux/man/3-get_parent_fragment/">get_parent_fragment</a></code>(3) </p>
<h2>Index</h2>
