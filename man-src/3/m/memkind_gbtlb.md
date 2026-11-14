---
title: "memkind_gbtlb(3)"
name: "memkind_gbtlb"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memkind_gbtlb/"
description: "memkind_gbtlb.h – gigabyte TLB memkind operations. Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (including non-backward compatible changes), or remove."
---

<h2>NAME</h2>
<p> memkind_gbtlb.h &#8211; gigabyte TLB memkind operations.<br />
 Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (including non-backward compatible changes), or remove.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;memkind/internal/memkind_gbtlb.h&gt;
Link with - lmemkind void *memkind_gbtlb_malloc(struct memkind *kind, size_t size);
void *memkind_gbtlb_calloc(struct memkind *kind, size_t num, size_t size);
int memkind_gbtlb_posix_memalign(struct memkind *kind, void **memptr, size_t alignment, size_t size);
void *memkind_gbtlb_realloc(struct memkind *kind, void *ptr, size_t size);
void memkind_gbtlb_free(struct memkind *kind, void *ptr);
int memkind_gbtlb_get_mmap_flags(struct memkind *kind, int *flags);
int memkind_gbtlb_check_addr(struct memkind *kind, void *addr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Gigabyte TLB implementations for memkind operations. These are implemented without using the jemalloc library. The implementation is a wrapper around <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) with a hash table for storing the address and extent of the mapped memory. The hash table is queried when freeing memory in order to determine the extent that should be passed to <code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2) The reason for using such a simplified implementation instead of using a heap is that a heap manager is intended to mitigate the overhead of the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) system call by calling it less frequently than the allocation requests that is services. Since there is a large amount of memory being allocated with each call in the case where there are gigabyte pages backing the allocation, the frequency of requests is assumed to be low. For this reason the traditional requirements of a heap manager to be faster than directly mapping memory from the operating system is relaxed. </p>
<p> <code>memkind_gbtlb_malloc</code>() calls <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) with <code>MAP_HUGE_1GB</code> mmap flag for allocating gigabyte pages for <i>size</i> bytes and <i>kind</i> can take <code>MEMKIND_GBTLB,</code> <code>MEMKIND_HBW_GBTLB,</code> <code>MEMKIND_HBW_GBTLB_PREFERRED</code> and stores the returned address in the internal hash table which can be queried to support the <code>memkind_gbtlb_free</code>() operation. If kind does not support GBTLB undefined behaviour occurs. </p>
<p> <code>memkind_gbtlb_calloc</code>() is exactly the same implementation and supports the same <i>kind</i> as <code>memkind_gbtlb_malloc</code>() since the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) system call is guaranteed to return memory of <i>size</i> bytes which has been zeroed. </p>
<p> <code>memkind_gbtlb_posix_memalign</code>() is a similar implementation to <code>memkind_gbtlb_malloc</code>() except that the returned address will be aligned as requested, and the error code returned will reflect the POSIX standard defined in <i>errno.h.</i> <code>memkind_gbtlb_posix_memalign</code> the return pointer for the allocated memory </p>
<p> <code>memkind_gbtlb_realloc</code>() can be used to extend or shrink an allocation previously created by one of the other interfaces defined here. Implementation reuses <code>memkind_gbtlb_malloc</code>() for allocating the new size of memory if needed. There is an optimization in place so that if a partial page was previously allocated then it can be extended to the end of the page transparently. (Details in NOTE) </p>
<p> <code>memkind_gbtlb_free</code>() queries the hash table to find the extent of the memory associated with the address passed by the user. It then calls <code><a href="/docs/linux/man/2-munmap/">munmap</a></code>(2) on that extent. </p>
<p> <code>memkind_gbtlb_get_mmap_flags</code>() Sets the <i>flags</i> appropriately for requesting anonymous gigabyte pages. </p>
<p> <code>memkind_gbtlb_check_addr</code>() queries the hash table to determine if the address reflects an extent previously allocated with one of the interfaces defined here, and returned 03 exact kind associated with the address.</p>
<h2>INTERNAL STATIC FUNCTIONS</h2>
<p> <code>memkind_store</code>() implements a hash table with a hash value calculated using the <code>crc32</code> SIMD instruction which returns <code>crc</code><i>+</i><code>CRC-32C(v)</code> where v is the virtual address pointer. This hash table is used to store the virtual address for retrieval and freeing. The table, stores the requested size, allocated size, the virtual address pointer and the mmap&#8217;ed address pointer information. </p>
<p> <code>memkind_gbtlb_ceil_size</code>() differentiates between STRICT and REGULAR gbtlb implementations by getting the ceil of the size if the requested size is not a modulo of a gigabyte. </p>
<p> <code>memkind_gbtlb_check_addr</code>() function looks in the gbtlb hash table to see if the virtual address was allocated with GB pages. This feature is used in determining the kind for realloc&#8217;ing in the hbw_realloc implementation. </p>
<h2>NOTES</h2>
<p> <code>memkind_gbtlb_realloc</code>() is special, as it allows to use the same page that was fetched. Since this implementation of gigabyte pages is not backed by an actual heap manager like other kinds (which use jemalloc), each allocation request would fetch a gigabyte page. So when a realloc is called on a virtual address pointer backed by a GB page which has not been completely used, and if the current request including previous request does not exceed a GB, no more pages are allocated. To summarize, realloc implementation of MEMKIND_GBTLB guarantees that gigabyte pages get allocated when its actually needed. </p>
<p> <code>memkind_gbtlb_free</code>() is a little different from the free of the other kinds. Since the other kinds are backed by jemalloc, a free will recycle the pages in recycle pools maintained by jemalloc, in the case of the gbtlb, the pages are actually returned to the operating system.</p>
<h2>REQUIREMENTS</h2>
<p> To allocated gigabyte pages from the operating system. This can be done by specifying <code>hugepagesz=1G nr_hugepages=N</code> on the kernel commandline. From <code>3.16</code> and later kernels, users can allocate gigabyte pages like its done for 2MB pages. i.e <code>echo no_pages &gt; /proc/sys/vm/nr_hugepages</code> </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2014 &#8211; 2016 Intel Corporation. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-memkind/">memkind</a></code>(3), <code><a href="/docs/linux/man/3-memkind_arena/">memkind_arena</a></code>(3), <code><a href="/docs/linux/man/3-memkind_default/">memkind_default</a></code>(3), <code><a href="/docs/linux/man/3-memkind_hbw/">memkind_hbw</a></code>(3), <code><a href="/docs/linux/man/3-memkind_hugetlb/">memkind_hugetlb</a></code>(3), <code><a href="/docs/linux/man/3-memkind_pmem/">memkind_pmem</a></code>(3), <code><a href="/docs/linux/man/3-jemalloc/">jemalloc</a></code>(3), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) </p>
<h2>Index</h2>
