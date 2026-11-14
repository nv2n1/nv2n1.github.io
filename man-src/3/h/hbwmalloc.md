---
title: "hbwmalloc(3)"
name: "hbwmalloc"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hbwmalloc/"
description: "hbwmalloc – The high bandwidth memory interface Note: hbwmalloc.h functionality is considered as stable API (STANDARD API)."
---

<h2>NAME</h2>
<p> hbwmalloc &#8211; The high bandwidth memory interface<br />
 Note: hbwmalloc.h functionality is considered as stable API (STANDARD API).</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;hbwmalloc.h&gt;
Link with - lmemkind int hbw_check_available(void);

void *hbw_malloc(size_t size);

void *hbw_calloc(size_t nmemb, size_t size);

void *hbw_realloc(void *ptr, size_t size);

void hbw_free(void *ptr);

int hbw_posix_memalign(void **memptr, size_t alignment, size_t size);

int hbw_posix_memalign_psize(void **memptr, size_t alignment, size_t size, hbw_pagesize_t pagesize);

hbw_policy_t hbw_get_policy(void);

int hbw_set_policy(hbw_policy_t mode);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>hbw_check_available</code>() returns 0 if high bandwidth memory is available and an error code described in the <code>ERRORS</code> section if not. </p>
<p> <code>hbw_malloc</code>() allocates <i>size</i> bytes of uninitialized high bandwidth memory. The allocated space is suitably aligned (after possible pointer coercion) for storage of any type of object. If <i>size</i> is zero then <code>hbw_malloc</code>() returns NULL. </p>
<p> <code>hbw_calloc</code>() allocates space for <i>nmemb</i> objects in high bandwidth memory, each <i>size</i> bytes in length. The result is identical to calling <code>hbw_malloc</code>() with an argument of <i>nmemb</i>*<i>size</i> , with the exception that the allocated memory is explicitly initialized to zero bytes. If <i>nmemb</i> or <i>size</i> is 0, then <code>hbw_calloc</code>() returns NULL. </p>
<p> <code>hbw_realloc</code>() changes the size of the previously allocated high bandwidth memory referenced by <i>ptr</i> to <i>size</i> bytes. The contents of the memory are unchanged up to the lesser of the new and old sizes. If the new size is larger, the contents of the newly allocated portion of the memory are undefined. Upon success, the memory referenced by <i>ptr</i> is freed and a pointer to the newly allocated high bandwidth memory is returned. </p>
<p> <code>Note:</code> <code>hbw_realloc</code>() may move the memory allocation, resulting in a different return value than <i>ptr</i>. </p>
<p> If <i>ptr</i> is NULL, the <code>hbw_realloc</code>() function behaves identically to <code>hbw_malloc</code>() for the specified size. The address <i>ptr</i>, if not NULL, was returned by a previous call to <code>hbw_malloc</code>(), <code>hbw_calloc</code>(), <code>hbw_realloc</code>(), or <code>hbw_posix_memalign</code>(). Otherwise, or if <i>hbw_free(ptr)</i> was called before, undefined behavior occurs. </p>
<p> <code>Note:</code> <code>hbw_realloc</code>() cannot be used with a pointer returned by <code>hbw_posix_memalign_psize</code>(). </p>
<p> <code>hbw_free</code>() causes the allocated memory referenced by <i>ptr</i> to be made available for future allocations. If <i>ptr</i> is NULL, no action occurs. The address <i>ptr</i>, if not NULL, must have been returned by a previous call to <code>hbw_malloc</code>(), <code>hbw_calloc</code>(), <code>hbw_realloc</code>(), <code>hbw_posix_memalign</code>(), or <code>hbw_posix_memalign_psize</code>(). Otherwise, if <i>hbw_free(ptr)</i> was called before, undefined behavior occurs. </p>
<p> <code>hbw_posix_memalign</code>() allocates <i>size</i> bytes of high bandwidth memory such that the allocation&#8217;s base address is an even multiple of <i>alignment</i>, and returns the allocation in the value pointed to by <i>memptr</i>. The requested <i>alignment</i> must be a power of 2 at least as large as <i>sizeof(void *)</i>. </p>
<p> <code>hbw_posix_memalign_psize</code>() allocates <i>size</i> bytes of high bandwidth memory such that the allocation&#8217;s base address is an even multiple of <i>alignment</i>, and returns the allocation in the value pointed to by <i>memptr</i>. The requested <i>alignment</i> must be a power of 2 at least as large as <i>sizeof(void *)</i>. The memory will be allocated using pages determined by the <i>pagesize</i> variable which may be one of the following enumerated values:</p>
<dl>
<dt><code>HBW_PAGESIZE_4KB</code></p>
<dd> The four kilobyte page size option. Note that with transparent huge pages enabled these allocations may be promoted by the operating system to two megabyte pages.</p>
<dt><code>HBW_PAGESIZE_2MB</code></p>
<dd> The two megabyte page size option.</p>
<dt><code>HBW_PAGESIZE_1GB</code></p>
<dd> This option allows the user to specify arbitrary sizes backed by one gigabytes pages. Gigabyte pages are allocated even if the size is not a modulo of 1GB. A good example of using this feature with realloc is shown in gb_realloc_example.c</p>
<dt><code>HBW_PAGESIZE_1GB_STRICT</code></p>
<dd> The one gigabyte page size option. The total size of the allocation must be a multiple of 1GB with this option, otherwise the allocation will fail.</dl>
<p> <code>hbw_get_policy</code>() returns the current fallback policy when insufficient high bandwith memory is available. </p>
<p> <code>hbw_set_policy</code>() sets the current fallback policy. The policy can be modified only once in the lifetime of an application and before calling hbw_*alloc() or hbw_posix_memalign*() function.<br />
 Note: If the policy is not set, than HBW_POLICY_PREFERRED will be used by default.</p>
<dl>
<dt><code>HBW_POLICY_BIND</code></p>
<dd> If insufficient high bandwidth memory from the nearest NUMA node is available to satisfy a request, the allocated pointer is set to NULL and <i>errno</i> is set to ENOMEM. If insufficient high bandwidth memory pages are available at fault time the Out Of Memory (OOM) killer is triggered. Note that pages are faulted exclusively from the high bandwidth NUMA node nearest at time of allocation, not at time of fault.</p>
<dt><code>HBW_POLICY_PREFERRED</code></p>
<dd> If insufficient memory is available from the high bandwidth NUMA node closest at allocation time, fall back to standard memory (default) with the smallest NUMA distance.</p>
<dt><code>HBW_POLICY_INTERLEAVE</code></p>
<dd> Interleave faulted pages from across all high bandwidth NUMA nodes using standard size pages (the Transparent Huge Page feature is disabled).</dl>
<h2>RETURN VALUE</h2>
<p> <code>hbw_get_policy</code>() returns <code>HBW_POLICY_BIND</code> or <code>HBW_POLICY_PREFERRED</code> which represents the current high bandwidth policy. <code>hbw_free</code>() do not have return value. <code>hbw_malloc</code>() <code>hbw_calloc</code>(), and <code>hbw_realloc</code>() return the pointer to the allocated memory, or NULL if the request fails. <code>hbw_posix_memalign</code>(), <code>hbw_posix_memalign_psize</code>() and <code>hbw_set_policy</code>() return zero on success and return an error code as described in the <code>ERRORS</code> section below on failure.</p>
<h2>ERRORS</h2>
<dl>
<dt>Error codes described here are the POSIX standard error codes as defined in &lt;errno.h&gt;</p>
<dd>
<dt><code>hbw_check_available</code>()</p>
<dd> returns <code>ENODEV</code> if high-bandwidth memory is unavailable.</p>
<dt><code>hbw_posix_memalign</code>() and <code>hbw_posix_memalign_psize</code>()</p>
<dd> If the <i>alignment</i> parameter is not a power of two, or was not a multiple of <i>sizoeof(void *)</i>, then <code>EINVAL</code> is returned. If there was insufficient memory to satisfy the request then <code>ENOMEM</code> is returned.</p>
<dt><code>hbw_set_policy</code>()</p>
<dd> returns <code>EPERM</code> if hbw_set_policy () was called more than once, or <code>EINVAL if</code> <i>mode</i> argument was neither <code>HBW_POLICY_PREFERRED,</code> <code>HBW_POLICY_BIND</code> nor <code>HBW_POLICY_INTERLEAVE.</code></dl>
<h2>NOTES</h2>
<p> The <i>hbwmalloc.h</i> file defines the external functions and enumerations for the hbwmalloc library. These interfaces define a heap manager that targets high bandwidth memory numa nodes.</p>
<h2>FILES</h2>
<dl>
<dt><i>/usr/bin/memkind-hbw-nodes</i></p>
<dd> Prints a comma separated list of high bandwidth nodes.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>MEMKIND_HBW_NODES</code></p>
<dd> This environment varaible is a comma separated list of NUMA nodes that are treated as high bandwidth. Uses the <i>libnuma</i> routine <code>numa_parse_nodestring</code>() for parsing, so the syntax described in the <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3) man page for this routine applies for example: 1-3,5 is a valid setting.</p>
<dt><code>MEMKIND_ARENA_NUM_PER_KIND</code></p>
<dd> This environment variable allows leveraging internal mechanism of the library for setting number of arenas per kind. Value should be a positive integer (not greater than INT_MAX defined in limits.h). The user should set the value based on the characteristics of application that is using the library. Higher value can provide better performance in extremely multithreaded applications at the cost of memory overhead. See section &quot;IMPLEMENTATION NOTES&quot; of <code><a href="/docs/linux/man/3-jemalloc/">jemalloc</a></code>(3) for more details about arenas.</dl>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2014 &#8211; 2016 Intel Corporation. All rights reserved.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-numa/">numa</a></code>(3), <code><a href="/docs/linux/man/8-numactl/">numactl</a></code>(8), <code><a href="/docs/linux/man/2-mbind/">mbind</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/2-move_pages/">move_pages</a></code>(2) <code><a href="/docs/linux/man/3-jemalloc/">jemalloc</a></code>(3) <code><a href="/docs/linux/man/3-memkind/">memkind</a></code>(3) </p>
<h2>Index</h2>
