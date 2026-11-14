---
title: "dirfile_move(3)"
name: "dirfile_move"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_move/"
description: "dirfile_move — move a dirfile field between format file fragments"
---

<h2>NAME</h2>
<p> dirfile_move &#8212; move a dirfile field between format file fragments</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_move(DIRFILE *</code><i>dirfile</i><code>, const char</code> <code>*</code><i>field_code</i><code>, int </code><i>new_fragment</i><code>, int </code><i>move_data</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_move</code>() function transfers the field specified by <i>field_code</i>, which should not have a representation suffix, defined in the dirfile specified by <i>dirfile</i> from it&#8217;s current format file fragment to the fragment index by <i>new_fragment</i>. If the field is already defined in the fragment index by <i>new_fragment</i>, this function does nothing. </p>
<p> If the flag <i>move_data</i> is non-zero, and <i>field_code</i> specifies a <code>RAW</code> field, the binary file associated with the field will be translated to account for the possibly different encoding, endianness, and frame offset of the new format file fragment. It will also be moved to a new directory, if necessary. If <i>move_data</i> is zero, no changes will be made to the binary file. If <i>field_code</i> specifies a field of type other than <code>RAW</code>, the <i>move_data</i> flag is ignored. </p>
<p> If the binary file is translated, and the frame offset of the destination fragment is larger than that of the source fragment, this will result in permanent deletion of data from the database. If the new frame offset is smaller than the old frame offset, the binary file will be padded at the front with zeroes. </p>
<h2>RETURN VALUE</h2>
<p> On success, <code>dirfile_move</code>() returns zero. On error, -1 is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></p>
<dd> The specified dirfile was opened read-only.</p>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> was not found.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_FIELD_TYPE</code></p>
<dd> An attempt was made to move the immutable <i>INDEX</i> field.</p>
<dt><code>GD_E_BAD_INDEX</code></p>
<dd> The <i>new_fragment</i> argument did not index a valid format file fragment.</p>
<dt><code>GD_E_PROTECTED</code></p>
<dd> The metadata of the source or destination format file fragments was protected from change, or the binary data of the source or destination fragments was protected from change and binary file translation was requested.</p>
<dt><code>GD_E_RAW_IO</code></p>
<dd> An I/O error occurred while attempting to translate a binary file.</p>
<dt><code>GD_E_UNKNOWN_ENCODING</code></p>
<dd> The encoding scheme of the source or destination fragment is unknown.</p>
<dt><code>GD_E_UNSUPPORTED</code></p>
<dd> The encoding scheme of the source or destination fragment does not support binary file translation. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>NOTES</h2>
<p> A binary file translation occurs out-of-place. As a result, sufficient space must be present on the filesystem for both the binary file before translation and the binary file after translation.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
