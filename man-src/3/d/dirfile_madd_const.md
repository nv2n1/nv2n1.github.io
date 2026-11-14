---
title: "dirfile_madd_const(3)"
name: "dirfile_madd_const"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_madd_const/"
description: "dirfile_madd_bit, dirfile_madd_clincom, dirfile_madd_const, dirfile_madd_cpolynom, dirfile_madd_lincom, dirfile_madd_linterp, dirfile_madd_multiply, dirfile_madd_phase, dirfile_madd_polynom, dirfil..."
---

<h2>NAME</h2>
<p> dirfile_madd_bit, dirfile_madd_clincom, dirfile_madd_const, dirfile_madd_cpolynom, dirfile_madd_lincom, dirfile_madd_linterp, dirfile_madd_multiply, dirfile_madd_phase, dirfile_madd_polynom, dirfile_madd_bit, dirfile_madd_string &#8212; add a field to a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_madd_bit(DIRFILE *</code><i>dirfile</i><code>,</code> <code>const char *</code><i>parent</i><code>, const char *</code><i>field_name</i><code>,</code> <code>const char *</code><i>in_field</i><code>, gd_bit_t </code><i>bitnum</i><code>, gd_bit_t </code><i>numbits</i><code>);</code></p>
<dt> <code>int dirfile_madd_clincom(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>parent</i><code>,</code> <code>const char *</code><i>field_name</i><code>, int </code><i>n_fields</i><code>, const char **</code><i>in_fields</i><code>,</code> <code>const double complex *</code><i>cm</i><code>, const double complex *</code><i>cb</i><code>);</code></p>
<dt> <code>int dirfile_madd_const(DIRFILE *</code><i>dirfile</i><code>,</code> <code>const char *</code><i>parent</i><code>, const char *</code><i>field_name</i><code>,</code> <code>gd_type_t </code><i>const_type</i><code>, gd_type_t </code><i>data_type</i><code>, void *</code><i>value</i><code>);</code></p>
<dt> <code>int dirfile_madd_cpolynom(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>parent</i><code>,</code> <code>const char *</code><i>field_name</i><code>, int </code><i>poly_ord</i><code>, const char *</code><i>in_field</i><code>,</code> <code>const double complex *</code><i>ca</i><code>);</code></p>
<dt> <code>int dirfile_madd_lincom(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>parent</i><code>,</code> <code>const char *</code><i>field_name</i><code>, int </code><i>n_fields</i><code>, const char **</code><i>in_fields</i><code>,</code> <code>const double *</code><i>m</i><code>, const double *</code><i>b</i><code>);</code></p>
<dt> <code>int dirfile_madd_linterp(DIRFILE *</code><i>dirfile</i><code>,</code> <code>const char *</code><i>parent</i><code>, const char *</code><i>field_name</i><code>,</code> <code>const char *</code><i>in_field</i><code>, const char *</code><i>table</i><code>);</code></p>
<dt> <code>int dirfile_madd_multiply(DIRFILE *</code><i>dirfile</i><code>,</code> <code>const char *</code><i>parent</i><code>, const char *</code><i>field_name</i><code>,</code> <code> const char *</code><i>in_field1</i><code>, const char *</code><i>in_field2</i><code>);</code></p>
<dt> <code>int dirfile_madd_polynom(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>parent</i><code>,</code> <code>const char *</code><i>field_name</i><code>, int </code><i>poly_ord</i><code>, const char *</code><i>in_field</i><code>,</code> <code>const double *</code><i>a</i><code>);</code></p>
<dt> <code>int dirfile_madd_phase(DIRFILE *</code><i>dirfile</i><code>,</code> <code>const char *</code><i>parent</i><code>, const char *</code><i>field_name</i><code>,</code> <code>const char *</code><i>in_field</i><code>, gd_shift_t </code><i>shift</i><code>);</code></p>
<dt> <code>int dirfile_madd_sbit(DIRFILE *</code><i>dirfile</i><code>,</code> <code>const char *</code><i>parent</i><code>, const char *</code><i>field_name</i><code>,</code> <code>const char *</code><i>in_field</i><code>, gd_bit_t </code><i>bitnum</i><code>, gd_bit_t </code><i>numbits</i><code>);</code></p>
<dt> <code>int dirfile_madd_string(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>parent</i><code>,</code> <code>const char *</code><i>field_name</i><code>, const char *</code><i>value</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>These functions provide alternatives to using the <code>dirfile_madd</code>() function to add a new metafield of the indicated type under the parent field given by <i>parent</i> in the dirfile specified by <i>dirfile</i>. In all of these calls, <i>field_name</i> indicates the name of the field to be added. It should not be the full <i>&lt;parent-field&gt;</i><code>/</code><i>&lt;meta-field&gt;</i> field code. The meaning and valid types of other arguments may be obtained from the <code><a href="/docs/linux/man/3-get_entry/">get_entry</a></code>(3) and <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) manual pages. </p>
<p> The <code>dirfile_madd_clincom</code>() and <code>dirfile_madd_cpolynom</code>() functions are identical to <code>dirfile_madd_lincom</code>() and <code>dirfile_madd_polynom</code>(), except they take complex scalar parameters, instead of purely real values. </p>
<p> The <code>dirfile_madd_lincom</code>() and <code>dirfile_madd_clincom</code>() functions take pointers to three arrays of length <i>n_fields</i> containing the input field names (<i>in_fields</i>), the gain factors (<i>m</i> or <i>cm</i>), and the offset terms (<i>b</i> or <i>cb</i>). Similarly, <code>dirfile_madd_polynom</code>() and <code>dirfile_madd_cpolynom</code>() take an array of length <i>poly_ord</i> + 1 containing the polynomial co-efficients (<i>a</i> or <i>ca</i>). </p>
<p> The <code>dirfile_madd_string</code>() and <code>dirfile_madd_const</code>() functions both add the field and set the value of the field to <i>value</i>. For <code>dirfile_madd_const</code>(), the <i>const_type</i> argument specifies the storage type for the const, while <i>data_type</i> specifies the data type of the value pointed to by <i>value</i>. </p>
<p> The <code>gd_bit_t</code> type is a signed 16-bit integer type. The <code>gd_shift_t</code> type is a signed 64-bit integer type. </p>
<p> All fields added with this interface must contain numerical parameters. Fields with <code>CONST</code> fields as parameters cannot be added with these functions. Those fields must be added with <code><a href="/docs/linux/man/3-dirfile_madd/">dirfile_madd</a></code>(3) or <code><a href="/docs/linux/man/3-dirfile_madd_spec/">dirfile_madd_spec</a></code>(3). </p>
<p> See <code>NOTES</code> below for information on using <code>dirfile_madd_clincom</code>() and <code>dirfile_madd_cpolynom</code>() in the C89 GetData API. </p>
<h2>RETURN VALUE</h2>
<p> On success, any of these functions returns zero. On error, -1 is returned and the dirfile error is set to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></p>
<dd> The specified dirfile was opened read-only.</p>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The <i>field_name</i> argument contained invalid characters. Alternately, the <i>parent</i> field code was not found, or was already a metafield.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_ENTRY</code></p>
<dd> One or more of the field parameters specified was invalid.</p>
<dt><code>GD_E_BAD_TYPE</code></p>
<dd> The <i>data_type</i> or <i>const_type</i> argument provided to <code>dirfile_madd_const</code>(), was invalid.</p>
<dt><code>GD_E_DUPLICATE</code></p>
<dd> The <i>field_name</i> provided duplicated that of an already existing field.</p>
<dt><code>GD_E_PROTECTED</code></p>
<dd> The metadata of the fragment was protected from change. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3). </p>
</dl>
<h2>NOTES</h2>
<p> The C89 GetData API provides different prototypes for <code>dirfile_madd_clincom</code>() and <code>dirfile_madd_cpolynom</code>(): </p>
<pre><code>
#define GETDATA_C89_API
#include &lt;getdata.h&gt;

int dirfile_madd_clincom(DIRFILE *dirfile, const char *parent,
                         const char *field_name, int n_fields, const char **in_fields,
                         const double *cm, const double *cb);
int dirfile_madd_cpolynom(DIRFILE *dirfile, const char *parent,
                          const char *field_name, int poly_ord, const char *in_field,
                          const double *ca);
</code></pre>
<dd>In this case, the array pointers passed as <i>cm</i>,~<i>cb</i> or <i>ca</i> should have twice as many (purely real) elements, consisting of alternating real and imaginary parts for the complex data. For example, <i>ca</i>[0] should be the real part of the first co-efficient, <i>ca</i>[1] the imaginary part of the first co-efficient, <i>ca</i>[2] the real part of the second co-efficient, <i>ca</i>[3] the imaginary part of the second co-efficient, and so on. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_add_bit/">dirfile_add_bit</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_const/">dirfile_add_const</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_lincom/">dirfile_add_lincom</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_linterp/">dirfile_add_linterp</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_multiply/">dirfile_add_multiply</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_phase/">dirfile_add_phase</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_add_string/">dirfile_add_string</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd/">dirfile_madd</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_madd_spec/">dirfile_madd_spec</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5) </p>
<h2>Index</h2>
