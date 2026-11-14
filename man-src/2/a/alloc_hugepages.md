---
title: "alloc_hugepages(2)"
name: "alloc_hugepages"
section: "2"
letter: "a"
url: "/docs/linux/man/2-alloc_hugepages/"
description: "alloc_hugepages, free_hugepages – allocate or free huge pages"
---

<h2 class="name">NAME</h2>
<p> alloc_hugepages, free_hugepages &#8211; allocate or free huge pages </p>
<h2>SYNOPSIS</h2>
<pre><code>
void *alloc_hugepages(int key, void *addr, size_t len,
                      int prot, int flag);
int free_hugepages(void *addr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The system calls <code>alloc_hugepages</code>() and <code>free_hugepages</code>() were introduced in Linux 2.5.36 and removed again in 2.5.54. They existed only on i386 and ia64 (when built with <code>CONFIG_HUGETLB_PAGE</code>). In Linux 2.4.20, the syscall numbers exist, but the calls fail with the error <code>ENOSYS</code>. </p>
<p> On i386 the memory management hardware knows about ordinary pages (4 KiB) and huge pages (2 or 4 MiB). Similarly ia64 knows about huge pages of several sizes. These system calls serve to map huge pages into the process&#8217;s memory or to free them again. Huge pages are locked into memory, and are not swapped. </p>
<p> The <i>key</i> argument is an identifier. When zero the pages are private, and not inherited by children. When positive the pages are shared with other applications using the same <i>key</i>, and inherited by child processes. </p>
<p> The <i>addr</i> argument of <code>free_hugepages</code>() tells which page is being freed: it was the return value of a call to <code>alloc_hugepages</code>(). (The memory is first actually freed when all users have released it.) The <i>addr</i> argument of <code>alloc_hugepages</code>() is a hint, that the kernel may or may not follow. Addresses must be properly aligned. </p>
<p> The <i>len</i> argument is the length of the required segment. It must be a multiple of the huge page size. </p>
<p> The <i>prot</i> argument specifies the memory protection of the segment. It is one of <code>PROT_READ</code>, <code>PROT_WRITE</code>, <code>PROT_EXEC</code>. </p>
<p> The <i>flag</i> argument is ignored, unless <i>key</i> is positive. In that case, if <i>flag</i> is <code>IPC_CREAT</code>, then a new huge page segment is created when none with the given key existed. If this flag is not set, then <code>ENOENT</code> is returned when no segment with the given key exists.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>alloc_hugepages</code>() returns the allocated virtual address, and <code>free_hugepages</code>() returns zero. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOSYS</code></p>
<dd> The system call is not supported on this kernel.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/proc/sys/vm/nr_hugepages</i></p>
<dd> Number of configured hugetlb pages. This can be read and written.</p>
<dt><i>/proc/meminfo</i></p>
<dd> Gives info on the number of configured hugetlb pages and on their size in the three variables HugePages_Total, HugePages_Free, Hugepagesize.</dl>
<h2>CONFORMING TO</h2>
<p> These calls are specific to Linux on Intel processors, and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> These system calls are gone; they existed only in Linux 2.5.36 through to 2.5.54. Now the hugetlbfs filesystem can be used instead. Memory backed by huge pages (if the CPU supports them) is obtained by using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) to map files in this virtual filesystem. </p>
<p> The maximal number of huge pages can be specified using the <code>hugepages=</code> boot parameter.</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
