---
title: "sigaltstack(2)"
name: "sigaltstack"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sigaltstack/"
description: "sigaltstack – set and/or get signal stack context"
---

<h2 class="name">NAME</h2>
<p> sigaltstack &#8211; set and/or get signal stack context </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;signal.h&gt;</code> </p>
<p> <code>int sigaltstack(const stack_t *</code><i>ss</i><code>, stack_t *</code><i>old_ss</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>sigaltstack</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Since glibc 2.12:&nbsp;*/&nbsp;_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<h2>DESCRIPTION</h2>
<p> <code>sigaltstack</code>() allows a thread to define a new alternate signal stack and/or retrieve the state of an existing alternate signal stack. An alternate signal stack is used during the execution of a signal handler if the establishment of that handler (see <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)) requested it. </p>
<p> The normal sequence of events for using an alternate signal stack is the following:</p>
<dl>
<dt>1.</p>
<dd> Allocate an area of memory to be used for the alternate signal stack.</p>
<dt>2.</p>
<dd> Use <code>sigaltstack</code>() to inform the system of the existence and location of the alternate signal stack.</p>
<dt>3.</p>
<dd> When establishing a signal handler using <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), inform the system that the signal handler should be executed on the alternate signal stack by specifying the <code>SA_ONSTACK</code> flag.</dl>
<p> The <i>ss</i> argument is used to specify a new alternate signal stack, while the <i>old_ss</i> argument is used to retrieve information about the currently established signal stack. If we are interested in performing just one of these tasks, then the other argument can be specified as NULL. </p>
<p> The <i>stack_t</i> type used to type the arguments of this function is defined as follows: </p>
<p> typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;*ss_sp;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Base address of stack&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ss_flags;&nbsp;<wbr>&nbsp;/*&nbsp;Flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t ss_size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of bytes in stack&nbsp;*/ } stack_t; </p>
<p> To establish a new alternate signal stack, the fields of this structure are set as follows:</p>
<dl>
<dt><i>ss.ss_flags</i></p>
<dd> This field contains either 0, or the following flag:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>SS_AUTODISARM</code> (since Linux 4.7)</p>
<dd> Clear the alternate signal stack settings on entry to the signal handler. When the signal handler returns, the previous alternate signal stack settings are restored.</p>
<dt>
<dd> This flag was added in order make it safe to switch away from the signal handler with <code><a href="/docs/linux/man/3-swapcontext/">swapcontext</a></code>(3). Without this flag, a subsequently handled signal will corrupt the state of the switched-away signal handler. On kernels where this flag is not supported, <code>sigaltstack</code>() fails with the error <code>EINVAL</code> when this flag is supplied.</dl>
</dl>
<dt><i>ss.ss_sp</i></p>
<dd> This field specifies the starting address of the stack. When a signal handler is invoked on the alternate stack, the kernel automatically aligns the address given in <i>ss.ss_sp</i> to a suitable address boundary for the underlying hardware architecture.</p>
<dt><i>ss.ss_size</i></p>
<dd> This field specifies the size of the stack. The constant <code>SIGSTKSZ</code> is defined to be large enough to cover the usual size requirements for an alternate signal stack, and the constant <code>MINSIGSTKSZ</code> defines the minimum size required to execute a signal handler.</dl>
<p> To disable an existing stack, specify <i>ss.ss_flags</i> as <code>SS_DISABLE</code>. In this case, the kernel ignores any other flags in <i>ss.ss_flags</i> and the remaining fields in <i>ss</i>. </p>
<p> If <i>old_ss</i> is not NULL, then it is used to return information about the alternate signal stack which was in effect prior to the call to <code>sigaltstack</code>(). The <i>old_ss.ss_sp</i> and <i>old_ss.ss_size</i> fields return the starting address and size of that stack. The <i>old_ss.ss_flags</i> may return either of the following values:</p>
<dl>
<dt><code>SS_ONSTACK</code></p>
<dd> The thread is currently executing on the alternate signal stack. (Note that it is not possible to change the alternate signal stack if the thread is currently executing on it.)</p>
<dt><code>SS_DISABLE</code></p>
<dd> The alternate signal stack is currently disabled.</p>
<dt>
<dd> Alternatively, this value is returned if the thread is currently executing on an alternate signal stack that was established using the <code>SS_AUTODISARM</code> flag. In this case, it is safe to switch away from the signal handler with <code><a href="/docs/linux/man/3-swapcontext/">swapcontext</a></code>(3). It is also possible to set up a different alternative signal stack using a further call to <code>sigaltstack</code>().</p>
<dt><code>SS_AUTODISARM</code></p>
<dd> The alternate signal stack has been marked to be autodisarmed as described above.</dl>
<p> By specifying <i>ss</i> as NULL, and <i>old_ss</i> as a non-NULL value, one can obtain the current settings for the alternate signal stack without changing them.</p>
<h2>RETURN VALUE</h2>
<p> <code>sigaltstack</code>() returns 0 on success, or -1 on failure with <i>errno</i> set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Either <i>ss</i> or <i>old_ss</i> is not NULL and points to an area outside of the process&#8217;s address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>ss</i> is not NULL and the <i>ss_flags</i> field contains an invalid flag.</p>
<dt><code>ENOMEM</code></p>
<dd> The specified size of the new alternate signal stack <i>ss.ss_size</i> was less than <code>MINSIGSTKSZ</code>.</p>
<dt><code>EPERM</code></p>
<dd> An attempt was made to change the alternate signal stack while it was active (i.e., the thread was already executing on the current alternate signal stack).</dl>
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
<td> <code>sigaltstack</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SUSv2, SVr4. </p>
<p> The <code>SS_AUTODISARM</code> flag is a Linux extension.</p>
<h2>NOTES</h2>
<p> The most common usage of an alternate signal stack is to handle the <code>SIGSEGV</code> signal that is generated if the space available for the standard stack is exhausted: in this case, a signal handler for <code>SIGSEGV</code> cannot be invoked on the standard stack; if we wish to handle it, we must use an alternate signal stack. </p>
<p> Establishing an alternate signal stack is useful if a thread expects that it may exhaust its standard stack. This may occur, for example, because the stack grows so large that it encounters the upwardly growing heap, or it reaches a limit established by a call to <code>setrlimit(RLIMIT_STACK, &amp;rlim)</code>. If the standard stack is exhausted, the kernel sends the thread a <code>SIGSEGV</code> signal. In these circumstances the only way to catch this signal is on an alternate signal stack. </p>
<p> On most hardware architectures supported by Linux, stacks grow downward. <code>sigaltstack</code>() automatically takes account of the direction of stack growth. </p>
<p> Functions called from a signal handler executing on an alternate signal stack will also use the alternate signal stack. (This also applies to any handlers invoked for other signals while the thread is executing on the alternate signal stack.) Unlike the standard stack, the system does not automatically extend the alternate signal stack. Exceeding the allocated size of the alternate signal stack will lead to unpredictable results. </p>
<p> A successful call to <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) removes any existing alternate signal stack. A child process created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) inherits a copy of its parent&#8217;s alternate signal stack settings. The same is also true for a child process created using <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2), unless the clone flags include <code>CLONE_VM</code> and do not include <code>CLONE_VFORK</code>, in which case any alternate signal stack that was established in the parent is disabled in the child process. </p>
<p> <code>sigaltstack</code>() supersedes the older <code>sigstack</code>() call. For backward compatibility, glibc also provides <code>sigstack</code>(). All new applications should be written using <code>sigaltstack</code>().</p>
<h3>History</h3>
<p> 4.2BSD had a <code>sigstack</code>() system call. It used a slightly different struct, and had the major disadvantage that the caller had to know the direction of stack growth.</p>
<h2>BUGS</h2>
<p> In Linux 2.2 and earlier, the only flag that could be specified in <i>ss.sa_flags</i> was <code>SS_DISABLE</code>. In the lead up to the release of the Linux 2.4 kernel, a change was made to allow <code>sigaltstack</code>() to allow <i>ss.ss_flags==SS_ONSTACK</i> with the same meaning as <i>ss.ss_flags==0</i> (i.e., the inclusion of <code>SS_ONSTACK</code> in <i>ss.ss_flags</i> is a no-op). On other implementations, and according to POSIX.1, <code>SS_ONSTACK</code> appears only as a reported flag in <i>old_ss.ss_flags</i>. On Linux, there is no need ever to specify <code>SS_ONSTACK</code> in <i>ss.ss_flags</i>, and indeed doing so should be avoided on portability grounds: various other systems give an error if <code>SS_ONSTACK</code> is specified in <i>ss.ss_flags</i>.</p>
<h2>EXAMPLES</h2>
<p> The following code segment demonstrates the use of <code>sigaltstack</code>() (and <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2)) to install an alternate signal stack that is employed by a handler for the <code>SIGSEGV</code> signal: </p>
<p> stack_t ss; </p>
<p> ss.ss_sp = malloc(SIGSTKSZ); if (ss.ss_sp == NULL) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;malloc&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); } </p>
<p> ss.ss_size = SIGSTKSZ; ss.ss_flags = 0; if (sigaltstack(&amp;ss, NULL) == -1) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;sigaltstack&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); } </p>
<p> sa.sa_flags = SA_ONSTACK; sa.sa_handler = handler(); /* Address of a signal handler */ sigemptyset(&amp;sa.sa_mask); if (sigaction(SIGSEGV, &amp;sa, NULL) == -1) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;sigaction&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-setrlimit/">setrlimit</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/3-siglongjmp/">siglongjmp</a></code>(3), <code><a href="/docs/linux/man/3-sigsetjmp/">sigsetjmp</a></code>(3), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
