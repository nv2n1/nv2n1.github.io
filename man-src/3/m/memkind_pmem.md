---
title: "memkind_pmem(3)"
name: "memkind_pmem"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memkind_pmem/"
description: "memkind_pmem.h – file-backed memory memkind operations. Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (including non-backward compatible changes), or r..."
---

<h2>NAME</h2>
<p> memkind_pmem.h &#8211; file-backed memory memkind operations.<br />
 Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (including non-backward compatible changes), or remove.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;memkind/internal/memkind_pmem.h&gt;
Link with - lmemkind int memkind_pmem_create(struct memkind *kind, const struct memkind_ops *ops, const char *name);

int memkind_pmem_destroy(struct memkind *kind);

void *memkind_pmem_mmap(struct memkind *kind, void *addr, size_t size);

int memkind_pmem_get_mmap_flags(struct memkind *kind, int *flags);

int memkind_pmem_get_size(struct memkind *kind, size_t *total, size_t *free);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The pmem memory memkind operations enable memory kinds built on memory-mapped files. These support traditional <code>volatile</code> memory allocation in a fashion similar to <code><a href="/docs/linux/man/3-libvmem/">libvmem</a></code>(3) library. It uses the <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) system call to create a pool of volatile memory. Such memory may have different attributes, depending on the file system containing the memory-mapped files. (See also <i><a rel="nofollow" href="http://pmem.io/nvml/libvmem">http://pmem.io/nvml/libvmem</a></i>). </p>
<p> The pmem memkinds are most useful when used with <i>Direct Access</i> storage (DAX), which is memory-addressable persistent storage that supports load/store access without being paged via the system page cache. A Persistent Memory-aware file system is typically used to provide this type of access. </p>
<p> The most convenient way to create pmem memkinds is to use <code>memkind_create_pmem</code>() (see <code><a href="/docs/linux/man/3-memkind/">memkind</a></code>(3)). </p>
<p> <code>memkind_pmem_create</code>() is an implementation of the memkind &quot;create&quot; operation for file-backed memory kinds. This allocates a space for some pmem-specific metadata, then calls <code>memkind_arena_create</code>() (see <code><a href="/docs/linux/man/3-memkind_arena/">memkind_arena</a></code>(3)) </p>
<p> <code>memkind_pmem_destroy</code>() is an implementation of the memkind &quot;destroy&quot; operation for file-backed memory kinds. This releases all of the resources allocated by <code>memkind_pmem_create</code>() and allows the file system space to be reclaimed. </p>
<p> <code>memkind_pmem_mmap</code>() allocates the file system space for a block of <i>size</i> bytes in the memory-mapped file associated with given kind. The <i>addr</i> hint is ignored. The return value is the address of mapped memory region or <code>MAP_FAILED</code> in the case of an error. </p>
<p> <code>memkind_pmem_get_mmap_flags</code>() sets <i>flags</i> to <code>MAP_SHARED</code>. See <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) for more information about these flags. </p>
<p> <code>memkind_pmem_get_size</code>() sets <i>total</i> to the number of bytes of the entire usable space in the memory-mapped file associated with the specified kind, and sets <i>free</i> to the number of unused bytes available in the memory-mapped file.</p>
<dl>
<dt><code>MEMKIND_PMEM_MIN_SIZE</code></p>
<dd> The minimum size of the file-backed memory partition.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2015 &#8211; 2016 Intel Corporation. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-memkind/">memkind</a></code>(3), <code><a href="/docs/linux/man/3-memkind_arena/">memkind_arena</a></code>(3), <code><a href="/docs/linux/man/3-memkind_default/">memkind_default</a></code>(3), <code><a href="/docs/linux/man/3-memkind_gbtlb/">memkind_gbtlb</a></code>(3), <code><a href="/docs/linux/man/3-memkind_hbw/">memkind_hbw</a></code>(3), <code><a href="/docs/linux/man/3-memkind_hugetlb/">memkind_hugetlb</a></code>(3), <code><a href="/docs/linux/man/3-libvmem/">libvmem</a></code>(3), <code><a href="/docs/linux/man/3-jemalloc/">jemalloc</a></code>(3), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) </p>
<h2>Index</h2>
