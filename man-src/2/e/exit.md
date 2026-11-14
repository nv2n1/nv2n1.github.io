---
title: "exit(2)"
name: "exit"
section: "2"
letter: "e"
url: "/docs/linux/man/2-exit/"
description: "_exit, _Exit – terminate the calling process"
---

<h2 class="name">NAME</h2>
<p> _exit, _Exit &#8211; terminate the calling process </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>void _exit(int </code><i>status</i><code>);</code> </p>
<p> <code>#include &lt;stdlib.h&gt;</code> </p>
<p> <code>void _Exit(int </code><i>status</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>_Exit</code>():</p>
<dl>
<dt>
<dd> _ISOC99_SOURCE || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>DESCRIPTION</h2>
<p> <code>_exit</code>() terminates the calling process &quot;immediately&quot;. Any open file descriptors belonging to the process are closed. Any children of the process are inherited by <code><a href="/docs/linux/man/1-init/">init</a></code>(1) (or by the nearest &quot;subreaper&quot; process as defined through the use of the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_CHILD_SUBREAPER</code> operation). The process&#8217;s parent is sent a <code>SIGCHLD</code> signal. </p>
<p> The value <i>status &amp; 0xFF</i> is returned to the parent process as the process&#8217;s exit status, and can be collected by the parent using one of the <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) family of calls. </p>
<p> The function <code>_Exit</code>() is equivalent to <code>_exit</code>().</p>
<h2>RETURN VALUE</h2>
<p> These functions do not return.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD. The function <code>_Exit</code>() was introduced by C99.</p>
<h2>NOTES</h2>
<p> For a discussion on the effects of an exit, the transmission of exit status, zombie processes, signals sent, and so on, see <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3). </p>
<p> The function <code>_exit</code>() is like <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), but does not call any functions registered with <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3) or <code><a href="/docs/linux/man/3-on_exit/">on_exit</a></code>(3). Open <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3) streams are not flushed. On the other hand, <code>_exit</code>() does close open file descriptors, and this may cause an unknown delay, waiting for pending output to finish. If the delay is undesired, it may be useful to call functions like <code><a href="/docs/linux/man/3-tcflush/">tcflush</a></code>(3) before calling <code>_exit</code>(). Whether any pending I/O is canceled, and which pending I/O may be canceled upon <code>_exit</code>(), is implementation-dependent.</p>
<h3>C library/kernel differences</h3>
<p> In glibc up to version 2.3, the <code>_exit</code>() wrapper function invoked the kernel system call of the same name. Since glibc 2.3, the wrapper function invokes <code><a href="/docs/linux/man/2-exit_group/">exit_group</a></code>(2), in order to terminate all of the threads in a process. (The raw <code>_exit</code>() system call terminates only the calling thread.)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-exit_group/">exit_group</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2), <code><a href="/docs/linux/man/2-wait4/">wait4</a></code>(2), <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2), <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3), <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), <code><a href="/docs/linux/man/3-on_exit/">on_exit</a></code>(3), <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
