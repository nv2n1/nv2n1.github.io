---
title: "wait4(2)"
name: "wait4"
section: "2"
letter: "w"
url: "/docs/linux/man/2-wait4/"
description: "wait3, wait4 – wait for process to change state, BSD style"
---

<h2 class="name">NAME</h2>
<p> wait3, wait4 &#8211; wait for process to change state, BSD style </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/resource.h&gt;
#include &lt;sys/time.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;sys/wait.h&gt;
pid_t wait3(int *wstatus, int options,
            struct rusage *rusage);
pid_t wait4(pid_t pid, int *wstatus, int options,
            struct rusage *rusage);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>wait3</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.26:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE ||<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500&nbsp;&amp;&amp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;!&nbsp;(_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L ||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;600))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;From glibc 2.19 to 2.25:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE ||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
 <code>wait4</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> These functions are nonstandard; in new programs, the use of <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) or <code><a href="/docs/linux/man/2-waitid/">waitid</a></code>(2) is preferable. </p>
<p> The <code>wait3</code>() and <code>wait4</code>() system calls are similar to <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2), but additionally return resource usage information about the child in the structure pointed to by <i>rusage</i>. </p>
<p> Other than the use of the <i>rusage</i> argument, the following <code>wait3</code>() call: </p>
<p> wait3(wstatus, options, rusage); </p>
<p> is equivalent to: </p>
<p> waitpid(-1, wstatus, options); </p>
<p> Similarly, the following <code>wait4</code>() call: </p>
<p> wait4(pid, wstatus, options, rusage); </p>
<p> is equivalent to: </p>
<p> waitpid(pid, wstatus, options); </p>
<p> In other words, <code>wait3</code>() waits of any child, while <code>wait4</code>() can be used to select a specific child, or children, on which to wait. See <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) for further details. </p>
<p> If <i>rusage</i> is not NULL, the <i>struct rusage</i> to which it points will be filled with accounting information about the child. See <code><a href="/docs/linux/man/2-getrusage/">getrusage</a></code>(2) for details.</p>
<h2>RETURN VALUE</h2>
<p> As for <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2).</p>
<h2>ERRORS</h2>
<p> As for <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2).</p>
<h2>CONFORMING TO</h2>
<p> 4.3BSD. </p>
<p> SUSv1 included a specification of <code>wait3</code>(); SUSv2 included <code>wait3</code>(), but marked it LEGACY; SUSv3 removed it.</p>
<h2>NOTES</h2>
<p> Including <i>&lt;sys/time.h&gt;</i> is not required these days, but increases portability. (Indeed, <i>&lt;sys/resource.h&gt;</i> defines the <i>rusage</i> structure with fields of type <i>struct timeval</i> defined in <i>&lt;sys/time.h&gt;</i>.)</p>
<h3>C library/kernel differences</h3>
<p> On Linux, <code>wait3</code>() is a library function implemented on top of the <code>wait4</code>() system call.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-getrusage/">getrusage</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
