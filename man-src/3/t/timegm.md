---
title: "timegm(3)"
name: "timegm"
section: "3"
letter: "t"
url: "/docs/linux/man/3-timegm/"
description: "timegm, timelocal – inverses of gmtime and localtime"
---

<p>timegm, timelocal &#8211; inverses of gmtime and localtime</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;time.h&gt;

time_t timelocal(struct tm *tm);

time_t timegm(struct tm *tm);

Feature Test Macro Requirements for glibc (see
feature_test_macros(7)):</code></pre>
<p> <code>timelocal</code>(), <code>timegm</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>Description</h2>
<p>The functions <code>timelocal</code>() and <code>timegm</code>() are the inverses of <code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3) and <code><a href="/docs/linux/man/3-gmtime/">gmtime</a></code>(3). Both functions take a broken-down time and convert it to calendar time (seconds since the Epoch, 1970-01-01 00:00:00 +0000, UTC). The difference between the two functions is that <code>timelocal</code>() takes the local timezone into account when doing the conversion, while <code>timegm</code>() takes the input value to be Coordinated Universal Time (UTC).</p>
<h2>Return Value</h2>
<p>On success, these functions return the calendar time (seconds since the Epoch), expressed as a value of type <i>time_t</i>. On error, they return the value <i>(time_t)&nbsp;-1</i> and set <i>errno</i> to indicate the cause of the error.</p>
<h2>Errors</h2>
<dl>
<dt><code>EOVERFLOW</code></p>
<dd>The result cannot be represented.</dl>
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
<td> <code>timelocal</code>(), <code>timegm</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are nonstandard GNU extensions that are also present on the BSDs. Avoid their use.</p>
<h2>Notes</h2>
<p>The <code>timelocal</code>() function is equivalent to the POSIX standard function <code><a href="/docs/linux/man/3-mktime/">mktime</a></code>(3). There is no reason to ever use it.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-gmtime/">gmtime</a></code>(3), <code><a href="/docs/linux/man/3-localtime/">localtime</a></code>(3), <code><a href="/docs/linux/man/3-mktime/">mktime</a></code>(3), <code><a href="/docs/linux/man/3-tzset/">tzset</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
