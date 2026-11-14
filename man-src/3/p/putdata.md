---
title: "putdata(3)"
name: "putdata"
section: "3"
letter: "p"
url: "/docs/linux/man/3-putdata/"
description: "putdata — write data to a dirfile database"
---

<p>putdata &#8212; write data to a dirfile database</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;getdata.h&gt;

size_t putdata(DIRFILE *dirfile, const char *field_code, off_t

                                                             first_frame,
               off_t first_sample, size_t num_frames, size_t

                                                          num_samples,
               gd_type_t data_type, const void *data_in);</code></pre>
<h2>Description</h2>
<dd>The <code>putdata</code>() function writes data to a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> for the field <i>field_code</i>, which may not contain a representation suffix. It writes <i>num_frames</i> frames plus <i>num_samples</i> samples to this field, starting <i>first_sample</i> samples past frame <i>first_frame</i>. The data is read from the user-supplied buffer <i>data_in,</i> which is has a data type specified by <i>data_type</i>. This interface cannot write to field representations. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<p> The first sample written will be</p>
<dl>
<dd><i>first_frame</i> * <i>samples_per_frame</i> + <i>first_sample</i></dl>
<p> as measured from the start of the dirfile, where <i>samples_per_frame</i> is the number of samples per frame as returned by <code><a href="/docs/linux/man/3-get_spf/">get_spf</a></code>(3). The number of samples which <code>putdata</code>() attempts to write is, similarly,</p>
<dl>
<dd><i>num_frames</i> * <i>samples_per_frame</i> + <i>num_samples</i>.</dl>
<p> Although calling <code>putdata</code>() using both samples and frames is possible, the function is typically called with either <i>num_samples</i> and <i>first_sample</i>, or <i>num_frames</i> and <i>first_frames</i>, equal to zero. </p>
<p> The <i>data_type</i> argument should be one of the following symbols, which indicates the type of the input data:</p>
<dl>
<dd>
<dl>
<dt><i>GD_UINT8</i></p>
<dd>unsigned 8-bit integer</p>
<dt><i>GD_INT8</i></p>
<dd>signed (two&#8217;s complement) 8-bit integer</p>
<dt><i>GD_UINT16</i></p>
<dd>unsigned 16-bit integer</p>
<dt><i>GD_INT16</i></p>
<dd>signed (two&#8217;s complement) 16-bit integer</p>
<dt><i>GD_UINT32</i></p>
<dd>unsigned 32-bit integer</p>
<dt><i>GD_INT32</i></p>
<dd>signed (two&#8217;s complement) 32-bit integer</p>
<dt><i>GD_UINT64</i></p>
<dd>unsigned 64-bit integer</p>
<dt><i>GD_INT64</i></p>
<dd>signed (two&#8217;s complement) 64-bit integer</p>
<dt><i>GD_FLOAT32</i>~or~<i>GD_FLOAT</i></p>
<dd>IEEE-754 standard 32-bit single precision floating point number</p>
<dt><i>GD_FLOAT64</i>~or~<i>GD_DOUBLE</i></p>
<dd>IEEE-754 standard 64-bit double precision floating point number</dl>
</dl>
<p> The type of the input data need not be the same as the type of the data stored in the database. Type conversion will be performed as necessary to write the appropriate type. The argument <i>data_in</i> must point to a valid memory location of containing all the data to be written.</p>
<h2>Return Value</h2>
<p>In all cases, <code>putdata</code>() returns the number of samples (not bytes) successfully written to the database, which may be zero if an error has occurred. </p>
<p> If an error has occurred, the dirfile error will be set to a non-zero value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ACCMODE</code></p>
<dd>The specified <i>dirfile</i> was opened read-only.</p>
<dt><code>GD_E_ALLOC</code></p>
<dd>The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd>The field specified by <i>field_code</i>, or one of the fields it uses for input, was not found in the database.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd>An invalid <i>dirfile</i> was supplied.</p>
<dt><code>GD_E_BAD_FIELD_TYPE</code></p>
<dd>Either the field specified by <i>field_code</i>, or one of the fields it uses for input, was of <code>MULTIPLY</code> type, or <code>LINCOM</code> type with more than one input fields. In this case, <code>putdata</code>() has no knowledge on how to partition the input data. Alternately, the caller may have attempted to write to the implicit INDEX field, which is not possible.</p>
<dt><code>GD_E_BAD_REPR</code></p>
<dd>The representation suffix specified in <i>field_code</i> was not recognised, or an attempt was made to write to a field representation, instead of the underlying field.</p>
<dt><code>GD_E_BAD_TYPE</code></p>
<dd>An invalid <i>data_type</i> was specified.</p>
<dt><code>GD_E_INTERNAL_ERROR</code></p>
<dd>An internal error occurred in the library while trying to perform the task. This indicates a bug in the library. Please report the incident to the maintainer.</p>
<dt><code>GD_E_OPEN_LINFILE</code></p>
<dd>An error occurred while trying to read a LINTERP table from disk.</p>
<dt><code>GD_E_PROTECTED</code></p>
<dd>The data of the <code>RAW</code> field backing <i>field_code</i> was protected from change by a PROTECT directive.</p>
<dt><code>GD_E_RANGE</code></p>
<dd>An attempt was made to write data before the beginning-of-frame marker for <i>field_code</i>, or the raw field it depends on.</p>
<dt><code>GD_E_RAW_IO</code></p>
<dd>An error occurred while trying to open, read from, or write to a file on disk containing a raw field.</p>
<dt><code>GD_E_RECURSE_LEVEL</code></p>
<dd>Too many levels of recursion were encountered while trying to resolve <i>field_code</i>. This usually indicates a circular dependency in field specification in the dirfile.</p>
<dt><code>GD_E_UNSUPPORTED</code></p>
<dd>Reading from dirfiles with the encoding scheme of the specified dirfile is not supported by the library. See <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5) for details on dirfile encoding schemes. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_spf/">get_spf</a></code>(3) </p>
