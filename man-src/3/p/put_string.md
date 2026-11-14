---
title: "put_string(3)"
name: "put_string"
section: "3"
letter: "p"
url: "/docs/linux/man/3-put_string/"
description: "put_string — retrieve a string from a dirfile database"
---

<p>put_string &#8212; retrieve a string from a dirfile database</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;getdata.h&gt;

int put_string(DIRFILE *dirfile, const char *field_code,

               const char *data_in);</code></pre>
<h2>Description</h2>
<dd>The <code>put_string</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and sets the <code>STRING</code> <i>field_code ,</i> which should not contain a representation suffix, to the value specified in <i>data_in</i>. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<p> Because string values are stored in the dirfile metadata, the new value of <i>field_code</i> won&#8217;t be written to disk until the dirfile metadata is flushed with <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), or until the dirfile is closed.</p>
<h2>Return Value</h2>
<p>On success, <code>put_string</code>() returns the length of the string stored, including the trailing NUL character. On error, it returns 0 and sets the dirfile error to a non-zero value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_CODE</code></p>
<dd>The field specified by <i>field_code</i> was not found in the database.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd>An invalid <i>dirfile</i> was supplied.</p>
<dt><code>GD_E_BAD_FIELD_TYPE</code></p>
<dd>The supplied <i>field_code</i> referred to a field of type other than <code>STRING</code>. The caller should use <code><a href="/docs/linux/man/3-putdata/">putdata</a></code>(3), or <code><a href="/docs/linux/man/3-put_constant/">put_constant</a></code>(3) instead.</p>
<dt><code>GD_E_BAD_REPR</code></p>
<dd>The representation suffix specified in <i>field_code</i> was not recognised.</p>
<dt><code>GD_E_BAD_TYPE</code></p>
<dd>An invalid <i>data_type</i> was specified.</p>
<dt><code>GD_E_INTERNAL_ERROR</code></p>
<dd>An internal error occurred in the library while trying to perform the task. This indicates a bug in the library. Please report the incident to the maintainer.</p>
<dt><code>GD_E_PROTECTED</code></p>
<dd>The fragment containing the string was protected from change. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered may be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_metaflush/">dirfile_metaflush</a></code>(3), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_string/">get_string</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-putdata/">putdata</a></code>(3) </p>
