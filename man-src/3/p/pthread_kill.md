---
title: "pthread_kill(3)"
name: "pthread_kill"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_kill/"
description: "pthread_kill – send a signal to a thread"
---

<p>pthread_kill &#8211; send a signal to a thread</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;signal.h&gt;

int pthread_kill(pthread_t thread, int sig);</code></pre>
<p> Compile and link with <i>-pthread</i>. Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>pthread_kill</code>():</p>
<dl>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199506L || _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
<h2>Description</h2>
<p>The <code>pthread_kill</code>() function sends the signal <i>sig</i> to <i>thread</i>, a thread in the same process as the caller. The signal is asynchronously directed to <i>thread</i>. </p>
<p> If <i>sig</i> is 0, then no signal is sent, but error checking is still performed.</p>
<h2>Return Value</h2>
<p>On success, <code>pthread_kill</code>() returns 0; on error, it returns an error number, and no signal is sent.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd>An invalid signal was specified.</dl>
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
<td> <code>pthread_kill</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>Signal dispositions are process-wide: if a signal handler is installed, the handler will be invoked in the thread <i>thread</i>, but if the disposition of the signal is &quot;stop&quot;, &quot;continue&quot;, or &quot;terminate&quot;, this action will affect the whole process. </p>
<p> The glibc implementation of <code>pthread_kill</code>() gives an error (<code>EINVAL</code>) on attempts to send either of the real-time signals used internally by the NPTL threading implementation. See <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7) for details. </p>
<p> POSIX.1-2008 recommends that if an implementation detects the use of a thread ID after the end of its lifetime, <code>pthread_kill</code>() should return the error <code>ESRCH</code>. The glibc implementation returns this error in the cases where an invalid thread ID can be detected. But note also that POSIX says that an attempt to use a thread ID whose lifetime has ended produces undefined behavior, and an attempt to use an invalid thread ID in a call to <code>pthread_kill</code>() can, for example, cause a segmentation fault.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2), <code><a href="/docs/linux/man/3-pthread_self/">pthread_self</a></code>(3), <code><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></code>(3), <code><a href="/docs/linux/man/3-raise/">raise</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
