---
title: "getpagesize(2)"
name: "getpagesize"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getpagesize/"
description: "getpagesize – get memory page size"
---

<h2 class="name">NAME</h2>
<p> getpagesize &#8211; get memory page size </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int getpagesize(void);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>getpagesize</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.19:</p>
<dd>
<pre><code>
_DEFAULT_SOURCE || !(_POSIX_C_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 200112L)
</code></pre>
<dt>From glibc 2.12 to 2.19:</p>
<dd>
<pre><code>
_BSD_SOURCE || !(_POSIX_C_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 200112L)
</code></pre>
<dt>Before glibc 2.12:</p>
<dd> _BSD_SOURCE || _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The function <code>getpagesize</code>() returns the number of bytes in a memory page, where &quot;page&quot; is a fixed-length block, the unit for memory allocation and file mapping performed by <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2).</p>
<h2>CONFORMING TO</h2>
<p> SVr4, 4.4BSD, SUSv2. In SUSv2 the <code>getpagesize</code>() call is labeled LEGACY, and in POSIX.1-2001 it has been dropped; HP-UX does not have this call.</p>
<h2>NOTES</h2>
<p> Portable applications should employ <i>sysconf(_SC_PAGESIZE)</i> instead of <code>getpagesize</code>(): </p>
<p> #include &lt;unistd.h&gt; long sz = sysconf(_SC_PAGESIZE); </p>
<p> (Most systems allow the synonym <code>_SC_PAGE_SIZE</code> for <code>_SC_PAGESIZE</code>.) </p>
<p> Whether <code>getpagesize</code>() is present as a Linux system call depends on the architecture. If it is, it returns the kernel symbol <code>PAGE_SIZE</code>, whose value depends on the architecture and machine model. Generally, one uses binaries that are dependent on the architecture but not on the machine model, in order to have a single binary distribution per architecture. This means that a user program should not find <code>PAGE_SIZE</code> at compile time from a header file, but use an actual system call, at least for those architectures (like sun4) where this dependency exists. Here glibc 2.0 fails because its <code>getpagesize</code>() returns a statically derived value, and does not use a system call. Things are OK in glibc 2.1.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/3-sysconf/">sysconf</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
