---
title: "arch_prctl(2)"
name: "arch_prctl"
section: "2"
letter: "a"
url: "/docs/linux/man/2-arch_prctl/"
description: "arch_prctl – set architecture-specific thread state"
---

<h2 class="name">NAME</h2>
<p> arch_prctl &#8211; set architecture-specific thread state </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;asm/prctl.h&gt;
#include &lt;sys/prctl.h&gt;
int arch_prctl(int code, unsigned long addr);
int arch_prctl(int code, unsigned long *addr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>arch_prctl</code>() sets architecture-specific process or thread state. <i>code</i> selects a subfunction and passes argument <i>addr</i> to it; <i>addr</i> is interpreted as either an <i>unsigned long</i> for the &quot;set&quot; operations, or as an <i>unsigned long&nbsp;*</i>, for the &quot;get&quot; operations. </p>
<p> Subfunctions for both x86 and x86-64 are:</p>
<dl>
<dt><code>ARCH_SET_CPUID</code> (since Linux 4.12)</p>
<dd> Enable (<i>addr != 0</i>) or disable (<i>addr == 0</i>) the <i>cpuid</i> instruction for the calling thread. The instruction is enabled by default. If disabled, any execution of a <i>cpuid</i> instruction will instead generate a <code>SIGSEGV</code> signal. This feature can be used to emulate <i>cpuid</i> results that differ from what the underlying hardware would have produced (e.g., in a paravirtualization setting).</p>
<dt>
<dd> The <code>ARCH_SET_CPUID</code> setting is preserved across <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and <code><a href="/docs/linux/man/2-clone/">clone</a></code>(2) but reset to the default (i.e., <i>cpuid</i> enabled) on <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt><code>ARCH_GET_CPUID</code> (since Linux 4.12)</p>
<dd> Return the setting of the flag manipulated by <code>ARCH_SET_CPUID</code> as the result of the system call (1 for enabled, 0 for disabled). <i>addr</i> is ignored.</p>
<dt>Subfunctions for x86-64 only are:</p>
<dd>
<dt><code>ARCH_SET_FS</code></p>
<dd> Set the 64-bit base for the <i>FS</i> register to <i>addr</i>.</p>
<dt><code>ARCH_GET_FS</code></p>
<dd> Return the 64-bit base value for the <i>FS</i> register of the calling thread in the <i>unsigned long</i> pointed to by <i>addr</i>.</p>
<dt><code>ARCH_SET_GS</code></p>
<dd> Set the 64-bit base for the <i>GS</i> register to <i>addr</i>.</p>
<dt><code>ARCH_GET_GS</code></p>
<dd> Return the 64-bit base value for the <i>GS</i> register of the calling thread in the <i>unsigned long</i> pointed to by <i>addr</i>.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>arch_prctl</code>() returns 0; on error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>addr</i> points to an unmapped address or is outside the process address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>code</i> is not a valid subcommand.</p>
<dt><code>EPERM</code></p>
<dd> <i>addr</i> is outside the process address space.</p>
<dt><code>ENODEV</code></p>
<dd> <code>ARCH_SET_CPUID</code> was requested, but the underlying hardware does not support CPUID faulting.</dl>
<h2>CONFORMING TO</h2>
<p> <code>arch_prctl</code>() is a Linux/x86-64 extension and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> <code>arch_prctl</code>() is supported only on Linux/x86-64 for 64-bit programs currently. </p>
<p> The 64-bit base changes when a new 32-bit segment selector is loaded. </p>
<p> <code>ARCH_SET_GS</code> is disabled in some kernels. </p>
<p> Context switches for 64-bit segment bases are rather expensive. As an optimization, if a 32-bit TLS base address is used, <code>arch_prctl</code>() may use a real TLS entry as if <code><a href="/docs/linux/man/2-set_thread_area/">set_thread_area</a></code>(2) had been called, instead of manipulating the segment base register directly. Memory in the first 2 GB of address space can be allocated by using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) with the <code>MAP_32BIT</code> flag. </p>
<p> Because of the aforementioned optimization, using <code>arch_prctl</code>() and <code><a href="/docs/linux/man/2-set_thread_area/">set_thread_area</a></code>(2) in the same thread is dangerous, as they may overwrite each other&#8217;s TLS entries. </p>
<p> As of version 2.7, glibc provides no prototype for <code>arch_prctl</code>(). You have to declare it yourself for now. This may be fixed in future glibc versions. </p>
<p> <i>FS</i> may be already used by the threading library. Programs that use <code>ARCH_SET_FS</code> directly are very likely to crash.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-modify_ldt/">modify_ldt</a></code>(2), <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), <code><a href="/docs/linux/man/2-set_thread_area/">set_thread_area</a></code>(2) </p>
<p> AMD X86-64 Programmer&#8217;s manual</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
