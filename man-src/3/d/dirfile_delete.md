---
title: "dirfile_delete(3)"
name: "dirfile_delete"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_delete/"
description: "dirfile_delete — remove a field from a dirfile"
---

<h2>NAME</h2>
<p> dirfile_delete &#8212; remove a field from a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_delete(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>int </code><i>flags</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_delete</code>() function attempts to delete the field specified by <i>field_code</i> in the dirfile specified by <i>dirfile</i>. The <i>field_code</i> should not contain a representation suffix. </p>
<p> The <i>flags</i> argument influences how the deletion attempt occurs. It may be zero, for the default behaviour, or else one or more of the following flags, bitwise or&#8217;d together:</p>
<dl>
<dt><code>GD_DEL_DATA</code></p>
<dd> If the field to be deleted is a <code>RAW</code> field, also delete the binary data file associated with it. If <i>field_code</i> specified a <code>RAW</code> field and this flag is not specified, the field will still be deleted but the binary file will be left untouched.</p>
<dt><code>GD_DEL_DEREF</code></p>
<dd> If the field to be deleted is a <code>CONST</code> field which is used as a parameter in the specification of other fields, resolve these other fields dependence on <i>field_code</i> by replacing instances of <i>field_code</i> in their field specifications with the value of the <code>CONST</code> field.</p>
<dt><code>GD_DEL_FORCE</code></p>
<dd> Delete the specified field even if it is used in the specification of other fields, either as a input for a derived vector field or as a <code>CONST</code> parameter in a field specification.</p>
<dt><code>GD_DEL_META</code></p>
<dd> If the field to be deleted has metafields attached to it, attempt to delete those, too. If the field has metafields and this flag is not specified, the call will fail with the <code>GD_E_DELETE</code> error.</dl>
<h2>RETURN VALUE</h2>
<p> On successful deletion, zero is returned. On error, -1 is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></p>
<dd> The specified dirfile was opened read-only.</p>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> was not found in the database.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_DELETE</code></p>
<dd> The attempt to delete the field failed. Either the specified field is used in the specification of other fields and <code>GD_DEL_FORCE</code> or <code>GD_DEL_DEREF</code> was not specified, or it has metafields and <code>GD_DEL_META</code> was not specified.</p>
<dt><code>GD_E_INTERNAL_ERROR</code></p>
<dd> An internal error occurred in the library while trying to perform the task. This indicates a bug in the library. Please report the incident to the GetData developers.</p>
<dt><code>GD_E_PROTECTED</code></p>
<dd> The metadata of the fragment containing the field was protected from change. Or, the deletion of the binary data file associated with a <code>RAW</code> field was attempted and the data of the fragment was protected.</p>
<dt><code>GD_E_RAW_IO</code></p>
<dd> An error occurred while trying to close or delete the binary file associated with a <code>RAW</code> field.</p>
<dt><code>GD_E_UNKNOWN_ENCODING</code></p>
<dd> The <code>GD_DEL_DATA</code> flag was specified but the encoding scheme of the specified format file fragment is not known to the library. As a result, the library was unable to delete the binary file associated with a <code>RAW</code> field.</p>
<dt><code>GD_E_UNSUPPORTED</code></p>
<dd> The <code>GD_DEL_DATA</code> flag was specified but the encoding scheme of the specified format file fragment does not support deleting the binary file associated with a <code>RAW</code> field. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_close/">dirfile_close</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3) </p>
<h2>Index</h2>
