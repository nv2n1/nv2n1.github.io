---
title: "canonicalize_file_name(3)"
name: "canonicalize_file_name"
section: "3"
letter: "c"
url: "/docs/linux/man/3-canonicalize_file_name/"
description: "canonicalize_file_name – return the canonicalized absolute pathname"
---

<h2 class="name">NAME</h2>
<p> canonicalize_file_name &#8211; return the canonicalized absolute pathname </p>
<h2>SYNOPSIS</h2>
<p> <code>#define _GNU_SOURCE</code> /* See <a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a>(7) */<br />
 <code>#include &lt;stdlib.h&gt;</code> </p>
<p> <code>char *canonicalize_file_name(const char *</code><i>path</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>canonicalize_file_name</code>() function returns a null-terminated string containing the canonicalized absolute pathname corresponding to <i>path</i>. In the returned string, symbolic links are resolved, as are <i>.</i> and <i>..</i> pathname components. Consecutive slash (<i>/</i>) characters are replaced by a single slash. </p>
<p> The returned string is dynamically allocated by <code>canonicalize_file_name</code>() and the caller should deallocate it with <code><a href="/docs/linux/man/3-free/">free</a></code>(3) when it is no longer required. </p>
<p> The call <i>canonicalize_file_name(path)</i> is equivalent to the call: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;realpath(path, NULL);</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>canonicalize_file_name</code>() returns a null-terminated string. On error (e.g., a pathname component is unreadable or does not exist), <code>canonicalize_file_name</code>() returns NULL and sets <i>errno</i> to indicate the error.</p>
<h2>ERRORS</h2>
<p> See <code><a href="/docs/linux/man/3-realpath/">realpath</a></code>(3).</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>canonicalize_file_name</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function is a GNU extension.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-readlink/">readlink</a></code>(2), <code><a href="/docs/linux/man/3-realpath/">realpath</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
