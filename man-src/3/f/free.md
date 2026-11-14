---
title: "free(3)"
name: "free"
section: "3"
letter: "f"
url: "/docs/linux/man/3-free/"
description: "malloc, free, calloc, realloc, reallocarray – allocate and free dynamic memory"
---

<h2 class="name">NAME</h2>
<p> malloc, free, calloc, realloc, reallocarray &#8211; allocate and free dynamic memory </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
void *malloc(size_t size);
void free(void *ptr);
void *calloc(size_t nmemb, size_t size);
void *realloc(void *ptr, size_t size);
void *reallocarray(void *ptr, size_t nmemb, size_t size);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>reallocarray</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.29:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.28 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_GNU_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>malloc</code>() function allocates <i>size</i> bytes and returns a pointer to the allocated memory. <i>The memory is not initialized</i>. If <i>size</i> is 0, then <code>malloc</code>() returns either NULL, or a unique pointer value that can later be successfully passed to <code>free</code>(). </p>
<p> The <code>free</code>() function frees the memory space pointed to by <i>ptr</i>, which must have been returned by a previous call to <code>malloc</code>(), <code>calloc</code>(), or <code>realloc</code>(). Otherwise, or if <i>free(ptr)</i> has already been called before, undefined behavior occurs. If <i>ptr</i> is NULL, no operation is performed. </p>
<p> The <code>calloc</code>() function allocates memory for an array of <i>nmemb</i> elements of <i>size</i> bytes each and returns a pointer to the allocated memory. The memory is set to zero. If <i>nmemb</i> or <i>size</i> is 0, then <code>calloc</code>() returns either NULL, or a unique pointer value that can later be successfully passed to <code>free</code>(). If the multiplication of <i>nmemb</i> and <i>size</i> would result in integer overflow, then <code>calloc</code>() returns an error. By contrast, an integer overflow would not be detected in the following call to <code>malloc</code>(), with the result that an incorrectly sized block of memory would be allocated: </p>
<p> malloc(nmemb * size); </p>
<p> The <code>realloc</code>() function changes the size of the memory block pointed to by <i>ptr</i> to <i>size</i> bytes. The contents will be unchanged in the range from the start of the region up to the minimum of the old and new sizes. If the new size is larger than the old size, the added memory will <i>not</i> be initialized. If <i>ptr</i> is NULL, then the call is equivalent to <i>malloc(size)</i>, for all values of <i>size</i>; if <i>size</i> is equal to zero, and <i>ptr</i> is not NULL, then the call is equivalent to <i>free(ptr)</i>. Unless <i>ptr</i> is NULL, it must have been returned by an earlier call to <code>malloc</code>(), <code>calloc</code>(), or <code>realloc</code>(). If the area pointed to was moved, a <i>free(ptr)</i> is done. </p>
<p> The <code>reallocarray</code>() function changes the size of the memory block pointed to by <i>ptr</i> to be large enough for an array of <i>nmemb</i> elements, each of which is <i>size</i> bytes. It is equivalent to the call </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;realloc(ptr, nmemb&nbsp;*&nbsp;size); </p>
<p> However, unlike that <code>realloc</code>() call, <code>reallocarray</code>() fails safely in the case where the multiplication would overflow. If such an overflow occurs, <code>reallocarray</code>() returns NULL, sets <i>errno</i> to <code>ENOMEM</code>, and leaves the original block of memory unchanged.</p>
<h2>RETURN VALUE</h2>
<p> The <code>malloc</code>() and <code>calloc</code>() functions return a pointer to the allocated memory, which is suitably aligned for any built-in type. On error, these functions return NULL. NULL may also be returned by a successful call to <code>malloc</code>() with a <i>size</i> of zero, or by a successful call to <code>calloc</code>() with <i>nmemb</i> or <i>size</i> equal to zero. </p>
<p> The <code>free</code>() function returns no value. </p>
<p> The <code>realloc</code>() function returns a pointer to the newly allocated memory, which is suitably aligned for any built-in type, or NULL if the request failed. The returned pointer may be the same as <i>ptr</i> if the allocation was not moved (e.g., there was room to expand the allocation in-place), or different from <i>ptr</i> if the allocation was moved to a new address. If <i>size</i> was equal to 0, either NULL or a pointer suitable to be passed to <code>free</code>() is returned. If <code>realloc</code>() fails, the original block is left untouched; it is not freed or moved. </p>
<p> On success, the <code>reallocarray</code>() function returns a pointer to the newly allocated memory. On failure, it returns NULL and the original block of memory is left untouched.</p>
<h2>ERRORS</h2>
<p> <code>calloc</code>(), <code>malloc</code>(), <code>realloc</code>(), and <code>reallocarray</code>() can fail with the following error:</p>
<dl>
<dt><code>ENOMEM</code></p>
<dd> Out of memory. Possibly, the application hit the <code>RLIMIT_AS</code> or <code>RLIMIT_DATA</code> limit described in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2).</dl>
<h2>VERSIONS</h2>
<p> <code>reallocarray</code>() first appeared in glibc in version 2.26.</p>
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
<td> <code>malloc</code>(), <code>free</code>(),<br />
 <code>calloc</code>(), <code>realloc</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>malloc</code>(), <code>free</code>(), <code>calloc</code>(), <code>realloc</code>(): POSIX.1-2001, POSIX.1-2008, C89, C99. </p>
<p> <code>reallocarray</code>() is a nonstandard extension that first appeared in OpenBSD 5.6 and FreeBSD 11.0.</p>
<h2>NOTES</h2>
<p> By default, Linux follows an optimistic memory allocation strategy. This means that when <code>malloc</code>() returns non-NULL there is no guarantee that the memory really is available. In case it turns out that the system is out of memory, one or more processes will be killed by the OOM killer. For more information, see the description of <i>/proc/sys/vm/overcommit_memory</i> and <i>/proc/sys/vm/oom_adj</i> in <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), and the Linux kernel source file <i>Documentation/vm/overcommit-accounting.rst</i>. </p>
<p> Normally, <code>malloc</code>() allocates memory from the heap, and adjusts the size of the heap as required, using <code><a href="/docs/linux/man/2-sbrk/">sbrk</a></code>(2). When allocating blocks of memory larger than <code>MMAP_THRESHOLD</code> bytes, the glibc <code>malloc</code>() implementation allocates the memory as a private anonymous mapping using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). <code>MMAP_THRESHOLD</code> is 128 kB by default, but is adjustable using <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3). Prior to Linux 4.7 allocations performed using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2) were unaffected by the <code>RLIMIT_DATA</code> resource limit; since Linux 4.7, this limit is also enforced for allocations performed using <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2). </p>
<p> To avoid corruption in multithreaded applications, mutexes are used internally to protect the memory-management data structures employed by these functions. In a multithreaded application in which threads simultaneously allocate and free memory, there could be contention for these mutexes. To scalably handle memory allocation in multithreaded applications, glibc creates additional <i>memory allocation arenas</i> if mutex contention is detected. Each arena is a large region of memory that is internally allocated by the system (using <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2) or <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2)), and managed with its own mutexes. </p>
<p> SUSv2 requires <code>malloc</code>(), <code>calloc</code>(), and <code>realloc</code>() to set <i>errno</i> to <code>ENOMEM</code> upon failure. Glibc assumes that this is done (and the glibc versions of these routines do this); if you use a private malloc implementation that does not set <i>errno</i>, then certain library routines may fail without having a reason in <i>errno</i>. </p>
<p> Crashes in <code>malloc</code>(), <code>calloc</code>(), <code>realloc</code>(), or <code>free</code>() are almost always related to heap corruption, such as overflowing an allocated chunk or freeing the same pointer twice. </p>
<p> The <code>malloc</code>() implementation is tunable via environment variables; see <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3) for details.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-valgrind/">valgrind</a></code>(1), <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2), <code><a href="/docs/linux/man/2-mmap/">mmap</a></code>(2), <code><a href="/docs/linux/man/3-alloca/">alloca</a></code>(3), <code><a href="/docs/linux/man/3-malloc_get_state/">malloc_get_state</a></code>(3), <code><a href="/docs/linux/man/3-malloc_info/">malloc_info</a></code>(3), <code><a href="/docs/linux/man/3-malloc_trim/">malloc_trim</a></code>(3), <code><a href="/docs/linux/man/3-malloc_usable_size/">malloc_usable_size</a></code>(3), <code><a href="/docs/linux/man/3-mallopt/">mallopt</a></code>(3), <code><a href="/docs/linux/man/3-mcheck/">mcheck</a></code>(3), <code><a href="/docs/linux/man/3-mtrace/">mtrace</a></code>(3), <code><a href="/docs/linux/man/3-posix_memalign/">posix_memalign</a></code>(3) </p>
<p> For details of the GNU C library implementation, see</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
