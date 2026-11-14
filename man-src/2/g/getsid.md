---
title: "getsid(2)"
name: "getsid"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getsid/"
description: "getsid – get session ID"
---

<h2 class="name">NAME</h2>
<p> getsid &#8211; get session ID </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>pid_t getsid(pid_t</code><i> pid</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getsid</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.12:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dl>
<h2>DESCRIPTION</h2>
<p> <i>getsid(0)</i> returns the session ID of the calling process. <code>getsid</code>() returns the session ID of the process with process ID <i>pid</i>. If <i>pid</i> is 0, <code>getsid</code>() returns the session ID of the calling process.</p>
<h2>RETURN VALUE</h2>
<p> On success, a session ID is returned. On error, <i>(pid_t)&nbsp;-1</i> will be returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EPERM</code></p>
<dd> A process with process ID <i>pid</i> exists, but it is not in the same session as the calling process, and the implementation considers this an error.</p>
<dt><code>ESRCH</code></p>
<dd> No process with process ID <i>pid</i> was found.</dl>
<h2>VERSIONS</h2>
<p> This system call is available on Linux since version 2.0.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4.</p>
<h2>NOTES</h2>
<p> Linux does not return <code>EPERM</code>. </p>
<p> See <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7) for a description of sessions and session IDs.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getpgid/">getpgid</a></code>(2), <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
