---
title: "malloc(3)"
name: "malloc"
section: "3"
letter: "m"
url: "/docs/linux/man/3-malloc/"
description: "malloc, free, calloc, realloc, reallocarray – allocate and free dynamic memory"
---

<h2 id="name">NAME</h2>
<p>malloc, free, calloc, realloc, reallocarray &#8211; allocate and free dynamic memory</p>
<h2 id="synopsis">SYNOPSIS</h2>
<pre><code>#include &lt;stdlib.h&gt;

void *malloc(size_t size);
void free(void *ptr);
void *calloc(size_t nmemb, size_t size);
void *realloc(void *ptr, size_t size);
void *reallocarray(void *ptr, size_t nmemb, size_t size);
</code></pre>
<p>Feature Test Macro Requirements for glibc (see <a href="/docs/linux/man/7-feature_test_macros/"><code>feature_test_macros</code></a>(7)):</p>
<p><code>reallocarray</code>():</p>
<pre><code>Since glibc 2.29:
    _DEFAULT_SOURCE
Glibc 2.28 and earlier:
    _GNU_SOURCE</code></pre>
<h2 id="description">DESCRIPTION</h2>
<p>The <code>malloc</code>() function allocates <em>size</em> bytes and returns a pointer to the allocated memory. <em>The memory is not initialized</em>. If <em>size</em> is 0, then <code>malloc</code>() returns either NULL, or a unique pointer value that can later be successfully passed to <code>free</code>().</p>
<p>The <code>free</code>() function frees the memory space pointed to by <em>ptr</em>, which must have been returned by a previous call to <code>malloc</code>(), <code>calloc</code>(), or <code>realloc</code>(). Otherwise, or if <code>free(ptr)</code> has already been called before, undefined behavior occurs. If <em>ptr</em> is NULL, no operation is performed.</p>
<p>The <code>calloc</code>() function allocates memory for an array of <em>nmemb</em> elements of <em>size</em> bytes each and returns a pointer to the allocated memory. The memory is set to zero. If <em>nmemb</em> or <em>size</em> is 0, then <code>calloc</code>() returns either NULL, or a unique pointer value that can later be successfully passed to <code>free</code>(). If the multiplication of <em>nmemb</em> and <em>size</em> would result in integer overflow, then <code>calloc</code>() returns an error. By contrast, an integer overflow would not be detected in the following call to <code>malloc</code>(), with the result that an incorrectly sized block of memory would be allocated:</p>
<pre><code>malloc(nmemb * size);</code></pre>
<p>The <code>realloc</code>() function changes the size of the memory block pointed to by <em>ptr</em> to <em>size</em> bytes. The contents will be unchanged in the range from the start of the region up to the minimum of the old and new sizes. If the new size is larger than the old size, the added memory will <em>not</em> be initialized. If <em>ptr</em> is NULL, then the call is equivalent to <code>malloc(size)</code>, for all values of <em>size</em>; if <em>size</em> is equal to zero, and <em>ptr</em> is not NULL, then the call is equivalent to <code>free(ptr)</code>. Unless <em>ptr</em> is NULL, it must have been returned by an earlier call to <code>malloc</code>(), <code>calloc</code>(), or <code>realloc</code>(). If the area pointed to was moved, a <code>free(ptr)</code> is done.</p>
<p>The <code>reallocarray</code>() function changes the size of the memory block pointed to by <em>ptr</em> to be large enough for an array of <em>nmemb</em> elements, each of which is <em>size</em> bytes. It is equivalent to the call:</p>
<pre><code>realloc(ptr, nmemb * size);</code></pre>
<p>However, unlike that <code>realloc</code>() call, <code>reallocarray</code>() fails safely in the case where the multiplication would overflow. If such an overflow occurs, <code>reallocarray</code>() returns NULL, sets <em>errno</em> to <code>ENOMEM</code>, and leaves the original block of memory unchanged.</p>
<h2 id="return-value">RETURN VALUE</h2>
<p>The <code>malloc</code>() and <code>calloc</code>() functions return a pointer to the allocated memory, which is suitably aligned for any built-in type. On error, these functions return NULL. NULL may also be returned by a successful call to <code>malloc</code>() with a <em>size</em> of zero, or by a successful call to <code>calloc</code>() with <em>nmemb</em> or <em>size</em> equal to zero.</p>
<p>The <code>free</code>() function returns no value.</p>
<p>The <code>realloc</code>() function returns a pointer to the newly allocated memory, which is suitably aligned for any built-in type, or NULL if the request failed. The returned pointer may be the same as <em>ptr</em> if the allocation was not moved (e.g., there was room to expand the allocation in-place), or different from <em>ptr</em> if the allocation was moved to a new address. If <em>size</em> was equal to 0, either NULL or a pointer suitable to be passed to <code>free</code>() is returned. If <code>realloc</code>() fails, the original block is left untouched; it is not freed or moved.</p>
<p>On success, the <code>reallocarray</code>() function returns a pointer to the newly allocated memory. On failure, it returns NULL and the original block of memory is left untouched.</p>
<h2 id="errors">ERRORS</h2>
<p><code>calloc</code>(), <code>malloc</code>(), <code>realloc</code>(), and <code>reallocarray</code>() can fail with the following error:</p>
<dl>
<dt><code>ENOMEM</code></dt>
<dd>Out of memory. Possibly, the application hit the <code>RLIMIT_AS</code> or <code>RLIMIT_DATA</code> limit described in <a href="/docs/linux/man/2-getrlimit/"><code>getrlimit</code></a>(2).</dd>
</dl>
<h2 id="versions">VERSIONS</h2>
<p><code>reallocarray</code>() first appeared in glibc in version 2.26.</p>
<h2 id="attributes">ATTRIBUTES</h2>
<p>For an explanation of the terms used in this section, see <a href="/docs/linux/man/7-attributes/"><code>attributes</code></a>(7).</p>
<table class="man-table">
<tr>
<th>Interface</th>
<th>Attribute</th>
<th>Value</th>
</tr>
<tr>
<td><code>malloc</code>(), <code>free</code>(),<br />
<code>calloc</code>(), <code>realloc</code>()</td>
<td>Thread safety</td>
<td>MT-Safe</td>
</tr>
</table>
<h2 id="conforming-to">CONFORMING TO</h2>
<p><code>malloc</code>(), <code>free</code>(), <code>calloc</code>(), <code>realloc</code>(): POSIX.1-2001, POSIX.1-2008, C89, C99.</p>
<p><code>reallocarray</code>() is a nonstandard extension that first appeared in OpenBSD 5.6 and FreeBSD 11.0.</p>
<h2 id="notes">NOTES</h2>
<p>By default, Linux follows an optimistic memory allocation strategy. This means that when <code>malloc</code>() returns non-NULL there is no guarantee that the memory really is available. In case it turns out that the system is out of memory, one or more processes will be killed by the OOM killer. For more information, see the description of <em>/proc/sys/vm/overcommit_memory</em> and <em>/proc/sys/vm/oom_adj</em> in <a href="/docs/linux/man/5-proc/"><code>proc</code></a>(5), and the Linux kernel source file <em>Documentation/vm/overcommit-accounting.rst</em>.</p>
<p>Normally, <code>malloc</code>() allocates memory from the heap, and adjusts the size of the heap as required, using <a href="/docs/linux/man/2-sbrk/"><code>sbrk</code></a>(2). When allocating blocks of memory larger than <code>MMAP_THRESHOLD</code> bytes, the glibc <code>malloc</code>() implementation allocates the memory as a private anonymous mapping using <a href="/docs/linux/man/2-mmap/"><code>mmap</code></a>(2). <code>MMAP_THRESHOLD</code> is 128 kB by default, but is adjustable using <a href="/docs/linux/man/3-mallopt/"><code>mallopt</code></a>(3). Prior to Linux 4.7 allocations performed using <a href="/docs/linux/man/2-mmap/"><code>mmap</code></a>(2) were unaffected by the <code>RLIMIT_DATA</code> resource limit; since Linux 4.7, this limit is also enforced for allocations performed using <a href="/docs/linux/man/2-mmap/"><code>mmap</code></a>(2).</p>
<p>To avoid corruption in multithreaded applications, mutexes are used internally to protect the memory-management data structures employed by these functions. In a multithreaded application in which threads simultaneously allocate and free memory, there could be contention for these mutexes. To scalably handle memory allocation in multithreaded applications, glibc creates additional <em>memory allocation arenas</em> if mutex contention is detected. Each arena is a large region of memory that is internally allocated by the system (using <a href="/docs/linux/man/2-brk/"><code>brk</code></a>(2) or <a href="/docs/linux/man/2-mmap/"><code>mmap</code></a>(2)), and managed with its own mutexes.</p>
<p>SUSv2 requires <code>malloc</code>(), <code>calloc</code>(), and <code>realloc</code>() to set <em>errno</em> to <code>ENOMEM</code> upon failure. Glibc assumes that this is done (and the glibc versions of these routines do this); if you use a private malloc implementation that does not set <em>errno</em>, then certain library routines may fail without having a reason in <em>errno</em>.</p>
<p>Crashes in <code>malloc</code>(), <code>calloc</code>(), <code>realloc</code>(), or <code>free</code>() are almost always related to heap corruption, such as overflowing an allocated chunk or freeing the same pointer twice.</p>
<p>The <code>malloc</code>() implementation is tunable via environment variables; see <a href="/docs/linux/man/3-mallopt/"><code>mallopt</code></a>(3) for details.</p>
<h2 id="see-also">SEE ALSO</h2>
<p><a href="/docs/linux/man/1-valgrind/"><code>valgrind</code></a>(1), <a href="/docs/linux/man/2-brk/"><code>brk</code></a>(2), <a href="/docs/linux/man/2-mmap/"><code>mmap</code></a>(2), <a href="/docs/linux/man/3-alloca/"><code>alloca</code></a>(3), <a href="/docs/linux/man/3-malloc_get_state/"><code>malloc_get_state</code></a>(3), <a href="/docs/linux/man/3-malloc_info/"><code>malloc_info</code></a>(3), <a href="/docs/linux/man/3-malloc_trim/"><code>malloc_trim</code></a>(3), <a href="/docs/linux/man/3-malloc_usable_size/"><code>malloc_usable_size</code></a>(3), <a href="/docs/linux/man/3-mallopt/"><code>mallopt</code></a>(3), <a href="/docs/linux/man/3-mcheck/"><code>mcheck</code></a>(3), <a href="/docs/linux/man/3-mtrace/"><code>mtrace</code></a>(3), <a href="/docs/linux/man/3-posix_memalign/"><code>posix_memalign</code></a>(3)</p>
<p>For details of the GNU C library implementation, see</p>
<h2 id="colophon">COLOPHON</h2>
<p>This page is part of release 5.10 of the Linux <em>man-pages</em> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/">https://www.kernel.org/doc/man-pages/</a>.</p>
<h2 id="index">Index</h2>
