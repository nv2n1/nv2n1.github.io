---
title: "sigorset-3(3)"
name: "sigorset-3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sigorset-3/"
description: "sigemptyset, sigfillset, sigaddset, sigdelset, sigismember – POSIX signal set operations"
---

<p>sigemptyset, sigfillset, sigaddset, sigdelset, sigismember &#8211; POSIX signal set operations</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;signal.h&gt;
int sigemptyset(sigset_t *set);
int sigfillset(sigset_t *set);
int sigaddset(sigset_t *set, int signum);
int sigdelset(sigset_t *set, int signum);
int sigismember(const sigset_t *set, int signum);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>sigemptyset</code>(), <code>sigfillset</code>(), <code>sigaddset</code>(), <code>sigdelset</code>(), <code>sigismember</code>():</p>
<dl>
<dd>_POSIX_C_SOURCE</dl>
<h2>Description</h2>
<p>These functions allow the manipulation of POSIX signal sets. </p>
<p> <code>sigemptyset</code>() initializes the signal set given by <i>set</i> to empty, with all signals excluded from the set. </p>
<p> <code>sigfillset</code>() initializes <i>set</i> to full, including all signals. </p>
<p> <code>sigaddset</code>() and <code>sigdelset</code>() add and delete respectively signal <i>signum</i> from <i>set</i>. </p>
<p> <code>sigismember</code>() tests whether <i>signum</i> is a member of <i>set</i>. </p>
<p> Objects of type <i>sigset_t</i> must be initialized by a call to either <code>sigemptyset</code>() or <code>sigfillset</code>() before being passed to the functions <code>sigaddset</code>(), <code>sigdelset</code>(), and <code>sigismember</code>() or the additional glibc functions described below (<code>sigisemptyset</code>(), <code>sigandset</code>(), and <code>sigorset</code>()). The results are undefined if this is not done.</p>
<h2>Return Value</h2>
<p><code>sigemptyset</code>(), <code>sigfillset</code>(), <code>sigaddset</code>(), and <code>sigdelset</code>() return 0 on success and -1 on error. </p>
<p> <code>sigismember</code>() returns 1 if <i>signum</i> is a member of <i>set</i>, 0 if <i>signum</i> is not a member, and -1 on error. </p>
<p> On error, these functions set <i>errno</i> to indicate the cause of the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>signum</i> is not a valid signal.</dl>
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
<td> <code>sigemptyset</code>(), <code>sigfillset</code>(),<br />
 <code>sigaddset</code>(), <code>sigdelset</code>(),<br />
 <code>sigismember</code>(), <code>sigisemptyset</code>(),<br />
 <code>sigorset</code>(), <code>sigandset</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>When creating a filled signal set, the glibc <code>sigfillset</code>() function does not include the two real-time signals used internally by the NPTL threading implementation. See <code><a href="/docs/linux/man/7-nptl/">nptl</a></code>(7) for details.</p>
<h3>Glibc extensions</h3>
<p>If the <code>_GNU_SOURCE</code> feature test macro is defined, then <i>&lt;signal.h&gt;</i> exposes three other functions for manipulating signal sets: </p>
<pre><code>int sigisemptyset(const sigset_t *set);
int sigorset(sigset_t *dest, const sigset_t *left,
             const sigset_t *right);
int sigandset(sigset_t *dest, const sigset_t *left,
              const sigset_t *right);</code></pre>
<p> <code>sigisemptyset</code>() returns 1 if <i>set</i> contains no signals, and 0 otherwise. <code>sigorset</code>() places the union of the sets <i>left</i> and <i>right</i> in <i>dest</i>. <code>sigandset</code>() places the intersection of the sets <i>left</i> and <i>right</i> in <i>dest</i>. Both functions return 0 on success, and -1 on failure. These functions are nonstandard (a few other systems provide similar functions) and their use should be avoided in portable applications.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigpending/">sigpending</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
