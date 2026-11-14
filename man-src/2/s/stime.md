---
title: "stime(2)"
name: "stime"
section: "2"
letter: "s"
url: "/docs/linux/man/2-stime/"
description: "stime – set time"
---

<h2 class="name">NAME</h2>
<p> stime &#8211; set time </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;time.h&gt;</code> </p>
<p> <code>int stime(const time_t *</code><i>t</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>stime</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> <code>NOTE</code>: This function is deprecated; use <code><a href="/docs/linux/man/2-clock_settime/">clock_settime</a></code>(2) instead. </p>
<p> <code>stime</code>() sets the system&#8217;s idea of the time and date. The time, pointed to by <i>t</i>, is measured in seconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC). <code>stime</code>() may be executed only by the superuser.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Error in getting information from user space.</p>
<dt><code>EPERM</code></p>
<dd> The calling process has insufficient privilege. Under Linux, the <code>CAP_SYS_TIME</code> privilege is required.</dl>
<h2>CONFORMING TO</h2>
<p> SVr4.</p>
<h2>NOTES</h2>
<p> Starting with glibc 2.31, this function is no longer available to newly linked applications and is no longer declared in <i>&lt;time.h&gt;</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-date/">date</a></code>(1), <code><a href="/docs/linux/man/2-settimeofday/">settimeofday</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
