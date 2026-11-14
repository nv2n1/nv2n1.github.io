---
title: "siggetmask(3)"
name: "siggetmask"
section: "3"
letter: "s"
url: "/docs/linux/man/3-siggetmask/"
description: "sigvec, sigblock, sigsetmask, siggetmask, sigmask – BSD signal API"
---

<p>sigvec, sigblock, sigsetmask, siggetmask, sigmask &#8211; BSD signal API</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;signal.h&gt;
int sigvec(int sig, const struct sigvec *vec, struct sigvec *ovec);
int sigmask(int signum);
int sigblock(int mask);
int sigsetmask(int mask);
int siggetmask(void);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): All functions shown above:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>Description</h2>
<p>These functions are provided in glibc as a compatibility interface for programs that make use of the historical BSD signal API. This API is obsolete: new applications should use the POSIX signal API (<code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), etc.). The <code>sigvec</code>() function sets and/or gets the disposition of the signal <i>sig</i> (like the POSIX <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)). If <i>vec</i> is not NULL, it points to a <i>sigvec</i> structure that defines the new disposition for <i>sig</i>. If <i>ovec</i> is not NULL, it points to a <i>sigvec</i> structure that is used to return the previous disposition of <i>sig</i>. To obtain the current disposition of <i>sig</i> without changing it, specify NULL for <i>vec</i>, and a non-null pointer for <i>ovec</i>. The dispositions for <code>SIGKILL</code> and <code>SIGSTOP</code> cannot be changed. The <i>sigvec</i> structure has the following form: </p>
<pre><code>struct sigvec {
    void (*sv_handler)(int); /* Signal disposition */
    int sv_mask;             /* Signals to be blocked in handler */
    int sv_flags;            /* Flags */
};</code></pre>
<p> The <i>sv_handler</i> field specifies the disposition of the signal, and is either: the address of a signal handler function; <code>SIG_DFL</code>, meaning the default disposition applies for the signal; or <code>SIG_IGN</code>, meaning that the signal is ignored. If <i>sv_handler</i> specifies the address of a signal handler, then <i>sv_mask</i> specifies a mask of signals that are to be blocked while the handler is executing. In addition, the signal for which the handler is invoked is also blocked. Attempts to block <code>SIGKILL</code> or <code>SIGSTOP</code> are silently ignored. If <i>sv_handler</i> specifies the address of a signal handler, then the <i>sv_flags</i> field specifies flags controlling what happens when the handler is called. This field may contain zero or more of the following flags:</p>
<dl>
<dt><code>SV_INTERRUPT</code></p>
<dd>If the signal handler interrupts a blocking system call, then upon return from the handler the system call s not be restarted: instead it fails with the error <code>EINTR</code>. If this flag is not specified, then system calls are restarted by default.</p>
<dt><code>SV_RESETHAND</code></p>
<dd>Reset the disposition of the signal to the default before calling the signal handler. If this flag is not specified, then the handler remains established until explicitly removed by a later call to <code>sigvec</code>() or until the process performs an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt><code>SV_ONSTACK</code></p>
<dd>Handle the signal on the alternate signal stack (historically established under BSD using the obsolete <code>sigstack</code>() function; the POSIX replacement is <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2)).</dl>
<p> The <code>sigmask</code>() macro constructs and returns a &quot;signal mask&quot; for <i>signum</i>. For example, we can initialize the <i>vec.sv_mask</i> field given to <code>sigvec</code>() using code such as the following: vec.sv_mask = sigmask(SIGQUIT) | sigmask(SIGABRT);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Block SIGQUIT and SIGABRT during<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handler execution&nbsp;*/ The <code>sigblock</code>() function adds the signals in <i>mask</i> to the process&#8217;s signal mask (like POSIX <i>sigprocmask(SIG_BLOCK)</i>), and returns the process&#8217;s previous signal mask. Attempts to block <code>SIGKILL</code> or <code>SIGSTOP</code> are silently ignored. The <code>sigsetmask</code>() function sets the process&#8217;s signal mask to the value given in <i>mask</i> (like POSIX <i>sigprocmask(SIG_SETMASK)</i>), and returns the process&#8217;s previous signal mask. The <code>siggetmask</code>() function returns the process&#8217;s current signal mask. This call is equivalent to <i>sigblock(0)</i>.</p>
<h2>Return Value</h2>
<p>The <code>sigvec</code>() function returns 0 on success; on error, it returns -1 and sets <i>errno</i> to indicate the error. </p>
<p> The <code>sigblock</code>() and <code>sigsetmask</code>() functions return the previous signal mask. </p>
<p> The <code>sigmask</code>() macro returns the signal mask for <i>signum</i>.</p>
<h2>Errors</h2>
<p>See the ERRORS under <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2) and <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2).</p>
<h2>Versions</h2>
<p>Starting with version 2.21, the GNU C library no longer exports the <code>sigvec</code>() function as part of the ABI. (To ensure backward compatibility, the glibc symbol versioning scheme continues to export the interface to binaries linked against older versions of the library.)</p>
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
<td> <code>sigvec</code>(), <code>sigmask</code>(), <code>sigblock</code>(), <code>sigsetmask</code>(), <code>siggetmask</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>All of these functions were in 4.3BSD, except <code>siggetmask</code>(), whose origin is unclear. These functions are obsolete: do not use them in new programs.</p>
<h2>Notes</h2>
<p>On 4.3BSD, the <code>signal</code>() function provided reliable semantics (as when calling <code>sigvec</code>() with <i>vec.sv_mask</i> equal to 0). On System V, <code>signal</code>() provides unreliable semantics. POSIX.1 leaves these aspects of <code>signal</code>() unspecified. See <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2) for further details. </p>
<p> In order to wait for a signal, BSD and System V both provided a function named <code><a href="/docs/linux/man/3-sigpause/">sigpause</a></code>(3), but this function has a different argument on the two systems. See <code><a href="/docs/linux/man/3-sigpause/">sigpause</a></code>(3) for details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-pause/">pause</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/3-raise/">raise</a></code>(3), <code><a href="/docs/linux/man/3-sigpause/">sigpause</a></code>(3), <code><a href="/docs/linux/man/3-sigset/">sigset</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
