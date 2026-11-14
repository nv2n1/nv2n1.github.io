---
title: "mkdtemp(3)"
name: "mkdtemp"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mkdtemp/"
description: "mkdtemp – create a unique temporary directory"
---

<h2 class="name">NAME</h2>
<p> mkdtemp &#8211; create a unique temporary directory </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
char *mkdtemp(char *template);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>mkdtemp</code>(): </p>
<dl>
<dt>
<dd> /* Since glibc 2.19: */ _DEFAULT_SOURCE<br />
 || /* Glibc 2.19 and earlier: */ _BSD_SOURCE<br />
 || /* Since glibc 2.10: */ _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dl>
<h2>DESCRIPTION</h2>
<p> The <code>mkdtemp</code>() function generates a uniquely named temporary directory from <i>template</i>. The last six characters of <i>template</i> must be XXXXXX and these are replaced with a string that makes the directory name unique. The directory is then created with permissions 0700. Since it will be modified, <i>template</i> must not be a string constant, but should be declared as a character array.</p>
<h2>RETURN VALUE</h2>
<p> The <code>mkdtemp</code>() function returns a pointer to the modified template string on success, and NULL on failure, in which case <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> The last six characters of <i>template</i> were not XXXXXX. Now <i>template</i> is unchanged.</dl>
<p> Also see <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2) for other possible values for <i>errno</i>.</p>
<h2>VERSIONS</h2>
<p> Available since glibc 2.1.91.</p>
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
<td> <code>mkdtemp</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2008. This function is present on the BSDs.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mktemp/">mktemp</a></code>(1), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3), <code><a href="/docs/linux/man/3-mktemp/">mktemp</a></code>(3), <code><a href="/docs/linux/man/3-tempnam/">tempnam</a></code>(3), <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3), <code><a href="/docs/linux/man/3-tmpnam/">tmpnam</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
