---
title: "kill(2)"
name: "kill"
section: "2"
letter: "k"
url: "/docs/linux/man/2-kill/"
description: "kill – send signal to a process"
---

<h2 class="name">NAME</h2>
<p> kill &#8211; send signal to a process </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;signal.h&gt;
#include &lt;sys/types.h&gt;
int kill(pid_t pid, int sig);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>kill</code>(): _POSIX_C_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>kill</code>() system call can be used to send any signal to any process group or process. </p>
<p> If <i>pid</i> is positive, then signal <i>sig</i> is sent to the process with the ID specified by <i>pid</i>. </p>
<p> If <i>pid</i> equals 0, then <i>sig</i> is sent to every process in the process group of the calling process. </p>
<p> If <i>pid</i> equals -1, then <i>sig</i> is sent to every process for which the calling process has permission to send signals, except for process 1 (<i>init</i>), but see below. </p>
<p> If <i>pid</i> is less than -1, then <i>sig</i> is sent to every process in the process group whose ID is <i>-pid</i>. </p>
<p> If <i>sig</i> is 0, then no signal is sent, but existence and permission checks are still performed; this can be used to check for the existence of a process ID or process group ID that the caller is permitted to signal. </p>
<p> For a process to have permission to send a signal, it must either be privileged (under Linux: have the <code>CAP_KILL</code> capability in the user namespace of the target process), or the real or effective user ID of the sending process must equal the real or saved set-user-ID of the target process. In the case of <code>SIGCONT</code>, it suffices when the sending and receiving processes belong to the same session. (Historically, the rules were different; see NOTES.)</p>
<h2>RETURN VALUE</h2>
<p> On success (at least one signal was sent), zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> An invalid signal was specified.</p>
<dt><code>EPERM</code></p>
<dd> The calling process does not have permission to send the signal to any of the target processes.</p>
<dt><code>ESRCH</code></p>
<dd> The target process or process group does not exist. Note that an existing process might be a zombie, a process that has terminated execution, but has not yet been <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2)ed for.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> The only signals that can be sent to process ID 1, the <i>init</i> process, are those for which <i>init</i> has explicitly installed signal handlers. This is done to assure the system is not brought down accidentally. </p>
<p> POSIX.1 requires that <i>kill(-1,sig)</i> send <i>sig</i> to all processes that the calling process may send signals to, except possibly for some implementation-defined system processes. Linux allows a process to signal itself, but on Linux the call <i>kill(-1,sig)</i> does not signal the calling process. </p>
<p> POSIX.1 requires that if a process sends a signal to itself, and the sending thread does not have the signal blocked, and no other thread has it unblocked or is waiting for it in <code><a href="/docs/linux/man/3-sigwait/">sigwait</a></code>(3), at least one unblocked signal must be delivered to the sending thread before the <code>kill</code>() returns.</p>
<h3>Linux notes</h3>
<p> Across different kernel versions, Linux has enforced different rules for the permissions required for an unprivileged process to send a signal to another process. In kernels 1.0 to 1.2.2, a signal could be sent if the effective user ID of the sender matched effective user ID of the target, or the real user ID of the sender matched the real user ID of the target. From kernel 1.2.3 until 1.3.77, a signal could be sent if the effective user ID of the sender matched either the real or effective user ID of the target. The current rules, which conform to POSIX.1, were adopted in kernel 1.3.78.</p>
<h2>BUGS</h2>
<p> In 2.6 kernels up to and including 2.6.7, there was a bug that meant that when sending signals to a process group, <code>kill</code>() failed with the error <code>EPERM</code> if the caller did not have permission to send the signal to <i>any</i> (rather than <i>all</i>) of the members of the process group. Notwithstanding this error return, the signal was still delivered to all of the processes for which the caller had permission to signal.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kill/">kill</a></code>(1), <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), <code><a href="/docs/linux/man/2-pidfd_send_signal/">pidfd_send_signal</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-tkill/">tkill</a></code>(2), <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), <code><a href="/docs/linux/man/3-killpg/">killpg</a></code>(3), <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-credentials/">credentials</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
