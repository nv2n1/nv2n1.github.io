---
title: "tempnam(3)"
name: "tempnam"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tempnam/"
description: "tempnam – create a name for a temporary file"
---

<p>tempnam &#8211; create a name for a temporary file</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;

char *tempnam(const char *dir, const char *pfx);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>tempnam</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>Description</h2>
<p><i>Never use this function.</i> Use <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3) or <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3) instead. </p>
<p> The <code>tempnam</code>() function returns a pointer to a string that is a valid filename, and such that a file with this name did not exist when <code>tempnam</code>() checked. The filename suffix of the pathname generated will start with <i>pfx</i> in case <i>pfx</i> is a non-NULL string of at most five bytes. The directory prefix part of the pathname generated is required to be &quot;appropriate&quot; (often that at least implies writable). </p>
<p> Attempts to find an appropriate directory go through the following steps:</p>
<dl>
<dt>a)</p>
<dd>In case the environment variable <code>TMPDIR</code> exists and contains the name of an appropriate directory, that is used.</p>
<dt>b)</p>
<dd>Otherwise, if the <i>dir</i> argument is non-NULL and appropriate, it is used.</p>
<dt>c)</p>
<dd>Otherwise, <i>P_tmpdir</i> (as defined in <i>&lt;stdio.h&gt;</i>) is used when appropriate.</p>
<dt>d)</p>
<dd>Finally an implementation-defined directory may be used.</dl>
<p> The string returned by <code>tempnam</code>() is allocated using <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) and hence should be freed by <code><a href="/docs/linux/man/3-free/">free</a></code>(3).</p>
<h2>Return Value</h2>
<p>On success, the <code>tempnam</code>() function returns a pointer to a unique temporary filename. It returns NULL if a unique name cannot be generated, with <i>errno</i> set to indicate the cause of the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd>Allocation of storage failed.</dl>
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
<td> <code>tempnam</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>SVr4, 4.3BSD, POSIX.1-2001. POSIX.1-2008 marks <code>tempnam</code>() as obsolete.</p>
<h2>Notes</h2>
<p>Although <code>tempnam</code>() generates names that are difficult to guess, it is nevertheless possible that between the time that <code>tempnam</code>() returns a pathname, and the time that the program opens it, another program might create that pathname using <code><a href="/docs/linux/man/2-open/">open</a></code>(2), or create it as a symbolic link. This can lead to security holes. To avoid such possibilities, use the <code><a href="/docs/linux/man/2-open/">open</a></code>(2) <code>O_EXCL</code> flag to open the pathname. Or better yet, use <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3) or <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3). </p>
<p> SUSv2 does not mention the use of <code>TMPDIR</code>; glibc will use it only when the program is not set-user-ID. On SVr4, the directory used under <code>d)</code> is <i>/tmp</i> (and this is what glibc does). </p>
<p> Because it dynamically allocates memory used to return the pathname, <code>tempnam</code>() is reentrant, and thus thread safe, unlike <code><a href="/docs/linux/man/3-tmpnam/">tmpnam</a></code>(3). </p>
<p> The <code>tempnam</code>() function generates a different string each time it is called, up to <code>TMP_MAX</code> (defined in <i>&lt;stdio.h&gt;</i>) times. If it is called more than <code>TMP_MAX</code> times, the behavior is implementation defined. </p>
<p> <code>tempnam</code>() uses at most the first five bytes from <i>pfx</i>. </p>
<p> The glibc implementation of <code>tempnam</code>() fails with the error <code>EEXIST</code> upon failure to find a unique name.</p>
<h2>Bugs</h2>
<p>The precise meaning of &quot;appropriate&quot; is undefined; it is unspecified how accessibility of a directory is determined.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3), <code><a href="/docs/linux/man/3-mktemp/">mktemp</a></code>(3), <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3), <code><a href="/docs/linux/man/3-tmpnam/">tmpnam</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
