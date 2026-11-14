---
title: "forkpty(3)"
name: "forkpty"
section: "3"
letter: "f"
url: "/docs/linux/man/3-forkpty/"
description: "openpty, login_tty, forkpty – terminal utility functions"
---

<h2 class="name">NAME</h2>
<p> openpty, login_tty, forkpty &#8211; terminal utility functions </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;pty.h&gt;
int openpty(int *amaster, int *aslave, char *name,
            const struct termios *termp,
            const struct winsize *winp);
pid_t forkpty(int *amaster, char *name,
              const struct termios *termp,
              const struct winsize *winp);
#include &lt;utmp.h&gt;
int login_tty(int fd);
Link with - lutil.
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>openpty</code>() function finds an available pseudoterminal and returns file descriptors for the master and slave in <i>amaster</i> and <i>aslave</i>. If <i>name</i> is not NULL, the filename of the slave is returned in <i>name</i>. If <i>termp</i> is not NULL, the terminal parameters of the slave will be set to the values in <i>termp</i>. If <i>winp</i> is not NULL, the window size of the slave will be set to the values in <i>winp</i>. </p>
<p> The <code>login_tty</code>() function prepares for a login on the terminal referred to by the file descriptor <i>fd</i> (which may be a real terminal device, or the slave of a pseudoterminal as returned by <code>openpty</code>()) by creating a new session, making <i>fd</i> the controlling terminal for the calling process, setting <i>fd</i> to be the standard input, output, and error streams of the current process, and closing <i>fd</i>. </p>
<p> The <code>forkpty</code>() function combines <code>openpty</code>(), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), and <code>login_tty</code>() to create a new process operating in a pseudoterminal. A file descriptor referring to master side of the pseudoterminal is returned in <i>amaster</i>. If <i>name</i> is not NULL, the buffer it points to is used to return the filename of the slave. The <i>termp</i> and <i>winp</i> arguments, if not NULL, will determine the terminal attributes and window size of the slave side of the pseudoterminal.</p>
<h2>RETURN VALUE</h2>
<p> If a call to <code>openpty</code>(), <code>login_tty</code>(), or <code>forkpty</code>() is not successful, -1 is returned and <i>errno</i> is set to indicate the error. Otherwise, <code>openpty</code>(), <code>login_tty</code>(), and the child process of <code>forkpty</code>() return 0, and the parent process of <code>forkpty</code>() returns the process ID of the child process.</p>
<h2>ERRORS</h2>
<p> <code>openpty</code>() fails if:</p>
<dl>
<dt><code>ENOENT</code></p>
<dd> There are no available terminals.</dl>
<p> <code>login_tty</code>() fails if <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) fails to set <i>fd</i> to the controlling terminal of the calling process. </p>
<p> <code>forkpty</code>() fails if either <code>openpty</code>() or <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) fails.</p>
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
<td> <code>forkpty</code>(), <code>openpty</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
<tr VALIGN=top>
<td> <code>login_tty</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:ttyname
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These are BSD functions, present in glibc. They are not standardized in POSIX.</p>
<h2>NOTES</h2>
<p> The <code>const</code> modifiers were added to the structure pointer arguments of <code>openpty</code>() and <code>forkpty</code>() in glibc 2.8. </p>
<p> In versions of glibc before 2.0.92, <code>openpty</code>() returns file descriptors for a BSD pseudoterminal pair; since glibc 2.0.92, it first attempts to open a UNIX 98 pseudoterminal pair, and falls back to opening a BSD pseudoterminal pair if that fails.</p>
<h2>BUGS</h2>
<p> Nobody knows how much space should be reserved for <i>name</i>. So, calling <code>openpty</code>() or <code>forkpty</code>() with non-NULL <i>name</i> may not be secure.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/3-ttyname/">ttyname</a></code>(3), <code><a href="/docs/linux/man/7-pty/">pty</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
