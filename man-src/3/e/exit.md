---
title: "exit(3)"
name: "exit"
section: "3"
letter: "e"
url: "/docs/linux/man/3-exit/"
description: "exit – cause normal process termination"
---

<h2 class="name">NAME</h2>
<p> exit &#8211; cause normal process termination </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
void exit(int status);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>exit</code>() function causes normal process termination and the least significant byte of <i>status</i> (i.e., <i>status &amp; 0xFF</i>) is returned to the parent (see <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2)). </p>
<p> All functions registered with <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3) and <code><a href="/docs/linux/man/3-on_exit/">on_exit</a></code>(3) are called, in the reverse order of their registration. (It is possible for one of these functions to use <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3) or <code><a href="/docs/linux/man/3-on_exit/">on_exit</a></code>(3) to register an additional function to be executed during exit processing; the new registration is added to the front of the list of functions that remain to be called.) If one of these functions does not return (e.g., it calls <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), or kills itself with a signal), then none of the remaining functions is called, and further exit processing (in particular, flushing of <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3) streams) is abandoned. If a function has been registered multiple times using <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3) or <code><a href="/docs/linux/man/3-on_exit/">on_exit</a></code>(3), then it is called as many times as it was registered. </p>
<p> All open <code><a href="/docs/linux/man/3-stdio/">stdio</a></code>(3) streams are flushed and closed. Files created by <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3) are removed. </p>
<p> The C standard specifies two constants, <code>EXIT_SUCCESS</code> and <code>EXIT_FAILURE</code>, that may be passed to <code>exit</code>() to indicate successful or unsuccessful termination, respectively.</p>
<h2>RETURN VALUE</h2>
<p> The <code>exit</code>() function does not return.</p>
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
<td> <code>exit</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:exit
</td>
</tr>
</table>
<p> The <code>exit</code>() function uses a global variable that is not protected, so it is not thread-safe.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> The behavior is undefined if one of the functions registered using <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3) and <code><a href="/docs/linux/man/3-on_exit/">on_exit</a></code>(3) calls either <code>exit</code>() or <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3). Note that a call to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) removes registrations created using <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3) and <code><a href="/docs/linux/man/3-on_exit/">on_exit</a></code>(3). </p>
<p> The use of <code>EXIT_SUCCESS</code> and <code>EXIT_FAILURE</code> is slightly more portable (to non-UNIX environments) than the use of 0 and some nonzero value like 1 or -1. In particular, VMS uses a different convention. </p>
<p> BSD has attempted to standardize exit codes (which some C libraries such as the GNU C library have also adopted); see the file <i>&lt;sysexits.h&gt;</i>. </p>
<p> After <code>exit</code>(), the exit status must be transmitted to the parent process. There are three cases:</p>
<dl>
<dt>&bull;</p>
<dd> If the parent has set <code>SA_NOCLDWAIT</code>, or has set the <code>SIGCHLD</code> handler to <code>SIG_IGN</code>, the status is discarded and the child dies immediately.</p>
<dt>&bull;</p>
<dd> If the parent was waiting on the child, it is notified of the exit status and the child dies immediately.</p>
<dt>&bull;</p>
<dd> Otherwise, the child becomes a &quot;zombie&quot; process: most of the process resources are recycled, but a slot containing minimal information about the child process (termination status, resource usage statistics) is retained in process table. This allows the parent to subsequently use <code><a href="/docs/linux/man/2-waitpid/">waitpid</a></code>(2) (or similar) to learn the termination status of the child; at that point the zombie process slot is released.</dl>
<p> If the implementation supports the <code>SIGCHLD</code> signal, this signal is sent to the parent. If the parent has set <code>SA_NOCLDWAIT</code>, it is undefined whether a <code>SIGCHLD</code> signal is sent.</p>
<h3>Signals sent to other processes</h3>
<p> If the exiting process is a session leader and its controlling terminal is the controlling terminal of the session, then each process in the foreground process group of this controlling terminal is sent a <code>SIGHUP</code> signal, and the terminal is disassociated from this session, allowing it to be acquired by a new controlling process. </p>
<p> If the exit of the process causes a process group to become orphaned, and if any member of the newly orphaned process group is stopped, then a <code>SIGHUP</code> signal followed by a <code>SIGCONT</code> signal will be sent to each process in this process group. See <code><a href="/docs/linux/man/2-setpgid/">setpgid</a></code>(2) for an explanation of orphaned process groups. </p>
<p> Except in the above cases, where the signalled processes may be children of the terminating process, termination of a process does <i>not</i> in general cause a signal to be sent to children of that process. However, a process can use the <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2) <code>PR_SET_PDEATHSIG</code> operation to arrange that it receives a signal if its parent terminates.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), <code><a href="/docs/linux/man/2-get_robust_list/">get_robust_list</a></code>(2), <code><a href="/docs/linux/man/2-setpgid/">setpgid</a></code>(2), <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2), <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3), <code><a href="/docs/linux/man/3-on_exit/">on_exit</a></code>(3), <code><a href="/docs/linux/man/3-tmpfile/">tmpfile</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
