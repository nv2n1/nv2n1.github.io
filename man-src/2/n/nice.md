---
title: "nice(2)"
name: "nice"
section: "2"
letter: "n"
url: "/docs/linux/man/2-nice/"
description: "nice – change process priority"
---

<h2 class="name">NAME</h2>
<p> nice &#8211; change process priority </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int nice(int </code><i>inc</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>nice</code>(): _XOPEN_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.19:&nbsp;*/&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> <code>nice</code>() adds <i>inc</i> to the nice value for the calling thread. (A higher nice value means a lower priority.) </p>
<p> The range of the nice value is +19 (low priority) to -20 (high priority). Attempts to set a nice value outside the range are clamped to the range. </p>
<p> Traditionally, only a privileged process could lower the nice value (i.e., set a higher priority). However, since Linux 2.6.12, an unprivileged process can decrease the nice value of a target process that has a suitable <code>RLIMIT_NICE</code> soft limit; see <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2) for details.</p>
<h2>RETURN VALUE</h2>
<p> On success, the new nice value is returned (but see NOTES below). On error, -1 is returned, and <i>errno</i> is set appropriately. </p>
<p> A successful call can legitimately return -1. To detect an error, set <i>errno</i> to 0 before the call, and check whether it is nonzero after <code>nice</code>() returns -1.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EPERM</code></p>
<dd> The calling process attempted to increase its priority by supplying a negative <i>inc</i> but has insufficient privileges. Under Linux, the <code>CAP_SYS_NICE</code> capability is required. (But see the discussion of the <code>RLIMIT_NICE</code> resource limit in <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2).)</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD. However, the raw system call and (g)libc (earlier than glibc 2.2.4) return value is nonstandard, see below.</p>
<h2>NOTES</h2>
<p> For further details on the nice value, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7). </p>
<p> <i>Note</i>: the addition of the &quot;autogroup&quot; feature in Linux 2.6.38 means that the nice value no longer has its traditional effect in many circumstances. For details, see <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7).</p>
<h3>C library/kernel differences</h3>
<p> POSIX.1 specifies that <code>nice</code>() should return the new nice value. However, the raw Linux system call returns 0 on success. Likewise, the <code>nice</code>() wrapper function provided in glibc 2.2.3 and earlier returns 0 on success. </p>
<p> Since glibc 2.2.4, the <code>nice</code>() wrapper function provided by glibc provides conformance to POSIX.1 by calling <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2) to obtain the new nice value, which is then returned to the caller.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nice/">nice</a></code>(1), <code><a href="/docs/linux/man/1-renice/">renice</a></code>(1), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-getpriority/">getpriority</a></code>(2), <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/2-setpriority/">setpriority</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
