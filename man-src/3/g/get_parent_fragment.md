---
title: "get_parent_fragment(3)"
name: "get_parent_fragment"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_parent_fragment/"
description: "get_parent_fragment — retrieve the parent fragment of a fragment in a dirfile"
---

<h2>NAME</h2>
<p> get_parent_fragment &#8212; retrieve the parent fragment of a fragment in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int get_parent_fragment(const DIRFILE *</code><i>dirfile</i><code>, int </code><i>fragment_index</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_parent_fragment</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the index of the fragment which contains the <code>INCLUDE</code> directive for the fragment indexed by <i>fragment_index</i>. </p>
<p> Since the primary format file fragment is not included in any other fragment, passing zero for <i>fragment_index</i> will result in an error. </p>
<h2>RETURN VALUE</h2>
<p> On success, <code>get_parent_fragment</code>() returns the index of the specified fragment&#8217;s parent. On error, <code>get_parent_fragment</code>() returns -1 and sets the dirfile error to a non-zero value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_INDEX</code></p>
<dd> The supplied index was out of range, or was equal to zero. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_include/">dirfile_include</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_fragmentname/">get_fragmentname</a></code>(3), <code><a href="/docs/linux/man/3-get_nfragments/">get_nfragments</a></code>(3) </p>
<h2>Index</h2>
