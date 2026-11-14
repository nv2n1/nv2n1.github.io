---
title: "setcontext(2)"
name: "setcontext"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setcontext/"
description: "getcontext, setcontext – get or set the user context"
---

<h2 class="name">NAME</h2>
<p> getcontext, setcontext &#8211; get or set the user context </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;ucontext.h&gt;</code> </p>
<p> <code>int getcontext(ucontext_t *</code><i>ucp</i><code>);</code><br />
 <code>int setcontext(const ucontext_t *</code><i>ucp</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> In a System V-like environment, one has the two types <i>mcontext_t</i> and <i>ucontext_t</i> defined in <i>&lt;ucontext.h&gt;</i> and the four functions <code>getcontext</code>(), <code>setcontext</code>(), <code><a href="/docs/linux/man/3-makecontext/">makecontext</a></code>(3), and <code><a href="/docs/linux/man/3-swapcontext/">swapcontext</a></code>(3) that allow user-level context switching between multiple threads of control within a process. </p>
<p> The <i>mcontext_t</i> type is machine-dependent and opaque. The <i>ucontext_t</i> type is a structure that has at least the following fields: </p>
<p> typedef struct ucontext_t {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct ucontext_t&nbsp;*uc_link;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sigset_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uc_sigmask;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;stack_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uc_stack;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mcontext_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uc_mcontext;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8230; } ucontext_t; </p>
<p> with <i>sigset_t</i> and <i>stack_t</i> defined in <i>&lt;signal.h&gt;</i>. Here <i>uc_link</i> points to the context that will be resumed when the current context terminates (in case the current context was created using <code><a href="/docs/linux/man/3-makecontext/">makecontext</a></code>(3)), <i>uc_sigmask</i> is the set of signals blocked in this context (see <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2)), <i>uc_stack</i> is the stack used by this context (see <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2)), and <i>uc_mcontext</i> is the machine-specific representation of the saved context, that includes the calling thread&#8217;s machine registers. </p>
<p> The function <code>getcontext</code>() initializes the structure pointed at by <i>ucp</i> to the currently active context. </p>
<p> The function <code>setcontext</code>() restores the user context pointed at by <i>ucp</i>. A successful call does not return. The context should have been obtained by a call of <code>getcontext</code>(), or <code><a href="/docs/linux/man/3-makecontext/">makecontext</a></code>(3), or passed as third argument to a signal handler. </p>
<p> If the context was obtained by a call of <code>getcontext</code>(), program execution continues as if this call just returned. </p>
<p> If the context was obtained by a call of <code><a href="/docs/linux/man/3-makecontext/">makecontext</a></code>(3), program execution continues by a call to the function <i>func</i> specified as the second argument of that call to <code><a href="/docs/linux/man/3-makecontext/">makecontext</a></code>(3). When the function <i>func</i> returns, we continue with the <i>uc_link</i> member of the structure <i>ucp</i> specified as the first argument of that call to <code><a href="/docs/linux/man/3-makecontext/">makecontext</a></code>(3). When this member is NULL, the thread exits. </p>
<p> If the context was obtained by a call to a signal handler, then old standard text says that &quot;program execution continues with the program instruction following the instruction interrupted by the signal&quot;. However, this sentence was removed in SUSv2, and the present verdict is &quot;the result is unspecified&quot;.</p>
<h2>RETURN VALUE</h2>
<p> When successful, <code>getcontext</code>() returns 0 and <code>setcontext</code>() does not return. On error, both return -1 and set <i>errno</i> appropriately.</p>
<h2>ERRORS</h2>
<p> None defined.</p>
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
<td> <code>getcontext</code>(), <code>setcontext</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:ucp
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> SUSv2, POSIX.1-2001. POSIX.1-2008 removes the specification of <code>getcontext</code>(), citing portability issues, and recommending that applications be rewritten to use POSIX threads instead.</p>
<h2>NOTES</h2>
<p> The earliest incarnation of this mechanism was the <code><a href="/docs/linux/man/3-setjmp/">setjmp</a></code>(3)/<code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3) mechanism. Since that does not define the handling of the signal context, the next stage was the <code><a href="/docs/linux/man/3-sigsetjmp/">sigsetjmp</a></code>(3)/<code><a href="/docs/linux/man/3-siglongjmp/">siglongjmp</a></code>(3) pair. The present mechanism gives much more control. On the other hand, there is no easy way to detect whether a return from <code>getcontext</code>() is from the first call, or via a <code>setcontext</code>() call. The user has to invent their own bookkeeping device, and a register variable won&#8217;t do since registers are restored. </p>
<p> When a signal occurs, the current user context is saved and a new context is created by the kernel for the signal handler. Do not leave the handler using <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3): it is undefined what would happen with contexts. Use <code><a href="/docs/linux/man/3-siglongjmp/">siglongjmp</a></code>(3) or <code>setcontext</code>() instead.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3), <code><a href="/docs/linux/man/3-makecontext/">makecontext</a></code>(3), <code><a href="/docs/linux/man/3-sigsetjmp/">sigsetjmp</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.05 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
