---
title: "adjtime(3)"
name: "adjtime"
section: "3"
letter: "a"
url: "/docs/linux/man/3-adjtime/"
description: "adjtime – correct the time to synchronize the system clock"
---

<h2 class="name">NAME</h2>
<p> adjtime &#8211; correct the time to synchronize the system clock </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/time.h&gt;
int adjtime(const struct timeval *delta, struct timeval *olddelta);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>adjtime</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>adjtime</code>() function gradually adjusts the system clock (as returned by <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2)). The amount of time by which the clock is to be adjusted is specified in the structure pointed to by <i>delta</i>. This structure has the following form: </p>
<p> struct timeval {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;suseconds_t tv_usec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;microseconds&nbsp;*/ }; </p>
<p> If the adjustment in <i>delta</i> is positive, then the system clock is speeded up by some small percentage (i.e., by adding a small amount of time to the clock value in each second) until the adjustment has been completed. If the adjustment in <i>delta</i> is negative, then the clock is slowed down in a similar fashion. </p>
<p> If a clock adjustment from an earlier <code>adjtime</code>() call is already in progress at the time of a later <code>adjtime</code>() call, and <i>delta</i> is not NULL for the later call, then the earlier adjustment is stopped, but any already completed part of that adjustment is not undone. </p>
<p> If <i>olddelta</i> is not NULL, then the buffer that it points to is used to return the amount of time remaining from any previous adjustment that has not yet been completed.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>adjtime</code>() returns 0. On failure, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> The adjustment in <i>delta</i> is outside the permitted range.</p>
<dt><code>EPERM</code></p>
<dd> The caller does not have sufficient privilege to adjust the time. Under Linux, the <code>CAP_SYS_TIME</code> capability is required.</dl>
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
<td> <code>adjtime</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> 4.3BSD, System V.</p>
<h2>NOTES</h2>
<p> The adjustment that <code>adjtime</code>() makes to the clock is carried out in such a manner that the clock is always monotonically increasing. Using <code>adjtime</code>() to adjust the time prevents the problems that can be caused for certain applications (e.g., <code><a href="/docs/linux/man/1-make/">make</a></code>(1)) by abrupt positive or negative jumps in the system time. </p>
<p> <code>adjtime</code>() is intended to be used to make small adjustments to the system time. Most systems impose a limit on the adjustment that can be specified in <i>delta</i>. In the glibc implementation, <i>delta</i> must be less than or equal to (INT_MAX / 1000000 &#8211; 2) and greater than or equal to (INT_MIN / 1000000 + 2) (respectively 2145 and -2145 seconds on i386).</p>
<h2>BUGS</h2>
<p> A longstanding bug meant that if <i>delta</i> was specified as NULL, no valid information about the outstanding clock adjustment was returned in <i>olddelta</i>. (In this circumstance, <code>adjtime</code>() should return the outstanding clock adjustment, without changing it.) This bug is fixed on systems with glibc 2.8 or later and Linux kernel 2.6.26 or later.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-adjtimex/">adjtimex</a></code>(2), <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
