---
title: "cacheflush(2)"
name: "cacheflush"
section: "2"
letter: "c"
url: "/docs/linux/man/2-cacheflush/"
description: "cacheflush – flush contents of instruction and/or data cache"
---

<h2 class="name">NAME</h2>
<p> cacheflush &#8211; flush contents of instruction and/or data cache </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;asm/cachectl.h&gt;
int cacheflush(char *addr, int nbytes, int cache);
</code></pre>
<p> <i>Note</i>: On some architectures, there is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <code>cacheflush</code>() flushes the contents of the indicated cache(s) for the user addresses in the range <i>addr</i> to <i>(addr+nbytes-1)</i>. <i>cache</i> may be one of:</p>
<dl>
<dt><code>ICACHE</code></p>
<dd> Flush the instruction cache.</p>
<dt><code>DCACHE</code></p>
<dd> Write back to memory and invalidate the affected valid cache lines.</p>
<dt><code>BCACHE</code></p>
<dd> Same as <code>(ICACHE|DCACHE)</code>.</dl>
<h2>RETURN VALUE</h2>
<p> <code>cacheflush</code>() returns 0 on success or -1 on error. If errors are detected, <i>errno</i> will indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Some or all of the address range <i>addr</i> to <i>(addr+nbytes-1)</i> is not accessible.</p>
<dt><code>EINVAL</code></p>
<dd> <i>cache</i> is not one of <code>ICACHE</code>, <code>DCACHE</code>, or <code>BCACHE</code> (but see BUGS).</dl>
<h2>CONFORMING TO</h2>
<p> Historically, this system call was available on all MIPS UNIX variants including RISC/os, IRIX, Ultrix, NetBSD, OpenBSD, and FreeBSD (and also on some non-UNIX MIPS operating systems), so that the existence of this call in MIPS operating systems is a de-facto standard.</p>
<h3>Caveat</h3>
<p> <code>cacheflush</code>() should not be used in programs intended to be portable. On Linux, this call first appeared on the MIPS architecture, but nowadays, Linux provides a <code>cacheflush</code>() system call on some other architectures, but with different arguments.</p>
<h2>NOTES</h2>
<h3>Architecture-specific variants</h3>
<p> Glibc provides a wrapper for this system call, with the prototype shown in SYNOPSIS, for the following architectures: ARC, CSKY, MIPS, and NIOS2. </p>
<p> On some other architectures, Linux provides this system call, with different arguments:</p>
<dl>
<dt>M68K:</p>
<dd>
int cacheflush(unsigned long addr, int scope, int cache,<br />
               unsigned long len);</p>
<dt>SH:</p>
<dd>
int cacheflush(unsigned long addr, unsigned long len, int op);</p>
<dt>NDS32:</p>
<dd>
<pre><code>
int cacheflush(unsigned int start, unsigned int end, int cache);
</code></pre>
</dl>
<p> On the above architectures, glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).</p>
<h3>GCC alternative</h3>
<p> Unless you need the finer grained control that this system call provides, you probably want to use the GCC built-in function <code>__builtin___clear_cache</code>(), which provides a portable interface across platforms supported by GCC and compatible compilers: </p>
<p> <code>void __builtin___clear_cache(void *</code><i>begin</i><code>, void *</code><i>end</i><code>);</code> </p>
<p> On platforms that don&#8217;t require instruction cache flushes, <code>__builtin___clear_cache</code>() has no effect. </p>
<p> <i>Note</i>: On some GCC-compatible compilers, the prototype for this built-in function uses <i>char *</i> instead of <i>void *</i> for the parameters.</p>
<h2>BUGS</h2>
<p> Linux kernels older than version 2.6.11 ignore the <i>addr</i> and <i>nbytes</i> arguments, making this function fairly expensive. Therefore, the whole cache is always flushed. </p>
<p> This function always behaves as if <code>BCACHE</code> has been passed for the <i>cache</i> argument and does not do any error checking on the <i>cache</i> argument.</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
