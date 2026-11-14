---
title: "subpage_prot(2)"
name: "subpage_prot"
section: "2"
letter: "s"
url: "/docs/linux/man/2-subpage_prot/"
description: "subpage_prot – define a subpage protection for an address range"
---

<h2 class="name">NAME</h2>
<p> subpage_prot &#8211; define a subpage protection for an address range </p>
<h2>SYNOPSIS</h2>
<pre><code>
int subpage_prot(unsigned long addr, unsigned long len,
                 uint32_t *map);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> The PowerPC-specific <code>subpage_prot</code>() system call provides the facility to control the access permissions on individual 4 kB subpages on systems configured with a page size of 64 kB. </p>
<p> The protection map is applied to the memory pages in the region starting at <i>addr</i> and continuing for <i>len</i> bytes. Both of these arguments must be aligned to a 64-kB boundary. </p>
<p> The protection map is specified in the buffer pointed to by <i>map</i>. The map has 2 bits per 4 kB subpage; thus each 32-bit word specifies the protections of 16 4 kB subpages inside a 64 kB page (so, the number of 32-bit words pointed to by <i>map</i> should equate to the number of 64-kB pages specified by <i>len</i>). Each 2-bit field in the protection map is either 0 to allow any access, 1 to prevent writes, or 2 or 3 to prevent all accesses.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>subpage_prot</code>() returns 0. Otherwise, one of the error codes specified below is returned.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> The buffer referred to by <i>map</i> is not accessible.</p>
<dt><code>EINVAL</code></p>
<dd> The <i>addr</i> or <i>len</i> arguments are incorrect. Both of these arguments must be aligned to a multiple of the system page size, and they must not refer to a region outside of the address space of the process or to a region that consists of huge pages.</p>
<dt><code>ENOMEM</code></p>
<dd> Out of memory.</dl>
<h2>VERSIONS</h2>
<p> This system call is provided on the PowerPC architecture since Linux 2.6.25. The system call is provided only if the kernel is configured with <code>CONFIG_PPC_64K_PAGES</code>. No library support is provided.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). </p>
<p> Normal page protections (at the 64-kB page level) also apply; the subpage protection mechanism is an additional constraint, so putting 0 in a 2-bit field won&#8217;t allow writes to a page that is otherwise write-protected.</p>
<h3>Rationale</h3>
<p> This system call is provided to assist writing emulators that operate using 64-kB pages on PowerPC systems. When emulating systems such as x86, which uses a smaller page size, the emulator can no longer use the memory-management unit (MMU) and normal system calls for controlling page protections. (The emulator could emulate the MMU by checking and possibly remapping the address for each memory access in software, but that is slow.) The idea is that the emulator supplies an array of protection masks to apply to a specified range of virtual addresses. These masks are applied at the level where hardware page-table entries (PTEs) are inserted into the hardware page table based on the Linux PTEs, so the Linux PTEs are not affected. Implicit in this is that the regions of the address space that are protected are switched to use 4-kB hardware pages rather than 64-kB hardware pages (on machines with hardware 64-kB page support).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2), <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2) </p>
<p> <i>Documentation/admin-guide/mm/hugetlbpage.rst</i> in the Linux kernel source tree</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
