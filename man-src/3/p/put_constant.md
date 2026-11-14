---
title: "put_constant(3)"
name: "put_constant"
section: "3"
letter: "p"
url: "/docs/linux/man/3-put_constant/"
description: "put_constant — retrieve a scalar constant from a dirfile database"
---

<p>put_constant &#8212; retrieve a scalar constant from a dirfile database</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;getdata.h&gt;

int put_constant(DIRFILE *dirfile, const char *field_code,

                 gd_type_t data_type, const void *data_in);</code></pre>
<h2>Description</h2>
<dd>The <code>put_constant</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and sets the <code>CONST</code> scalar <i>field_code ,</i> which may not contain a representation suffix, to the value specified in <i>data_in</i>, which should be of the type indicated by <i>data_type</i>. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<p> The <i>data_type</i> argument should be one of the following symbols, which indicates the desired return type of the data:</p>
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
<p> The data type of the supplied value need not be the same as the type of the storage type of the constant in the database. Type conversion will be performed as necessary to return the requested type. The argument <i>data_out</i> must point to valid data type of the specified type. </p>
<p> Because constant values are stored in the dirfile metadata, the new value of <i>field_code</i> won&#8217;t be written to disk until the dirfile metadata is flushed with <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), or until the dirfile is closed.</p>
<h2>Return Value</h2>
<p>On success, <code>put_constant</code>() returns zero. On error, it returns -1 and sets the dirfile error to a non-zero value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_CODE</code></p>
<dd>The field specified by <i>field_code</i> was not found in the database.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd>An invalid <i>dirfile</i> was supplied.</p>
<dt><code>GD_E_BAD_FIELD_TYPE</code></p>
<dd>The supplied <i>field_code</i> referred to a field of type other than <code>CONST</code>. The caller should use <code><a href="/docs/linux/man/3-putdata/">putdata</a></code>(3), or <code><a href="/docs/linux/man/3-put_string/">put_string</a></code>(3) instead.</p>
<dt><code>GD_E_BAD_REPR</code></p>
<dd>The representation suffix specified in <i>field_code</i> was not recognised.</p>
<dt><code>GD_E_BAD_TYPE</code></p>
<dd>An invalid <i>data_type</i> was specified.</p>
<dt><code>GD_E_INTERNAL_ERROR</code></p>
<dd>An internal error occurred in the library while trying to perform the task. This indicates a bug in the library. Please report the incident to the maintainer.</p>
<dt><code>GD_E_PROTECTED</code></p>
<dd>The fragment containing the constant was protected from change. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered may be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_constant/">get_constant</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-put_string/">put_string</a></code>(3), <code><a href="/docs/linux/man/3-putdata/">putdata</a></code>(3) </p>
