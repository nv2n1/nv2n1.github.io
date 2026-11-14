---
title: "get_nvectors(3)"
name: "get_nvectors"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_nvectors/"
description: "get_nvectors — report the number of vector fields in a dirfile"
---

<h2>NAME</h2>
<p> get_nvectors &#8212; report the number of vector fields in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>unsigned int get_nvectors(DIRFILE *</code><i>dirfile</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_nvectors</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the number of vector fields defined in the database (<i>i.e.</i> fields of types <code>BIT</code>,~<code>LINCOM</code>,~<code>LINTERP</code>,~<code>MULTIPLY</code>,~<code>PHASE</code>,~<code>POLYNOM</code>,~<code>RAW</code>, <code>SBIT</code>). Notably, this count does not include /META fields. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_nvectors</code>() returns the number of vector fields in the dirfile. On error, it returns zero and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_nfields/">get_nfields</a></code>(3), <code><a href="/docs/linux/man/3-get_nmvectors/">get_nmvectors</a></code>(3), <code><a href="/docs/linux/man/3-get_vector_list/">get_vector_list</a></code>(3) </p>
<h2>Index</h2>
