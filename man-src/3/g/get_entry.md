---
title: "get_entry(3)"
name: "get_entry"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_entry/"
description: "get_entry — retrieve a dirfile field’s metadata"
---

<h2>NAME</h2>
<p> get_entry &#8212; retrieve a dirfile field&#8217;s metadata</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int get_entry(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>gd_entry_t *</code><i>entry</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_entry</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the metadata associated with the field specified by <i>field_code</i>. If <i>field_code</i> contains a valid representation suffix, the suffix will be ignored. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<p> The entry will be stored in the gd_entry_t structure indicated by the <i>entry</i> argument, which must be allocated by the caller. Members available in this structure depend on the field type of the field queried. See below for a complete description of this data type. </p>
<p> Strings members in <i>entry</i> filled by this function (variously, depending on field type: <i>field</i>, the elements of the <i>in_fields</i>[] array, <i>table</i>; see below) will by dynamically allocated by <code>get_entry</code>() and should not point to allocated memory locations before calling this function. Only strings provided by the gd_entry_t for the particular field type described will be allocated. These strings should be deallocated with <code><a href="/docs/linux/man/3-free/">free</a></code>(3) by the caller once they are no longer needed. The <code><a href="/docs/linux/man/3-dirfile_free_entry_strings/">dirfile_free_entry_strings</a></code>(3) function is provided as a convenience to do this. </p>
<p> The returned <i>entry</i> structure, including strings and their pointers may be freely modified by the caller. </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_entry</code>() returns zero, and writes the field metadata in the supplied gd_entry_t buffer. On error, the supplied gd_entry_t buffer is not modified. In this case, <code>get_entry</code>() returns -1 and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> was not found in the database.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_REPR</code></p>
<dd> The representation suffix specified in <i>field_code</i> was not recognised.</p>
<dt><code>GD_E_BAD_SCALAR</code></p>
<dd> A scalar parameter used in the definition of the field was invalid. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>THE ENTRY TYPE</h2>
<p> Members available in the gd_entry_t structure depend on the field type described. All gd_entry_t objects are guaranteed to have at least: </p>
<pre><code>
typedef struct {
    ... const char *field;  /* field code */
    gd_entype_t field_type; /* field type */
    int fragment_index;     /* format file fragment index */
    ...
} gd_entry_t;
</code></pre>
<p> The <i>field</i> member is the field code of the entry (i.e. its string name). If the call to <code><a href="/docs/linux/man/3-get_entry/">get_entry</a></code>(3) is successful, this will be the field name specified as part of the <i>field_code</i> argument. The <i>field_type</i> member indicates the field type of the entry. This is an integer type equal to one of the following symbols:</p>
<dl>
<dt>
<dd> <code>GD_BIT_ENTRY</code>,~<code>GD_CONST_ENTRY</code>,~<code>GD_INDEX_ENTRY</code>,~ <code>GD_LINCOM_ENTRY</code>,~<code>GD_LINTERP_ENTRY</code>,~<code>GD_MULTIPLY_ENTRY</code>,~ <code>GD_PHASE_ENTRY</code>,~<code>GD_POLYNOM_ENTRY</code>,~<code>GD_RAW_ENTRY</code>,~<code>GD_SBIT_ENTRY</code>,~ <code>GD_STRING_ENTRY</code>. <code>GD_INDEX_ENTRY</code> is a special field type used only for the implicit <i>INDEX</i> field. The meaning of the other symbols should be self-explanatory. The <i>fragment_index</i> member indicates the format file fragment in which this field is defined. This is an integer index to the Dirfile&#8217;s list of parsed format file fragments. The name of the file corresponding to <i>fragment_index</i> may be obtained by calling <code><a href="/docs/linux/man/3-get_fragmentname/">get_fragmentname</a></code>(3). A value of zero for this field indicates that the field is defined in the primary format file, the file called <code>format</code> in the root dirfile directory (see <i><a href="/docs/linux/man/5-dirfile/">dirfile</a></i>(5)). Remaining fields in the gd_entry_t structure depend on the value of <i>field_type</i>. Callers are advised to check <i>field_type</i> before attempting to access the remaining members. Members for different field types may be stored in the same physical location in core. Accordingly, attempting to access a member not declared for the appropriate field type will have unspecified results. </p>
</dl>
<h3>BIT and SBIT Members</h3>
<p> A gd_entry_t describing a <code>BIT</code> or <code>SBIT</code> entry, will also provide: </p>
<p>typedef struct {<br />
    &#8230; const char *in_fields[1]; /* input field code */<br />
    const char *scalar[2];        /* parameter field codes */<br />
    gd_bit_t bitnum;              /* first bit */<br />
    gd_bit_t numbits;             /* bit length */<br />
    &#8230;<br />
} gd_entry_t;<br />
 The <i>in_fields</i> member is an array of length one containing the input field code. The <i>scalar</i> member is an array of length two containing the field codes specifying <i>bitnum</i> and <i>numbits</i>, or NULLs if numeric literal parameters were used. The <i>bitnum</i> member indicates the number of the first bit (counted from zero) extracted from the input. The <i>gd_bit_t</i> type is a signed 16-bit integer type. If this value was specified as a <code>CONST</code> field code, this will be the numerical value of that field, and <i>scalar</i>[0] will contain the field code itself, otherwise <i>scalar</i>[0] will be NULL. The <i>numbits</i> member indicates the number of bits which are extracted from the input. If this value was specified as a <code>CONST</code> field code, this will be the numerical value of that field, and <i>scalar</i>[1] will contain the field code itself, otherwise <i>scalar</i>[1] will be NULL. </p>
<h3>CONST Members</h3>
<p> A gd_entry_t describing a <code>CONST</code> entry, will also provide: </p>
<p>typedef struct {<br />
    &#8230; gd_type_t const_type; /* data type in format file */<br />
    &#8230;<br />
} gd_entry_t;<br />
 The <i>const_type</i> member indicates the data type of the constant value stored in the format file metadata. See <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3) for a list of valid values that a variable of type <code>gd_type_t</code> may take. </p>
<h3>INDEX Members</h3>
<p> A gd_entry_t describing an <code>INDEX</code> entry, which is used only for the implicit <i>INDEX</i> field, provides no additional data. </p>
<h3>LINCOM Members</h3>
<p> A gd_entry_t describing a <code>LINCOM</code> entry, will also provide: </p>
<p>typedef struct {<br />
    &#8230; int n_fields;                      /* # of input fields */<br />
    int comp_scal;                         /* complex scalar flag */<br />
    const char *in_fields[GD_MAX_LINCOM];  /* input field code(s) */<br />
    const char *scalar[2 * GD_MAX_LINCOM]; /* param. field codes */<br />
    double complex cm[GD_MAX_LINCOM];      /* scale factor(s) */<br />
    double m[GD_MAX_LINCOM];               /* scale factor(s) */<br />
    double complex cb[GD_MAX_LINCOM];      /* offset terms(s) */<br />
    double b[GD_MAX_LINCOM];               /* offset terms(s) */<br />
    &#8230;<br />
} gd_entry_t;<br />
 The <i>n_fields</i> member indicates the number of input fields. It will be between one and <code>GD_MAX_LINCOM</code> inclusive, which is defined in getdata.h to the maximum number of input fields permitted by a <code>LINCOM</code>. The <i>comp_scal</i> member is non-zero if any of the scale factors or offset terms have a non-zero imaginary part. (That is, if comp_scal is zero, the elements of <i>cm</i>~and~<i>cb</i> equal the corresponding elements of <i>m</i>~and~<i>b</i>.) members.) The <i>in_fields</i> member is an array of length <code>GD_MAX_LINCOM</code> containing the input field code(s). Only the first <i>n_fields</i> elements of this array are initialised. The remaining elements contain uninitialised data. The <i>scalar</i> member is an array of length twice <code>GD_MAX_LINCOM</code> containing the field codes specifying the slope factors and offset terms for the field, or NULLs if numberical literal parameters were used. The first <code>GD_MAX_LINCOM</code> array elements contain the scale factors. The remaining <code>GD_MAX_LINCOM</code> array elements contain the offset terms. Array elements <i>scalar</i>[<i>i</i>] and <i>scalar</i>[<i>i</i> + <code>GD_MAX_LINCOM</code>], for <i>i</i>~&gt;=~<i>n_fields</i>, contain uninitialised data. The <i>cm</i> and <i>cb</i> members are arrays of the scale factor(s) and offset term(s) for the <code>LINCOM</code>. Only the first <i>n_fields</i> elements of these array contain meaningful data. If any of these values were specified as a <code>CONST</code> field code, this will be the numerical value of that field. The field code corresponding to <i>cm</i>[<i>i</i>] will be stored in <i>scalar</i>[<i>i</i>] and the field code associated with <i>cb</i>[<i>i</i>] will be stored in <i>scalar</i>[<i>i</i> + <code>GD_MAX_LINCOM</code>]. Otherwise the corresponding <i>scalar</i> member will be NULL. See <code>NOTES</code> below on changes to the declaration of <i>cm</i> and <i>cb</i> when using the C89 GetData API. The elements of <i>m</i> and <i>b</i> are the real parts of the corresponding elements of <i>cm</i> and <i>cb</i>. </p>
<h3>LINTERP Members</h3>
<p> A gd_entry_t describing a <code>LINTERP</code> entry, will also provide: </p>
<p>typedef struct {<br />
    &#8230; const char *table         /* linterp table filename */<br />
        const char *in_fields[1]; /* input field code */<br />
    &#8230;<br />
} gd_entry_t;<br />
 The <i>table</i> member is the pathname to the look up table on disk. The <i>in_fields</i> member is an array of length one containing the input field code. </p>
<h3>MULTIPLY Members</h3>
<p> A gd_entry_t describing a <code>MULTIPLY</code> entry, will also provide: </p>
<p>typedef struct {<br />
    &#8230; const char *in_fields[2]; /* input field codes */<br />
    &#8230;<br />
} gd_entry_t;<br />
 The <i>in_fields</i> member is an array of length two containing the input field codes. </p>
<h3>PHASE Members</h3>
<p> A gd_entry_t describing a <code>PHASE</code> entry, will also provide: </p>
<p>typedef struct {<br />
    &#8230; const char *in_fields[1]; /* input field code */<br />
    const char *scalar[1];        /* parameter field codes */<br />
    gd_shift_t shift;             /* phase shift */<br />
    &#8230;<br />
} gd_entry_t;<br />
 The <i>in_fields</i> member is an array of length one containing the input field code. The <i>scalar</i> member is an array of length one containing the field code specifying <i>shift</i>, or NULL if a numeric literal parameter was used. The <i>shift</i> member indicates the shift in samples. The <i>gd_shift_t</i> type is a 64-bit signed integer type. A positive value indicates a shift forward in time (towards larger frame numbers). If this value was specified as a <code>CONST</code> field code, this will be the numerical value of that field, and <i>scalar</i>[0] will contain the field code itself, otherwise <i>scalar</i>[0] will be NULL. </p>
<h3>POLYNOM Members</h3>
<p> A gd_entry_t describing a <code>POLYNOM</code> entry, will also provide: </p>
<p>typedef struct {<br />
    &#8230; int poly_ord;         /* polynomial order */<br />
    int comp_scal;            /* complex scalar flag */<br />
    const char *in_fields[1]; /* input field code(s) */<br />
    const char *scalar[GD_MAX_POLY_ORD + 1];<br />
    /* co-eff. field codes */<br />
    double complex ca[GD_MAX_POLY_ORD + 1]; /* co-efficients(s) */<br />
    double a[GD_MAX_POLY_ORD + 1];          /* co-efficients(s) */<br />
    &#8230;<br />
} gd_entry_t;<br />
 The <i>poly_ord</i> member indicates the order of the polynomial. It will be between one and <code>GD_MAX_POLY_ORD</code> inclusive, which is defined in getdata.h to the maximum order of polynomial permitted by a <code>POLYNOM</code>. The <i>comp_scal</i> member is non-zero if any of the co-efficients have a non-zero imaginary part. (That is, if comp_scal is zero, the elements of <i>ca</i> equal the corresponding elements of <i>a</i>.) The <i>in_fields</i> member is an array of length one containing the input field code. The <i>scalar</i> member is an array of length one more than <code>GD_MAX_POLYORD</code> containing the field codes specifying the co-efficients for the field, or NULLs if numberical literal parameters were used. Only the first <i>poly_ord</i> + 1 elements are initialised. The remaining elements contain uninitialised data. The <i>ca</i> members are arrays of the co-efficient(s) for the <code>POLYNOM</code>. Only the first <i>poly_ord</i> + 1 elements of this array contains meaningful data. If any of these values were specified as a <code>CONST</code> field code, this will be the numerical value of that field. The field code corresponding to <i>ca</i>[<i>i</i>] will be stored in <i>scalar</i>[<i>i</i>]. Otherwise the corresponding <i>scalar</i> member will be NULL. See <code>NOTES</code> below on changes to the declaration of <i>ca</i> when using the C89 GetData API. The elements of <i>a</i> are the real parts of the corresponding elements of <i>ca</i>. </p>
<h3>RAW Members</h3>
<p> A gd_entry_t describing a <code>RAW</code> entry, will also provide: </p>
<p>typedef struct {<br />
    &#8230; const char *scalar[1]; /* parameter field codes */<br />
    gd_spf_t spf;              /* samples per frame on disk */<br />
    gd_type_t data_type;       /* data type on disk */<br />
    &#8230;<br />
} gd_entry_t;<br />
 The <i>scalar</i> member is an array of length one containing the field code specifying <i>spf</i>, or NULL if a numeric literal parameter was used. The <i>spf</i> member contains the samples per frame of the binary data on disk. The <i>gd_spf_t</i> type is an unsigned 16-bit integer type. If this value was specified as a <code>CONST</code> field code, this will be the numerical value of that field, and <i>scalar</i>[0] will contain the field code itself, otherwise <i>scalar</i>[0] will be NULL. The <i>data_type</i> member indicates the data type of the binary data on disk. See <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3) for a list of valid values that a variable of type <code>gd_type_t</code> may take. </p>
<h3>STRING Members</h3>
<p> A gd_entry_t describing a <code>STRING</code> entry provides no additional data. </p>
<h2>NOTES</h2>
<p> When using the C89 GetData API (by defining <code>GETDATA_C89_API</code> before including getdata.h), the complex valued array members of gd_entry_t used in the specification of <code>LINCOM</code> and <code>POLYNOM</code> entries will be replaced by purely real arrays. These will have the prototypes such as: </p>
<pre><code>
double cm[GD_MAX_LINCOM][2];
double cb[GD_MAX_LINCOM][2];
double ca[GD_MAX_POLY_ORD + 1][2];
</code></pre>
<p> The first element of the two element array is the real part of the complex number, and the second element is the imaginary part. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_free_entry_strings/">dirfile_free_entry_strings</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_field_list/">get_field_list</a></code>(3), <code><a href="/docs/linux/man/3-get_fragmentname/">get_fragmentname</a></code>(3), <code><a href="/docs/linux/man/3-get_raw_filename/">get_raw_filename</a></code>(3) </p>
<h2>Index</h2>
