---
title: "personality(2)"
name: "personality"
section: "2"
letter: "p"
url: "/docs/linux/man/2-personality/"
description: "personality – set the process execution domain"
---

<h2 class="name">NAME</h2>
<p> personality &#8211; set the process execution domain </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/personality.h&gt;</code> </p>
<p> <code>int personality(unsigned long </code><i>persona</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> Linux supports different execution domains, or personalities, for each process. Among other things, execution domains tell Linux how to map signal numbers into signal actions. The execution domain system allows Linux to provide limited support for binaries compiled under other UNIX-like operating systems. </p>
<p> If <i>persona</i> is not 0xffffffff, then <code>personality</code>() sets the caller&#8217;s execution domain to the value specified by <i>persona</i>. Specifying <i>persona</i> as 0xffffffff provides a way of retrieving the current persona without changing it. </p>
<p> A list of the available execution domains can be found in <i>&lt;sys/personality.h&gt;</i>. The execution domain is a 32-bit value in which the top three bytes are set aside for flags that cause the kernel to modify the behavior of certain system calls so as to emulate historical or architectural quirks. The least significant byte is a value defining the personality the kernel should assume. The flag values are as follows:</p>
<dl>
<dt><code>ADDR_COMPAT_LAYOUT</code> (since Linux 2.6.9)</dt>
<dd> With this flag set, provide legacy virtual address space layout.</dd>
<dt><code>ADDR_NO_RANDOMIZE</code> (since Linux 2.6.12)</dt>
<dd> With this flag set, disable address-space-layout randomization.</dd>
<dt><code>ADDR_LIMIT_32BIT</code> (since Linux 2.2)</dt>
<dd> Limit the address space to 32 bits.</dd>
<dt><code>ADDR_LIMIT_3GB</code> (since Linux 2.4.0)</dt>
<dd> With this flag set, use 0xc0000000 as the offset at which to search a virtual memory chunk on <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2); otherwise use 0xffffe000.</dd>
<dt><code>FDPIC_FUNCPTRS</code> (since Linux 2.6.11)</dt>
<dd> User-space function pointers to signal handlers point (on certain architectures) to descriptors.</dd>
<dt><code>MMAP_PAGE_ZERO</code> (since Linux 2.4.0)</dt>
<dd> Map page 0 as read-only (to support binaries that depend on this SVr4 behavior).</dd>
<dt><code>READ_IMPLIES_EXEC</code> (since Linux 2.6.8)</dt>
<dd> With this flag set, <code>PROT_READ</code> implies <code>PROT_EXEC</code> for <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2).</dd>
<dt><code>SHORT_INODE</code> (since Linux 2.4.0)</dt>
<dd> No effects(?).</dd>
<dt><code>STICKY_TIMEOUTS</code> (since Linux 1.2.0)</dt>
<dd> With this flag set, <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2), and <code><a href="/docs/linux/man/2-ppoll/">ppoll</a></code>(2) do not modify the returned timeout argument when interrupted by a signal handler.</dd>
<dt><code>UNAME26</code> (since Linux 3.1)</dt>
<dd> Have <code><a href="/docs/linux/man/2-uname/">uname</a></code>(2) report a 2.6.40+ version number rather than a 3.x version number. Added as a stopgap measure to support broken applications that could not handle the kernel version-numbering switch from 2.6.x to 3.x.</dd>
<dt><code>WHOLE_SECONDS</code> (since Linux 1.2.0)</dt>
<dd> No effects(?).</dd></dl>
<p> The available execution domains are:</p>
<dl>
<dt><code>PER_BSD</code> (since Linux 1.2.0)</dt>
<dd> BSD. (No effects.)</dd>
<dt><code>PER_HPUX</code> (since Linux 2.4)</dt>
<dd> Support for 32-bit HP/UX. This support was never complete, and was dropped so that since Linux 4.0, this value has no effect.</dd>
<dt><code>PER_IRIX32</code> (since Linux 2.2)</dt>
<dd> IRIX 5 32-bit. Never fully functional; support dropped in Linux 2.6.27. Implies <code>STICKY_TIMEOUTS</code>.</dd>
<dt><code>PER_IRIX64</code> (since Linux 2.2)</dt>
<dd> IRIX 6 64-bit. Implies <code>STICKY_TIMEOUTS</code>; otherwise no effects.</dd>
<dt><code>PER_IRIXN32</code> (since Linux 2.2)</dt>
<dd> IRIX 6 new 32-bit. Implies <code>STICKY_TIMEOUTS</code>; otherwise no effects.</dd>
<dt><code>PER_ISCR4</code> (since Linux 1.2.0)</dt>
<dd> Implies <code>STICKY_TIMEOUTS</code>; otherwise no effects.</dd>
<dt><code>PER_LINUX</code> (since Linux 1.2.0)</dt>
<dd> Linux.</dd>
<dt><code>PER_LINUX32</code> (since Linux 2.2)</dt>
<dd> [To be documented.]</dd>
<dt><code>PER_LINUX32_3GB</code> (since Linux 2.4)</dt>
<dd> Implies <code>ADDR_LIMIT_3GB</code>.</dd>
<dt><code>PER_LINUX_32BIT</code> (since Linux 2.0)</dt>
<dd> Implies <code>ADDR_LIMIT_32BIT</code>.</dd>
<dt><code>PER_LINUX_FDPIC</code> (since Linux 2.6.11)</dt>
<dd> Implies <code>FDPIC_FUNCPTRS</code>.</dd>
<dt><code>PER_OSF4</code> (since Linux 2.4)</dt>
<dd> OSF/1 v4. On alpha, clear top 32 bits of iov_len in the user&#8217;s buffer for compatibility with old versions of OSF/1 where iov_len was defined as. <i>int</i>.</dd>
<dt><code>PER_OSR5</code> (since Linux 2.4)</dt>
<dd> Implies <code>STICKY_TIMEOUTS</code> and <code>WHOLE_SECONDS</code>; otherwise no effects.</dd>
<dt><code>PER_RISCOS</code> (since Linux 2.2)</dt>
<dd> [To be documented.]</dd>
<dt><code>PER_SCOSVR3</code> (since Linux 1.2.0)</dt>
<dd> Implies <code>STICKY_TIMEOUTS</code>, <code>WHOLE_SECONDS</code>, and <code>SHORT_INODE</code>; otherwise no effects.</dd>
<dt><code>PER_SOLARIS</code> (since Linux 2.4)</dt>
<dd> Implies <code>STICKY_TIMEOUTS</code>; otherwise no effects.</dd>
<dt><code>PER_SUNOS</code> (since Linux 2.4.0)</dt>
<dd> Implies <code>STICKY_TIMEOUTS</code>. Divert library and dynamic linker searches to <i>/usr/gnemul</i>. Buggy, largely unmaintained, and almost entirely unused; support was removed in Linux 2.6.26.</dd>
<dt><code>PER_SVR3</code> (since Linux 1.2.0)</dt>
<dd> Implies <code>STICKY_TIMEOUTS</code> and <code>SHORT_INODE</code>; otherwise no effects.</dd>
<dt><code>PER_SVR4</code> (since Linux 1.2.0)</dt>
<dd> Implies <code>STICKY_TIMEOUTS</code> and <code>MMAP_PAGE_ZERO</code>; otherwise no effects.</dd>
<dt><code>PER_UW7</code> (since Linux 2.4)</dt>
<dd> Implies <code>STICKY_TIMEOUTS</code> and <code>MMAP_PAGE_ZERO</code>; otherwise no effects.</dd>
<dt><code>PER_WYSEV386</code> (since Linux 1.2.0)</dt>
<dd> Implies <code>STICKY_TIMEOUTS</code> and <code>SHORT_INODE</code>; otherwise no effects.</dd>
<dt><code>PER_XENIX</code> (since Linux 1.2.0)</dt>
<dd> Implies <code>STICKY_TIMEOUTS</code> and <code>SHORT_INODE</code>; otherwise no effects.</dd></dl>
<h2>RETURN VALUE</h2>
<p> On success, the previous <i>persona</i> is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></dt>
<dd> The kernel was unable to change the personality.</dd></dl>
<h2>VERSIONS</h2>
<p> This system call first appeared in Linux 1.1.20 (and thus first in a stable kernel release with Linux 1.2.0); library support was added in glibc 2.3.</p>
<h2>CONFORMING TO</h2>
<p> <code>personality</code>() is Linux-specific and should not be used in programs intended to be portable.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-setarch/">setarch</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
