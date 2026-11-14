---
title: "grantpt(3)"
name: "grantpt"
section: "3"
letter: "g"
url: "/docs/linux/man/3-grantpt/"
description: "grantpt – grant access to the slave pseudoterminal"
---

<h2 class="name">NAME</h2>
<p> grantpt &#8211; grant access to the slave pseudoterminal </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;stdlib.h&gt;</code> </p>
<p> <code>int grantpt(int </code><i>fd</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>grantpt</code>(): </p>
<dl>
<dt>
<dd> Since glibc 2.24:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500 ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(_XOPEN_SOURCE&nbsp;&amp;&amp;&nbsp;_XOPEN_SOURCE_EXTENDED)<br />
 Glibc 2.23 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_XOPEN_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> The <code>grantpt</code>() function changes the mode and owner of the slave pseudoterminal device corresponding to the master pseudoterminal referred to by the file descriptor <i>fd</i>. The user ID of the slave is set to the real UID of the calling process. The group ID is set to an unspecified value (e.g., <i>tty</i>). The mode of the slave is set to 0620 (crw&#8211;w&#8212;-). </p>
<p> The behavior of <code>grantpt</code>() is unspecified if a signal handler is installed to catch <code>SIGCHLD</code> signals.</p>
<h2>RETURN VALUE</h2>
<p> When successful, <code>grantpt</code>() returns 0. Otherwise, it returns -1 and sets <i>errno</i> appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> The corresponding slave pseudoterminal could not be accessed.</p>
<dt><code>EBADF</code></p>
<dd> The <i>fd</i> argument is not a valid open file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> The <i>fd</i> argument is valid but not associated with a master pseudoterminal.</dl>
<h2>VERSIONS</h2>
<p> <code>grantpt</code>() is provided in glibc since version 2.1.</p>
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
<td> <code>grantpt</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> This is part of the UNIX 98 pseudoterminal support, see <code><a href="/docs/linux/man/4-pts/">pts</a></code>(4). </p>
<p> Many systems implement this function via a set-user-ID helper binary called &quot;pt_chown&quot;. On Linux systems with a devpts filesystem (present since Linux 2.2), the kernel normally sets the correct ownership and permissions for the pseudoterminal slave when the master is opened (<code><a href="/docs/linux/man/3-posix_openpt/">posix_openpt</a></code>(3)), so that nothing must be done by <code>grantpt</code>(). Thus, no such helper binary is required (and indeed it is configured to be absent during the glibc build that is typical on many systems).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/3-posix_openpt/">posix_openpt</a></code>(3), <code><a href="/docs/linux/man/3-ptsname/">ptsname</a></code>(3), <code><a href="/docs/linux/man/3-unlockpt/">unlockpt</a></code>(3), <code><a href="/docs/linux/man/4-pts/">pts</a></code>(4), <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
