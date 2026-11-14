---
title: "setsid(2)"
name: "setsid"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setsid/"
description: "setsid – creates a session and sets the process group ID"
---

<h2 class="name">NAME</h2>
<p> setsid &#8211; creates a session and sets the process group ID </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>pid_t setsid(void);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>setsid</code>() creates a new session if the calling process is not a process group leader. The calling process is the leader of the new session (i.e., its session ID is made the same as its process ID). The calling process also becomes the process group leader of a new process group in the session (i.e., its process group ID is made the same as its process ID). </p>
<p> The calling process will be the only process in the new process group and in the new session. </p>
<p> Initially, the new session has no controlling terminal. For details of how a session acquires a controlling terminal, see <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7).</p>
<h2>RETURN VALUE</h2>
<p> On success, the (new) session ID of the calling process is returned. On error, <i>(pid_t)&nbsp;-1</i> is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EPERM</code></p>
<dd> The process group ID of any process equals the PID of the calling process. Thus, in particular, <code>setsid</code>() fails if the calling process is already a process group leader.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4.</p>
<h2>NOTES</h2>
<p> A child created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits its parent&#8217;s session ID. The session ID is preserved across an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> A process group leader is a process whose process group ID equals its PID. Disallowing a process group leader from calling <code>setsid</code>() prevents the possibility that a process group leader places itself in a new session while other processes in the process group remain in the original session; such a scenario would break the strict two-level hierarchy of sessions and process groups. In order to be sure that <code>setsid</code>() will succeed, call <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and have the parent <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), while the child (which by definition can&#8217;t be a process group leader) calls <code>setsid</code>(). </p>
<p> If a session has a controlling terminal, and the <code>CLOCAL</code> flag for that terminal is not set, and a terminal hangup occurs, then the session leader is sent a <code>SIGHUP</code> signal. </p>
<p> If a process that is a session leader terminates, then a <code>SIGHUP</code> signal is sent to each process in the foreground process group of the controlling terminal.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-setsid/">setsid</a></code>(1), <code><a href="/docs/linux/man/2-getsid/">getsid</a></code>(2), <code><a href="/docs/linux/man/2-setpgid/">setpgid</a></code>(2), <code><a href="/docs/linux/man/2-setpgrp/">setpgrp</a></code>(2), <code><a href="/docs/linux/man/3-tcgetsid/">tcgetsid</a></code>(3), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-sched/">sched</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
