---
title: "getloadavg(3)"
name: "getloadavg"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getloadavg/"
description: "getloadavg – get system load averages"
---

<h2 class="name">NAME</h2>
<p> getloadavg &#8211; get system load averages </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
int getloadavg(double loadavg[], int nelem);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getloadavg</code>(): </p>
<pre>
    Since glibc 2.19:
        _DEFAULT_SOURCE
    In glibc up to and including 2.19:
        _BSD_SOURCE
</pre>
<h2>DESCRIPTION</h2>
<p> The <code>getloadavg</code>() function returns the number of processes in the system run queue averaged over various periods of time. Up to <i>nelem</i> samples are retrieved and assigned to successive elements of <i>loadavg[]</i>. The system imposes a maximum of 3 samples, representing averages over the last 1, 5, and 15 minutes, respectively.</p>
<h2>RETURN VALUE</h2>
<p> If the load average was unobtainable, -1 is returned; otherwise, the number of samples actually retrieved is returned.</p>
<h2>VERSIONS</h2>
<p> This function is available in glibc since version 2.2.</p>
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
<td> <code>getloadavg</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> Not in POSIX.1. Present on the BSDs and Solaris.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-uptime/">uptime</a></code>(1), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
