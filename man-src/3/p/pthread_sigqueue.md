---
title: "pthread_sigqueue(3)"
name: "pthread_sigqueue"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_sigqueue/"
description: "pthread_sigqueue – queue a signal and data to a thread"
---

<p>pthread_sigqueue &#8211; queue a signal and data to a thread</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;
#include &lt;signal.h&gt;

int pthread_sigqueue(pthread_t thread, int sig,
                     const union sigval value);</code></pre>
<p> Compile and link with <i>-pthread</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>pthread_sigqueue</code>(): _GNU_SOURCE</p>
<h2>Description</h2>
<p>The <code>pthread_sigqueue</code>() function performs a similar task to <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3), but, rather than sending a signal to a process, it sends a signal to a thread in the same process as the calling thread. </p>
<p> The <i>thread</i> argument is the ID of a thread in the same process as the caller. The <i>sig</i> argument specifies the signal to be sent. The <i>value</i> argument specifies data to accompany the signal; see <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3) for details.</p>
<h2>Return Value</h2>
<p>On success, <code>pthread_sigqueue</code>() returns 0; on error, it returns an error number.</p>
<h2>Errors</h2>
<dl>
<dt><code>EAGAIN</code></p>
<dd>The limit of signals which may be queued has been reached. (See <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7) for further information.)</p>
<dt><code>EINVAL</code></p>
<dd><i>sig</i> was invalid.</p>
<dt><code>ENOSYS</code></p>
<dd><code>pthread_sigqueue</code>() is not supported on this system.</p>
<dt><code>ESRCH</code></p>
<dd><i>thread</i> is not valid.</dl>
<h2>Versions</h2>
<p>The <code>pthread_sigqueue</code>() function first appeared in glibc 2.11.</p>
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
<td> <code>pthread_sigqueue</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>This function is a GNU extension.</p>
<h2>Notes</h2>
<p>The glibc implementation of <code>pthread_sigqueue</code>() gives an error (<code>EINVAL</code>) on attempts to send either of the real-time signals used internally by the NPTL threading implementation. See <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7) for details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-rt_tgsigqueueinfo/">rt_tgsigqueueinfo</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></code>(3), <code><a href="/docs/linux/man/3-sigqueue/">sigqueue</a></code>(3), <code><a href="/docs/linux/man/3-sigwait/">sigwait</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
