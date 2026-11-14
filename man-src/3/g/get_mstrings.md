---
title: "get_mstrings(3)"
name: "get_mstrings"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_mstrings/"
description: "get_mstrings — retrieve a list of string values from a dirfile"
---

<h2>NAME</h2>
<p> get_mstrings &#8212; retrieve a list of string values from a dirfile</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>const char **get_mstrings(DIRFILE *</code><i>dirfile</i><code>, const char *</code><i>parent</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>get_mstrings</code>() function queries a <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5) database specified by <i>dirfile</i> and returns a read-only list of values of the all <code>STRING</code> type metafields for the supplied <i>parent</i> field. </p>
<p> The <i>dirfile</i> argument must point to a valid DIRFILE object previously created by a call to <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3). </p>
<p> The array returned will be de-allocated by a call to <code><a href="/docs/linux/man/3-dirfile_close/">dirfile_close</a></code>(3) and should not be de-allocated by the caller. The list returned should not be assumed to be in any particular order, although it is guaranteed to be in the same order as the list of <code>STRING</code> fields returned by <code><a href="/docs/linux/man/3-get_mfield_list_by_type/">get_mfield_list_by_type</a></code>(3). The array is terminated by a NULL pointer. The number of strings in the array can be obtained from a call to <code><a href="/docs/linux/man/3-get_nmfields_by_type/">get_nmfields_by_type</a></code>(3). </p>
<p> The caller may not modify any strings in the array, or the array itself. Doing so may cause database corruption. The pointer returned is guaranteed to be valid until <code>get_mstrings</code>() is called again with the same arguments, or until the array is deallocated by a call to <code><a href="/docs/linux/man/3-dirfile_close/">dirfile_close</a></code>(3). </p>
<p> A corresponding list of names for these fields may be obtained by calling <code><a href="/docs/linux/man/3-get_mfield_list_by_type/">get_mfield_list_by_type</a></code>(3). </p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>get_mstrings</code>() returns a pointer to an array of strings containing the values of all the <code>STRING</code> metafields for the specified parent field. On error it returns NULL and sets the dirfile error to a non-zero error value. Possible error values are:</p>
<dl>
<dt><code>GD_E_ALLOC</code></p>
<dd> The library was unable to allocate memory.</p>
<dt><code>GD_E_BAD_CODE</code></p>
<dd> The supplied parent field code was not found, or referred to a metafield itself.</p>
<dt><code>GD_E_BAD_DIRFILE</code></p>
<dd> The supplied dirfile was invalid. The dirfile error may be retrieved by calling <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3). A descriptive error string for the last error encountered can be obtained from a call to <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/3-dirfile_open/">dirfile_open</a></code>(3), <code><a href="/docs/linux/man/3-get_error/">get_error</a></code>(3), <code><a href="/docs/linux/man/3-get_error_string/">get_error_string</a></code>(3), <code><a href="/docs/linux/man/3-get_mfield_list_by_type/">get_mfield_list_by_type</a></code>(3), <code><a href="/docs/linux/man/3-get_nmfields_by_type/">get_nmfields_by_type</a></code>(3), <code><a href="/docs/linux/man/3-get_strings/">get_strings</a></code>(3) </p>
<h2>Index</h2>
