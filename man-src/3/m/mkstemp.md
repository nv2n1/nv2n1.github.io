---
title: "mkstemp(3)"
name: "mkstemp"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mkstemp/"
description: "mkstemp, mkostemp, mkstemps, mkostemps – create a unique temporary file"
---

<h2 class="name">NAME</h2>
<p> mkstemp, mkostemp, mkstemps, mkostemps &#8211; create a unique temporary file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
int mkstemp(char *template);
int mkostemp(char *template, int flags);
int mkstemps(char *template, int suffixlen);
int mkostemps(char *template, int suffixlen, int flags);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>mkstemp</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.12:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE</dl>
<p> <code>mkostemp</code>(): _GNU_SOURCE<br />
 <code>mkstemps</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Glibc since 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_SVID_SOURCE ||&nbsp;_BSD_SOURCE<br />
 <code>mkostemps</code>(): _GNU_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>mkstemp</code>() function generates a unique temporary filename from <i>template</i>, creates and opens the file, and returns an open file descriptor for the file. </p>
<p> The last six characters of <i>template</i> must be &quot;XXXXXX&quot; and these are replaced with a string that makes the filename unique. Since it will be modified, <i>template</i> must not be a string constant, but should be declared as a character array. </p>
<p> The file is created with permissions 0600, that is, read plus write for owner only. The returned file descriptor provides both read and write access to the file. The file is opened with the <code><a href="/docs/linux/man/2-open/">open</a></code>(2) <code>O_EXCL</code> flag, guaranteeing that the caller is the process that creates the file. </p>
<p> The <code>mkostemp</code>() function is like <code>mkstemp</code>(), with the difference that the following bits&#8212;with the same meaning as for <code><a href="/docs/linux/man/2-open/">open</a></code>(2)&#8212;may be specified in <i>flags</i>: <code>O_APPEND</code>, <code>O_CLOEXEC</code>, and <code>O_SYNC</code>. Note that when creating the file, <code>mkostemp</code>() includes the values <code>O_RDWR</code>, <code>O_CREAT</code>, and <code>O_EXCL</code> in the <i>flags</i> argument given to <code><a href="/docs/linux/man/2-open/">open</a></code>(2); including these values in the <i>flags</i> argument given to <code>mkostemp</code>() is unnecessary, and produces errors on some systems. </p>
<p> The <code>mkstemps</code>() function is like <code>mkstemp</code>(), except that the string in <i>template</i> contains a suffix of <i>suffixlen</i> characters. Thus, <i>template</i> is of the form <i>prefixXXXXXXsuffix</i>, and the string XXXXXX is modified as for <code>mkstemp</code>(). </p>
<p> The <code>mkostemps</code>() function is to <code>mkstemps</code>() as <code>mkostemp</code>() is to <code>mkstemp</code>().</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return the file descriptor of the temporary file. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EEXIST</code></p>
<dd> Could not create a unique temporary filename. Now the contents of <i>template</i> are undefined.</p>
<dt><code>EINVAL</code></p>
<dd> For <code>mkstemp</code>() and <code>mkostemp</code>(): The last six characters of <i>template</i> were not XXXXXX; now <i>template</i> is unchanged.</p>
<dt>
<dd> For <code>mkstemps</code>() and <code>mkostemps</code>(): <i>template</i> is less than <i>(6 + suffixlen)</i> characters long, or the last 6 characters before the suffix in <i>template</i> were not XXXXXX.</dl>
<p> These functions may also fail with any of the errors described for <code><a href="/docs/linux/man/2-open/">open</a></code>(2).</p>
<h2>VERSIONS</h2>
<p> <code>mkostemp</code>() is available since glibc 2.7. <code>mkstemps</code>() and <code>mkostemps</code>() are available since glibc 2.11.</p>
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
<td> <code>mkstemp</code>(), <code>mkostemp</code>(),<br />
 <code>mkstemps</code>(), <code>mkostemps</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>mkstemp</code>(): 4.3BSD, POSIX.1-2001. </p>
<p> <code>mkstemps</code>(): unstandardized, but appears on several other systems. </p>
<p> <code>mkostemp</code>() and <code>mkostemps</code>(): are glibc extensions.</p>
<h2>NOTES</h2>
<p> In glibc versions 2.06 and earlier, the file is created with permissions 0666, that is, read and write for all users. This old behavior may be a security risk, especially since other UNIX flavors use 0600, and somebody might overlook this detail when porting programs. POSIX.1-2008 adds a requirement that the file be created with mode 0600. </p>
<p> More generally, the POSIX specification of <code>mkstemp</code>() does not say anything about file modes, so the application should make sure its file mode creation mask (see <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)) is set appropriately before calling <code>mkstemp</code>() (and <code>mkostemp</code>()).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mkdtemp/">mkdtemp</a></code>(3), <code><a href="/docs/linux/man/3-mktemp/">mktemp</a></code>(3), <code><a href="/docs/linux/man/3-tempnam/">tempnam</a></code>(3), <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3), <code><a href="/docs/linux/man/3-tmpnam/">tmpnam</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
