---
title: "asprintf(3)"
name: "asprintf"
section: "3"
letter: "a"
url: "/docs/linux/man/3-asprintf/"
description: "asprintf, vasprintf – print to allocated string"
---

<h2 class="name">NAME</h2>
<p> asprintf, vasprintf &#8211; print to allocated string </p>
<h2>SYNOPSIS</h2>
<p> <code>#define _GNU_SOURCE</code> /* See <a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a>(7) */<br />
 <code>#include &lt;stdio.h&gt;</code> </p>
<p> <code>int asprintf(char **</code><i>strp</i><code>, const char *</code><i>fmt</i><code>, &#8230;);</code> </p>
<p> <code>int vasprintf(char **</code><i>strp</i><code>, const char *</code><i>fmt</i><code>, va_list </code><i>ap</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The functions <code>asprintf</code>() and <code>vasprintf</code>() are analogs of <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3) and <code><a href="/docs/linux/man/3-vsprintf/">vsprintf</a></code>(3), except that they allocate a string large enough to hold the output including the terminating null byte (&#8216;\0&#8217;), and return a pointer to it via the first argument. This pointer should be passed to <code><a href="/docs/linux/man/3-free/">free</a></code>(3) to release the allocated storage when it is no longer needed.  </p>
<h2>RETURN VALUE</h2>
<p> When successful, these functions return the number of bytes printed, just like <code><a href="/docs/linux/man/3-sprintf/">sprintf</a></code>(3). If memory allocation wasn&#8217;t possible, or some other error occurs, these functions will return -1, and the contents of <i>strp</i> are undefined.  </p>
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
<td> <code>asprintf</code>(), <code>vasprintf</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are GNU extensions, not in C or POSIX. They are also available under *BSD. The FreeBSD implementation sets <i>strp</i> to NULL on error.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-free/">free</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
