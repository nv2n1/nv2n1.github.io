---
title: "memalign(3)"
name: "memalign"
section: "3"
letter: "m"
url: "/docs/linux/man/3-memalign/"
description: "posix_memalign, aligned_alloc, memalign, valloc, pvalloc – allocate aligned memory"
---

<h2 class="name">NAME</h2>
<p> posix_memalign, aligned_alloc, memalign, valloc, pvalloc &#8211; allocate aligned memory </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;stdlib.h&gt;
int posix_memalign(void **memptr, size_t alignment, size_t size);
void *aligned_alloc(size_t alignment, size_t size);
void *valloc(size_t size);
#include &lt;malloc.h&gt;
void *memalign(size_t alignment, size_t size);
void *pvalloc(size_t size);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>posix_memalign</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L </p>
<p> <code>aligned_alloc</code>(): _ISOC11_SOURCE </p>
<p> <code>valloc</code>(): </p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.12:</p>
<dd>
<pre><code>
(_XOPEN_SOURCE &amp;nbsp; &gt;= &amp;nbsp; 500) &amp;&amp; !(_POSIX_C_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 200112L) || /* Glibc since 2.19: */ _DEFAULT_SOURCE
    || /* Glibc versions &lt;= 2.19: */ _SVID_SOURCE || _BSD_SOURCE
</code></pre>
<dt>Before glibc 2.12:</p>
<dd> _BSD_SOURCE || _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500<br />
 (The (nonstandard) header file <i>&lt;malloc.h&gt;</i> also exposes the declaration of <code>valloc</code>(); no feature test macros are required.)</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> The function <code>posix_memalign</code>() allocates <i>size</i> bytes and places the address of the allocated memory in <i>*memptr</i>. The address of the allocated memory will be a multiple of <i>alignment</i>, which must be a power of two and a multiple of <i>sizeof(void&nbsp;*)</i>. This address can later be successfully passed to <code><a href="/docs/linux/man/3-free/">free</a></code>(3). If <i>size</i> is 0, then the value placed in <i>*memptr</i> is either NULL or a unique pointer value. </p>
<p> The obsolete function <code>memalign</code>() allocates <i>size</i> bytes and returns a pointer to the allocated memory. The memory address will be a multiple of <i>alignment</i>, which must be a power of two. </p>
<p> The function <code>aligned_alloc</code>() is the same as <code>memalign</code>(), except for the added restriction that <i>size</i> should be a multiple of <i>alignment</i>. </p>
<p> The obsolete function <code>valloc</code>() allocates <i>size</i> bytes and returns a pointer to the allocated memory. The memory address will be a multiple of the page size. It is equivalent to <i>memalign(sysconf(_SC_PAGESIZE),size)</i>. </p>
<p> The obsolete function <code>pvalloc</code>() is similar to <code>valloc</code>(), but rounds the size of the allocation up to the next multiple of the system page size. </p>
<p> For all of these functions, the memory is not zeroed.</p>
<h2>RETURN VALUE</h2>
<p> <code>aligned_alloc</code>(), <code>memalign</code>(), <code>valloc</code>(), and <code>pvalloc</code>() return a pointer to the allocated memory on success. On error, NULL is returned, and <i>errno</i> is set to indicate the cause of the error. </p>
<p> <code>posix_memalign</code>() returns zero on success, or one of the error values listed in the next section on failure. The value of <i>errno</i> is not set. On Linux (and other systems), <code>posix_memalign</code>() does not modify <i>memptr</i> on failure. A requirement standardizing this behavior was added in POSIX.1-2008 TC2.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> The <i>alignment</i> argument was not a power of two, or was not a multiple of <i>sizeof(void&nbsp;*)</i>.</p>
<dt><code>ENOMEM</code></p>
<dd> There was insufficient memory to fulfill the allocation request.</dl>
<h2>VERSIONS</h2>
<p> The functions <code>memalign</code>(), <code>valloc</code>(), and <code>pvalloc</code>() have been available since at least glibc 2.0. </p>
<p> The function <code>aligned_alloc</code>() was added to glibc in version 2.16. </p>
<p> The function <code>posix_memalign</code>() is available since glibc 2.1.91.</p>
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
<td> <code>aligned_alloc</code>(),<br />
 <code>memalign</code>(),<br />
 <code>posix_memalign</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>valloc</code>(),<br />
 <code>pvalloc</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe init
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> The function <code>valloc</code>() appeared in 3.0BSD. It is documented as being obsolete in 4.3BSD, and as legacy in SUSv2. It does not appear in POSIX.1. </p>
<p> The function <code>pvalloc</code>() is a GNU extension. </p>
<p> The function <code>memalign</code>() appears in SunOS 4.1.3 but not in 4.4BSD. </p>
<p> The function <code>posix_memalign</code>() comes from POSIX.1d and is specified in POSIX.1-2001 and POSIX.1-2008. </p>
<p> The function <code>aligned_alloc</code>() is specified in the C11 standard.</p>
<h3>Headers</h3>
<p> Everybody agrees that <code>posix_memalign</code>() is declared in <i>&lt;stdlib.h&gt;</i>. </p>
<p> On some systems <code>memalign</code>() is declared in <i>&lt;stdlib.h&gt;</i> instead of <i>&lt;malloc.h&gt;</i>. </p>
<p> According to SUSv2, <code>valloc</code>() is declared in <i>&lt;stdlib.h&gt;</i>. Glibc declares it in <i>&lt;malloc.h&gt;</i>, and also in <i>&lt;stdlib.h&gt;</i> if suitable feature test macros are defined (see above).</p>
<h2>NOTES</h2>
<p> On many systems there are alignment restrictions, for example, on buffers used for direct block device I/O. POSIX specifies the <i>pathconf(path,_PC_REC_XFER_ALIGN)</i> call that tells what alignment is needed. Now one can use <code>posix_memalign</code>() to satisfy this requirement. </p>
<p> <code>posix_memalign</code>() verifies that <i>alignment</i> matches the requirements detailed above. <code>memalign</code>() may not check that the <i>alignment</i> argument is correct. </p>
<p> POSIX requires that memory obtained from <code>posix_memalign</code>() can be freed using <code><a href="/docs/linux/man/3-free/">free</a></code>(3). Some systems provide no way to reclaim memory allocated with <code>memalign</code>() or <code>valloc</code>() (because one can pass to <code><a href="/docs/linux/man/3-free/">free</a></code>(3) only a pointer obtained from <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), while, for example, <code>memalign</code>() would call <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) and then align the obtained value). The glibc implementation allows memory obtained from any of these functions to be reclaimed with <code><a href="/docs/linux/man/3-free/">free</a></code>(3). </p>
<p> The glibc <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) always returns 8-byte aligned memory addresses, so these functions are needed only if you require larger alignment values.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-brk/">brk</a></code>(2), <code><a href="/docs/linux/man/2-getpagesize/">getpagesize</a></code>(2), <code><a href="/docs/linux/man/3-free/">free</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
