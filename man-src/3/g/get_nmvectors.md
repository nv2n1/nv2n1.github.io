---
title: "get_nmvectors(3)"
name: "get_nmvectors"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_nmvectors/"
description: "get_nmvectors — report the number of vector fields in a dirfile"
---

<h2>NAME</h2>
<p> get_nmvectors &#8212; report the number of vector fields in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>unsigned int get_nmvectors(DIRFILE *</code><i>dirfile</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_nmvectors</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the number of vector metafields defined in the database (<i>i.e.</i> fields of types <code>BIT</code>, <code>LINCOM</code>, <code>LINTERP</code>, <code>MULTIPLY</code>, <code>PHASE</code>, and <code>RAW</code>)<code>for</code> the supplied parent field. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_nmvectors</code>() returns the number of vector metafields in the dirfile for the given parent. On error, it returns zero and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The supplied parent field code was not found, or referred to a metafield itself.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_mvector_list/">get_mvector_list</a></code>(3), <code><a href="/docs/linux/man/3-get_nmfields/">get_nmfields</a></code>(3), <code><a href="/docs/linux/man/3-get_nvectors/">get_nvectors</a></code>(3) </p>
<h2>Index</h2>
