---
title: "timercmp(3)"
name: "timercmp"
section: "3"
letter: "t"
url: "/docs/linux/man/3-timercmp/"
description: "timeradd, timersub, timercmp, timerclear, timerisset – timeval operations"
---

<p>timeradd, timersub, timercmp, timerclear, timerisset &#8211; timeval operations</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/time.h&gt;

void timeradd(struct timeval *a, struct timeval *b,
              struct timeval *res);

void timersub(struct timeval *a, struct timeval *b,
              struct timeval *res);

void timerclear(struct timeval *tvp);

int timerisset(struct timeval *tvp);

int timercmp(struct timeval *a, struct timeval *b, CMP);</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): All functions shown above:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>Description</h2>
<p>The macros are provided to operate on <i>timeval</i> structures, defined in <i>&lt;sys/time.h&gt;</i> as: </p>
<pre><code>struct timeval {
    time_t tv_sec;       /* seconds */
    suseconds_t tv_usec; /* microseconds */
};</code></pre>
<p> <code>timeradd</code>() adds the time values in <i>a</i> and <i>b</i>, and places the sum in the <i>timeval</i> pointed to by <i>res</i>. The result is normalized such that <i>res-&gt;tv_usec</i> has a value in the range 0 to 999,999. <code>timersub</code>() subtracts the time value in <i>b</i> from the time value in <i>a</i>, and places the result in the <i>timeval</i> pointed to by <i>res</i>. The result is normalized such that <i>res-&gt;tv_usec</i> has a value in the range 0 to 999,999. <code>timerclear</code>() zeros out the <i>timeval</i> structure pointed to by <i>tvp</i>, so that it represents the Epoch: 1970-01-01 00:00:00 +0000 (UTC). <code>timerisset</code>() returns true (nonzero) if either field of the <i>timeval</i> structure pointed to by <i>tvp</i> contains a nonzero value. <code>timercmp</code>() compares the timer values in <i>a</i> and <i>b</i> using the comparison operator <i>CMP</i>, and returns true (nonzero) or false (0) depending on the result of the comparison. Some systems (but not Linux/glibc), have a broken <code>timercmp</code>() implementation, in which <i>CMP</i> of <i>&gt;=</i>, <i>&lt;=</i>, and <i>==</i> do not work; portable applications can instead use<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;!timercmp(&#8230;,&nbsp;&lt;)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;!timercmp(&#8230;,&nbsp;&gt;)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;!timercmp(&#8230;,&nbsp;!=)</p>
<h2>Return Value</h2>
<p><code>timerisset</code>() and <code>timercmp</code>() return true (nonzero) or false (0).</p>
<h2>Errors</h2>
<p>No errors are defined.</p>
<h2>Conforming To</h2>
<p>Not in POSIX.1. Present on most BSD derivatives.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
