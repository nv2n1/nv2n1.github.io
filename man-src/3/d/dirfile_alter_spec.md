---

title: "dirfile_alter_spec(3)"
name: "dirfile_alter_spec"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_alter_spec/"
description: "dirfile_alter_spec, dirfile_malter_spec — modify a field in a dirfile"
---

<p> dirfile_alter_spec, dirfile_malter_spec &#8212; modify a field in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_alter_spec(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>line</i><code>,</code> <code>int </code><i>recode</i><code>);</code></dt>
<dt> <code>int dirfile_malter_spec(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>line</i><code>,</code> <code>const char *</code><i>parent</i><code>, int </code><i>recode</i><code>);</code></dt></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_alter_spec</code>() function modifies the field described by the field specification line in <i>line</i> to the dirfile specified by <i>dirfile</i>. The <code>dirfile_malter_spec</code>() function behaves similarly, but modifies the metafield under the field indicated by the field code <i>parent</i>. Field specification lines are described in detail in <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5). </dd>
<p> The name of the field to be modified, which must already exist, will be obtained from the field specification line. When adding a metafield, <i>line</i> should only contain a field specification, and not a <code>/META</code> directive. </p>
<p> If the modified field is of type <code>RAW</code> and the <i>recode</i> argument is non-zero, the binary file associated with the field will be converted for changes in data type and samples-per-frame. If <i>recode</i> is zero, no binary file conversion will take place. </p>
<p> If the modified field is of type <code>LINTERP</code> and the <i>recode</i> argument is non-zero, the look-up table file will be moved if <i>entry</i>-&gt;<i>table</i> specifies a different path, overwriting an existing file with the new pathname, if present. If the field specified by <i>field_code</i> is of type other than <code>RAW</code> or <code>LINTERP</code>, the <i>recode</i> argument is ignored. </p>
<p> Passing these functions a directive line instead of a field specification line will result in a syntax error. These functions never call the registered parser callback function, even if <i>line</i> contains a syntax error. </p>
<h2>RETURN VALUE</h2>
<p> On success, <code>dirfile_alter_spec</code>() and <code>dirfile_malter_spec</code>() return zero. On error, -1 is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></dt>
<dd> The specified dirfile was opened read-only.</dd>
<dt><code>GD_E_ALLOC</code></dt>
<dd> The library was unable to allocate memory.</dd>
<dt><code>GD_E_BAD_CODE</code></dt>
<dd> The field specified in <i>line</i> was not found, or the <i>parent</i> field code was not found.</dd>
<dt><code>GD_E_BAD_DIRFILE</code></dt>
<dd> The supplied dirfile was invalid.</dd>
<dt><code>GD_E_FORMAT</code></dt>
<dd> A syntax error was encountered in <i>line</i>.</dd>
<dt><code>GD_E_PROTECTED</code></dt>
<dd> The metadata of the fragment was protected from change. Or, a request to translate the binary file associated with a <code>RAW</code> field was attempted, but the data of the fragment was protected.</dd>
<dt><code>GD_E_RAW_IO</code></dt>
<dd> An I/O error occurred while translating the binary file associated with a modified <code>RAW</code> field, or an I/O error occurred while attempting to rename a <code>LINTERP</code> table file.</dd>
<dt><code>GD_E_UNKNOWN_ENCODING</code></dt>
<dd> The encoding scheme of the specified format file fragment is not known to the library. As a result, the library was unable to translate the binary file be associated with a modified <code>RAW</code> field.</dd>
<dt><code>GD_E_UNSUPPORTED</code></dt>
<dd> The encoding scheme of the specified format file fragment does not support translating the empty binary file associated with a modified <code>RAW</code> field. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_alter_bit/">dirfile_alter_bit</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_const/">dirfile_alter_const</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_entry/">dirfile_alter_entry</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_lincom/">dirfile_alter_lincom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_linterp/">dirfile_alter_linterp</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_multiply/">dirfile_alter_multiply</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_phase/">dirfile_alter_phase</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_raw/">dirfile_alter_raw</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_spec/">dirfile_alter_spec</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
