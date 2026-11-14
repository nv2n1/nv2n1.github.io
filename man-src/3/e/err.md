---
title: "err(3)"
name: "err"
section: "3"
letter: "e"
url: "/docs/linux/man/3-err/"
description: "err, verr, errx, verrx, warn, vwarn, warnx, vwarnx – formatted error messages"
---

<h2 class="name">NAME</h2>
<p> err, verr, errx, verrx, warn, vwarn, warnx, vwarnx &#8211; formatted error messages </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;err.h&gt;
void err(int eval, const char *fmt, ...);
void errx(int eval, const char *fmt, ...);
void warn(const char *fmt, ...);
void warnx(const char *fmt, ...);
#include &lt;stdarg.h&gt;
void verr(int eval, const char *fmt, va_list args);
void verrx(int eval, const char *fmt, va_list args);
void vwarn(const char *fmt, va_list args);
void vwarnx(const char *fmt, va_list args);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>err</code>() and <code>warn</code>() family of functions display a formatted error message on the standard error output. In all cases, the last component of the program name, a colon character, and a space are output. If the <i>fmt</i> argument is not NULL, the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3)-like formatted error message is output. The output is terminated by a newline character. </p>
<p> The <code>err</code>(), <code>verr</code>(), <code>warn</code>(), and <code>vwarn</code>() functions append an error message obtained from <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3) based on the global variable <i>errno</i>, preceded by another colon and space unless the <i>fmt</i> argument is NULL. </p>
<p> The <code>errx</code>() and <code>warnx</code>() functions do not append an error message. </p>
<p> The <code>err</code>(), <code>verr</code>(), <code>errx</code>(), and <code>verrx</code>() functions do not return, but exit with the value of the argument <i>eval</i>.</p>
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
<td> <code>err</code>(), <code>errx</code>(),<br />
 <code>warn</code>(), <code>warnx</code>(),<br />
 <code>verr</code>(), <code>verrx</code>(),<br />
 <code>vwarn</code>(), <code>vwarnx</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> These functions are nonstandard BSD extensions.</p>
<h2>EXAMPLES</h2>
<p> Display the current <i>errno</i> information string and exit: </p>
<p> p = malloc(size); if (p == NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;err(EXIT_FAILURE, NULL); fd = open(file_name, O_RDONLY, 0); if (fd == -1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;err(EXIT_FAILURE,&nbsp;&quot;%s&quot;, file_name); </p>
<p> Display an error message and exit: </p>
<p> if (tm.tm_hour &lt; START_TIME)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errx(EXIT_FAILURE,&nbsp;&quot;too early, wait until&nbsp;%s&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;start_time_string); </p>
<p> Warn of an error: </p>
<p> fd = open(raw_device, O_RDONLY, 0); if (fd == -1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;warnx(&quot;%s:&nbsp;%s: trying the block device&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;raw_device, strerror(errno)); fd = open(block_device, O_RDONLY, 0); if (fd == -1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;err(EXIT_FAILURE,&nbsp;&quot;%s&quot;, block_device);</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-error/">error</a></code>(3), <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3), <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
