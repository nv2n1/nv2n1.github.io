---
title: "logwtmp(3)"
name: "logwtmp"
section: "3"
letter: "l"
url: "/docs/linux/man/3-logwtmp/"
description: "updwtmp, logwtmp – append an entry to the wtmp file"
---

<h2 class="name">NAME</h2>
<p> updwtmp, logwtmp &#8211; append an entry to the wtmp file </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;utmp.h&gt;
void updwtmp(const char *wtmp_file, const struct utmp *ut);
void logwtmp(const char *line, const char *name, const char *host);
</code></pre>
<p> For <code>logwtmp</code>(), link with <i>-lutil</i>.</p>
<h2>DESCRIPTION</h2>
<p> <code>updwtmp</code>() appends the utmp structure <i>ut</i> to the wtmp file. </p>
<p> <code>logwtmp</code>() constructs a utmp structure using <i>line</i>, <i>name</i>, <i>host</i>, current time and current process ID. Then it calls <code>updwtmp</code>() to append the structure to the wtmp file.</p>
<h2>FILES</h2>
<dl>
<dt><i>/var/log/wtmp</i></p>
<dd> database of past user logins</dl>
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
<td> <code>updwtmp</code>(),<br />
 <code>logwtmp</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe sig:ALRM timer
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> Not in POSIX.1. Present on Solaris, NetBSD, and perhaps other systems.</p>
<h2>NOTES</h2>
<p> For consistency with the other &quot;utmpx&quot; functions (see <code><a href="/docs/linux/man/3-getutxent/">getutxent</a></code>(3)), glibc provides (since version 2.1): </p>
<p> <code>#include &lt;utmpx.h&gt;</code> <code>void updwtmpx (const char *</code><i>wtmpx_file</i><code>, const struct utmpx *</code><i>utx</i><code>);</code> </p>
<p> This function performs the same task as <code>updwtmp</code>(), but differs in that it takes a <i>utmpx</i> structure as its last argument.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getutxent/">getutxent</a></code>(3), <code><a href="/docs/linux/man/5-wtmp/">wtmp</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
