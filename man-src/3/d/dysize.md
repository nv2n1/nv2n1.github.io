---
title: "dysize(3)"
name: "dysize"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dysize/"
description: "dysize – get number of days for a given year"
---

<h2 class="name">NAME</h2>
<p> dysize &#8211; get number of days for a given year </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;time.h&gt;</code> </p>
<p> <code>int dysize(int </code><i>year</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>dysize</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE ||&nbsp;_SVID_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The function returns 365 for a normal year and 366 for a leap year. The calculation for leap year is based on: </p>
<p> (year) %4 == 0 &amp;&amp; ((year) %100 != 0 || (year) %400 == 0) </p>
<p> The formula is defined in the macro <i>__isleap(year)</i> also found in <i>&lt;time.h&gt;</i>.</p>
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
<td> <code>dysize</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function occurs in SunOS 4.x.</p>
<h2>NOTES</h2>
<p> This is a compatibility function only. Don&#8217;t use it in new programs.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-strftime/">strftime</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
