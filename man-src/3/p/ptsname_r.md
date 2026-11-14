---
title: "ptsname_r(3)"
name: "ptsname_r"
section: "3"
letter: "p"
url: "/docs/linux/man/3-ptsname_r/"
description: "ptsname, ptsname_r – get the name of the slave pseudoterminal"
---

<p>ptsname, ptsname_r &#8211; get the name of the slave pseudoterminal</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdlib.h&gt;
char *ptsname(int fd);

int ptsname_r(int fd, char *buf, size_t buflen);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>ptsname</code>(): </p>
<dl>
<dd>Since glibc 2.24:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500 ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(_XOPEN_SOURCE&nbsp;&amp;&amp;&nbsp;_XOPEN_SOURCE_EXTENDED)<br />
 Glibc 2.23 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE</dl>
<p> <code>ptsname_r</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_GNU_SOURCE</p>
<h2>Description</h2>
<p>The <code>ptsname</code>() function returns the name of the slave pseudoterminal device corresponding to the master referred to by the file descriptor <i>fd</i>. </p>
<p> The <code>ptsname_r</code>() function is the reentrant equivalent of <code>ptsname</code>(). It returns the name of the slave pseudoterminal device as a null-terminated string in the buffer pointed to by <i>buf</i>. The <i>buflen</i> argument specifies the number of bytes available in <i>buf</i>.</p>
<h2>Return Value</h2>
<p>On success, <code>ptsname</code>() returns a pointer to a string in static storage which will be overwritten by subsequent calls. This pointer must not be freed. On failure, NULL is returned. </p>
<p> On success, <code>ptsname_r</code>() returns 0. On failure, an error number is returned to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>(<code>ptsname_r</code>() only) <i>buf</i> is NULL. (This error is returned only for glibc 2.25 and earlier.)</p>
<dt><code>ENOTTY</code></p>
<dd><i>fd</i> does not refer to a pseudoterminal master device.</p>
<dt><code>ERANGE</code></p>
<dd>(<code>ptsname_r</code>() only) <i>buf</i> is too small.</dl>
<h2>Versions</h2>
<p><code>ptsname</code>() is provided in glibc since version 2.1.</p>
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
<td> <code>ptsname</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:ptsname
</td>
</tr>
<tr VALIGN=top>
<td> <code>ptsname_r</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p><code>ptsname</code>():<br />
&nbsp;POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>ptsname</code>() is part of the UNIX 98 pseudoterminal support (see <code><a href="/docs/linux/man/4-pts/">pts</a></code>(4)). </p>
<p> <code>ptsname_r</code>() is a Linux extension, that is proposed for inclusion in the next major revision of POSIX.1 (Issue 8). A version of this function is documented on Tru64 and HP-UX, but on those implementations, -1 is returned on error, with <i>errno</i> set to indicate the error. Avoid using this function in portable programs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-grantpt/">grantpt</a></code>(3), <code><a href="/docs/linux/man/3-posix_openpt/">posix_openpt</a></code>(3), <code><a href="/docs/linux/man/3-ttyname/">ttyname</a></code>(3), <code><a href="/docs/linux/man/3-unlockpt/">unlockpt</a></code>(3), <code><a href="/docs/linux/man/4-pts/">pts</a></code>(4), <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
