---
title: "getauxval(3)"
name: "getauxval"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getauxval/"
description: "getauxval – retrieve a value from the auxiliary vector"
---

<h2 class="name">NAME</h2>
<p> getauxval &#8211; retrieve a value from the auxiliary vector </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/auxv.h&gt;
unsigned long getauxval(unsigned long type);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>getauxval</code>() function retrieves values from the auxiliary vector, a mechanism that the kernel&#8217;s ELF binary loader uses to pass certain information to user space when a program is executed. </p>
<p> Each entry in the auxiliary vector consists of a pair of values: a type that identifies what this entry represents, and a value for that type. Given the argument <i>type</i>, <code>getauxval</code>() returns the corresponding value. </p>
<p> The value returned for each <i>type</i> is given in the following list. Not all <i>type</i> values are present on all architectures.</p>
<dl>
<dt><code>AT_BASE</code></p>
<dd> The base address of the program interpreter (usually, the dynamic linker).</p>
<dt><code>AT_BASE_PLATFORM</code></p>
<dd> A pointer to a string (PowerPC and MIPS only). On PowerPC, this identifies the real platform; may differ from <code>AT_PLATFORM</code>. On MIPS, this identifies the ISA level (since Linux 5.7).</p>
<dt><code>AT_CLKTCK</code></p>
<dd> The frequency with which <code><a href="/docs/linux/man/2-times/">times</a></code>(2) counts. This value can also be obtained via <i>sysconf(_SC_CLK_TCK)</i>.</p>
<dt><code>AT_DCACHEBSIZE</code></p>
<dd> The data cache block size.</p>
<dt><code>AT_EGID</code></p>
<dd> The effective group ID of the thread.</p>
<dt><code>AT_ENTRY</code></p>
<dd> The entry address of the executable.</p>
<dt><code>AT_EUID</code></p>
<dd> The effective user ID of the thread.</p>
<dt><code>AT_EXECFD</code></p>
<dd> File descriptor of program.</p>
<dt><code>AT_EXECFN</code></p>
<dd> A pointer to a string containing the pathname used to execute the program.</p>
<dt><code>AT_FLAGS</code></p>
<dd> Flags (unused).</p>
<dt><code>AT_FPUCW</code></p>
<dd> Used FPU control word (SuperH architecture only). This gives some information about the FPU initialization performed by the kernel.</p>
<dt><code>AT_GID</code></p>
<dd> The real group ID of the thread.</p>
<dt><code>AT_HWCAP</code></p>
<dd> An architecture and ABI dependent bit-mask whose settings indicate detailed processor capabilities. The contents of the bit mask are hardware dependent (for example, see the kernel source file <i>arch/x86/include/asm/cpufeature.h</i> for details relating to the Intel x86 architecture; the value returned is the first 32-bit word of the array described there). A human-readable version of the same information is available via <i>/proc/cpuinfo</i>.</p>
<dt><code>AT_HWCAP2</code> (since glibc 2.18)</p>
<dd> Further machine-dependent hints about processor capabilities.</p>
<dt><code>AT_ICACHEBSIZE</code></p>
<dd> The instruction cache block size.</p>
<dt>
<dd> <code>AT_L1D_CACHEGEOMETRY</code> Geometry of the L1 data cache, encoded with the cache line size in bytes in the bottom 16 bits and the cache associativity in the next 16 bits. The associativity is such that if N is the 16-bit value, the cache is N-way set associative.</p>
<dt><code>AT_L1D_CACHESIZE</code></p>
<dd> The L1 data cache size.</p>
<dt><code>AT_L1I_CACHEGEOMETRY</code></p>
<dd> Geometry of the L1 instruction cache, encoded as for <code>AT_L1D_CACHEGEOMETRY</code>.</p>
<dt><code>AT_L1I_CACHESIZE</code></p>
<dd> The L1 instruction cache size.</p>
<dt><code>AT_L2_CACHEGEOMETRY</code></p>
<dd> Geometry of the L2 cache, encoded as for <code>AT_L1D_CACHEGEOMETRY</code>.</p>
<dt><code>AT_L2_CACHESIZE</code></p>
<dd> The L2 cache size.</p>
<dt><code>AT_L3_CACHEGEOMETRY</code></p>
<dd> Geometry of the L3 cache, encoded as for <code>AT_L1D_CACHEGEOMETRY</code>.</p>
<dt><code>AT_L3_CACHESIZE</code></p>
<dd> The L3 cache size.</p>
<dt><code>AT_PAGESZ</code></p>
<dd> The system page size (the same value returned by <i>sysconf(_SC_PAGESIZE)</i>).</p>
<dt><code>AT_PHDR</code></p>
<dd> The address of the program headers of the executable.</p>
<dt><code>AT_PHENT</code></p>
<dd> The size of program header entry.</p>
<dt><code>AT_PHNUM</code></p>
<dd> The number of program headers.</p>
<dt><code>AT_PLATFORM</code></p>
<dd> A pointer to a string that identifies the hardware platform that the program is running on. The dynamic linker uses this in the interpretation of <i>rpath</i> values.</p>
<dt><code>AT_RANDOM</code></p>
<dd> The address of sixteen bytes containing a random value.</p>
<dt><code>AT_SECURE</code></p>
<dd> Has a nonzero value if this executable should be treated securely. Most commonly, a nonzero value indicates that the process is executing a set-user-ID or set-group-ID binary (so that its real and effective UIDs or GIDs differ from one another), or that it gained capabilities by executing a binary file that has capabilities (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)). Alternatively, a nonzero value may be triggered by a Linux Security Module. When this value is nonzero, the dynamic linker disables the use of certain environment variables (see <code><a href="/docs/linux/man/8-ld-linux-so/">ld-linux.so</a></code>(8)) and glibc changes other aspects of its behavior. (See also <code><a href="/docs/linux/man/3-secure_getenv/">secure_getenv</a></code>(3).)</p>
<dt><code>AT_SYSINFO</code></p>
<dd> The entry point to the system call function in the vDSO. Not present/needed on all architectures (e.g., absent on x86-64).</p>
<dt><code>AT_SYSINFO_EHDR</code></p>
<dd> The address of a page containing the virtual Dynamic Shared Object (vDSO) that the kernel creates in order to provide fast implementations of certain system calls.</p>
<dt><code>AT_UCACHEBSIZE</code></p>
<dd> The unified cache block size.</p>
<dt><code>AT_UID</code></p>
<dd> The real user ID of the thread.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>getauxval</code>() returns the value corresponding to <i>type</i>. If <i>type</i> is not found, 0 is returned.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOENT</code> (since glibc 2.19)</p>
<dd> No entry corresponding to <i>type</i> could be found in the auxiliary vector.</dl>
<h2>VERSIONS</h2>
<p> The <code>getauxval</code>() function was added to glibc in version 2.16.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>getauxval</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> This function is a nonstandard glibc extension.</p>
<h2>NOTES</h2>
<p> The primary consumer of the information in the auxiliary vector is the dynamic linker, <code><a href="/docs/linux/man/8-ld-linux-so/">ld-linux.so</a></code>(8). The auxiliary vector is a convenient and efficient shortcut that allows the kernel to communicate a certain set of standard information that the dynamic linker usually or always needs. In some cases, the same information could be obtained by system calls, but using the auxiliary vector is cheaper. </p>
<p> The auxiliary vector resides just above the argument list and environment in the process address space. The auxiliary vector supplied to a program can be viewed by setting the <code>LD_SHOW_AUXV</code> environment variable when running a program: </p>
<p> $ LD_SHOW_AUXV=1 sleep 1 </p>
<p> The auxiliary vector of any process can (subject to file permissions) be obtained via <i>/proc/[pid]/auxv</i>; see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for more information.</p>
<h2>BUGS</h2>
<p> Before the addition of the <code>ENOENT</code> error in glibc 2.19, there was no way to unambiguously distinguish the case where <i>type</i> could not be found from the case where the value corresponding to <i>type</i> was zero.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-secure_getenv/">secure_getenv</a></code>(3), <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7), <code><a href="/docs/linux/man/8-ld-linux-so/">ld-linux.so</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
