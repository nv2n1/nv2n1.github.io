---
title: "sleep(3)"
name: "sleep"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sleep/"
description: "sleep – sleep for a specified number of seconds"
---

<p>sleep &#8211; sleep for a specified number of seconds</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;unistd.h&gt;

unsigned int sleep(unsigned int seconds);</code></pre>
<h2>Description</h2>
<p><code>sleep</code>() causes the calling thread to sleep either until the number of real-time seconds specified in <i>seconds</i> have elapsed or until a signal arrives which is not ignored.</p>
<h2>Return Value</h2>
<p>Zero if the requested time has elapsed, or the number of seconds left to sleep, if the call was interrupted by a signal handler.</p>
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
<td> <code>sleep</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe sig:SIGCHLD/linux
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>On Linux, <code>sleep</code>() is implemented via <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2). See the <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2) man page for a discussion of the clock used.</p>
<h3>Portability notes</h3>
<p>On some systems, <code>sleep</code>() may be implemented using <code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2) and <code>SIGALRM</code> (POSIX.1 permits this); mixing calls to <code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2) and <code>sleep</code>() is a bad idea. </p>
<p> Using <code><a href="/docs/linux/man/3-longjmp/">longjmp</a></code>(3) from a signal handler or modifying the handling of <code>SIGALRM</code> while sleeping will cause undefined results.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sleep/">sleep</a></code>(1), <code><a href="/docs/linux/man/2-alarm/">alarm</a></code>(2), <code><a href="/docs/linux/man/2-nanosleep/">nanosleep</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
