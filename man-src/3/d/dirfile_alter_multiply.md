---
title: "dirfile_alter_multiply(3)"
name: "dirfile_alter_multiply"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_alter_multiply/"
description: "dirfile_alter_bit, dirfile_alter_clincom, dirfile_alter_const, dirfile_alter_cpolynom, dirfile_alter_lincom, dirfile_alter_linterp, dirfile_alter_multiply, dirfile_alter_phase, dirfile_alter_polyno..."
---

<h2>NAME</h2>
<p> dirfile_alter_bit, dirfile_alter_clincom, dirfile_alter_const, dirfile_alter_cpolynom, dirfile_alter_lincom, dirfile_alter_linterp, dirfile_alter_multiply, dirfile_alter_phase, dirfile_alter_polynom, dirfile_alter_raw, dirfile_alter_sbit &#8212; modify a field in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_alter_bit(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>const char *</code><i>in_field</i><code>, gd_bit_t </code><i>bitnum</i><code>, gd_bit_t </code><i>numbits</i><code>);</code></p>
<dt> <code>int dirfile_alter_clincom(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>int </code><i>n_fields</i><code>, const char **</code><i>in_fields</i><code>, const double complex *</code><i>cm</i><code>,</code> <code>const double complex *</code><i>cb</i><code>);</code></p>
<dt> <code>int dirfile_alter_const(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>gd_type_t </code><i>const_type</i><code>);</code></p>
<dt> <code>int dirfile_alter_cpolynom(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>int </code><i>poly_ord</i><code>, const char *</code><i>in_field</i><code>, const double complex *</code><i>ca</i><code>);</code></p>
<dt> <code>int dirfile_alter_lincom(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>int </code><i>n_fields</i><code>, const char **</code><i>in_fields</i><code>, const double *</code><i>m</i><code>,</code> <code>const double *</code><i>b</i><code>);</code></p>
<dt> <code>int dirfile_alter_linterp(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>const char *</code><i>in_field</i><code>, const char *</code><i>table</i><code>, int </code><i>rename_table</i><code>);</code></p>
<dt> <code>int dirfile_alter_multiply(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>const char *</code><i>in_field1</i><code>, const char *</code><i>in_field2</i><code>);</code></p>
<dt> <code>int dirfile_alter_phase(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>const char *</code><i>in_field</i><code>, gd_shift_t </code><i>shift</i><code>);</code></p>
<dt> <code>int dirfile_alter_polynom(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>int </code><i>poly_ord</i><code>, const char *</code><i>in_field</i><code>, const double *</code><i>ca</i><code>);</code></p>
<dt> <code>int dirfile_alter_raw(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>gd_type_t </code><i>data_type</i><code>, gd_spf_t </code><i>spf</i><code>, int </code><i>recode</i><code>);</code></p>
<dt> <code>int dirfile_alter_sbit(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>const char *</code><i>in_field</i><code>, gd_bit_t </code><i>bitnum</i><code>, gd_bit_t </code><i>numbits</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>These functions provide alternatives to using the <code><a href="/docs/linux/man/3-dirfile_alter_entry/">dirfile_alter_entry</a></code>(3) function to modify a field of the indicated type in the dirfile specified by <i>dirfile</i>. In all of these calls, <i>field_code</i> indicates the the field to be modified, which may be a regular field, or a metafield specified by its full (slashed) field code, but should not contain a representtion suffix. The meaning and valid types of other arguments may be obtained from the <code><a href="/docs/linux/man/3-get_entry/">get_entry</a></code>(3) and <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) manual pages. </p>
<p> The <code>dirfile_alter_clincom</code>() and <code>dirfile_alter_cpolynom</code>() functions are identical to <code>dirfile_alter_lincom</code>() and <code>dirfile_alter_polynom</code>(), except they take complex scalar parameters, instead of purely real values. This only matters for the input of <i>new</i> parameters; if the scalar parameters are not changed (by passing NULL instead of a list of scalars), the functions can be used interchangeably, regardless of whether the altered field has complex scalar parameters or not. </p>
<p> If the corresponding parameters are to be changed, the <code>dirfile_alter_lincom</code>() and <code>dirfile_alter_clincom</code>() functions take pointers to three arrays of length <i>n_fields</i> containing the input field names (<i>in_fields</i>), the gain factors (<i>m</i> or <i>cm</i>), and the offset terms (<i>b</i> or <i>cb</i>). Similarly, <code>dirfile_alter_polynom</code>() and <code>dirfile_alter_cpolynom</code>() take an array of length <i>poly_ord</i> + 1 containing the polynomial co-efficients (<i>a</i> or <i>ca</i>). </p>
<p> Some field parameters have special values which indicate no change should be made to the parameter. Specifically, if any of the string parameters or <i>m</i>,~<i>b</i>, or <i>a</i> (<i>cm</i>,~<i>cb</i>, or <i>ca</i>) are NULL, the old values will be retained. Similarly, if <i>spf</i>, <i>n_fields</i>, or <i>numbits</i> is zero, or if <i>bitnum</i> is -1, or if <i>data_type</i>, or <i>const_type</i> are equal to <code>GD_NULL</code>, these parameters will not be modified. </p>
<p> All field parameters introduced with this interface must contain numerical parameters. Field parameters which are <code>CONST</code> cannot be introduced with these functions. To do that, use <code><a href="/docs/linux/man/3-dirfile_alter_entry/">dirfile_alter_entry</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_spec/">dirfile_alter_spec</a></code>(3) or <code><a href="/docs/linux/man/3-dirfile_malter_spec/">dirfile_malter_spec</a></code>(3), as appropriate. </p>
<p> If <i>rename_table</i> is non-zero, the look-up table referenced by the <code>LINTERP</code> field will be renamed to the path given by <i>table</i>. If <i>recode</i> is non-zero, the binary file associated with the <code>RAW</code> field will be re-encoded to reflect the new field parameters. </p>
<p> See <code>NOTES</code> below for information on using <code>dirfile_alter_clincom</code>() and <code>dirfile_alter_cpolynom</code>() in the C89 GetData API. </p>
<h2>RETURN VALUE</h2>
<p> On success, any of these functions returns zero. On error, -1 is returned and the dirfile error is set to a non-zero error value. Possible error values are: </p>
<p> The <code>gd_bit_t</code> type is a signed 16-bit integer type. The <code>gd_shift_t</code> type is a signed 64-bit integer type. The <code>gd_spf_t</code> type is an unsigned 16-bit integer type.</p>
<dl>
<dt><code>GD_E_ACCMODE</code></p>
<dd> The specified dirfile was opened read-only.</p>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> was not found.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_ENTRY</code></p>
<dd> One or more of the field parameters specified was invalid.</p>
<dt><code>GD_E_BAD_FIELD_TYPE</code></p>
<dd> The field specified by <i>field_code</i> was of the wrong type for the function called.</p>
<dt><code>GD_E_BAD_TYPE</code></p>
<dd> The <i>data_type</i> or <i>const_type</i> argument was invalid.</p>
<dt><code>GD_E_PROTECTED</code></p>
<dd> The metadata of the fragment was protected from change. Or, a request to translate the binary file associated with a <code>RAW</code> field was attempted, but the data of the fragment was protected.</p>
<dt><code>GD_E_RAW_IO</code></p>
<dd> An I/O error occurred while translating the binary file associated with a modified <code>RAW</code> field, or an I/O error occurred while attempting to rename a <code>LINTERP</code> table file.</p>
<dt><code>GD_E_UNKNOWN_ENCODING</code></p>
<dd> The encoding scheme of the specified format file fragment is not known to the library. As a result, the library was unable to translate the binary file be associated with a modified <code>RAW</code> field.</p>
<dt><code>GD_E_UNSUPPORTED</code></p>
<dd> The encoding scheme of the specified format file fragment does not support translating the empty binary file associated with a modified <code>RAW</code> field. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3). </p>
</dl>
<h2>NOTES</h2>
<p> The C89 GetData API provides different prototypes for <code>dirfile_alter_clincom</code>() and <code>dirfile_alter_cpolynom</code>(): </p>
<pre><code>
#define GETDATA_C89_API
#include &lt;getdata.h&gt;

int dirfile_alter_clincom(DIRFILE *dirfile, const char *field_code,
                          int n_fields, const char **in_fields, const double *cm,
                          const double *cb);
int dirfile_alter_cpolynom(DIRFILE *dirfile, const char *field_code,
                           int poly_ord, const char *in_fields, const double *ca);
</code></pre>
<dd>In this case, the array pointers passed as <i>cm</i>,~<i>cb</i> or <i>ca</i> should have twice as many (purely real) elements, consisting of alternating real and imaginary parts for the complex data. For example, <i>ca</i>[0] should be the real part of the first co-efficient, <i>ca</i>[1] the imaginary part of the first co-efficient, <i>ca</i>[2] the real part of the second co-efficient, <i>ca</i>[3] the imaginary part of the second co-efficient, and so on. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_alter_entry/">dirfile_alter_entry</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_alter_spec/">dirfile_alter_spec</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_malter_spec/">dirfile_malter_spec</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
