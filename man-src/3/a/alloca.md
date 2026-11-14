---
title: "alloca(3)"
name: "alloca"
section: "3"
letter: "a"
url: "/docs/linux/man/3-alloca/"
description: "alloca – allocate memory that is automatically freed"
---

<h2 class="name">NAME</h2>
<p> alloca &#8211; allocate memory that is automatically freed </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;alloca.h&gt;</code> </p>
<p> <code>void *alloca(size_t </code><i>size</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>alloca</code>() function allocates <i>size</i> bytes of space in the stack frame of the caller. This temporary space is automatically freed when the function that called <code>alloca</code>() returns to its caller.</p>
<h2>RETURN VALUE</h2>
<p> The <code>alloca</code>() function returns a pointer to the beginning of the allocated space. If the allocation causes stack overflow, program behavior is undefined.</p>
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
<td> <code>alloca</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function is not in POSIX.1. </p>
<p> There is evidence that the <code>alloca</code>() function appeared in 32V, PWB, PWB.2, 3BSD, and 4BSD. There is a man page for it in 4.3BSD. Linux uses the GNU version.</p>
<h2>NOTES</h2>
<p> The <code>alloca</code>() function is machine- and compiler-dependent. For certain applications, its use can improve efficiency compared to the use of <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) plus <code><a href="/docs/linux/man/3-free/">free</a></code>(3). In certain cases, it can also simplify memory deallocation in applications that use <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3) or <code><a href="/docs/linux/man/3-siglongjmp/">siglongjmp</a></code>(3). Otherwise, its use is discouraged. </p>
<p> Because the space allocated by <code>alloca</code>() is allocated within the stack frame, that space is automatically freed if the function return is jumped over by a call to <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3) or <code><a href="/docs/linux/man/3-siglongjmp/">siglongjmp</a></code>(3). </p>
<p> The space allocated by <code>alloca</code>() is <i>not</i> automatically deallocated if the pointer that refers to it simply goes out of scope. </p>
<p> Do not attempt to <code><a href="/docs/linux/man/3-free/">free</a></code>(3) space allocated by <code>alloca</code>()!</p>
<h3>Notes on the GNU version</h3>
<p> Normally, <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1) translates calls to <code>alloca</code>() with inlined code. This is not done when either the <i>-ansi</i>, <i>-std=c89</i>, <i>-std=c99</i>, or the <i>-std=c11</i> option is given <code>and</code> the header <i>&lt;alloca.h&gt;</i> is not included. Otherwise, (without an -ansi or -std=c* option) the glibc version of <i>&lt;stdlib.h&gt;</i> includes <i>&lt;alloca.h&gt;</i> and that contains the lines: </p>
<p> #ifdef __GNUC__ #define alloca(size) __builtin_alloca (size) #endif </p>
<p> with messy consequences if one has a private version of this function. </p>
<p> The fact that the code is inlined means that it is impossible to take the address of this function, or to change its behavior by linking with a different library. </p>
<p> The inlined code often consists of a single instruction adjusting the stack pointer, and does not check for stack overflow. Thus, there is no NULL error return.</p>
<h2>BUGS</h2>
<p> There is no error indication if the stack frame cannot be extended. (However, after a failed allocation, the program is likely to receive a <code>SIGSEGV</code> signal if it attempts to access the unallocated space.) </p>
<p> On many systems <code>alloca</code>() cannot be used inside the list of arguments of a function call, because the stack space reserved by <code>alloca</code>() would appear on the stack in the middle of the space for the function arguments.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2), <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
