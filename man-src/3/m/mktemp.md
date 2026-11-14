---
title: "mktemp(3)"
name: "mktemp"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mktemp/"
description: "mktemp – make a unique temporary filename"
---

<h2 class="name">NAME</h2>
<p> mktemp &#8211; make a unique temporary filename </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
char *mktemp(char *template);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>mktemp</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.12:</p>
<dd> (_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500) &amp;&amp; ! (_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</p>
<dt>Before glibc 2.12:</p>
<dd> _BSD_SOURCE || _SVID_SOURCE || _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <i>Never use this function</i>; see BUGS. </p>
<p> The <code>mktemp</code>() function generates a unique temporary filename from <i>template</i>. The last six characters of <i>template</i> must be XXXXXX and these are replaced with a string that makes the filename unique. Since it will be modified, <i>template</i> must not be a string constant, but should be declared as a character array.</p>
<h2>RETURN VALUE</h2>
<p> The <code>mktemp</code>() function always returns <i>template</i>. If a unique name was created, the last six bytes of <i>template</i> will have been modified in such a way that the resulting name is unique (i.e., does not exist already) If a unique name could not be created, <i>template</i> is made an empty string, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> The last six characters of <i>template</i> were not XXXXXX.</dl>
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
<td> <code>mktemp</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> 4.3BSD, POSIX.1-2001. POSIX.1-2008 removes the specification of <code>mktemp</code>().</p>
<h2>BUGS</h2>
<p> Never use <code>mktemp</code>(). Some implementations follow 4.3BSD and replace XXXXXX by the current process ID and a single letter, so that at most 26 different names can be returned. Since on the one hand the names are easy to guess, and on the other hand there is a race between testing whether the name exists and opening the file, every use of <code>mktemp</code>() is a security risk. The race is avoided by <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3) and <code><a href="/docs/linux/man/3-mkdtemp/">mkdtemp</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mktemp/">mktemp</a></code>(1), <code><a href="/docs/linux/man/3-mkdtemp/">mkdtemp</a></code>(3), <code><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></code>(3), <code><a href="/docs/linux/man/3-tempnam/">tempnam</a></code>(3), <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3), <code><a href="/docs/linux/man/3-tmpnam/">tmpnam</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
