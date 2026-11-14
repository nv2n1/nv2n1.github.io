---
title: "madvise(2)"
name: "madvise"
section: "2"
letter: "m"
url: "/docs/linux/man/2-madvise/"
description: "madvise – give advice about use of memory"
---

<h2 class="name">NAME</h2>
<p> madvise &#8211; give advice about use of memory </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/mman.h&gt;</code> </p>
<p> <code>int madvise(void *</code><i>addr</i><code>, size_t </code><i>length</i><code>, int </code><i>advice</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>madvise</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.19:</p>
<dd> _DEFAULT_SOURCE</p>
<dt>Up to and including glibc 2.19:</p>
<dd> _BSD_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The <code>madvise</code>() system call is used to give advice or directions to the kernel about the address range beginning at address <i>addr</i> and with size <i>length</i> bytes In most cases, the goal of such advice is to improve system or application performance. </p>
<p> Initially, the system call supported a set of &quot;conventional&quot; <i>advice</i> values, which are also available on several other implementations. (Note, though, that <code>madvise</code>() is not specified in POSIX.) Subsequently, a number of Linux-specific <i>advice</i> values have been added.</p>
<h3>Conventional advice values</h3>
<p> The <i>advice</i> values listed below allow an application to tell the kernel how it expects to use some mapped or shared memory areas, so that the kernel can choose appropriate read-ahead and caching techniques. These <i>advice</i> values do not influence the semantics of the application (except in the case of <code>MADV_DONTNEED</code>), but may influence its performance. All of the <i>advice</i> values listed here have analogs in the POSIX-specified <code><a href="/docs/linux/man/3-posix_madvise/">posix_madvise</a></code>(3) function, and the values have the same meanings, with the exception of <code>MADV_DONTNEED</code>. </p>
<p> The advice is indicated in the <i>advice</i> argument, which is one of the following:</p>
<dl>
<dt><code>MADV_NORMAL</code></p>
<dd> No special treatment. This is the default.</p>
<dt><code>MADV_RANDOM</code></p>
<dd> Expect page references in random order. (Hence, read ahead may be less useful than normally.)</p>
<dt><code>MADV_SEQUENTIAL</code></p>
<dd> Expect page references in sequential order. (Hence, pages in the given range can be aggressively read ahead, and may be freed soon after they are accessed.)</p>
<dt><code>MADV_WILLNEED</code></p>
<dd> Expect access in the near future. (Hence, it might be a good idea to read some pages ahead.)</p>
<dt><code>MADV_DONTNEED</code></p>
<dd> Do not expect access in the near future. (For the time being, the application is finished with the given range, so the kernel can free resources associated with it.)</p>
<dt>
<dd> After a successful <code>MADV_DONTNEED</code> operation, the semantics of memory access in the specified region are changed: subsequent accesses of pages in the range will succeed, but will result in either repopulating the memory contents from the up-to-date contents of the underlying mapped file (for shared file mappings, shared anonymous mappings, and shmem-based techniques such as System V shared memory segments) or zero-fill-on-demand pages for anonymous private mappings.</p>
<dt>
<dd> Note that, when applied to shared mappings, <code>MADV_DONTNEED</code> might not lead to immediate freeing of the pages in the range. The kernel is free to delay freeing the pages until an appropriate moment. The resident set size (RSS) of the calling process will be immediately reduced however.</p>
<dt>
<dd> <code>MADV_DONTNEED</code> cannot be applied to locked pages, Huge TLB pages, or <code>VM_PFNMAP</code> pages. (Pages marked with the kernel-internal <code>VM_PFNMAP</code> flag are special memory areas that are not managed by the virtual memory subsystem. Such pages are typically created by device drivers that map the pages into user space.)</dl>
<h3>Linux-specific advice values</h3>
<p> The following Linux-specific <i>advice</i> values have no counterparts in the POSIX-specified <code><a href="/docs/linux/man/3-posix_madvise/">posix_madvise</a></code>(3), and may or may not have counterparts in the <code>madvise</code>() interface available on other implementations. Note that some of these operations change the semantics of memory accesses.</p>
<dl>
<dt><code>MADV_REMOVE</code> (since Linux 2.6.16)</p>
<dd> Free up a given range of pages and its associated backing store. This is equivalent to punching a hole in the corresponding byte range of the backing store (see <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2)). Subsequent accesses in the specified address range will see bytes containing zero.</p>
<dt>
<dd> The specified address range must be mapped shared and writable. This flag cannot be applied to locked pages, Huge TLB pages, or <code>VM_PFNMAP</code> pages.</p>
<dt>
<dd> In the initial implementation, only <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) was supported <code>MADV_REMOVE</code>; but since Linux 3.5, any filesystem which supports the <code><a href="/docs/linux/man/2-fallocate/">fallocate</a></code>(2) <code>FALLOC_FL_PUNCH_HOLE</code> mode also supports <code>MADV_REMOVE</code>. Hugetlbfs fails with the error <code>EINVAL</code> and other filesystems fail with the error <code>EOPNOTSUPP</code>.</p>
<dt><code>MADV_DONTFORK</code> (since Linux 2.6.16)</p>
<dd> Do not make the pages in this range available to the child after a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). This is useful to prevent copy-on-write semantics from changing the physical location of a page if the parent writes to it after a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). (Such page relocations cause problems for hardware that DMAs into the page.)</p>
<dt><code>MADV_DOFORK</code> (since Linux 2.6.16)</p>
<dd> Undo the effect of <code>MADV_DONTFORK</code>, restoring the default behavior, whereby a mapping is inherited across <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2).</p>
<dt><code>MADV_HWPOISON</code> (since Linux 2.6.32)</p>
<dd> Poison the pages in the range specified by <i>addr</i> and <i>length</i> and handle subsequent references to those pages like a hardware memory corruption. This operation is available only for privileged (<code>CAP_SYS_ADMIN</code>) processes. This operation may result in the calling process receiving a <code>SIGBUS</code> and the page being unmapped.</p>
<dt>
<dd> This feature is intended for testing of memory error-handling code; it is available only if the kernel was configured with <code>CONFIG_MEMORY_FAILURE</code>.</p>
<dt><code>MADV_MERGEABLE</code> (since Linux 2.6.32)</p>
<dd> Enable Kernel Samepage Merging (KSM) for the pages in the range specified by <i>addr</i> and <i>length</i>. The kernel regularly scans those areas of user memory that have been marked as mergeable, looking for pages with identical content. These are replaced by a single write-protected page (which is automatically copied if a process later wants to update the content of the page). KSM merges only private anonymous pages (see <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)).</p>
<dt>
<dd> The KSM feature is intended for applications that generate many instances of the same data (e.g., virtualization systems such as KVM). It can consume a lot of processing power; use with care. See the Linux kernel source file <i>Documentation/admin-guide/mm/ksm.rst</i> for more details.</p>
<dt>
<dd> The <code>MADV_MERGEABLE</code> and <code>MADV_UNMERGEABLE</code> operations are available only if the kernel was configured with <code>CONFIG_KSM</code>.</p>
<dt><code>MADV_UNMERGEABLE</code> (since Linux 2.6.32)</p>
<dd> Undo the effect of an earlier <code>MADV_MERGEABLE</code> operation on the specified address range; KSM unmerges whatever pages it had merged in the address range specified by <i>addr</i> and <i>length</i>.</p>
<dt><code>MADV_SOFT_OFFLINE</code> (since Linux 2.6.33)</p>
<dd> Soft offline the pages in the range specified by <i>addr</i> and <i>length</i>. The memory of each page in the specified range is preserved (i.e., when next accessed, the same content will be visible, but in a new physical page frame), and the original page is offlined (i.e., no longer used, and taken out of normal memory management). The effect of the <code>MADV_SOFT_OFFLINE</code> operation is invisible to (i.e., does not change the semantics of) the calling process.</p>
<dt>
<dd> This feature is intended for testing of memory error-handling code; it is available only if the kernel was configured with <code>CONFIG_MEMORY_FAILURE</code>.</p>
<dt><code>MADV_HUGEPAGE</code> (since Linux 2.6.38)</p>
<dd> Enable Transparent Huge Pages (THP) for pages in the range specified by <i>addr</i> and <i>length</i>. Currently, Transparent Huge Pages work only with private anonymous pages (see <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)). The kernel will regularly scan the areas marked as huge page candidates to replace them with huge pages. The kernel will also allocate huge pages directly when the region is naturally aligned to the huge page size (see <code><a href="/docs/linux/man/2-posix_memalign/">posix_memalign</a></code>(2)).</p>
<dt>
<dd> This feature is primarily aimed at applications that use large mappings of data and access large regions of that memory at a time (e.g., virtualization systems such as QEMU). It can very easily waste memory (e.g., a 2 MB mapping that only ever accesses 1 byte will result in 2 MB of wired memory instead of one 4 KB page). See the Linux kernel source file <i>Documentation/admin-guide/mm/transhuge.rst</i> for more details.</p>
<dt>
<dd> Most common kernels configurations provide <code>MADV_HUGEPAGE</code>-style behavior by default, and thus <code>MADV_HUGEPAGE</code> is normally not necessary. It is mostly intended for embedded systems, where <code>MADV_HUGEPAGE</code>-style behavior may not be enabled by default in the kernel. On such systems, this flag can be used in order to selectively enable THP. Whenever <code>MADV_HUGEPAGE</code> is used, it should always be in regions of memory with an access pattern that the developer knows in advance won&#8217;t risk to increase the memory footprint of the application when transparent hugepages are enabled.</p>
<dt>
<dd> The <code>MADV_HUGEPAGE</code> and <code>MADV_NOHUGEPAGE</code> operations are available only if the kernel was configured with <code>CONFIG_TRANSPARENT_HUGEPAGE</code>.</p>
<dt><code>MADV_NOHUGEPAGE</code> (since Linux 2.6.38)</p>
<dd> Ensures that memory in the address range specified by <i>addr</i> and <i>length</i> will not be backed by transparent hugepages.</p>
<dt><code>MADV_DONTDUMP</code> (since Linux 3.4)</p>
<dd> Exclude from a core dump those pages in the range specified by <i>addr</i> and <i>length</i>. This is useful in applications that have large areas of memory that are known not to be useful in a core dump. The effect of <code>MADV_DONTDUMP</code> takes precedence over the bit mask that is set via the <i>/proc/[pid]/coredump_filter</i> file (see <code><a href="/docs/linux/man/5-core/">core</a></code>(5)).</p>
<dt><code>MADV_DODUMP</code> (since Linux 3.4)</p>
<dd> Undo the effect of an earlier <code>MADV_DONTDUMP</code>.</p>
<dt><code>MADV_FREE</code> (since Linux 4.5)</p>
<dd> The application no longer requires the pages in the range specified by <i>addr</i> and <i>len</i>. The kernel can thus free these pages, but the freeing could be delayed until memory pressure occurs. For each of the pages that has been marked to be freed but has not yet been freed, the free operation will be canceled if the caller writes into the page. After a successful <code>MADV_FREE</code> operation, any stale data (i.e., dirty, unwritten pages) will be lost when the kernel frees the pages. However, subsequent writes to pages in the range will succeed and then kernel cannot free those dirtied pages, so that the caller can always see just written data. If there is no subsequent write, the kernel can free the pages at any time. Once pages in the range have been freed, the caller will see zero-fill-on-demand pages upon subsequent page references.</p>
<dt>
<dd> The <code>MADV_FREE</code> operation can be applied only to private anonymous pages (see <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)). In Linux before version 4.12, when freeing pages on a swapless system, the pages in the given range are freed instantly, regardless of memory pressure.</p>
<dt><code>MADV_WIPEONFORK</code> (since Linux 4.14)</p>
<dd> Present the child process with zero-filled memory in this range after a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). This is useful in forking servers in order to ensure that sensitive per-process data (for example, PRNG seeds, cryptographic secrets, and so on) is not handed to child processes.</p>
<dt>
<dd> The <code>MADV_WIPEONFORK</code> operation can be applied only to private anonymous pages (see <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)).</p>
<dt>
<dd> Within the child created by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), the <code>MADV_WIPEONFORK</code> setting remains in place on the specified address range. This setting is cleared during <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt><code>MADV_KEEPONFORK</code> (since Linux 4.14)</p>
<dd> Undo the effect of an earlier <code>MADV_WIPEONFORK</code>.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>madvise</code>() returns zero. On error, it returns -1 and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> <i>advice</i> is <code>MADV_REMOVE</code>, but the specified address range is not a shared writable mapping.</p>
<dt><code>EAGAIN</code></p>
<dd> A kernel resource was temporarily unavailable.</p>
<dt><code>EBADF</code></p>
<dd> The map exists, but the area maps something that isn&#8217;t a file.</p>
<dt><code>EINVAL</code></p>
<dd> <i>addr</i> is not page-aligned or <i>length</i> is negative.</p>
<dt><code>EINVAL</code></p>
<dd> <i>advice</i> is not a valid.</p>
<dt><code>EINVAL</code></p>
<dd> <i>advice</i> is <code>MADV_DONTNEED</code> or <code>MADV_REMOVE</code> and the specified address range includes locked, Huge TLB pages, or <code>VM_PFNMAP</code> pages.</p>
<dt><code>EINVAL</code></p>
<dd> <i>advice</i> is <code>MADV_MERGEABLE</code> or <code>MADV_UNMERGEABLE</code>, but the kernel was not configured with <code>CONFIG_KSM</code>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>advice</i> is <code>MADV_FREE</code> or <code>MADV_WIPEONFORK</code> but the specified address range includes file, Huge TLB, <code>MAP_SHARED</code>, or <code>VM_PFNMAP</code> ranges.</p>
<dt><code>EIO</code></p>
<dd> (for <code>MADV_WILLNEED</code>) Paging in this area would exceed the process&#8217;s maximum resident set size.</p>
<dt><code>ENOMEM</code></p>
<dd> (for <code>MADV_WILLNEED</code>) Not enough memory: paging in failed.</p>
<dt><code>ENOMEM</code></p>
<dd> Addresses in the specified range are not currently mapped, or are outside the address space of the process.</p>
<dt><code>EPERM</code></p>
<dd> <i>advice</i> is <code>MADV_HWPOISON</code>, but the caller does not have the <code>CAP_SYS_ADMIN</code> capability.</dl>
<h2>VERSIONS</h2>
<p> Since Linux 3.18, support for this system call is optional, depending on the setting of the <code>CONFIG_ADVISE_SYSCALLS</code> configuration option.</p>
<h2>CONFORMING TO</h2>
<p> <code>madvise</code>() is not specified by any standards. Versions of this system call, implementing a wide variety of <i>advice</i> values, exist on many other implementations. Other implementations typically implement at least the flags listed above under <i>Conventional advice flags</i>, albeit with some variation in semantics. </p>
<p> POSIX.1-2001 describes <code><a href="/docs/linux/man/3-posix_madvise/">posix_madvise</a></code>(3) with constants <code>POSIX_MADV_NORMAL</code>, <code>POSIX_MADV_RANDOM</code>, <code>POSIX_MADV_SEQUENTIAL</code>, <code>POSIX_MADV_WILLNEED</code>, and <code>POSIX_MADV_DONTNEED</code>, and so on, with behavior close to the similarly named flags listed above.</p>
<h2>NOTES</h2>
<h3>Linux notes</h3>
<p> The Linux implementation requires that the address <i>addr</i> be page-aligned, and allows <i>length</i> to be zero. If there are some parts of the specified address range that are not mapped, the Linux version of <code>madvise</code>() ignores them and applies the call to the rest (but returns <code>ENOMEM</code> from the system call, as it should).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/2-mincore/">mincore</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-mprotect/">mprotect</a></code>(2), <code><a href="/docs/linux/man/2-msync/">msync</a></code>(2), <code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2), <code><a href="/docs/linux/man/2-prctl/">prctl</a></code>(2), <code><a href="/docs/linux/man/3-posix_madvise/">posix_madvise</a></code>(3), <code><a href="/docs/linux/man/5-core/">core</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
