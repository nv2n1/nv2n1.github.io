---
title: "warn(3)"
name: "warn"
section: "3"
letter: "w"
url: "/docs/linux/man/3-warn/"
description: "err, verr, errx, verrx, warn, vwarn, warnx, vwarnx – formatted error messages"
---

<p>err, verr, errx, verrx, warn, vwarn, warnx, vwarnx &#8211; formatted error messages</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;err.h&gt;

void err(int eval, const char *fmt, ...);

void errx(int eval, const char *fmt, ...);

void warn(const char *fmt, ...);

void warnx(const char *fmt, ...);

#include &lt;stdarg.h&gt;

void verr(int eval, const char *fmt, va_list args);

void verrx(int eval, const char *fmt, va_list args);

void vwarn(const char *fmt, va_list args);

void vwarnx(const char *fmt, va_list args);</code></pre>
<h2>Description</h2>
<p>The <code>err</code>() and <code>warn</code>() family of functions display a formatted error message on the standard error output. In all cases, the last component of the program name, a colon character, and a space are output. If the <i>fmt</i> argument is not NULL, the <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3)-like formatted error message is output. The output is terminated by a newline character. </p>
<p> The <code>err</code>(), <code>verr</code>(), <code>warn</code>(), and <code>vwarn</code>() functions append an error message obtained from <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3) based on the global variable <i>errno</i>, preceded by another colon and space unless the <i>fmt</i> argument is NULL. </p>
<p> The <code>errx</code>() and <code>warnx</code>() functions do not append an error message. </p>
<p> The <code>err</code>(), <code>verr</code>(), <code>errx</code>(), and <code>verrx</code>() functions do not return, but exit with the value of the argument <i>eval</i>.</p>
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
<td> <code>err</code>(), <code>errx</code>(),<br />
 <code>warn</code>(), <code>warnx</code>(),<br />
 <code>verr</code>(), <code>verrx</code>(),<br />
 <code>vwarn</code>(), <code>vwarnx</code>() </td>
<td>Thread safety</td>
<td>MT-Safe locale
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>These functions are nonstandard BSD extensions.</p>
<h2>Examples</h2>
<p>Display the current <i>errno</i> information string and exit: fd = open(raw_device, O_RDONLY, 0);<br />
if (fd == -1)<br />
    warnx(&quot;%s: %s: trying the block device&quot;,<br />
          raw_device, strerror(errno));<br />
fd = open(block_device, O_RDONLY, 0);<br />
if (fd == -1)<br />
    err(EXIT_FAILURE, &quot;%s&quot;, block_device); Display an error message and exit: if (tm.tm_hour &lt; START_TIME)<br />
    errx(EXIT_FAILURE, &quot;too early, wait until %s&quot;,<br />
         start_time_string); Warn of an error: </p>
<pre><code>fd = open(raw_device, O_RDONLY, 0);
if (fd == -1)
    warnx(&quot;%s: %s: trying the block device&quot;,
          raw_device, strerror(errno));
fd = open(block_device, O_RDONLY, 0);
if (fd == -1)
    err(EXIT_FAILURE, &quot;%s&quot;, block_device);</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-error/">error</a></code>(3), <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3), <code><a href="/docs/linux/man/3-perror/">perror</a></code>(3), <code><a href="/docs/linux/man/3-printf/">printf</a></code>(3), <code><a href="/docs/linux/man/3-strerror/">strerror</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
