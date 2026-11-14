---
title: "exit_group(2)"
name: "exit_group"
section: "2"
letter: "e"
url: "/docs/linux/man/2-exit_group/"
description: "exit_group – exit all threads in a process"
---

<h2 class="name">NAME</h2>
<p> exit_group &#8211; exit all threads in a process </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/unistd.h&gt;
void exit_group(int status);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This system call is equivalent to <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2) except that it terminates not only the calling thread, but all threads in the calling process&#8217;s thread group.</p>
<h2>RETURN VALUE</h2>
<p> This system call does not return.</p>
<h2>VERSIONS</h2>
<p> This call is present since Linux 2.5.35.</p>
<h2>CONFORMING TO</h2>
<p> This call is Linux-specific.</p>
<h2>NOTES</h2>
<p> Since glibc 2.3, this is the system call invoked when the <code><a href="/docs/linux/man/2-_exit/">_exit</a></code>(2) wrapper function is called.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-exit/">exit</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
