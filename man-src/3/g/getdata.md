---
title: "getdata(3)"
name: "getdata"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getdata/"
description: "getdata — retrieve data from a dirfile database"
---

<h2>NAME</h2>
<p> getdata &#8212; retrieve data from a dirfile database</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>size_t getdata(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>, off_t</code> <i>first_frame</i><code>, off_t </code><i>first_sample</i><code>, size_t </code><i>num_frames</i><code>, size_t</code> <i>num_samples</i><code>, gd_type_t </code><i>return_type</i><code>, void *</code><i>data_out</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>getdata</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> for the field <i>field_code</i>. It fetches <i>num_frames</i> frames plus <i>num_samples</i> samples from this field, starting <i>first_sample</i> samples past frame <i>first_frame</i>. The data is converted to the data type specified by <i>return_type</i>, and stored in the user-supplied buffer <i>data_out</i>. </p>
<p> The <i>field_code</i> may contain one of the representation suffixes listed in <a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a>(5). If it does, getdata will compute the appropriate complex norm before returning the data. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). The argument <i>data_out</i> must point to a valid memory location of sufficient size to hold all data requested. </p>
<p> The first sample returned will be</p>
<dl>
<dt>
<dd> <i>first_frame</i> * <i>samples_per_frame</i> + <i>first_sample</i></dl>
<p> as measured from the start of the dirfile, where <i>samples_per_frame</i> is the number of samples per frame as returned by <code><a href="/docs/linux/man/3-get_spf/">get_spf</a></code>(3). The number of samples fetched is, similarly,</p>
<dl>
<dt>
<dd> <i>num_frames</i> * <i>samples_per_frame</i> + <i>num_samples</i>.</dl>
<p> Although calling <code>getdata</code>() using both samples and frames is possible, the function is typically called with either <i>num_samples</i> and <i>first_sample</i>, or <i>num_frames</i> and <i>first_frames</i>, equal to zero. </p>
<p> The <i>return_type</i> argument should be one of the following symbols, which indicates the desired return type of the data:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>GD_UINT8</i></p>
<dd> unsigned 8-bit integer</p>
<dt><i>GD_INT8</i></p>
<dd> signed (two&#8217;s complement) 8-bit integer</p>
<dt><i>GD_UINT16</i></p>
<dd> unsigned 16-bit integer</p>
<dt><i>GD_INT16</i></p>
<dd> signed (two&#8217;s complement) 16-bit integer</p>
<dt><i>GD_UINT32</i></p>
<dd> unsigned 32-bit integer</p>
<dt><i>GD_INT32</i></p>
<dd> signed (two&#8217;s complement) 32-bit integer</p>
<dt><i>GD_UINT64</i></p>
<dd> unsigned 64-bit integer</p>
<dt><i>GD_INT64</i></p>
<dd> signed (two&#8217;s complement) 64-bit integer</p>
<dt><i>GD_FLOAT32</i></p>
<dd> IEEE-754 standard 32-bit single precision floating point number</p>
<dt><i>GD_FLOAT64</i></p>
<dd> IEEE-754 standard 64-bit double precision floating point number</p>
<dt><i>GD_COMPLEX64</i></p>
<dd> C99-conformant 64-bit single precision complex number</p>
<dt><i>GD_COMPLEX128</i></p>
<dd> C99-conformant 128-bit double precision complex number</p>
<dt><i>GD_NULL</i></p>
<dd> the null type: the database is queried as usual, but no data is returned. In this case, <i>data_out</i> is ignored and may be NULL.</dl>
</dl>
<p> The return type of the data need not be the same as the type of the data stored in the database. Type conversion will be performed as necessary to return the requested type. If the <i>field_code</i> does not indicate a representation, but conversion from a complex value to a purely real one is required, only the real portion of the requested vector will be returned. </p>
<h2>RETURN VALUE</h2>
<p> In all cases, <code>getdata</code>() returns the number of samples (not bytes) successfully read from the database. If the end-of-field is encountered before the requested number of samples have been read, a short count will result. The library does not consider this an error. Requests for data before the beginning-of-field marker, which may have been shifted from frame zero by the presence of a <code>FRAMEOFFSET</code> directive, will result in the the data being padded at the front by NaN or zero depending on whether the return type is of floating point or integral type. </p>
<p> If an error has occurred, zero is returned and the dirfile error will be set to a non-zero value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i>, or one of the fields it uses for input, was not found in the database.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> An invalid <i>dirfile</i> was supplied.</p>
<dt><code>GD_E_BAD_FIELD_TYPE</code></p>
<dd> The supplied <i>field_code</i> referred to a <code>CONST</code> or <code>STRING</code> field. The caller should use <code><a href="/docs/linux/man/3-get_constant/">get_constant</a></code>(3), or <code><a href="/docs/linux/man/3-get_string/">get_string</a></code>(3) instead.</p>
<dt><code>GD_E_BAD_REPR</code></p>
<dd> The representation suffix specified in <i>field_code</i>, or in one of the field codes it uses for input, was invalid.</p>
<dt><code>GD_E_BAD_SCALAR</code></p>
<dd> A scalar field used in the definition of the field was not found, or was not of scalar type.</p>
<dt><code>GD_E_BAD_TYPE</code></p>
<dd> An invalid <i>return_type</i> was specified.</p>
<dt><code>GD_E_DIMENSION</code></p>
<dd> A scalar field was found where a vector field was expected.</p>
<dt><code>GD_E_INTERNAL_ERROR</code></p>
<dd> An internal error occurred in the library while trying to perform the task. This indicates a bug in the library. Please report the incident to the maintainer.</p>
<dt><code>GD_E_OPEN_LINFILE</code></p>
<dd> An error occurred while trying to read a LINTERP table from disk.</p>
<dt><code>GD_E_RAW_IO</code></p>
<dd> An error occurred while trying to open or read from a file on disk containing a raw field.</p>
<dt><code>GD_E_RECURSE_LEVEL</code></p>
<dd> Too many levels of recursion were encountered while trying to resolve <i>field_code</i>. This usually indicates a circular dependency in field specification in the dirfile.</p>
<dt><code>GD_E_UNKNOWN_ENCODING</code></p>
<dd> The encoding scheme of a RAW field could not be determined. This may also indicate that the binary file associated with the RAW field could not be found.</p>
<dt><code>GD_E_UNSUPPORTED</code></p>
<dd> Reading from dirfiles with the encoding scheme of the specified dirfile is not supported by the library. See <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5) for details on dirfile encoding schemes. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>LIMITATIONS</h2>
<p> The <code>PHASE</code> field type is poorly defined, since a forward-shifted <code>PHASE</code> field will always encounter the end-of-field marker before its input field does. This has ramifications when using <code>getdata</code>() with streaming data. The Dirfile Standards make tacit admission to this problem by indicating the results of reading a <code>PHASE</code> field beyond the beginning- or end-of-field is &quot;implementation dependent&quot; (see <code><a href="/docs/linux/man/5-dirfile-format/">dirfile-format</a></code>(5)). As with any other field, <code>getdata</code>() will return a short count whenever a read from a <code>PHASE</code> field encounters the end-of-field marker. </p>
<p> Backward-shifted <code>PHASE</code> fields do not suffer from this problem, since <code>getdata</code>() pads reads past the beginning-of-field marker with NaN or zero as appropriate. Database creators who wish to use the <code>PHASE</code> field type with streaming data are encouraged to work around this limitation by only using backward-shifted <code>PHASE</code> fields, by writing <code>RAW</code> data at the maximal time lag, and then back-shifting all data which should have been written earlier. Another possible work-around is to write systematically less data to the first <code>RAW</code> field in proportion to the maximal forward phase shift. This method will work with applications which respect the database size reported by <code><a href="/docs/linux/man/3-get_nframes/">get_nframes</a></code>(3) resulting in these applications effectively ignoring all frames past the frame containing the maximally forward-shifted <code>PHASE</code> field&#8217;s end-of-field marker. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_constant/">get_constant</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_nframes/">get_nframes</a></code>(3), <code><a href="/docs/linux/man/3-get_spf/">get_spf</a></code>(3), <code><a href="/docs/linux/man/3-get_string/">get_string</a></code>(3), <code><a href="/docs/linux/man/3-putdata/">putdata</a></code>(3) </p>
<h2>Index</h2>
