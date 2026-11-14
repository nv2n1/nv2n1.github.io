---
title: "daemon(3)"
name: "daemon"
section: "3"
letter: "d"
url: "/docs/linux/man/3-daemon/"
description: "daemon – run in the background"
---

<h2 class="name">NAME</h2>
<p> daemon &#8211; run in the background </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int daemon(int </code><i>nochdir</i><code>, int </code><i>noclose</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>daemon</code>(): </p>
<pre><code>
Since glibc 2.21 : _DEFAULT_SOURCE
                       In glibc 2.19 and
                   2.20 : _DEFAULT_SOURCE ||
    (_XOPEN_SOURCE &amp;&amp; _XOPEN_SOURCE &amp; nbsp; &lt; &amp;nbsp; 500)
        Up to and including glibc 2.19 : _BSD_SOURCE
                                         ||
                                         (_XOPEN_SOURCE &amp;&amp; _XOPEN_SOURCE &amp; nbsp; &lt; &amp;nbsp; 500)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>daemon</code>() function is for programs wishing to detach themselves from the controlling terminal and run in the background as system daemons. </p>
<p> If <i>nochdir</i> is zero, <code>daemon</code>() changes the process&#8217;s current working directory to the root directory (&quot;/&quot;); otherwise, the current working directory is left unchanged. </p>
<p> If <i>noclose</i> is zero, <code>daemon</code>() redirects standard input, standard output and standard error to <i>/dev/null</i>; otherwise, no changes are made to these file descriptors.</p>
<h2>RETURN VALUE</h2>
<p> (This function forks, and if the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) succeeds, the parent calls <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2), so that further errors are seen by the child only.) On success <code>daemon</code>() returns zero. If an error occurs, <code>daemon</code>() returns -1 and sets <i>errno</i> to any of the errors specified for the <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2).</p>
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
<td> <code>daemon</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> Not in POSIX.1. A similar function appears on the BSDs. The <code>daemon</code>() function first appeared in 4.4BSD.</p>
<h2>NOTES</h2>
<p> The glibc implementation can also return -1 when <i>/dev/null</i> exists but is not a character device with the expected major and minor numbers. In this case, <i>errno</i> need not be set.</p>
<h2>BUGS</h2>
<p> The GNU C library implementation of this function was taken from BSD, and does not employ the double-fork technique (i.e., <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2), <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)) that is necessary to ensure that the resulting daemon process is not a session leader. Instead, the resulting daemon <i>is</i> a session leader. On systems that follow System V semantics (e.g., Linux), this means that if the daemon opens a terminal that is not already a controlling terminal for another session, then that terminal will inadvertently become the controlling terminal for the daemon.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), <code><a href="/docs/linux/man/2-setsid/">setsid</a></code>(2), <code><a href="/docs/linux/man/7-daemon/">daemon</a></code>(7), <code><a href="/docs/linux/man/8-logrotate/">logrotate</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
