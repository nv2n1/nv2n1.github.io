---

title: "dirfile_rename(3)"
name: "dirfile_rename"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_rename/"
description: "dirfile_rename — change the name of a dirfile field"
---

<h2>NAME</h2>
<p> dirfile_rename &#8212; change the name of a dirfile field</p>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_rename(DIRFILE *</code><i>dirfile</i><code>, const char</code> <code>*</code><i>old_code</i><code>, const char *</code><i>new_name</i><code>, int </code><i>move_data</i><code>);</code></dt></dl>
<dd>The <code>dirfile_rename</code>() function changes the name of the field specified by <i>old_code</i>, which should not contain a representation suffix, defined in the dirfile specified by <i>dirfile</i> to <i>new_name</i>. If the new name is the same as the old name, this function does nothing. </dd>
<p> When renaming a metafield, the metafield should be specified in <i>old_code</i> by its full (slashed) field code, while <i>new_name</i> should only contain the new name (without slash). </p>
<p> If the flag <i>move_data</i> is non-zero, and <i>old_code</i> specifies a <code>RAW</code> field, the binary file associated with the field will be renamed as well. If <i>move_data</i> is zero, no changes will be made to the binary file. If <i>field_code</i> specifies a field of type other than <code>RAW</code>, the <i>move_data</i> flag is ignored. </p>
<h2>RETURN VALUE</h2>
<p> On success, <code>dirfile_rename</code>() returns zero. On error, -1 is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></dt>
<dd> The specified dirfile was opened read-only.</dd>
<dt><code>GD_E_ALLOC</code></dt>
<dd> The library was unable to allocate memory.</dd>
<dt><code>GD_E_BAD_CODE</code></dt>
<dd> The field specified by <i>old_code</i> was not found.</dd>
<dt><code>GD_E_BAD_DIRFILE</code></dt>
<dd> The supplied dirfile was invalid.</dd>
<dt><code>GD_E_BAD_FIELD_TYPE</code></dt>
<dd> An attempt was made to rename the immutable <i>INDEX</i> field.</dd>
<dt><code>GD_E_BAD_REPR</code></dt>
<dd> The representation suffix specified in <i>field_code</i> was not recognised.</dd>
<dt><code>GD_E_DUPLICATE</code></dt>
<dd> The new name specified is already in use by another field.</dd>
<dt><code>GD_E_PROTECTED</code></dt>
<dd> The metadata of the format file fragment containing the field was protected from change, or the binary data of the fragments was protected from change and binary file translation was requested.</dd>
<dt><code>GD_E_RAW_IO</code></dt>
<dd> An I/O error occurred while attempting to rename the binary file.</dd>
<dt><code>GD_E_UNKNOWN_ENCODING</code></dt>
<dd> The encoding scheme of the specified field could not be determined or was not understood by GetData.</dd>
<dt><code>GD_E_UNSUPPORTED</code></dt>
<dd> The encoding scheme of the field does not support binary file renaming. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
