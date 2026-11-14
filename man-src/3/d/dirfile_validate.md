---
title: "dirfile_validate(3)"
name: "dirfile_validate"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_validate/"
description: "dirfile_validate — check a dirfile field code for validity"
---

<h2>NAME</h2>
<p> dirfile_validate &#8212; check a dirfile field code for validity</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>int dirfile_validate(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>field_code</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_validate</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and checks whether <i>field_code</i>, which may contain a representation suffix, specifies a valid field. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<p> This function checks whether the field and its input fields (if any) are found, whether the representation suffix (if any) is valid, and also that all non-literal scalar parameters specify valid <code>CONST</code> fields. </p>
<h2>RETURN VALUE</h2>
<p> If all checks pass, <code>dirfile_validate</code>() returns zero. On error, it returns -1 and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The field specified by <i>field_code</i> or one of the fields it uses as input was not found in the database.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid.</p>
<dt><code>GD_E_BAD_REPR</code></p>
<dd> The representation suffix specified in <i>field_code</i> was not recognised.</p>
<dt><code>GD_E_BAD_SCALAR</code></p>
<dd> A non-literal scalar used in the definition of the field or one of its inputs was not found, or was not a <code>CONST</code> field.</p>
<dt><code>GD_E_DIMENSION</code></p>
<dd> A scalar field was found where a vector field was expected.</p>
<dt><code>GD_E_RECURSE_LEVEL</code></p>
<dd> Too many levels of recursion were encountered while trying to resolve <i>field_code</i>. This usually indicates a circular dependency in field specification in the dirfile. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>NOTES</h2>
<p> It is not necessary to call this function before passing a field code to another GetData function: all functions which accept field codes perform these checks themselves.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3) </p>
<h2>Index</h2>
