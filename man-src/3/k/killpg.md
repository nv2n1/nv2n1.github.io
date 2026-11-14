---
title: "killpg(3)"
name: "killpg"
section: "3"
letter: "k"
url: "/docs/linux/man/3-killpg/"
description: "killpg – send signal to a process group"
---

<h2 class="name">NAME</h2>
<p> killpg &#8211; send signal to a process group </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;signal.h&gt;</code> </p>
<p> <code>int killpg(int </code><i>pgrp</i><code>, int </code><i>sig</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)):</p>
<dl>
<dt><code>killpg</code>():</p>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> <code>killpg</code>() sends the signal <i>sig</i> to the process group <i>pgrp</i>. See <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) for a list of signals. </p>
<p> If <i>pgrp</i> is 0, <code>killpg</code>() sends the signal to the calling process&#8217;s process group. (POSIX says: if <i>pgrp</i> is less than or equal to 1, the behavior is undefined.) </p>
<p> For the permissions required to send a signal to another process, see <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2).</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>sig</i> is not a valid signal number.</p>
<dt><code>EPERM</code></p>
<dd> The process does not have permission to send the signal to any of the target processes. For the required permissions, see <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2).</p>
<dt><code>ESRCH</code></p>
<dd> No process can be found in the process group specified by <i>pgrp</i>.</p>
<dt><code>ESRCH</code></p>
<dd> The process group was given as 0 but the sending process does not have a process group.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.4BSD (<code>killpg</code>() first appeared in 4BSD).</p>
<h2>NOTES</h2>
<p> There are various differences between the permission checking in BSD-type systems and System V-type systems. See the POSIX rationale for <code><a href="//www.systutorials.com/docs/linux/man/3p-kill/">kill</a></code>(3p). A difference not mentioned by POSIX concerns the return value <code>EPERM</code>: BSD documents that no signal is sent and <code>EPERM</code> returned when the permission check failed for at least one target process, while POSIX documents <code>EPERM</code> only when the permission check failed for all target processes.</p>
<h3>C library/kernel differences</h3>
<p> On Linux, <code>killpg</code>() is implemented as a library function that makes the call <i>kill(-pgrp, sig)</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getpgrp/">getpgrp</a></code>(2), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
