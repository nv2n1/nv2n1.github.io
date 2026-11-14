---
title: "dlerror(3)"
name: "dlerror"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlerror/"
description: "dlerror – obtain error diagnostic for functions in the dlopen API"
---

<h2 class="name">NAME</h2>
<p> dlerror &#8211; obtain error diagnostic for functions in the dlopen API </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;dlfcn.h&gt;</code> </p>
<p> <code>char *dlerror(void);</code> </p>
<p> Link with <i>-ldl</i>.</p>
<h2>DESCRIPTION</h2>
<p> The <code>dlerror</code>() function returns a human-readable, null-terminated string describing the most recent error that occurred from a call to one of the functions in the dlopen API since the last call to <code>dlerror</code>(). The returned string does <i>not</i> include a trailing newline. </p>
<p> <code>dlerror</code>() returns NULL if no errors have occurred since initialization or since it was last called.</p>
<h2>VERSIONS</h2>
<p> <code>dlerror</code>() is present in glibc 2.0 and later.</p>
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
<td> <code>dlerror</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001.</p>
<h2>NOTES</h2>
<p> The message returned by <code>dlerror</code>() may reside in a statically allocated buffer that is overwritten by subsequent <code>dlerror</code>() calls.</p>
<h3>History</h3>
<p> This function is part of the dlopen API, derived from SunOS.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-dladdr/">dladdr</a></code>(3), <code><a href="/docs/linux/man/3-dlinfo/">dlinfo</a></code>(3), <code><a href="/docs/linux/man/3-dlopen/">dlopen</a></code>(3), <code><a href="/docs/linux/man/3-dlsym/">dlsym</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
