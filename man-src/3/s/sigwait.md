---
title: "sigwait(3)"
name: "sigwait"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sigwait/"
description: "sigwait – wait for a signal"
---

<p>sigwait &#8211; wait for a signal</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;signal.h&gt;

int sigwait(const sigset_t *set, int *sig);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>sigwait</code>():</p>
<dl>
<dd>Since glibc 2.26:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;199506L<br />
 Glibc 2.25 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_POSIX_C_SOURCE</dl>
<h2>Description</h2>
<p>The <code>sigwait</code>() function suspends execution of the calling thread until one of the signals specified in the signal set <i>set</i> becomes pending. The function accepts the signal (removes it from the pending list of signals), and returns the signal number in <i>sig</i>. </p>
<p> The operation of <code>sigwait</code>() is the same as <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2), except that:</p>
<dl>
<dt>*</p>
<dd><code>sigwait</code>() returns only the signal number, rather than a <i>siginfo_t</i> structure describing the signal.</p>
<dt>*</p>
<dd>The return values of the two functions are different.</dl>
<h2>Return Value</h2>
<p>On success, <code>sigwait</code>() returns 0. On error, it returns a positive error number (listed in ERRORS).</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>set</i> contains an invalid signal number.</dl>
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
<td> <code>sigwait</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p><code>sigwait</code>() is implemented using <code><a href="/docs/linux/man/2-sigtimedwait/">sigtimedwait</a></code>(2). </p>
<p> The glibc implementation of <code>sigwait</code>() silently ignores attempts to wait for the two real-time signals that are used internally by the NPTL threading implementation. See <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7) for details.</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signalfd/">signalfd</a></code>(2), <code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2), <code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2), <code><a href="/docs/linux/man/2-sigwaitinfo/">sigwaitinfo</a></code>(2), <code><a href="/docs/linux/man/3-sigsetops/">sigsetops</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
