---
title: "dirfile_madd(3)"
name: "dirfile_madd"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_madd/"
description: "dirfile_add, dirfile_madd — add a field to a dirfile"
---

<h2>NAME</h2>
<p> dirfile_add, dirfile_madd &#8212; add a field to a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_add(DIRFILE *</code><i>dirfile</i><code>, const gd_entry_t *</code><i>entry</i><code>);</code></p>
<dt> <code>int dirfile_madd(DIRFILE *</code><i>dirfile</i><code>, const gd_entry_t *</code><i>entry</i><code>,</code> <code>const char *</code><i>parent</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_add</code>() function adds the field described by <i>entry</i> to the dirfile specified by <i>dirfile</i>. The <code>dirfile_madd</code>() function behaves similarly, but adds the field as a metafield under the field indicated by the field code <i>parent</i>. </p>
<p> The form of <i>entry</i> is described in detail on the <code><a href="/docs/linux/man/3-get_entry/">get_entry</a></code>(3) man page. All relevant members of <i>entry</i> for the field type specified must be properly initialised. </p>
<p> When adding a metafield, the <i>entry</i>-&gt;<i>field</i> member should contain just the metafield&#8217;s name, not the fully formed <i>&lt;parent-field&gt;</i><code>/</code><i>&lt;meta-field&gt;</i> field code. Also, <code>dirfile_madd</code>() ignores the value of <i>entry</i>-&gt;<i>fragment_index</i>, and instead adds the new meta field to the same format file fragment in which the parent field is defined. </p>
<p> Fields added with this interface may contain either numerical parameters or parameters based on <code>CONST</code> fields. If an element of the <i>entry</i>-&gt;<i>scalar</i> array defined for the specified field type is non-NULL, this element will be used as the <code>CONST</code> field code, and the corresponding numerical member will be ignored, and need not be initialised. Conversely, if numerical parameters are intended, the corresponding <i>entry</i>-&gt;<i>scalar</i> elements should be set to NULL. </p>
<h2>RETURN VALUE</h2>
<p> On success, <code>dirfile_add</code>() and <code>dirfile_madd</code>() return zero. On error, -1 is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></p>
<dd> The specified dirfile was opened read-only.</p>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field name provided in <i>entry</i>-&gt;<i>field</i> contained invalid characters. Alternately, the <i>parent</i> field code was not found, or was already a metafield.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_ENTRY</code></p>
<dd> There was an error in the specification of the field described by <i>entry</i>, or the caller attempted to add a field of type <code>RAW</code> as a metafield.</p>
<dt><code>GD_E_BAD_INDEX</code></p>
<dd> The <i>entry</i>-&gt;<i>fragment_index</i> parameter was out of range.</p>
<dt><code>GD_E_BAD_TYPE</code></p>
<dd> The <i>entry</i>-&gt;<i>data_type</i> parameter provided with a <code>RAW</code> entry, or the <i>entry</i>-&gt;<i>const_type</i> parameter provided with a <code>CONST</code> entry, was invalid.</p>
<dt><code>GD_E_DUPLICATE</code></p>
<dd> The field name provided in <i>entry</i>-&gt;<i>field</i> duplicated that of an already existing field.</p>
<dt><code>GD_E_PROTECTED</code></p>
<dd> The metadata of the fragment was protected from change. Or, the creation of a <code>RAW</code> field was attempted and the data of the fragment was protected.</p>
<dt><code>GD_E_RAW_IO</code></p>
<dd> An I/O error occurred while creating an empty binary file to be associated with a newly added <code>RAW</code> field.</p>
<dt><code>GD_E_UNKNOWN_ENCODING</code></p>
<dd> The encoding scheme of the specified format file fragment is not known to the library. As a result, the library was unable to create an empty binary file to be associated with a newly added <code>RAW</code> field.</p>
<dt><code>GD_E_UNSUPPORTED</code></p>
<dd> The encoding scheme of the specified format file fragment does not support creating an empty binary file to be associated with a newly added <code>RAW</code> field. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_add_bit/">dirfile_add_bit</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_clincom/">dirfile_add_clincom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_const/">dirfile_add_const</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_cpolynom/">dirfile_add_cpolynom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_lincom/">dirfile_add_lincom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_linterp/">dirfile_add_linterp</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_multiply/">dirfile_add_multiply</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_phase/">dirfile_add_phase</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_polynom/">dirfile_add_polynom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_raw/">dirfile_add_raw</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_sbit/">dirfile_add_sbit</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_spec/">dirfile_add_spec</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_string/">dirfile_add_string</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_bit/">dirfile_madd_bit</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_clincom/">dirfile_madd_clincom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_const/">dirfile_madd_const</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_cpolynom/">dirfile_madd_cpolynom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_lincom/">dirfile_madd_lincom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_linterp/">dirfile_madd_linterp</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_multiply/">dirfile_madd_multiply</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_phase/">dirfile_madd_phase</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_polynom/">dirfile_madd_polynom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_sbit/">dirfile_madd_sbit</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_spec/">dirfile_madd_spec</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_string/">dirfile_madd_string</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_entry/">get_entry</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
