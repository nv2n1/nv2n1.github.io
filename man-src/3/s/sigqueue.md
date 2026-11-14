---
title: "sigqueue(3)"
name: "sigqueue"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sigqueue/"
description: "sigqueue – queue a signal and data to a process"
---

<p>sigqueue &#8211; queue a signal and data to a process</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;signal.h&gt;
int sigqueue(pid_t pid, int sig, const union sigval value);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>sigqueue</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199309L</p>
<h2>Description</h2>
<p><code>sigqueue</code>() sends the signal specified in <i>sig</i> to the process whose PID is given in <i>pid</i>. The permissions required to send a signal are the same as for <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2). As with <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), the null signal (0) can be used to check if a process with a given PID exists. </p>
<p> The <i>value</i> argument is used to specify an accompanying item of data (either an integer or a pointer value) to be sent with the signal, and has the following type: </p>
<p> union sigval {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;sival_int;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;*sival_ptr; }; </p>
<p> If the receiving process has installed a handler for this signal using the <code>SA_SIGINFO</code> flag to <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), then it can obtain this data via the <i>si_value</i> field of the <i>siginfo_t</i> structure passed as the second argument to the handler. Furthermore, the <i>si_code</i> field of that structure will be set to <code>SI_QUEUE</code>.</p>
<h2>Return Value</h2>
<p>On success, <code>sigqueue</code>() returns 0, indicating that the signal was successfully queued to the receiving process. Otherwise, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd>The limit of signals which may be queued has been reached. (See <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) for further information.)</p>
<dt><code>EINVAL</code></p>
<dd><i>sig</i> was invalid.</p>
<dt><code>EPERM</code></p>
<dd>The process does not have permission to send the signal to the receiving process. For the required permissions, see <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2).</p>
<dt><code>ESRCH</code></p>
<dd>No process has a PID matching <i>pid</i>.</dl>
<h2>Versions</h2>
<p><code>sigqueue</code>() and the underlying <code>rt_sigqueueinfo</code>() system call first appeared in Linux 2.2.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>sigqueue</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>If this function results in the sending of a signal to the process that invoked it, and that signal was not blocked by the calling thread, and no other threads were willing to handle this signal (either by having it unblocked, or by waiting for it using <code><a href="/docs/linux/man/3-sigwait/">sigwait</a></code>(3)), then at least some signal must be delivered to this thread before this function returns.</p>
<h3>C library/kernel differences</h3>
<p>On Linux, <code>sigqueue</code>() is implemented using the <code><a href="/docs/linux/man/2-rt_sigqueueinfo/">rt_sigqueueinfo</a></code>(2) system call. The system call differs in its third argument, which is the <i>siginfo_t</i> structure that will be supplied to the receiving process&#8217;s signal handler or returned by the receiving process&#8217;s <code><a href="/docs/linux/man/2-sigtimedwait/">sigtimedwait</a></code>(2) call. Inside the glibc <code>sigqueue</code>() wrapper, this argument, <i>uinfo</i>, is initialized as follows: </p>
<p> uinfo.si_signo = sig; /* Argument supplied to sigqueue() */ uinfo.si_code = SI_QUEUE; uinfo.si_pid = getpid(); /* Process ID of sender */ uinfo.si_uid = getuid(); /* Real UID of sender */ uinfo.si_value = val; /* Argument supplied to sigqueue() */</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-rt_sigqueueinfo/">rt_sigqueueinfo</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/3-pthread_sigqueue/">pthread_sigqueue</a></code>(3), <code><a href="/docs/linux/man/3-sigwait/">sigwait</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
