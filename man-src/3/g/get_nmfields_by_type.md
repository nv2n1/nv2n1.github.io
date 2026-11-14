---
title: "get_nmfields_by_type(3)"
name: "get_nmfields_by_type"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_nmfields_by_type/"
description: "get_nmfields_by_type — report the number of fields of a given type in a dirfile"
---

<h2>NAME</h2>
<p> get_nmfields_by_type &#8212; report the number of fields of a given type in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>unsigned int get_nmfields_by_type(DIRFILE *</code><i>dirfile</i><code>,</code> <code>const char *</code><i>parent</i><code>, gd_entype_t </code><i>type</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_nmfields_by_type</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the number of metafields defined in the database for the supplied parent field. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). The <i>type</i> argument should be one of the following symbols indicating the type of field to count:</p>
<dl>
<dt>
<dd> <code>GD_LINCOM_ENTRY</code>,~<code>GD_LINTERP_ENTRY</code>,~<code>GD_BIT_ENTRY</code>,~ <code>GD_MULTIPLY_ENTRY</code>,~<code>GD_PHASE_ENTRY</code>,~<code>GD_CONST_ENTRY</code>,~ <code>GD_STRING_ENTRY</code>,~<code>GD_INDEX_ENTRY</code> </p>
</dl>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_nmfields_by_type</code>() returns the number of defined metafields for the given parent. On error, it returns zero and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The supplied parent field code was not found, or referred to a metafield itself.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_mfield_list_by_type/">get_mfield_list_by_type</a></code>(3), <code><a href="/docs/linux/man/3-get_nmfields/">get_nmfields</a></code>(3), <code><a href="/docs/linux/man/3-get_nfields_by_type/">get_nfields_by_type</a></code>(3) </p>
<h2>Index</h2>
