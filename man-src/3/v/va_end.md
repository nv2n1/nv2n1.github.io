---
title: "va_end(3)"
name: "va_end"
section: "3"
letter: "v"
url: "/docs/linux/man/3-va_end/"
description: "stdarg, va_start, va_arg, va_end, va_copy – variable argument lists"
---

<p>stdarg, va_start, va_arg, va_end, va_copy &#8211; variable argument lists</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdarg.h&gt;
void va_start(va_list ap, last);

type va_arg(va_list ap, type);

void va_end(va_list ap);

void va_copy(va_list dest, va_list src);</code></pre>
<h2>Description</h2>
<p>A function may be called with a varying number of arguments of varying types. The include file <i>&lt;stdarg.h&gt;</i> declares a type <i>va_list</i> and defines three macros for stepping through a list of arguments whose number and types are not known to the called function. The called function must declare an object of type <i>va_list</i> which is used by the macros <code>va_start</code>(), <code>va_arg</code>(), and <code>va_end</code>().</p>
<h3>va_start()</h3>
<p>The <code>va_start</code>() macro initializes <i>ap</i> for subsequent use by <code>va_arg</code>() and <code>va_end</code>(), and must be called first. The argument <i>last</i> is the name of the last argument before the variable argument list, that is, the last argument of which the calling function knows the type. Because the address of this argument may be used in the <code>va_start</code>() macro, it should not be declared as a register variable, or as a function or an array type.</p>
<h3>va_arg()</h3>
<p>The <code>va_arg</code>() macro expands to an expression that has the type and value of the next argument in the call. The argument <i>ap</i> is the <i>va_list</i> <i>ap</i> initialized by <code>va_start</code>(). Each call to <code>va_arg</code>() modifies <i>ap</i> so that the next call returns the next argument. The argument <i>type</i> is a type name specified so that the type of a pointer to an object that has the specified type can be obtained simply by adding a * to <i>type</i>. The first use of the <code>va_arg</code>() macro after that of the <code>va_start</code>() macro returns the argument after <i>last</i>. Successive invocations return the values of the remaining arguments. If there is no next argument, or if <i>type</i> is not compatible with the type of the actual next argument (as promoted according to the default argument promotions), random errors will occur. If <i>ap</i> is passed to a function that uses <code>va_arg(</code><i>ap</i><code>,</code><i>type</i><code>),</code> then the value of <i>ap</i> is undefined after the return of that function.</p>
<h3>va_end()</h3>
<p>Each invocation of <code>va_start</code>() must be matched by a corresponding invocation of <code>va_end</code>() in the same function. After the call <code>va_end(</code><i>ap</i><code>)</code> the variable <i>ap</i> is undefined. Multiple traversals of the list, each bracketed by <code>va_start</code>() and <code>va_end</code>() are possible. <code>va_end</code>() may be a macro or a function.</p>
<h3>va_copy()</h3>
<p>The <code>va_copy</code>() macro copies the (previously initialized) variable argument list <i>src</i> to <i>dest</i>. The behavior is as if <code>va_start</code>() were applied to <i>dest</i> with the same <i>last</i> argument, followed by the same number of <code>va_arg</code>() invocations that was used to reach the current state of <i>src</i>. An obvious implementation would have a <i>va_list</i> be a pointer to the stack frame of the variadic function. In such a setup (by far the most common) there seems nothing against an assignment va_list aq;<br />
va_copy(aq, ap);<br />
&#8230;<br />
va_end(aq); Unfortunately, there are also systems that make it an array of pointers (of length 1), and there one needs va_list aq;<br />
va_copy(aq, ap);<br />
&#8230;<br />
va_end(aq); Finally, on systems where arguments are passed in registers, it may be necessary for <code>va_start</code>() to allocate memory, store the arguments there, and also an indication of which argument is next, so that <code>va_arg</code>() can step through the list. Now <code>va_end</code>() can free the allocated memory again. To accommodate this situation, C99 adds a macro <code>va_copy</code>(), so that the above assignment can be replaced by va_list aq;<br />
va_copy(aq, ap);<br />
&#8230;<br />
va_end(aq); Each invocation of <code>va_copy</code>() must be matched by a corresponding invocation of <code>va_end</code>() in the same function. Some systems that do not supply <code>va_copy</code>() have <code>__va_copy</code> instead, since that was the name used in the draft proposal.</p>
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
<td> <code>va_start</code>(), <code>va_end</code>(), <code>va_copy</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>va_arg</code>() </td>
<td>Thread safety</td>
<td>MT-Safe race:ap
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>The <code>va_start</code>(), <code>va_arg</code>(), and <code>va_end</code>() macros conform to C89. C99 defines the <code>va_copy</code>() macro.</p>
<h2>Bugs</h2>
<p>Unlike the historical <code>varargs</code> macros, the <code>stdarg</code> macros do not permit programmers to code a function with no fixed arguments. This problem generates work mainly when converting <code>varargs</code> code to <code>stdarg</code> code, but it also creates difficulties for variadic functions that wish to pass all of their arguments on to a function that takes a <i>va_list</i> argument, such as <code><a href="/docs/linux/man/3-vfprintf/">vfprintf</a></code>(3).</p>
<h2>Examples</h2>
<p>The function <i>foo</i> takes a string of format characters and prints out the argument associated with each format character based on the type. #include &lt;stdio.h&gt;<br />
#include &lt;stdarg.h&gt; void foo(char *fmt, &#8230;) /* &#8216;&#8230;&#8217; is C syntax for a variadic function */ </p>
<pre><code>{
    va_list ap;
    int d;
    char c;
    char *s;
    va_start(ap, fmt);
    while (*fmt)
        switch (*fmt++) {
        case 's': /* string */
            s = va_arg(ap, char *);
            printf(&quot;string %s
&quot;, s);
            break;
        case 'd': /* int */
            d = va_arg(ap, int);
            printf(&quot;int %d
&quot;, d);
            break;
        case 'c': /* char */
            /* need a cast here since va_arg only
               takes fully promoted types */
            c = (char)va_arg(ap, int);
            printf(&quot;char %c
&quot;, c);
            break;
        }
    va_end(ap);
}</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-vprintf/">vprintf</a></code>(3), <code><a href="/docs/linux/man/3-vscanf/">vscanf</a></code>(3), <code><a href="/docs/linux/man/3-vsyslog/">vsyslog</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
