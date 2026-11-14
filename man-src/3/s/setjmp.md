---
title: "setjmp(3)"
name: "setjmp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setjmp/"
description: "setjmp, sigsetjmp, longjmp, siglongjmp – performing a nonlocal goto"
---

<p>setjmp, sigsetjmp, longjmp, siglongjmp &#8211; performing a nonlocal goto</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;setjmp.h&gt;

int setjmp(jmp_buf env);
int sigsetjmp(sigjmp_buf env, int savesigs);

void longjmp(jmp_buf env, int val);
void siglongjmp(sigjmp_buf env, int val);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): <code>setjmp</code>(): see NOTES. <code>sigsetjmp</code>(): _POSIX_C_SOURCE</p>
<h2>Description</h2>
<p>The functions described on this page are used for performing &quot;nonlocal gotos&quot;: transferring execution from one function to a predetermined location in another function. The <code>setjmp</code>() function dynamically establishes the target to which control will later be transferred, and <code>longjmp</code>() performs the transfer of execution. </p>
<p> The <code>setjmp</code>() function saves various information about the calling environment (typically, the stack pointer, the instruction pointer, possibly the values of other registers and the signal mask) in the buffer <i>env</i> for later use by <code>longjmp</code>(). In this case, <code>setjmp</code>() returns 0. </p>
<p> The <code>longjmp</code>() function uses the information saved in <i>env</i> to transfer control back to the point where <code>setjmp</code>() was called and to restore (&quot;rewind&quot;) the stack to its state at the time of the <code>setjmp</code>() call. In addition, and depending on the implementation (see NOTES), the values of some other registers and the process signal mask may be restored to their state at the time of the <code>setjmp</code>() call. </p>
<p> Following a successful <code>longjmp</code>(), execution continues as if <code>setjmp</code>() had returned for a second time. This &quot;fake&quot; return can be distinguished from a true <code>setjmp</code>() call because the &quot;fake&quot; return returns the value provided in <i>val</i>. If the programmer mistakenly passes the value 0 in <i>val</i>, the &quot;fake&quot; return will instead return 1.</p>
<h3>sigsetjmp() and siglongjmp()</h3>
<p><code>sigsetjmp</code>() and <code>siglongjmp</code>() also perform nonlocal gotos, but provide predictable handling of the process signal mask. </p>
<p> If, and only if, the <i>savesigs</i> argument provided to <code>sigsetjmp</code>() is nonzero, the process&#8217;s current signal mask is saved in <i>env</i> and will be restored if a <code>siglongjmp</code>() is later performed with this <i>env</i>.</p>
<h2>Return Value</h2>
<p><code>setjmp</code>() and <code>sigsetjmp</code>() return 0 when called directly; on the &quot;fake&quot; return that occurs after <code>longjmp</code>() or <code>siglongjmp</code>(), the nonzero value specified in <i>val</i> is returned. </p>
<p> The <code>longjmp</code>() or <code>siglongjmp</code>() functions do not return.</p>
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
<td> <code>setjmp</code>(), <code>sigsetjmp</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>longjmp</code>(), <code>siglongjmp</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p><code>setjmp</code>(), <code>longjmp</code>(): POSIX.1-2001, POSIX.1-2008, C89, C99. </p>
<p> <code>sigsetjmp</code>(), <code>siglongjmp</code>(): POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>POSIX does not specify whether <code>setjmp</code>() will save the signal mask (to be later restored during <code>longjmp</code>()). In System V it will not. In 4.3BSD it will, and there is a function <code>_setjmp</code>() that will not. The behavior under Linux depends on the glibc version and the setting of feature test macros. On Linux with glibc versions before 2.19, <code>setjmp</code>() follows the System V behavior by default, but the BSD behavior is provided if the <code>_BSD_SOURCE</code> feature test macro is explicitly defined and none of <code>_POSIX_SOURCE</code>, <code>_POSIX_C_SOURCE</code>, <code>_XOPEN_SOURCE</code>, <code>_GNU_SOURCE</code>, or <code>_SVID_SOURCE</code> is defined. Since glibc 2.19, <i>&lt;setjmp.h&gt;</i> exposes only the System V version of <code>setjmp</code>(). Programs that need the BSD semantics should replace calls to <code>setjmp</code>() with calls to <code>sigsetjmp</code>() with a nonzero <i>savesigs</i> argument. </p>
<p> <code>setjmp</code>() and <code>longjmp</code>() can be useful for dealing with errors inside deeply nested function calls or to allow a signal handler to pass control to a specific point in the program, rather than returning to the point where the handler interrupted the main program. In the latter case, if you want to portably save and restore signal masks, use <code>sigsetjmp</code>() and <code>siglongjmp</code>(). See also the discussion of program readability below. </p>
<p> The compiler may optimize variables into registers, and <code>longjmp</code>() may restore the values of other registers in addition to the stack pointer and program counter. Consequently, the values of automatic variables are unspecified after a call to <code>longjmp</code>() if they meet all the following criteria:</p>
<dl>
<dt>&bull;</p>
<dd>they are local to the function that made the corresponding <code>setjmp</code>() call;</p>
<dt>&bull;</p>
<dd>their values are changed between the calls to <code>setjmp</code>() and <code>longjmp</code>(); and</p>
<dt>&bull;</p>
<dd>they are not declared as <i>volatile</i>.</dl>
<p> Analogous remarks apply for <code>siglongjmp</code>().</p>
<h3>Nonlocal gotos and program readability</h3>
<p>While it can be abused, the traditional C &quot;goto&quot; statement at least has the benefit that lexical cues (the goto statement and the target label) allow the programmer to easily perceive the flow of control. Nonlocal gotos provide no such cues: multiple <code>setjmp</code>() calls might employ the same <i>jmp_buf</i> variable so that the content of the variable may change over the lifetime of the application. Consequently, the programmer may be forced to perform detailed reading of the code to determine the dynamic target of a particular <code>longjmp</code>() call. (To make the programmer&#8217;s life easier, each <code>setjmp</code>() call should employ a unique <i>jmp_buf</i> variable.) </p>
<p> Adding further difficulty, the <code>setjmp</code>() and <code>longjmp</code>() calls may not even be in the same source code module. </p>
<p> In summary, nonlocal gotos can make programs harder to understand and maintain, and an alternative should be used if possible.</p>
<h3>Caveats</h3>
<p>If the function which called <code>setjmp</code>() returns before <code>longjmp</code>() is called, the behavior is undefined. Some kind of subtle or unsubtle chaos is sure to result. </p>
<p> If, in a multithreaded program, a <code>longjmp</code>() call employs an <i>env</i> buffer that was initialized by a call to <code>setjmp</code>() in a different thread, the behavior is undefined. </p>
<p> POSIX.1-2008 Technical Corrigendum 2 adds <code>longjmp</code>() and <code>siglongjmp</code>() to the list of async-signal-safe functions. However, the standard recommends avoiding the use of these functions from signal handlers and goes on to point out that if these functions are called from a signal handler that interrupted a call to a non-async-signal-safe function (or some equivalent, such as the steps equivalent to <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) that occur upon a return from the initial call to <i>main</i>()), the behavior is undefined if the program subsequently makes a call to a non-async-signal-safe function. The only way of avoiding undefined behavior is to ensure one of the following:</p>
<dl>
<dt>*</p>
<dd>After long jumping from the signal handler, the program does not call any non-async-signal-safe functions and does not return from the initial call to <i>main</i>().</p>
<dt>*</p>
<dd>Any signal whose handler performs a long jump must be blocked during <i>every</i> call to a non-async-signal-safe function and no non-async-signal-safe functions are called after returning from the initial call to <i>main</i>().</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-signal/">signal</a></code>(7), <code><a href="/docs/linux/man/7-signal-safety/">signal-safety</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
