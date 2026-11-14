---
title: "sigrelse(3)"
name: "sigrelse"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sigrelse/"
description: "sigset, sighold, sigrelse, sigignore – System V signal API"
---

<p>sigset, sighold, sigrelse, sigignore &#8211; System V signal API</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;signal.h&gt;</code></pre>
<p> <code>typedef void (*sighandler_t)(int);</code> <code>sighandler_t sigset(int </code><i>sig</i><code>, sighandler_t </code><i>disp</i><code>);</code> </p>
<pre><code>int sighold(int sig);
int sigrelse(int sig);
int sigignore(int sig);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>sigset</code>(), <code>sighold</code>(), <code>sigrelse</code>(), <code>sigignore</code>(): </p>
<dl>
<dd>_XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
<h2>Description</h2>
<p>These functions are provided in glibc as a compatibility interface for programs that make use of the historical System V signal API. This API is obsolete: new applications should use the POSIX signal API (<code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), etc.) </p>
<p> The <code>sigset</code>() function modifies the disposition of the signal <i>sig</i>. The <i>disp</i> argument can be the address of a signal handler function, or one of the following constants:</p>
<dl>
<dt><code>SIG_DFL</code></p>
<dd>Reset the disposition of <i>sig</i> to the default.</p>
<dt><code>SIG_IGN</code></p>
<dd>Ignore <i>sig</i>.</p>
<dt><code>SIG_HOLD</code></p>
<dd>Add <i>sig</i> to the process&#8217;s signal mask, but leave the disposition of <i>sig</i> unchanged.</dl>
<p> If <i>disp</i> specifies the address of a signal handler, then <i>sig</i> is added to the process&#8217;s signal mask during execution of the handler. </p>
<p> If <i>disp</i> was specified as a value other than <code>SIG_HOLD</code>, then <i>sig</i> is removed from the process&#8217;s signal mask. </p>
<p> The dispositions for <code>SIGKILL</code> and <code>SIGSTOP</code> cannot be changed. </p>
<p> The <code>sighold</code>() function adds <i>sig</i> to the calling process&#8217;s signal mask. </p>
<p> The <code>sigrelse</code>() function removes <i>sig</i> from the calling process&#8217;s signal mask. </p>
<p> The <code>sigignore</code>() function sets the disposition of <i>sig</i> to <code>SIG_IGN</code>.</p>
<h2>Return Value</h2>
<p>On success, <code>sigset</code>() returns <code>SIG_HOLD</code> if <i>sig</i> was blocked before the call, or the signal&#8217;s previous disposition if it was not blocked before the call. On error, <code>sigset</code>() returns -1, with <i>errno</i> set to indicate the error. (But see BUGS below.) </p>
<p> The <code>sighold</code>(), <code>sigrelse</code>(), and <code>sigignore</code>() functions return 0 on success; on error, these functions return -1 and set <i>errno</i> to indicate the error.</p>
<h2>Errors</h2>
<p>For <code>sigset</code>() see the ERRORS under <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) and <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2). </p>
<p> For <code>sighold</code>() and <code>sigrelse</code>() see the ERRORS under <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2). </p>
<p> For <code>sigignore</code>(), see the errors under <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2).</p>
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
<td> <code>sigset</code>(), <code>sighold</code>(),<br />
 <code>sigrelse</code>(), <code>sigignore</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>SVr4, POSIX.1-2001, POSIX.1-2008. These functions are obsolete: do not use them in new programs. POSIX.1-2008 marks <code>sighold</code>(), <code>sigignore</code>(), <code><a href="/docs/linux/man/3-sigpause/">sigpause</a></code>(3), <code>sigrelse</code>(), and <code>sigset</code>() as obsolete, recommending the use of <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/3-pthread_sigmask/">pthread_sigmask</a></code>(3), and <code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2) instead.</p>
<h2>Notes</h2>
<p>These functions appeared in glibc version 2.1. </p>
<p> The <i>sighandler_t</i> type is a GNU extension; it is used on this page only to make the <code>sigset</code>() prototype more easily readable. </p>
<p> The <code>sigset</code>() function provides reliable signal handling semantics (as when calling <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) with <i>sa_mask</i> equal to 0). </p>
<p> On System V, the <code>signal</code>() function provides unreliable semantics (as when calling <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) with <i>sa_mask</i> equal to <i>SA_RESETHAND | SA_NODEFER</i>). On BSD, <code>signal</code>() provides reliable semantics. POSIX.1-2001 leaves these aspects of <code>signal</code>() unspecified. See <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2) for further details. </p>
<p> In order to wait for a signal, BSD and System V both provided a function named <code><a href="/docs/linux/man/3-sigpause/">sigpause</a></code>(3), but this function has a different argument on the two systems. See <code><a href="/docs/linux/man/3-sigpause/">sigpause</a></code>(3) for details.</p>
<h2>Bugs</h2>
<p>In versions of glibc before 2.2, <code>sigset</code>() did not unblock <i>sig</i> if <i>disp</i> was specified as a value other than <code>SIG_HOLD</code>. </p>
<p> In versions of glibc before 2.5, <code>sigset</code>() does not correctly return the previous disposition of the signal in two cases. First, if <i>disp</i> is specified as <code>SIG_HOLD</code>, then a successful <code>sigset</code>() always returns <code>SIG_HOLD</code>. Instead, it should return the previous disposition of the signal (unless the signal was blocked, in which case <code>SIG_HOLD</code> should be returned). Second, if the signal is currently blocked, then the return value of a successful <code>sigset</code>() should be <code>SIG_HOLD</code>. Instead, the previous disposition of the signal is returned. These problems have been fixed since glibc 2.5.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-pause/">pause</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/3-raise/">raise</a></code>(3), <code><a href="/docs/linux/man/3-sigpause/">sigpause</a></code>(3), <code><a href="/docs/linux/man/3-sigvec/">sigvec</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
