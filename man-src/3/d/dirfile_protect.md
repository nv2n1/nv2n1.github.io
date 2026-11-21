---

title: "dirfile_protect(3)"
name: "dirfile_protect"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_protect/"
description: "dirfile_protect — modify the protection level of a dirfile fragment"
---

<p> dirfile_protect &#8212; modify the protection level of a dirfile fragment</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_protect(DIRFILE *</code><i>dirfile</i><code>, int</code> <i>protection_level</i><code>, int </code><i>fragment_index</i><code>);</code></dt></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_protect</code>() function sets the advisory protection level of the format file fragment specified by <i>fragment_index</i> to <i>protection_level</i> in the <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i>. </dd>
<p> The <i>protection_level</i> argument should be one of the following:</p>
<dl>
<dt><code>GD_PROTECT_NONE</code></dt>
<dd> Indicating that the fragment should not be protected at all.</dd>
<dt><code>GD_PROTECT_FORMAT</code></dt>
<dd> Indicating that the fragment&#8217;s metadata should be protected.</dd>
<dt><code>GD_PROTECT_DATA</code></dt>
<dd> Indicating that the fragment&#8217;s binary data should be protected.</dd>
<dt><code>GD_PROTECT_ALL</code></dt>
<dd> Indicating that both the fragment&#8217;s metadata and its binary data should be protected. This symbol is equivalent to the bitwise or of <code>GD_PROTECT_FORMAT</code> and <code>GD_PROTECT_DATA</code>. In addition to being simply a valid fragment index, <i>fragment_index</i> may also be the special value <code>GD_ALL_FRAGMENTS</code>, which indicates that the protection level of all fragments in the database should be changed. </dd>
</dl>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>dirfile_protect</code>() returns zero. On error, it returns -1 and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></dt>
<dd> The specified dirfile was opened read-only.</dd>
<dt><code>GD_E_BAD_DIRFILE</code></dt>
<dd> The supplied dirfile was invalid.</dd>
<dt><code>GD_E_BAD_INDEX</code></dt>
<dd> The supplied index was out of range.</dd>
<dt><code>GD_E_BAD_PROTECTION</code></dt>
<dd> The supplied protection level was invalid. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dd></dl>
<h2>NOTES</h2>
<p> This is the only GetData function which ignores the (existing) protection level of a format file fragment.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_protection/">get_protection</a></code>(3), <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
