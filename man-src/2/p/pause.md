---
title: "pause(2)"
name: "pause"
section: "2"
letter: "p"
url: "/docs/linux/man/2-pause/"
description: "pause – wait for signal"
---

<h2 class="name">NAME</h2>
<p> pause &#8211; wait for signal </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int pause(void);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>pause</code>() causes the calling process (or thread) to sleep until a signal is delivered that either terminates the process or causes the invocation of a signal-catching function.</p>
<h2>RETURN VALUE</h2>
<p> <code>pause</code>() returns only when a signal was caught and the signal-catching function returned. In this case, <code>pause</code>() returns -1, and <i>errno</i> is set to <code>EINTR</code>.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINTR</code></p>
<dd> a signal was caught and the signal-catching function returned.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-kill/">kill</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-sigsuspend/">sigsuspend</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
