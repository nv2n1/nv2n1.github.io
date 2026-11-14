---
title: "dirfile_alter_entry(3)"
name: "dirfile_alter_entry"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_alter_entry/"
description: "dirfile_alter_entry — modify the metadata of a dirfile field"
---

<h2>NAME</h2>
<p> dirfile_alter_entry &#8212; modify the metadata of a dirfile field</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_alter_entry(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>const gd_entry_t *</code><i>entry</i><code>, int </code><i>recode</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_alter_entry</code>() function modifies the field specified by <i>field_code</i> in the dirfile specified by <i>dirfile</i> to correspond to the new parameters specified by <i>entry</i>. In addition to specifying a regular field, <i>field_code</i> may also refer to a metafield by specifying it using its full (slashed) field code. However, <i>field_code</i> should never contain a represenation suffix. </p>
<p> The form of <i>entry</i> is described in detail in the <code><a href="/docs/linux/man/3-get_entry/">get_entry</a></code>(3) man page. The <i>entry</i>-&gt;<i>field</i> and <i>entry</i>-&gt;<i>fragment_index</i> members are ignored by this function and need not be initialised. All other members appropriate to the field type of <i>field_code</i> should be initialised, except as noted below. To change the fragment index of a field, use <code><a href="/docs/linux/man/3-dirfile_move/">dirfile_move</a></code>(3). To change the name of a field, use <code><a href="/docs/linux/man/3-dirfile_rename/">dirfile_rename</a></code>(3). </p>
<p> If <i>field_code</i> specifies a <code>RAW</code> field and the <i>recode</i> argument is non-zero, the binary file associated with the field will be converted for changes in data type and samples-per-frame. If <i>recode</i> is zero, no binary file conversion will take place. </p>
<p> If <i>field_code</i> specifies a <code>LINTERP</code> field and the <i>recode</i> argument is non-zero, the look-up table file will be moved if <i>entry</i>-&gt;<i>table</i> specifies a different path. If a file with the new pathname already exists, it will be overwritten. If the field specified by <i>field_code</i> is of type other than <code>RAW</code> or <code>LINTERP</code>, the <i>recode</i> argument is ignored. </p>
<p> If <i>field_code</i> specified a <code>LINCOM</code> or <code>POLYNOM</code> field, the value of <i>entry</i>-&gt;<i>comp_scal</i> indicates whether the purely real scalar lists (<i>entry</i>-&gt;<i>a</i>, or <i>entry</i>-&gt;<i>b</i> and <i>entry</i>-&gt;<i>m</i>) or the complex valued lists (<i>entry</i>-&gt;<i>ca</i>, or <i>entry</i>-&gt;<i>cb</i> and <i>entry</i>-&gt;<i>cm</i>) will be used. The unused counterparts need not be initialised. </p>
<p> The <i>entry</i>-&gt;<i>field_type</i> member must correspond to the field type of <i>field_code</i>. This interface cannot be used to change the type of a given field. To do so, delete the old field first with <code><a href="/docs/linux/man/3-dirfile_delete/">dirfile_delete</a></code>(3), and then create a new field of the desired type with <code><a href="/docs/linux/man/3-dirfile_add/">dirfile_add</a></code>(3). </p>
<p> Some field parameters have special values which indicate no change should be made to the parameter. Specifically, if any of the string parameters, or the parameters (<i>entry</i>-&gt;<i>a</i>,~<i>entry</i>-&gt;<i>b</i>,~<i>entry</i>-&gt;<i>m</i>,~<i>entry</i>-&gt;<i>ca</i>,~<i>entry</i>-&gt;<i>,</i> or <i>entry</i>-&gt;<i>cm</i>) are NULL, the old values will be retained. Similarly, if <i>entry</i>-&gt;<i>spf</i>, <i>entry</i>-&gt;<i>n_fields</i>, or <i>entry</i>-&gt;<i>numbits</i> is zero, or if <i>entry</i>-&gt;<i>bitnum</i> is -1, or if <i>entry</i>-&gt;<i>data_type</i>, or <i>entry</i>-&gt;<i>const_type</i> are equal to <code>GD_NULL</code>, these parameters will not be modified. </p>
<p> All <i>entry</i>-&gt;<i>scalar</i> elements relevant for the given field type must be initialised to one of the following values:</p>
<dl>
<dt>*</p>
<dd> a pointer to a field code indicating a new <code>CONST</code> field to be used for the corresponding field parameter. If the parameter was previously a literal number, it will be replaced by the specified field code. If the paramter was previously a field code, the new field code will replace the old one.</p>
<dt>*</p>
<dd> a pointer the empty string (&quot;&quot;). In this case, no change is made to the field code for the corresponding field parameter: if one already existed, it is kept, otherise the correponding literal numerical parameter is used. If the value of the corresponding numerical <i>entry</i> member is the special value listed above indicating no change, no change is made to the field parameter at all.</p>
<dt>*</p>
<dd> the NULL pointer. If the corresponding field parameter was previously a field code, the field code will be deleted and a literal number used instead. In the special case when a scalar element is NULL and the corresponding numerical <i>entry</i> member contains a special value indicating no change listed above, GetData will de-reference the previous field code value and convert it into a literal number before removing the field code from the entry. </p>
</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>dirfile_alter_entry</code>() returns zero. On error, -1 is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></p>
<dd> The specified dirfile was opened read-only.</p>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> was not found. This error may also result from attempting to dereference a scalar field code which indicates a non-existant field.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_ENTRY</code></p>
<dd> One or more of the parameters specified in <i>entry</i> was invalid.</p>
<dt><code>GD_E_BAD_FIELD_TYPE</code></p>
<dd> The <i>entry</i>-&gt;<i>field_type</i> parameter did not correspond to the type of the field specified by <i>field_code</i>, or an attempt was made to modify the immutable <i>INDEX</i> field. This error may also result from attempting to dereference a scalar field code which does not indicate a <code>CONST</code> field.</p>
<dt><code>GD_E_BAD_TYPE</code></p>
<dd> The <i>entry</i>-&gt;<i>data_type</i> parameter provided with a <code>RAW</code> entry, or the <i>entry</i>-&gt;<i>const_type</i> parameter provided with a <code>CONST</code> entry, was invalid.</p>
<dt><code>GD_E_PROTECTED</code></p>
<dd> The metadata of the fragment was protected from change. Or, a request to translate the binary file associated with a <code>RAW</code> field was attempted, but the data of the fragment was protected.</p>
<dt><code>GD_E_RAW_IO</code></p>
<dd> An I/O error occurred while translating the binary file associated with a modified <code>RAW</code> field, or an I/O error occurred while attempting to rename a <code>LINTERP</code> table file.</p>
<dt><code>GD_E_UNKNOWN_ENCODING</code></p>
<dd> The encoding scheme of the specified format file fragment is not known to the library. As a result, the library was unable to translate the binary file be associated with a modified <code>RAW</code> field.</p>
<dt><code>GD_E_UNSUPPORTED</code></p>
<dd> The encoding scheme of the specified format file fragment does not support translating the empty binary file associated with a modified <code>RAW</code> field. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_alter_bit/">dirfile_alter_bit</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_clincom/">dirfile_alter_clincom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_const/">dirfile_alter_const</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_cpolynom/">dirfile_alter_cpolynom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_lincom/">dirfile_alter_lincom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_linterp/">dirfile_alter_linterp</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_multiply/">dirfile_alter_multiply</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_phase/">dirfile_alter_phase</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_polynom/">dirfile_alter_polynom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_raw/">dirfile_alter_raw</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_spec/">dirfile_alter_spec</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_delete/">dirfile_delete</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_malter_spec/">dirfile_malter_spec</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_move/">dirfile_move</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_rename/">dirfile_rename</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
