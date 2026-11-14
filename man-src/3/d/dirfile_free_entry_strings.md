---
title: "dirfile_free_entry_strings(3)"
name: "dirfile_free_entry_strings"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dirfile_free_entry_strings/"
description: "dirfile_free_entry_strings — free strings in a GetData gd_entry_t object"
---

<h2>NAME</h2>
<p> dirfile_free_entry_strings &#8212; free strings in a GetData gd_entry_t object</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/getdata.h">getdata.h</a>&gt;</code></p>
<dl>
<dt> <code>gd_entry_t *dirfile_free_entry_strings(gd_entry_t *</code><i>entry</i><code>);</code></dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dirfile_free_entry_strings</code>() function frees the character strings found in the gd_entry_t object <i>entry</i> which were previously allocated by a call to <code><a href="/docs/linux/man/3-get_entry/">get_entry</a></code>(3). If <i>entry</i> is NULL, this function does nothing. </p>
<p> If non-NULL, <i>entry</i> must point to a valid and properly initialised gd_entry_t object, such as that returned by <code><a href="/docs/linux/man/3-get_entry/">get_entry</a></code>(3). As well, the caller may construct a properly initialised gd_entry_t object by first setting all bits to zero, then setting the field_type parameter to the desired gd_entype_t symbol, and finally initialising only the members defined for that type. The results of calling this function are undefined if the character strings pointed to by the string members of <i>entry</i> have not been allocated with <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), unless these pointer members are equal to NULL. </p>
<p> See <code><a href="/docs/linux/man/3-get_entry/">get_entry</a></code>(3) for a complete description of the gd_entry_t data type.</p>
<h2>RETURN VALUE</h2>
<p> A call to <code>dirfile_free_entry_strings</code>() always returns its input, <i>entry</i>.</p>
<h2>NOTES</h2>
<p> This function is provided as a convenience only. Callers may free strings allocated by <code><a href="/docs/linux/man/3-get_entry/">get_entry</a></code>(3) themselves by simply calling <code><a href="/docs/linux/man/3-free/">free</a></code>(3) on the appropriate members for the given entry type, if they prefer to do so.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-get_entry/">get_entry</a></code>(3), <code><a href="/docs/linux/man/3-free/">free</a></code>(3) </p>
<h2>Index</h2>
