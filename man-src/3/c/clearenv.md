---
title: "clearenv(3)"
name: "clearenv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clearenv/"
description: "clearenv – clear the environment"
---

<h2 class="name">NAME</h2>
<p> clearenv &#8211; clear the environment </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
int clearenv(void);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>clearenv</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>clearenv</code>() function clears the environment of all name-value pairs and sets the value of the external variable <i>environ</i> to NULL. After this call, new variables can be added to the environment using <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3) and <code><a href="/docs/linux/man/3-setenv/">setenv</a></code>(3).</p>
<h2>RETURN VALUE</h2>
<p> The <code>clearenv</code>() function returns zero on success, and a nonzero value on failure.</p>
<h2>VERSIONS</h2>
<p> Available since glibc 2.0.</p>
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
<td> <code>clearenv</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe const:env
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> Various UNIX variants (DG/UX, HP-UX, QNX, &#8230;). POSIX.9 (bindings for FORTRAN77). POSIX.1-1996 did not accept <code>clearenv</code>() and <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3), but changed its mind and scheduled these functions for some later issue of this standard (see &#167;B.4.6.1). However, POSIX.1-2001 adds only <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3), and rejected <code>clearenv</code>().</p>
<h2>NOTES</h2>
<p> On systems where <code>clearenv</code>() is unavailable, the assignment </p>
<p> environ = NULL; </p>
<p> will probably do. </p>
<p> The <code>clearenv</code>() function may be useful in security-conscious applications that want to precisely control the environment that is passed to programs executed using <code><a href="/docs/linux/man/3-exec/">exec</a></code>(3). The application would do this by first clearing the environment and then adding select environment variables. </p>
<p> Note that the main effect of <code>clearenv</code>() is to adjust the value of the pointer <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7); this function does not erase the contents of the buffers containing the environment definitions. </p>
<p> The DG/UX and Tru64 man pages write: If <i>environ</i> has been modified by anything other than the <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3), <code><a href="/docs/linux/man/3-getenv/">getenv</a></code>(3), or <code>clearenv</code>() functions, then <code>clearenv</code>() will return an error and the process environment will remain unchanged.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getenv/">getenv</a></code>(3), <code><a href="/docs/linux/man/3-putenv/">putenv</a></code>(3), <code><a href="/docs/linux/man/3-setenv/">setenv</a></code>(3), <code><a href="/docs/linux/man/3-unsetenv/">unsetenv</a></code>(3), <code><a href="/docs/linux/man/7-environ/">environ</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
