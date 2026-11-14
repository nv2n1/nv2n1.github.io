---
title: "getumask(3)"
name: "getumask"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getumask/"
description: "getumask – get file creation mask"
---

<h2 class="name">NAME</h2>
<p> getumask &#8211; get file creation mask </p>
<h2>SYNOPSIS</h2>
<p> <code>#define _GNU_SOURCE</code> /* See <a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a>(7) */<br />
 <code>#include &lt;sys/types.h&gt;</code><br />
 <code>#include &lt;sys/stat.h&gt;</code> </p>
<p> <code>mode_t getumask(void);</code></p>
<h2>DESCRIPTION</h2>
<p> This function returns the current file creation mask. It is equivalent to </p>
<p> mode_t getumask(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mode_t mask&nbsp;=&nbsp;umask(&nbsp;0&nbsp;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;umask(mask);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return mask; } </p>
<p> except that it is documented to be thread-safe (that is, shares a lock with the <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2) library call).</p>
<h2>CONFORMING TO</h2>
<p> This is a vaporware GNU extension.</p>
<h2>NOTES</h2>
<p> This function is documented in the glibc manual, but, as at glibc version 2.24, it is not implemented on Linux. (See <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2) for a thread-safe method of discovering a process&#8217;s umask.)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
