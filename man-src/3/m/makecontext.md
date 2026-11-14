---
title: "makecontext(3)"
name: "makecontext"
section: "3"
letter: "m"
url: "/docs/linux/man/3-makecontext/"
description: "makecontext, swapcontext – manipulate user context"
---

<h2 class="name">NAME</h2>
<p> makecontext, swapcontext &#8211; manipulate user context </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;ucontext.h&gt;</code> </p>
<p> <code>void makecontext(ucontext_t *</code><i>ucp</i><code>, void (*</code><i>func</i><code>)(),</code> <code>int </code><i>argc</i><code>, &#8230;);</code> </p>
<p> <code>int swapcontext(ucontext_t *</code><i>oucp</i><code>, const ucontext_t *</code><i>ucp</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> In a System V-like environment, one has the type <i>ucontext_t</i> (defined in <i>&lt;ucontext.h&gt;</i> and described in <code><a href="/docs/linux/man/3-getcontext/">getcontext</a></code>(3)) and the four functions <code><a href="/docs/linux/man/3-getcontext/">getcontext</a></code>(3), <code><a href="/docs/linux/man/3-setcontext/">setcontext</a></code>(3), <code>makecontext</code>(), and <code>swapcontext</code>() that allow user-level context switching between multiple threads of control within a process. </p>
<p> The <code>makecontext</code>() function modifies the context pointed to by <i>ucp</i> (which was obtained from a call to <code><a href="/docs/linux/man/3-getcontext/">getcontext</a></code>(3)). Before invoking <code>makecontext</code>(), the caller must allocate a new stack for this context and assign its address to <i>ucp-&gt;uc_stack</i>, and define a successor context and assign its address to <i>ucp-&gt;uc_link</i>. </p>
<p> When this context is later activated (using <code><a href="/docs/linux/man/3-setcontext/">setcontext</a></code>(3) or <code>swapcontext</code>()) the function <i>func</i> is called, and passed the series of integer (<i>int</i>) arguments that follow <i>argc</i>; the caller must specify the number of these arguments in <i>argc</i>. When this function returns, the successor context is activated. If the successor context pointer is NULL, the thread exits. </p>
<p> The <code>swapcontext</code>() function saves the current context in the structure pointed to by <i>oucp</i>, and then activates the context pointed to by <i>ucp</i>.</p>
<h2>RETURN VALUE</h2>
<p> When successful, <code>swapcontext</code>() does not return. (But we may return later, in case <i>oucp</i> is activated, in which case it looks like <code>swapcontext</code>() returns 0.) On error, <code>swapcontext</code>() returns -1 and sets <i>errno</i> appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd> Insufficient stack space left.</dl>
<h2>VERSIONS</h2>
<p> <code>makecontext</code>() and <code>swapcontext</code>() are provided in glibc since version 2.1.</p>
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
<td> <code>makecontext</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:ucp
</td>
</tr>
<tr VALIGN=top>
<td> <code>swapcontext</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:oucp race:ucp
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> SUSv2, POSIX.1-2001. POSIX.1-2008 removes the specifications of <code>makecontext</code>() and <code>swapcontext</code>(), citing portability issues, and recommending that applications be rewritten to use POSIX threads instead.</p>
<h2>NOTES</h2>
<p> The interpretation of <i>ucp-&gt;uc_stack</i> is just as in <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2), namely, this struct contains the start and length of a memory area to be used as the stack, regardless of the direction of growth of the stack. Thus, it is not necessary for the user program to worry about this direction. </p>
<p> On architectures where <i>int</i> and pointer types are the same size (e.g., x86-32, where both types are 32 bits), you may be able to get away with passing pointers as arguments to <code>makecontext</code>() following <i>argc</i>. However, doing this is not guaranteed to be portable, is undefined according to the standards, and won&#8217;t work on architectures where pointers are larger than <i>int</i>s. Nevertheless, starting with version 2.8, glibc makes some changes to <code>makecontext</code>(), to permit this on some 64-bit architectures (e.g., x86-64).</p>
<h2>EXAMPLES</h2>
<p> The example program below demonstrates the use of <code><a href="/docs/linux/man/3-getcontext/">getcontext</a></code>(3), <code>makecontext</code>(), and <code>swapcontext</code>(). Running the program produces the following output: </p>
<p> $<code> ./a.out</code> main: swapcontext(&amp;uctx_main, &amp;uctx_func2) func2: started func2: swapcontext(&amp;uctx_func2, &amp;uctx_func1) func1: started func1: swapcontext(&amp;uctx_func1, &amp;uctx_func2) func2: returning func1: returning main: exiting</p>
<h3>Program source</h3>
<p> #include &lt;ucontext.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; </p>
<p> static ucontext_t uctx_main, uctx_func1, uctx_func2; </p>
<p> #define handle_error(msg) \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{&nbsp;perror(msg);&nbsp;exit(EXIT_FAILURE);&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> static void func1(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;func1: started
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;func1: swapcontext(&amp;uctx_func1,&nbsp;&amp;uctx_func2)
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(swapcontext(&amp;uctx_func1,&nbsp;&amp;uctx_func2)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;swapcontext&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;func1: returning
&quot;); } </p>
<p> static void func2(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;func2: started
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;func2: swapcontext(&amp;uctx_func2,&nbsp;&amp;uctx_func1)
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(swapcontext(&amp;uctx_func2,&nbsp;&amp;uctx_func1)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;swapcontext&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;func2: returning
&quot;); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char func1_stack[16384];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char func2_stack[16384]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(getcontext(&amp;uctx_func1)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;getcontext&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uctx_func1.uc_stack.ss_sp&nbsp;=&nbsp;func1_stack;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uctx_func1.uc_stack.ss_size&nbsp;=&nbsp;sizeof(func1_stack);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uctx_func1.uc_link&nbsp;=&nbsp;&amp;uctx_main;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;makecontext(&amp;uctx_func1, func1, 0); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(getcontext(&amp;uctx_func2)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;getcontext&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uctx_func2.uc_stack.ss_sp&nbsp;=&nbsp;func2_stack;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uctx_func2.uc_stack.ss_size&nbsp;=&nbsp;sizeof(func2_stack);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Successor context is f1(), unless argc&nbsp;&gt;&nbsp;1&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uctx_func2.uc_link&nbsp;=&nbsp;(argc&nbsp;&gt;&nbsp;1)&nbsp;?&nbsp;NULL :&nbsp;&amp;uctx_func1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;makecontext(&amp;uctx_func2, func2, 0); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;main: swapcontext(&amp;uctx_main,&nbsp;&amp;uctx_func2)
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(swapcontext(&amp;uctx_main,&nbsp;&amp;uctx_func2)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;swapcontext&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;main: exiting
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/3-getcontext/">getcontext</a></code>(3), <code><a href="/docs/linux/man/3-sigsetjmp/">sigsetjmp</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
