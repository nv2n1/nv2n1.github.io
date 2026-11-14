---
title: "ntp_gettime(3)"
name: "ntp_gettime"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ntp_gettime/"
description: "ntp_gettime, ntp_gettimex – get time parameters (NTP daemon interface)"
---

<p>ntp_gettime, ntp_gettimex &#8211; get time parameters (NTP daemon interface)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/timex.h&gt;

int ntp_gettime(struct ntptimeval *ntv);

int ntp_gettimex(struct ntptimeval *ntv);</code></pre>
<h2>Description</h2>
<p>Both of these APIs return information to the caller via the <i>ntv</i> argument, a structure of the following type: struct ntptimeval {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timeval time;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Current time&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long maxerror;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Maximum error&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long esterror;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Estimated error&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long tai;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;TAI offset&nbsp;*/ </p>
<pre><code>/* Further padding bytes allowing for future expansion */
}
;</code></pre>
<p> The fields of this structure are as follows:</p>
<dl>
<dt><i>time</i></p>
<dd>The current time, expressed as a <i>timeval</i> structure:</p>
<dd>struct timeval {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Seconds since the Epoch&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;suseconds_t tv_usec;&nbsp;<wbr>&nbsp;/*&nbsp;Microseconds&nbsp;*/ };</p>
<dt><i>maxerror</i></p>
<dd>Maximum error, in microseconds. This value can be initialized by <code><a href="/docs/linux/man/3-ntp_adjtime/">ntp_adjtime</a></code>(3), and is increased periodically (on Linux: each second), but is clamped to an upper limit (the kernel constant <code>NTP_PHASE_MAX</code>, with a value of 16,000).</p>
<dt><i>esterror</i></p>
<dd>Estimated error, in microseconds. This value can be set via <code><a href="/docs/linux/man/3-ntp_adjtime/">ntp_adjtime</a></code>(3) to contain an estimate of the difference between the system clock and the true time. This value is not used inside the kernel.</p>
<dt><i>tai</i></p>
<dd>TAI (Atomic International Time) offset.</dl>
<p> <code>ntp_gettime</code>() returns an <i>ntptimeval</i> structure in which the <i>time</i>, <i>maxerror</i>, and <i>esterror</i> fields are filled in. <code>ntp_gettimex</code>() performs the same task as <code>ntp_gettime</code>(), but also returns information in the <i>tai</i> field.</p>
<h2>Return Value</h2>
<p>The return values for <code>ntp_gettime</code>() and <code>ntp_gettimex</code>() are as for <code><a href="/docs/linux/man/2-adjtimex/">adjtimex</a></code>(2). Given a correct pointer argument, these functions always succeed.</p>
<h2>Versions</h2>
<p>The <code>ntp_gettime</code>() function is available since glibc 2.1. The <code>ntp_gettimex</code>() function is available since glibc 2.12.</p>
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
<td> <code>ntp_gettime</code>(), <code>ntp_gettimex</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p><code>ntp_gettime</code>() is described in the NTP Kernel Application Program Interface. <code>ntp_gettimex</code>() is a GNU extension.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-adjtimex/">adjtimex</a></code>(2), <code><a href="/docs/linux/man/3-ntp_adjtime/">ntp_adjtime</a></code>(3), <code><a href="/docs/linux/man/7-time/">time</a></code>(7) </p>
<p> NTP &quot;Kernel Application Program Interface&quot;</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
