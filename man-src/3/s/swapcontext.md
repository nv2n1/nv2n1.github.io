---
title: "swapcontext(3)"
name: "swapcontext"
section: "3"
letter: "s"
url: "/docs/linux/man/3-swapcontext/"
description: "makecontext, swapcontext – manipulate user context"
---

<p>makecontext, swapcontext &#8211; manipulate user context</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ucontext.h&gt;
void makecontext(ucontext_t *ucp, void (*func)(),

                 int argc, ...);
int swapcontext(ucontext_t *oucp, const ucontext_t *ucp);</code></pre>
<h2>Description</h2>
<p>In a System V-like environment, one has the type <i>ucontext_t</i> (defined in <i>&lt;ucontext.h&gt;</i> and described in <code><a href="/docs/linux/man/3-getcontext/">getcontext</a></code>(3)) and the four functions <code><a href="/docs/linux/man/3-getcontext/">getcontext</a></code>(3), <code><a href="/docs/linux/man/3-setcontext/">setcontext</a></code>(3), <code>makecontext</code>(), and <code>swapcontext</code>() that allow user-level context switching between multiple threads of control within a process. </p>
<p> The <code>makecontext</code>() function modifies the context pointed to by <i>ucp</i> (which was obtained from a call to <code><a href="/docs/linux/man/3-getcontext/">getcontext</a></code>(3)). Before invoking <code>makecontext</code>(), the caller must allocate a new stack for this context and assign its address to <i>ucp-&gt;uc_stack</i>, and define a successor context and assign its address to <i>ucp-&gt;uc_link</i>. </p>
<p> When this context is later activated (using <code><a href="/docs/linux/man/3-setcontext/">setcontext</a></code>(3) or <code>swapcontext</code>()) the function <i>func</i> is called, and passed the series of integer (<i>int</i>) arguments that follow <i>argc</i>; the caller must specify the number of these arguments in <i>argc</i>. When this function returns, the successor context is activated. If the successor context pointer is NULL, the thread exits. </p>
<p> The <code>swapcontext</code>() function saves the current context in the structure pointed to by <i>oucp</i>, and then activates the context pointed to by <i>ucp</i>.</p>
<h2>Return Value</h2>
<p>When successful, <code>swapcontext</code>() does not return. (But we may return later, in case <i>oucp</i> is activated, in which case it looks like <code>swapcontext</code>() returns 0.) On error, <code>swapcontext</code>() returns -1 and sets <i>errno</i> appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>ENOMEM</code></p>
<dd>Insufficient stack space left.</dl>
<h2>Versions</h2>
<p><code>makecontext</code>() and <code>swapcontext</code>() are provided in glibc since version 2.1.</p>
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
<h2>Conforming To</h2>
<p>SUSv2, POSIX.1-2001. POSIX.1-2008 removes the specifications of <code>makecontext</code>() and <code>swapcontext</code>(), citing portability issues, and recommending that applications be rewritten to use POSIX threads instead.</p>
<h2>Notes</h2>
<p>The interpretation of <i>ucp-&gt;uc_stack</i> is just as in <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2), namely, this struct contains the start and length of a memory area to be used as the stack, regardless of the direction of growth of the stack. Thus, it is not necessary for the user program to worry about this direction. </p>
<p> On architectures where <i>int</i> and pointer types are the same size (e.g., x86-32, where both types are 32 bits), you may be able to get away with passing pointers as arguments to <code>makecontext</code>() following <i>argc</i>. However, doing this is not guaranteed to be portable, is undefined according to the standards, and won&#8217;t work on architectures where pointers are larger than <i>int</i>s. Nevertheless, starting with version 2.8, glibc makes some changes to <code>makecontext</code>(), to permit this on some 64-bit architectures (e.g., x86-64).</p>
<h2>Examples</h2>
<p>The example program below demonstrates the use of <code><a href="/docs/linux/man/3-getcontext/">getcontext</a></code>(3), <code>makecontext</code>(), and <code>swapcontext</code>(). Running the program produces the following output: </p>
<pre><code>$ ./a.out

main: swapcontext(&amp;uctx_main, &amp;uctx_func2)
func2: started
func2: swapcontext(&amp;uctx_func2, &amp;uctx_func1)
func1: started
func1: swapcontext(&amp;uctx_func1, &amp;uctx_func2)
func2: returning
func1: returning
main: exiting



Program source



#include &lt;ucontext.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
static ucontext_t uctx_main, uctx_func1, uctx_func2;
#define handle_error(msg) \
do { perror(msg); exit(EXIT_FAILURE); } while (0)
static void
func1(void)
{
    printf(&quot;func1: started
&quot;);
    printf(&quot;func1: swapcontext(&amp;uctx_func1, &amp;uctx_func2)
&quot;);
    if (swapcontext(&amp;uctx_func1, &amp;uctx_func2) == -1)
    handle_error(&quot;swapcontext&quot;);
    printf(&quot;func1: returning
&quot;);
}
static void
func2(void)
{
    printf(&quot;func2: started
&quot;);
    printf(&quot;func2: swapcontext(&amp;uctx_func2, &amp;uctx_func1)
&quot;);
    if (swapcontext(&amp;uctx_func2, &amp;uctx_func1) == -1)
    handle_error(&quot;swapcontext&quot;);
    printf(&quot;func2: returning
&quot;);
}
int
main(int argc, char *argv[])
{
    char func1_stack[16384];
    char func2_stack[16384];
    if (getcontext(&amp;uctx_func1) == -1)
    handle_error(&quot;getcontext&quot;);
    uctx_func1.uc_stack.ss_sp = func1_stack;
    uctx_func1.uc_stack.ss_size = sizeof(func1_stack);
    uctx_func1.uc_link = &amp;uctx_main;
    makecontext(&amp;uctx_func1, func1, 0);
    if (getcontext(&amp;uctx_func2) == -1)
    handle_error(&quot;getcontext&quot;);
    uctx_func2.uc_stack.ss_sp = func2_stack;
    uctx_func2.uc_stack.ss_size = sizeof(func2_stack);
    /* Successor context is f1(), unless argc &gt; 1 */
    uctx_func2.uc_link = (argc &gt; 1) ? NULL : &amp;uctx_func1;
    makecontext(&amp;uctx_func2, func2, 0);
    printf(&quot;main: swapcontext(&amp;uctx_main, &amp;uctx_func2)
&quot;);
    if (swapcontext(&amp;uctx_main, &amp;uctx_func2) == -1)
    handle_error(&quot;swapcontext&quot;);
    printf(&quot;main: exiting
&quot;);
    exit(EXIT_SUCCESS);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-sigaltstack/">sigaltstack</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/3-getcontext/">getcontext</a></code>(3), <code><a href="/docs/linux/man/3-sigsetjmp/">sigsetjmp</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
