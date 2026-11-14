---
title: "pkey_alloc(2)"
name: "pkey_alloc"
section: "2"
letter: "p"
url: "/docs/linux/man/2-pkey_alloc/"
description: "pkey_alloc, pkey_free – allocate or free a protection key"
---

<h2 class="name">NAME</h2>
<p> pkey_alloc, pkey_free &#8211; allocate or free a protection key </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;sys/mman.h&gt;
int pkey_alloc(unsigned int flags, unsigned int access_rights);
int pkey_free(int pkey);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>pkey_alloc</code>() allocates a protection key (pkey) and allows it to be passed to <code><a href="/docs/linux/man/2-pkey_mprotect/">pkey_mprotect</a></code>(2). </p>
<p> The <code>pkey_alloc</code>() <i>flags</i> is reserved for future use and currently must always be specified as 0. </p>
<p> The <code>pkey_alloc</code>() <i>access_rights</i> argument may contain zero or more disable operations:</p>
<dl>
<dt><code>PKEY_DISABLE_ACCESS</code></p>
<dd> Disable all data access to memory covered by the returned protection key.</p>
<dt><code>PKEY_DISABLE_WRITE</code></p>
<dd> Disable write access to memory covered by the returned protection key.</dl>
<p> <code>pkey_free</code>() frees a protection key and makes it available for later allocations. After a protection key has been freed, it may no longer be used in any protection-key-related operations. </p>
<p> An application should not call <code>pkey_free</code>() on any protection key which has been assigned to an address range by <code><a href="/docs/linux/man/2-pkey_mprotect/">pkey_mprotect</a></code>(2) and which is still in use. The behavior in this case is undefined and may result in an error.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>pkey_alloc</code>() returns a positive protection key value. On success, <code>pkey_free</code>() returns zero. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>pkey</i>, <i>flags</i>, or <i>access_rights</i> is invalid.</p>
<dt><code>ENOSPC</code></p>
<dd> (<code>pkey_alloc</code>()) All protection keys available for the current process have been allocated. The number of keys available is architecture-specific and implementation-specific and may be reduced by kernel-internal use of certain keys. There are currently 15 keys available to user programs on x86.</p>
<dt>
<dd> This error will also be returned if the processor or operating system does not support protection keys. Applications should always be prepared to handle this error, since factors outside of the application&#8217;s control can reduce the number of available pkeys.</dl>
<h2>VERSIONS</h2>
<p> <code>pkey_alloc</code>() and <code>pkey_free</code>() were added to Linux in kernel 4.9; library support was added in glibc 2.27.</p>
<h2>CONFORMING TO</h2>
<p> The <code>pkey_alloc</code>() and <code>pkey_free</code>() system calls are Linux-specific.</p>
<h2>NOTES</h2>
<p> <code>pkey_alloc</code>() is always safe to call regardless of whether or not the operating system supports protection keys. It can be used in lieu of any other mechanism for detecting pkey support and will simply fail with the error <code>ENOSPC</code> if the operating system has no pkey support. </p>
<p> The kernel guarantees that the contents of the hardware rights register (PKRU) will be preserved only for allocated protection keys. Any time a key is unallocated (either before the first call returning that key from <code>pkey_alloc</code>() or after it is freed via <code>pkey_free</code>()), the kernel may make arbitrary changes to the parts of the rights register affecting access to that key.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/7-pkeys/">pkeys</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-pkey_mprotect/">pkey_mprotect</a></code>(2), <code><a href="/docs/linux/man/7-pkeys/">pkeys</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
