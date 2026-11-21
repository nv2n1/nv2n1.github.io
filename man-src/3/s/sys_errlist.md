---
title: "sys_errlist(3)"
name: "sys_errlist"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sys_errlist/"
description: "perror – print a system error message"
---

<p>perror &#8211; print a system error message</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;
void perror(const char *s);
#include &lt;errno.h&gt;</code></pre>
<p> <code>const char * const </code><i>sys_errlist</i><code>[];</code><br />
 <code>int </code><i>sys_nerr</i><code>;</code><br />
 <code>int </code><i>errno</i><code>; </code>/* Not really declared this way; see <a href="/docs/linux/man/3-errno/">errno</a>(3) */ Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <i>sys_errlist</i>, <i>sys_nerr</i>:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;From glibc 2.19 to 2.31:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>Description</h2>
<p>The <code>perror</code>() function produces a message on standard error describing the last error encountered during a call to a system or library function. </p>
<p> First (if <i>s</i> is not NULL and <i>*s</i> is not a null byte (&#8216;\0&#8217;)), the argument string <i>s</i> is printed, followed by a colon and a blank. Then an error message corresponding to the current value of <i>errno</i> and a new-line. </p>
<p> To be of most use, the argument string should include the name of the function that incurred the error. </p>
<p> The global error list <i>sys_errlist</i>[], which can be indexed by <i>errno</i>, can be used to obtain the error message without the newline. The largest message number provided in the table is <i>sys_nerr</i>-1. Be careful when directly accessing this list, because new error values may not have been added to <i>sys_errlist</i>[]. The use of <i>sys_errlist</i>[] is nowadays deprecated; use <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3) instead. </p>
<p> When a system call fails, it usually returns -1 and sets the variable <i>errno</i> to a value describing what went wrong. (These values can be found in <i>&lt;errno.h&gt;</i>.) Many library functions do likewise. The function <code>perror</code>() serves to translate this error code into human-readable form. Note that <i>errno</i> is undefined after a successful system call or library function call: this call may well change this variable, even though it succeeds, for example because it internally used some other library function that failed. Thus, if a failing call is not immediately followed by a call to <code>perror</code>(), the value of <i>errno</i> should be saved.  </p>
<h2>VERSIONS</h2>
<p> Since glibc version 2.32, the declarations of <i>sys_errlist</i> and <i>sys_nerr</i> are no longer exposed by <i>&lt;stdio.h&gt;</i>.  </p>
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
<td> <code>perror</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:stderr
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>perror</code>(), <i>errno</i>: POSIX.1-2001, POSIX.1-2008, C89, C99, 4.3BSD. </p>
<p> The externals <i>sys_nerr</i> and <i>sys_errlist</i> derive from BSD, but are not specified in POSIX.1.  </p>
<h2>NOTES</h2>
<p> The externals <i>sys_nerr</i> and <i>sys_errlist</i> are defined by glibc, but in <i>&lt;stdio.h&gt;</i>.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-err/">err</a></code>(3), <code><a href="/docs/linux/man/3-errno/">errno</a></code>(3), <code><a href="/docs/linux/man/3-error/">error</a></code>(3), <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
