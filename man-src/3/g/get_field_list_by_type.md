---
title: "get_field_list_by_type(3)"
name: "get_field_list_by_type"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_field_list_by_type/"
description: "get_field_list_by_type — retrieve a list of fields in a dirfile"
---

<h2>NAME</h2>
<p> get_field_list_by_type &#8212; retrieve a list of fields in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>const char **get_field_list_by_type(DIRFILE *</code><i>dirfile</i><code>, gd_entype_t </code> <i>type</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_field_list_by_type</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns a read-only list of names of the all fields of the indicated type which are defined in the database. Notably, this list does not include /META subfields. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). The <i>type</i> argument should be one of the following symbols indicating the desired field type:</p>
<dl>
<dt>
<dd> <code>GD_BIT_ENTRY</code>,~<code>GD_CONST_ENTRY</code>,~<code>GD_INDEX_ENTRY</code>,~ <code>GD_LINCOM_ENTRY</code>,~<code>GD_LINTERP_ENTRY</code>,~<code>GD_MULTIPLY_ENTRY</code>,~ <code>GD_PHASE_ENTRY</code>,~<code>GD_POLYNOM_ENTRY</code>,~<code>GD_RAW_ENTRY</code>,~<code>GD_SBIT_ENTRY</code>,~ <code>GD_STRING_ENTRY</code>.</dl>
<p> The array returned will be de-allocated by a call to <code><a href="/docs/linux/man/3-dirfile_close/">dirfile_close</a></code>(3) and should not be de-allocated by the caller. The list returned should not be assumed to be in any particular order. The array is terminated by a NULL pointer. The number of fields in the array can be obtained from a call to <code><a href="/docs/linux/man/3-get_nfields_by_type/">get_nfields_by_type</a></code>(3). </p>
<p> The caller may not modify any strings in the array, or the array itself. Doing so may cause database corruption. The pointer returned is guaranteed to be valid until <code>get_field_list_by_type</code>() is called again on the same DIRFILE object with the same <i>type</i> argument, or until the array is deallocated by a call to <code><a href="/docs/linux/man/3-dirfile_close/">dirfile_close</a></code>(3). </p>
<p> For <code>CONST</code> and <code>STRING</code> field types, corresponding lists of values for may be obtained by calling <code><a href="/docs/linux/man/3-get_constants/">get_constants</a></code>(3) or <code><a href="/docs/linux/man/3-get_strings/">get_strings</a></code>(3). </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_field_list_by_type</code>() returns a pointer to an array of strings containing the names of all the fields defined in the dirfile database of the specific type. On error it returns NULL and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_constants/">get_constants</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_field_list/">get_field_list</a></code>(3), <code><a href="/docs/linux/man/3-get_mfield_list_by_type/">get_mfield_list_by_type</a></code>(3), <code><a href="/docs/linux/man/3-get_nfields_by_type/">get_nfields_by_type</a></code>(3), <code><a href="/docs/linux/man/3-get_strings/">get_strings</a></code>(3) </p>
<h2>Index</h2>
