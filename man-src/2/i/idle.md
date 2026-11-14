---
title: "idle(2)"
name: "idle"
section: "2"
letter: "i"
url: "/docs/linux/man/2-idle/"
description: "idle – make process 0 idle"
---

<h2 class="name">NAME</h2>
<p> idle &#8211; make process 0 idle </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int idle(void);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>idle</code>() is an internal system call used during bootstrap. It marks the process&#8217;s pages as swappable, lowers its priority, and enters the main scheduling loop. <code>idle</code>() never returns. </p>
<p> Only process 0 may call <code>idle</code>(). Any user process, even a process with superuser permission, will receive <code>EPERM</code>.</p>
<h2>RETURN VALUE</h2>
<p> <code>idle</code>() never returns for process 0, and always returns -1 for a user process.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EPERM</code></p>
<dd> Always, for a user process.</dl>
<h2>VERSIONS</h2>
<p> Since Linux 2.3.13, this system call does not exist anymore.</p>
<h2>CONFORMING TO</h2>
<p> This function is Linux-specific, and should not be used in programs intended to be portable.</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
