---
title: "get_framenum_subset(3)"
name: "get_framenum_subset"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_framenum_subset/"
description: "get_framenum_subset, get_framenum — perform a reverse look-up on a monotonic dirfile field"
---

<h2>NAME</h2>
<p> get_framenum_subset, get_framenum &#8212; perform a reverse look-up on a monotonic dirfile field</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>double get_framenum_subset(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>double </code><i>value</i><code>, off_t </code><i>field_start</i><code>, off_t </code><i>field_end</i><code>);</code></p>
<dt> <code>double get_framenum(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>,</code> <code>double </code><i>value</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_framenum_subset</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the fractional frame number at which the field specified by <i>field_code</i>, which may contain a representation suffix, equals <i>value</i>, by considering the field between the frame limits <i>field_start</i> and <i>field_end</i>. </p>
<p> If <i>field_start</i> is zero, the frame offset of the field is used as the lower limit instead (which may, in fact, be zero; see <code><a href="/docs/linux/man/3-get_frameoffset/">get_frameoffset</a></code>(3)). If <i>field_end</i> is zero, the number of frames in the dirfile, as reported by <code><a href="/docs/linux/man/3-get_nframes/">get_nframes</a></code>(3), is used instead as the upper limit. </p>
<p> The <code>get_framenum</code>() function is equivalent to calling <code>get_framenum_subset</code>() with <i>field_start</i> and <i>field_end</i> equal to zero. </p>
<p> The field must be monotonic (either increasing or decreasing) between the supplied limits. It is not required to be strictly monotonic. </p>
<p> If the value searched for lies between two sample values, the frame number returned will be calculated by linear interpolation of the field between these two samples. If more than one consecutive sample is equal to the value searched for, the fractional frame number of one of these samples will be returned, without specifying which particular one will be used. </p>
<p> If the value searched for is found to lie outside of the supplied limits, the first two or last two samples of the field will be used to linearly extrapolate the returned frame number. If these two samples happen to have the same value, positive or negative infinity will be returned. When extrapolating, this function will never consider data outside the supplied limits, even if such data exists. As a result, the extrapolated value may differ greatly from the value considering all the data. </p>
<p> All computation is done in double precision. As a result, using this function on a 64-bit integer field with more precision than a double precision floating point number, may result in an inaccurate returned value. Attempting to use this function on a complex valued field will result in an error. </p>
<p> If the field is constant across the entire range, and error results, even if the value to search for is equal to the constant value of the field. </p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the fractional frame number at which the given function would attain the supplied value, based only on that portion of the field between the given limits. This might be any number, even values outside of the supplied limits, up to and including positive or negaitve infinity. </p>
<p> On error, these functions return an IEEE-754 conforming not-a-number (NaN), and set the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> was not found.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_FIELD_TYPE</code></p>
<dd> The field specified by <i>field_code</i> was not a vector field.</p>
<dt><code>GD_E_BAD_REPR</code></p>
<dd> The representation suffix specified in <i>field_code</i>, or in one of its input fields, was not recognised.</p>
<dt><code>GD_E_BAD_SCALAR</code></p>
<dd> A scalar field used in the definition of the field was not found, or was not of scalar type.</p>
<dt><code>GD_E_DIMENSION</code></p>
<dd> A scalar field was found where a vector field was expected.</p>
<dt><code>GD_E_DOMAIN</code></p>
<dd> The specified field was complex valued, or the supplied frame range was too small. This error may also arise if data is deleted from the field as the function is executing.</p>
<dt><code>GD_E_INTERNAL_ERROR</code></p>
<dd> An internal error occurred in the library while trying to perform the task. This indicates a bug in the library. Please report the incident to the maintainer.</p>
<dt><code>GD_E_OPEN_LINFILE</code></p>
<dd> An error occurred while trying to read a LINTERP table from disk.</p>
<dt><code>GD_E_RANGE</code></p>
<dd> The specified field is constant across the specified range.</p>
<dt><code>GD_E_RAW_IO</code></p>
<dd> An error occurred while trying to open or read from a file on disk containing a raw field.</p>
<dt><code>GD_E_RECURSE_LEVEL</code></p>
<dd> Too many levels of recursion were encountered while trying to resolve <i>field_code</i>. This usually indicates a circular dependency in field specification in the dirfile.</p>
<dt><code>GD_E_UNKNOWN_ENCODING</code></p>
<dd> The encoding scheme of a RAW field could not be determined. This may also indicate that the binary file associated with the RAW field could not be found.</p>
<dt><code>GD_E_UNSUPPORTED</code></p>
<dd> Reading from dirfiles with the encoding scheme of the specified dirfile is not supported by the library. See <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5) for details on dirfile encoding schemes. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_frameoffset/">get_frameoffset</a></code>(3), <code><a href="/docs/linux/man/3-get_nframes/">get_nframes</a></code>(3). </p>
<h2>Index</h2>
