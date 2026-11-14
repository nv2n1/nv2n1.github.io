---
title: "ftime(3)"
name: "ftime"
section: "3"
letter: "f"
url: "/docs/linux/man/3-ftime/"
description: "ftime – return date and time"
---

<h2 class="name">NAME</h2>
<p> ftime &#8211; return date and time </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/timeb.h&gt;</code> </p>
<p> <code>int ftime(struct timeb *</code><i>tp</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>NOTE</code>: This function is deprecated, and will be removed in a future version of the GNU C library. Use <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) instead. </p>
<p> This function returns the current time as seconds and milliseconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC). The time is returned in <i>tp</i>, which is declared as follows: </p>
<p> struct timeb {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short millitm;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;timezone;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dstflag; }; </p>
<p> Here <i>time</i> is the number of seconds since the Epoch, and <i>millitm</i> is the number of milliseconds since <i>time</i> seconds since the Epoch. The <i>timezone</i> field is the local timezone measured in minutes of time west of Greenwich (with a negative value indicating minutes east of Greenwich). The <i>dstflag</i> field is a flag that, if nonzero, indicates that Daylight Saving time applies locally during the appropriate part of the year. </p>
<p> POSIX.1-2001 says that the contents of the <i>timezone</i> and <i>dstflag</i> fields are unspecified; avoid relying on them.</p>
<h2>RETURN VALUE</h2>
<p> This function always returns 0. (POSIX.1-2001 specifies, and some systems document, a -1 error return.)</p>
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
<td> <code>ftime</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> 4.2BSD, POSIX.1-2001. POSIX.1-2008 removes the specification of <code>ftime</code>(). </p>
<p> This function is obsolete. Don&#8217;t use it. If the time in seconds suffices, <code><a href="/docs/linux/man/2-time/">time</a></code>(2) can be used; <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2) gives microseconds; <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2) gives nanoseconds but is not as widely available.</p>
<h2>BUGS</h2>
<p> Early glibc2 is buggy and returns 0 in the <i>millitm</i> field; glibc 2.1.1 is correct again.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-time/">time</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
