---
title: "tmpnam(3)"
name: "tmpnam"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tmpnam/"
description: "tmpnam, tmpnam_r – create a name for a temporary file"
---

<p>tmpnam, tmpnam_r &#8211; create a name for a temporary file</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;

char *tmpnam(char *s);
char *tmpnam_r(char *s);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>tmpnam_r</code>()</p>
<dl>
<dd>
<dl>
<dt>Since glibc 2.19:</p>
<dd>_DEFAULT_SOURCE</p>
<dt>Up to and including glibc 2.19:</p>
<dd>_BSD_SOURCE || _SVID_SOURCE</dl>
</dl>
<h2>Description</h2>
<p><code>Note:</code> avoid using these functions; use <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3) or <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3) instead. </p>
<p> The <code>tmpnam</code>() function returns a pointer to a string that is a valid filename, and such that a file with this name did not exist at some point in time, so that naive programmers may think it a suitable name for a temporary file. If the argument <i>s</i> is NULL, this name is generated in an internal static buffer and may be overwritten by the next call to <code>tmpnam</code>(). If <i>s</i> is not NULL, the name is copied to the character array (of length at least <i>L_tmpnam</i>) pointed to by <i>s</i> and the value <i>s</i> is returned in case of success. </p>
<p> The created pathname has a directory prefix <i>P_tmpdir</i>. (Both <i>L_tmpnam</i> and <i>P_tmpdir</i> are defined in <i>&lt;stdio.h&gt;</i>, just like the <code>TMP_MAX</code> mentioned below.) </p>
<p> The <code>tmpnam_r</code>() function performs the same task as <code>tmpnam</code>(), but returns NULL (to indicate an error) if <i>s</i> is NULL.</p>
<h2>Return Value</h2>
<p>These functions return a pointer to a unique temporary filename, or NULL if a unique name cannot be generated.</p>
<h2>Errors</h2>
<p>No errors are defined.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>tmpnam</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:tmpnam/!s
</td>
</tr>
<tr VALIGN=top>
<td> <code>tmpnam_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p><code>tmpnam</code>(): SVr4, 4.3BSD, C89, C99, POSIX.1-2001. POSIX.1-2008 marks <code>tmpnam</code>() as obsolete. </p>
<p> <code>tmpnam_r</code>() is a nonstandard extension that is also available on a few other systems.</p>
<h2>Notes</h2>
<p>The <code>tmpnam</code>() function generates a different string each time it is called, up to <code>TMP_MAX</code> times. If it is called more than <code>TMP_MAX</code> times, the behavior is implementation defined. </p>
<p> Although these functions generate names that are difficult to guess, it is nevertheless possible that between the time that the pathname is returned and the time that the program opens it, another program might create that pathname using <code><a href="/docs/linux/man/2-open/">open</a></code>(2), or create it as a symbolic link. This can lead to security holes. To avoid such possibilities, use the <code><a href="/docs/linux/man/2-open/">open</a></code>(2) <code>O_EXCL</code> flag to open the pathname. Or better yet, use <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3) or <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3). </p>
<p> Portable applications that use threads cannot call <code>tmpnam</code>() with a NULL argument if either <code>_POSIX_THREADS</code> or <code>_POSIX_THREAD_SAFE_FUNCTIONS</code> is defined.</p>
<h2>Bugs</h2>
<p>Never use these functions. Use <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3) or <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3) instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3), <code><a href="/docs/linux/man/3-mktemp/">mktemp</a></code>(3), <code><a href="/docs/linux/man/3-tempnam/">tempnam</a></code>(3), <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
