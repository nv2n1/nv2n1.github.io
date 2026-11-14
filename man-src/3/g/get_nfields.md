---
title: "get_nfields(3)"
name: "get_nfields"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_nfields/"
description: "get_nfields — report the number of fields in a dirfile"
---

<h2>NAME</h2>
<p> get_nfields &#8212; report the number of fields in a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>unsigned int get_nfields(DIRFILE *</code><i>dirfile</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_nfields</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns the number of fields defined in the database. Notably, this count does not include /META fields. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_nfields</code>() returns the number of defined fields in the dirfile. On error, it returns zero and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_field_list/">get_field_list</a></code>(3), <code><a href="/docs/linux/man/3-get_nfields_by_type/">get_nfields_by_type</a></code>(3), <code><a href="/docs/linux/man/3-get_nmfields/">get_nmfields</a></code>(3), <code><a href="/docs/linux/man/3-get_nvectors/">get_nvectors</a></code>(3) </p>
<h2>Index</h2>
