---
title: "sigpause(3)"
name: "sigpause"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sigpause/"
description: "sigpause – atomically release blocked signals and wait for interrupt"
---

<p>sigpause &#8211; atomically release blocked signals and wait for interrupt</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;signal.h&gt;

int sigpause(int sigmask); /* BSD (but see NOTES) */

int sigpause(int sig); /* System V / UNIX 95 */</code></pre>
<h2>Description</h2>
<p>Don&#8217;t use this function. Use <code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2) instead. </p>
<p> The function <code>sigpause</code>() is designed to wait for some signal. It changes the process&#8217;s signal mask (set of blocked signals), and then waits for a signal to arrive. Upon arrival of a signal, the original signal mask is restored.</p>
<h2>Return Value</h2>
<p>If <code>sigpause</code>() returns, it was interrupted by a signal and the return value is -1 with <i>errno</i> set to <code>EINTR</code>.</p>
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
<td> <code>sigpause</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>The System V version of <code>sigpause</code>() is standardized in POSIX.1-2001. It is also specified in POSIX.1-2008, where it is marked obsolete.</p>
<h2>Notes</h2>
<h3>History</h3>
<p>The classical BSD version of this function appeared in 4.2BSD. It sets the process&#8217;s signal mask to <i>sigmask</i>. UNIX 95 standardized the incompatible System V version of this function, which removes only the specified signal <i>sig</i> from the process&#8217;s signal mask. The unfortunate situation with two incompatible functions with the same name was solved by the <code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2) function, that takes a <i>sigset_t&nbsp;*</i> argument (instead of an <i>int</i>).</p>
<h3>Linux notes</h3>
<p>On Linux, this routine is a system call only on the Sparc (sparc64) architecture. </p>
<p> Glibc uses the BSD version if the <code>_BSD_SOURCE</code> feature test macro is defined and none of <code>_POSIX_SOURCE</code>, <code>_POSIX_C_SOURCE</code>, <code>_XOPEN_SOURCE</code>, <code>_GNU_SOURCE</code>, or <code>_SVID_SOURCE</code> is defined. Otherwise, the System V version is used, and feature test macros must be defined as follows to obtain the declaration:</p>
<dl>
<dt>*</p>
<dd>Since glibc 2.26: _XOPEN_SOURCE &gt;= 500</p>
<dt>*</p>
<dd>Glibc 2.25 and earlier: _XOPEN_SOURCE</dl>
<p> Since glibc 2.19, only the System V version is exposed by <i>&lt;signal.h&gt;</i>; applications that formerly used the BSD <code>sigpause</code>() should be amended to use <code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2), <code><a href="/docs/linux/man/3-sigblock/">sigblock</a></code>(3), <code><a href="/docs/linux/man/3-sigvec/">sigvec</a></code>(3), <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
