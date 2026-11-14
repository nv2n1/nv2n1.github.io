---
title: "memkind_arena(3)"
name: "memkind_arena"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memkind_arena/"
description: "memkind_arena.h – jemalloc arena allocation memkind operations. Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (including non-backward compatible change..."
---

<h2>NAME</h2>
<p> memkind_arena.h &#8211; jemalloc arena allocation memkind operations.<br />
 Note: This is EXEPRIMENTAL API. The functionality and the header file itself can be changed (including non-backward compatible changes), or remove.</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;memkind/internal/memkind_arena.h&gt;
Link with - lmemkind int memkind_arena_create(struct memkind *kind, const struct memkind_ops *ops, const char *name);
int memkind_arena_create_map(struct memkind *kind);
int memkind_arena_destroy(struct memkind *kind);
void *memkind_arena_malloc(struct memkind *kind, size_t size);
void *memkind_arena_calloc(struct memkind *kind, size_t num, size_t size);
int memkind_arena_posix_memalign(struct memkind *kind, void **memptr, size_t alignment, size_t size);
void *memkind_arena_realloc(struct memkind *kind, void *ptr, size_t size);
int memkind_thread_get_arena(struct memkind *kind, unsigned int *arena, size_t size);
int memkind_bijective_get_arena(struct memkind *kind, unsigned int *arena, size_t size);
</code></pre>
<h2>DESCRIPTION</h2>
<p> This header file is a collection of functions can be used to populate the memkind operations structure for memory kinds that use jemalloc. </p>
<p> <code>memkind_arena_create</code>() is an implementation of the memkind &quot;create&quot; operation for memory kinds that use jemalloc. This calls <code>memkind_default_create</code>() (see <code><a href="/docs/linux/man/3-memkind_default-h/">memkind_default.h</a></code>(3)) followed by <code>memkind_arena_create_map</code>() described below. </p>
<p> <code>memkind_arena_create_map</code>() creates the <i>arena_map</i> array for the memkind structure pointed to by <i>kind</i> which can be indexed by the <code>ops.get_arena</code>() function from the kind&#8217;s operations. If get_arena points <code>memkind_thread_get_arena</code>() then there will be four arenas created for each processor, and if get_arena points to <code>memkind_bijective_get_arena</code>() then just one arena is created. </p>
<p> <code>memkind_arena_destroy</code>() is an implementation of the memkind &quot;destroy&quot; operation for memory kinds that use jemalloc. This releases all of the resources allocated by <code>memkind_arena_create</code>(). </p>
<p> <code>memkind_arena_malloc</code>() is an implementation of the memkind &quot;malloc&quot; operation for memory kinds that use jemalloc. This allocates memory using the arenas created by <code>memkind_arena_create</code>() though the jemalloc <code>jemk_mallocx</code>() interface. It uses the memkind &quot;get_arena&quot; operation to select the arena. </p>
<p> <code>memkind_arena_calloc</code>() is an implementation of the memkind &quot;calloc&quot; operation for memory kinds that use jemalloc. This allocates memory using the arenas created by <code>memkind_arena_create</code>() though the jemalloc <code>jemk_mallocx</code>() interface. It uses the memkind &quot;get_arena&quot; operation to select the arena. </p>
<p> <code>memkind_arena_posix_memalign</code>() is an implementation of the memkind &quot;posix_memalign&quot; operation for memory kinds that use jemalloc. This allocates memory using the arenas created by <code>memkind_arena_create</code>() though the jemalloc <code>jemk_mallocx</code>() interface. It uses the memkind &quot;get_arena&quot; operation to select the arena. The POSIX standard requires that <code><a href="/docs/linux/man/3-posix_memalign/">posix_memalign</a></code>(3) may not set <i>errno</i> however the <code>jemk_mallocx</code>() routine may. In an attempt to abide by the standard <i>errno</i> is recorded before calling <code>jemk_mallocx</code>() and then reset after the call. </p>
<p> <code>memkind_arena_realloc</code>() is an implementation of the memkind &quot;realloc&quot; operation for memory kinds that use jemalloc. This allocates memory using the arenas created by <code>memkind_arena_create</code>() though the jemalloc <code>jemk_mallocx</code>() interface. It uses the memkind &quot;get_arena&quot; operation to select the arena. </p>
<p> <code>memkind_thread_get_arena</code>() Retrieves the <i>arena</i> index that is bound to to the calling thread based on a hash of its thread ID. The <i>arena</i> index can be used with the MALLOCX_ARENA macro to set flags for <code>jemk_mallocx</code>(). </p>
<p> <code>memkind_bijective_arena_get_arena</code>() Retrieves the <i>arena</i> index to be used with the MALLOCX_ARENA macro to set flags for <code>jemk_mallocx</code>(). Use of this operation implies that only one arena is used for the <i>kind</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2014 &#8211; 2016 Intel Corporation. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-memkind/">memkind</a></code>(3), <code><a href="/docs/linux/man/3-memkind_default/">memkind_default</a></code>(3), <code><a href="/docs/linux/man/3-memkind_hbw/">memkind_hbw</a></code>(3), <code><a href="/docs/linux/man/3-memkind_hugetlb/">memkind_hugetlb</a></code>(3), <code><a href="/docs/linux/man/3-memkind_gbtlb/">memkind_gbtlb</a></code>(3), <code><a href="/docs/linux/man/3-memkind_pmem/">memkind_pmem</a></code>(3), <code><a href="/docs/linux/man/3-jemalloc/">jemalloc</a></code>(3), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) </p>
<h2>Index</h2>
