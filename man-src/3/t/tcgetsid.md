---
title: "tcgetsid(3)"
name: "tcgetsid"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tcgetsid/"
description: "tcgetsid – get session ID"
---

<p>tcgetsid &#8211; get session ID</p>
<h2>Synopsis</h2>
<pre><code>#define _XOPEN_SOURCE 500        /* See feature_test_macros(7) */


#include &lt;termios.h&gt;</code></pre>
<p> <code>pid_t tcgetsid(int </code><i>fd</i><code>);</code></p>
<h2>Description</h2>
<p>The function <code>tcgetsid</code>() returns the session ID of the current session that has the terminal associated to <i>fd</i> as controlling terminal. This terminal must be the controlling terminal of the calling process.</p>
<h2>Return Value</h2>
<p>When <i>fd</i> refers to the controlling terminal of our session, the function <code>tcgetsid</code>() will return the session ID of this session. Otherwise, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>EBADF</code></p>
<dd><i>fd</i> is not a valid file descriptor.</p>
<dt><code>ENOTTY</code></p>
<dd>The calling process does not have a controlling terminal, or it has one but it is not described by <i>fd</i>.</dl>
<h2>Versions</h2>
<p><code>tcgetsid</code>() is provided in glibc since version 2.1.</p>
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
<td> <code>tcgetsid</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>This function is implemented via the <code>TIOCGSID</code> <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2), present since Linux 2.1.71.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-getsid/">getsid</a></code>(2)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
