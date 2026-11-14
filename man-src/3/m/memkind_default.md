---
title: "memkind_default(3)"
name: "memkind_default"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memkind_default/"
description: "memkind_default.h – default implementations for memkind operations. Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (including non-backward compatible ch..."
---

<h2>NAME</h2>
<p> memkind_default.h &#8211; default implementations for memkind operations.<br />
 Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (including non-backward compatible changes), or remove.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;memkind/internal/memkind_default.h&gt;
Link with - lmemkind int memkind_default_create(struct memkind *kind, const struct memkind_ops *ops, const char *name);

int memkind_default_destroy(struct memkind *kind);

void *memkind_default_malloc(struct memkind *kind, size_t size);

void *memkind_default_calloc(struct memkind *kind, size_t num, size_t size);

int memkind_default_posix_memalign(struct memkind *kind, void **memptr, size_t alignment, size_t size);

void *memkind_default_realloc(struct memkind *kind, void *ptr, size_t size);

void memkind_default_free(struct memkind *kind, void *ptr);

void *memkind_default_mmap(struct memkind *kind, void *addr, size_t size);

int memkind_default_mbind(struct memkind *kind, void *ptr, size_t len);

int memkind_default_get_mmap_flags(struct memkind *kind, int *flags);

int memkind_default_get_mbind_mode(struct memkind *kind, int *mode);

int memkind_preferred_get_mbind_mode(struct memkind *kind, int *mode);

int memkind_interleave_get_mbind_mode(struct memkind *kind, int *mode);

int memkind_nohugepage_madvise(struct memkind *kind, void *addr, size_t size);

int memkind_default_get_size(struct memkind *kind, size_t *total, size_t *free);

int memkind_posix_check_alignment(struct memkind *kind, size_t alignment);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Default implementations for memkind operations which include a several useful methods that are not part of the <code>MEMKIND_DEFAULT</code> kind which is a fall through to the jemalloc implementation. </p>
<p> <code>memkind_default_create</code>() implements the required start up for every kind. If a kind does not point to this function directly for its <code>ops.create</code>() operation, then the function that it points to must call <code>memkind_default_create</code>() at its start. </p>
<p> <code>memkind_default_destroy</code>() implements the required shutdown for every kind. If a kind does not point to this function directly for its <code>ops.destroy</code>() operation, then the function that it points to must call <code>memkind_default_destroy</code>() at its end. </p>
<p> <code>memkind_default_malloc</code>() is a direct call through to <code>jemk_malloc</code>(). </p>
<p> <code>memkind_default_calloc</code>() is a direct call through to <code>jemk_calloc</code>(). </p>
<p> <code>memkind_default_posix_memalign</code>() is a direct call through to <code>jemk_posix_memalign</code>(). </p>
<p> <code>memkind_default_realloc</code>() is a direct call through to <code>jemk_realloc</code>(). </p>
<p> <code>memkind_default_free</code>(). is a direct call through to <code>jemk_free</code>(). Note that this method can be called on any pointer returned by a jemalloc allocation, and in particular, all of the arena allocations described in <code><a href="/docs/linux/man/3-memkind_arena/">memkind_arena</a></code>(3) can use this function for freeing. </p>
<p> <code>memkind_default_mmap</code>() This calls the ops-&gt;get_mmap_flags() operations for the kind, or falls back on the default implementations if the function pointers are NULL. The results of these calls are passed to the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) call to allocate pages from the operating system. The <i>addr</i> is the hint passed through to <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) and <i>size</i> is the size of the buffer to be allocated. The return value is the allocated buffer or <code>MAP_FAILED</code> in the case of an error. </p>
<p> <code>memkind_default_mbind</code>() makes calls the kind&#8217;s <code>ops.get_mbind_nodemask</code>() and <code>ops.get_mbind_mode</code>() operations to gather inputs and then calls the <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) system call using the results along with and user input <i>ptr</i> and <i>len</i>. </p>
<p> <code>memkind_default_get_mmap_flags</code>() sets <i>flags</i> to <code>MAP_PRIVATE | MAP_ANONYMOUS</code>. See <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) for more information about these flags. </p>
<p> <code>memkind_default_get_mbind_mode</code>() sets <i>mode</i> to <code>MPOL_BIND</code>. See <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) for more information about this flag. </p>
<p> <code>memkind_preferred_get_mbind_mode</code>() sets <i>mode</i> to <code>MPOL_PREFERRED</code>. See <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) for more information about this flag. </p>
<p> <code>memkind_interleave_get_mbind_mode</code>() sets <i>mode</i> to <code>MPOL_INTERLEAVE</code>. See <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2) for more information about this flag. </p>
<p> <code>memkind_nohugepage_madvise</code>() calls <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) with the <code>MADV_NOHUGEPAGE</code> advice. See <code><a href="/docs/linux/man/2-madvise/">madvise</a></code>(2) for more information about this option. </p>
<p> <code>memkind_default_get_size</code>() sums the values returned by <code>numa_node_size64</code>() function for every NUMA node set by the <code>.get_node_mask</code>() operation. If the <i>.get_node_mask</i> pointer is <code>NULL</code> then the values are summed for all NUMA nodes. </p>
<p> <code>memkind_posix_check_alignment</code>() can be used to check the alignment value for <code>memkind_posix_memalign</code>() to ensure that is abides by the POSIX requirements: alignment must be a power of 2 at least as large as sizeof(<code>void *</code>).</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2014 &#8211; 2016 Intel Corporation. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-memkind/">memkind</a></code>(3), <code><a href="/docs/linux/man/3-memkind_arena/">memkind_arena</a></code>(3), <code><a href="/docs/linux/man/3-memkind_hbw/">memkind_hbw</a></code>(3), <code><a href="/docs/linux/man/3-memkind_hugetlb/">memkind_hugetlb</a></code>(3), <code><a href="/docs/linux/man/3-memkind_gbtlb/">memkind_gbtlb</a></code>(3), <code><a href="/docs/linux/man/3-memkind_pmem/">memkind_pmem</a></code>(3), <code><a href="/docs/linux/man/3-jemalloc/">jemalloc</a></code>(3), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) </p>
<h2>Index</h2>
