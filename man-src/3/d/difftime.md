---
title: "difftime(3)"
name: "difftime"
section: "3"
letter: "d"
url: "/docs/linux/man/3-difftime/"
description: "difftime – calculate time difference"
---

<h2 class="name">NAME</h2>
<p> difftime &#8211; calculate time difference </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;time.h&gt;
double difftime(time_t time1, time_t time0);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>difftime</code>() function returns the number of seconds elapsed between time <i>time1</i> and time <i>time0</i>, represented as a <i>double</i>. Each of the times is specified in calendar time, which means its value is a measurement (in seconds) relative to the Epoch, 1970-01-01 00:00:00 +0000 (UTC).</p>
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
<td> <code>difftime</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, C89, C99, SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> On a POSIX system, <i>time_t</i> is an arithmetic type, and one could just define </p>
<p> #define difftime(t1,t0) (double)(t1 &#8211; t0) </p>
<p> when the possible overflow in the subtraction is not a concern.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-time/">time</a></code>(2), <code><a href="/docs/linux/man/3-ctime/">ctime</a></code>(3), <code><a href="/docs/linux/man/3-gmtime/">gmtime</a></code>(3), <code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
