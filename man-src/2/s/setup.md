---
title: "setup(2)"
name: "setup"
section: "2"
letter: "s"
url: "/docs/linux/man/2-setup/"
description: "setup – setup devices and filesystems, mount root filesystem"
---

<h2 class="name">NAME</h2>
<p> setup &#8211; setup devices and filesystems, mount root filesystem </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int setup(void);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>setup</code>() is called once from within <i>linux/init/main.c</i>. It calls initialization functions for devices and filesystems configured into the kernel and then mounts the root filesystem. </p>
<p> No user process may call <code>setup</code>(). Any user process, even a process with superuser permission, will receive <code>EPERM</code>.</p>
<h2>RETURN VALUE</h2>
<p> <code>setup</code>() always returns -1 for a user process.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EPERM</code></p>
<dd> Always, for a user process.</dl>
<h2>VERSIONS</h2>
<p> Since Linux 2.1.121, no such function exists anymore.</p>
<h2>CONFORMING TO</h2>
<p> This function is Linux-specific, and should not be used in programs intended to be portable, or indeed in any programs at all.</p>
<h2>NOTES</h2>
<p> The calling sequence varied: at some times <code>setup</code>() has had a single argument <i>void&nbsp;*BIOS</i> and at other times a single argument <i>int magic</i>.</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
