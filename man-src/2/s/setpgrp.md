---
title: "setpgrp(2)"
name: "setpgrp"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setpgrp/"
description: "setpgid, getpgid, setpgrp, getpgrp – set/get process group"
---

<h2 class="name">NAME</h2>
<p> setpgid, getpgid, setpgrp, getpgrp &#8211; set/get process group </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int setpgid(pid_t </code><i>pid</i><code>, pid_t </code><i>pgid</i><code>);</code><br />
 <code>pid_t getpgid(pid_t </code><i>pid</i><code>);</code> </p>
<p> <code>pid_t getpgrp(void);</code> /* POSIX.1 version */<br />
 <code>pid_t getpgrp(pid_t </code><i>pid</i><code>);</code> /* BSD version */ </p>
<p> <code>int setpgrp(void);</code> /* System V version */<br />
 <code>int setpgrp(pid_t </code><i>pid</i><code>, pid_t </code><i>pgid</i><code>);</code> /* BSD version */ </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getpgid</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.12:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</dl>
<p> <code>setpgrp</code>() (POSIX.1): </p>
<pre><code>
_XOPEN_SOURCE &amp;nbsp;
&gt;= &amp;nbsp;
500 || /* Since glibc 2.19: */ _DEFAULT_SOURCE || /* Glibc versions &lt;= 2.19: */ _SVID_SOURCE
</code></pre>
<p> <code>setpgrp</code>()&nbsp;(BSD), <code>getpgrp</code>()&nbsp;(BSD): </p>
<pre><code>
[These are available only before glibc 2.19] _BSD_SOURCE &amp;&amp;
    !&amp;nbsp;
(_POSIX_SOURCE || _POSIX_C_SOURCE || _XOPEN_SOURCE ||
 _GNU_SOURCE || _SVID_SOURCE)
</code></pre>
<h2>DESCRIPTION</h2>
<p> All of these interfaces are available on Linux, and are used for getting and setting the process group ID (PGID) of a process. The preferred, POSIX.1-specified ways of doing this are: <code>getpgrp</code>(void), for retrieving the calling process&#8217;s PGID; and <code>setpgid</code>(), for setting a process&#8217;s PGID. </p>
<p> <code>setpgid</code>() sets the PGID of the process specified by <i>pid</i> to <i>pgid</i>. If <i>pid</i> is zero, then the process ID of the calling process is used. If <i>pgid</i> is zero, then the PGID of the process specified by <i>pid</i> is made the same as its process ID. If <code>setpgid</code>() is used to move a process from one process group to another (as is done by some shells when creating pipelines), both process groups must be part of the same session (see <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2) and <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)). In this case, the <i>pgid</i> specifies an existing process group to be joined and the session ID of that group must match the session ID of the joining process. </p>
<p> The POSIX.1 version of <code>getpgrp</code>(), which takes no arguments, returns the PGID of the calling process. </p>
<p> <code>getpgid</code>() returns the PGID of the process specified by <i>pid</i>. If <i>pid</i> is zero, the process ID of the calling process is used. (Retrieving the PGID of a process other than the caller is rarely necessary, and the POSIX.1 <code>getpgrp</code>() is preferred for that task.) </p>
<p> The System V-style <code>setpgrp</code>(), which takes no arguments, is equivalent to <i>setpgid(0, 0)</i>. </p>
<p> The BSD-specific <code>setpgrp</code>() call, which takes arguments <i>pid</i> and <i>pgid</i>, is a wrapper function that calls </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;setpgid(pid, pgid) </p>
<p> Since glibc 2.19, the BSD-specific <code>setpgrp</code>() function is no longer exposed by <i>&lt;unistd.h&gt;</i>; calls should be replaced with the <code>setpgid</code>() call shown above. </p>
<p> The BSD-specific <code>getpgrp</code>() call, which takes a single <i>pid</i> argument, is a wrapper function that calls </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;getpgid(pid) </p>
<p> Since glibc 2.19, the BSD-specific <code>getpgrp</code>() function is no longer exposed by <i>&lt;unistd.h&gt;</i>; calls should be replaced with calls to the POSIX.1 <code>getpgrp</code>() which takes no arguments (if the intent is to obtain the caller&#8217;s PGID), or with the <code>getpgid</code>() call shown above.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>setpgid</code>() and <code>setpgrp</code>() return zero. On error, -1 is returned, and <i>errno</i> is set appropriately. </p>
<p> The POSIX.1 <code>getpgrp</code>() always returns the PGID of the caller. </p>
<p> <code>getpgid</code>(), and the BSD-specific <code>getpgrp</code>() return a process group on success. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> An attempt was made to change the process group ID of one of the children of the calling process and the child had already performed an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) (<code>setpgid</code>(), <code>setpgrp</code>()).</p>
<dt><code>EINVAL</code></p>
<dd> <i>pgid</i> is less than 0 (<code>setpgid</code>(), <code>setpgrp</code>()).</p>
<dt><code>EPERM</code></p>
<dd> An attempt was made to move a process into a process group in a different session, or to change the process group ID of one of the children of the calling process and the child was in a different session, or to change the process group ID of a session leader (<code>setpgid</code>(), <code>setpgrp</code>()).</p>
<dt><code>ESRCH</code></p>
<dd> For <code>getpgid</code>(): <i>pid</i> does not match any process. For <code>setpgid</code>(): <i>pid</i> is not the calling process and not a child of the calling process.</dl>
<h2>CONFORMING TO</h2>
<p> <code>setpgid</code>() and the version of <code>getpgrp</code>() with no arguments conform to POSIX.1-2001. </p>
<p> POSIX.1-2001 also specifies <code>getpgid</code>() and the version of <code>setpgrp</code>() that takes no arguments. (POSIX.1-2008 marks this <code>setpgrp</code>() specification as obsolete.) </p>
<p> The version of <code>getpgrp</code>() with one argument and the version of <code>setpgrp</code>() that takes two arguments derive from 4.2BSD, and are not specified by POSIX.1.</p>
<h2>NOTES</h2>
<p> A child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits its parent&#8217;s process group ID. The PGID is preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> Each process group is a member of a session and each process is a member of the session of which its process group is a member. (See <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7).) </p>
<p> A session can have a controlling terminal. At any time, one (and only one) of the process groups in the session can be the foreground process group for the terminal; the remaining process groups are in the background. If a signal is generated from the terminal (e.g., typing the interrupt key to generate <code>SIGINT</code>), that signal is sent to the foreground process group. (See <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3) for a description of the characters that generate signals.) Only the foreground process group may <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from the terminal; if a background process group tries to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from the terminal, then the group is sent a <code>SIGTTIN</code> signal, which suspends it. The <code><a href="/docs/linux/man/3-tcgetpgrp/">tcgetpgrp</a></code>(3) and <code><a href="/docs/linux/man/3-tcsetpgrp/">tcsetpgrp</a></code>(3) functions are used to get/set the foreground process group of the controlling terminal. </p>
<p> The <code>setpgid</code>() and <code>getpgrp</code>() calls are used by programs such as <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1) to create process groups in order to implement shell job control. </p>
<p> If the termination of a process causes a process group to become orphaned, and if any member of the newly orphaned process group is stopped, then a <code>SIGHUP</code> signal followed by a <code>SIGCONT</code> signal will be sent to each process in the newly orphaned process group. An orphaned process group is one in which the parent of every member of process group is either itself also a member of the process group or is a member of a process group in a different session (see also <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getuid/">getuid</a></code>(2), <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2), <code><a href="/docs/linux/man/3-tcgetpgrp/">tcgetpgrp</a></code>(3), <code><a href="/docs/linux/man/3-tcsetpgrp/">tcsetpgrp</a></code>(3), <code><a href="/docs/linux/man/3-termios/">termios</a></code>(3), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
