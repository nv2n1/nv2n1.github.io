---
title: "clock(3)"
name: "clock"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clock/"
description: "clock – determine processor time"
---

<h2 class="name">NAME</h2>
<p> clock &#8211; determine processor time </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;time.h&gt;
clock_t clock(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>clock</code>() function returns an approximation of processor time used by the program.</p>
<h2>RETURN VALUE</h2>
<p> The value returned is the CPU time used so far as a <i>clock_t</i>; to get the number of seconds used, divide by <code>CLOCKS_PER_SEC</code>. If the processor time used is not available or its value cannot be represented, the function returns the value <i>(clock_t)&nbsp;-1</i>.</p>
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
<td> <code>clock</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99. XSI requires that <code>CLOCKS_PER_SEC</code> equals 1000000 independent of the actual resolution.</p>
<h2>NOTES</h2>
<p> The C standard allows for arbitrary values at the start of the program; subtract the value returned from a call to <code>clock</code>() at the start of the program to get maximum portability. </p>
<p> Note that the time can wrap around. On a 32-bit system where <code>CLOCKS_PER_SEC</code> equals 1000000 this function will return the same value approximately every 72 minutes. </p>
<p> On several other implementations, the value returned by <code>clock</code>() also includes the times of any children whose status has been collected via <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2) (or another wait-type call). Linux does not include the times of waited-for children in the value returned by <code>clock</code>(). The <code><a href="/docs/linux/man/2-times/">times</a></code>(2) function, which explicitly returns (separate) information about the caller and its children, may be preferable. </p>
<p> In glibc 2.17 and earlier, <code>clock</code>() was implemented on top of <code><a href="/docs/linux/man/2-times/">times</a></code>(2). For improved accuracy, since glibc 2.18, it is implemented on top of <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) (using the <code>CLOCK_PROCESS_CPUTIME_ID</code> clock).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/2-getrusage/">getrusage</a></code>(2), <code><a href="/docs/linux/man/2-times/">times</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
