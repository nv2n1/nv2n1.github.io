---
title: "fcloseall(3)"
name: "fcloseall"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fcloseall/"
description: "fcloseall – close all open streams"
---

<h2 class="name">NAME</h2>
<p> fcloseall &#8211; close all open streams </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;stdio.h&gt;
int fcloseall(void);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>fcloseall</code>() function closes all of the calling process&#8217;s open streams. Buffered output for each stream is written before it is closed (as for <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3)); buffered input is discarded. </p>
<p> The standard streams, <i>stdin</i>, <i>stdout</i>, and <i>stderr</i> are also closed.</p>
<h2>RETURN VALUE</h2>
<p> This function returns 0 if all files were successfully closed; on error, <code>EOF</code> is returned.</p>
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
<td> <code>fcloseall</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe race:streams
</td>
</tr>
</table>
<p> The <code>fcloseall</code>() function does not lock the streams, so it is not thread-safe.</p>
<h2>CONFORMING TO</h2>
<p> This function is a GNU extension.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3), <code><a href="/docs/linux/man/3-fflush/">fflush</a></code>(3), <code><a href="/docs/linux/man/3-fopen/">fopen</a></code>(3), <code><a href="/docs/linux/man/3-setbuf/">setbuf</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
