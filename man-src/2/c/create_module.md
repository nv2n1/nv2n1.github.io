---
title: "create_module(2)"
name: "create_module"
section: "2"
letter: "c"
url: "/docs/linux/man/2-create_module/"
description: "create_module – create a loadable module entry"
---

<h2 class="name">NAME</h2>
<p> create_module &#8211; create a loadable module entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/module.h&gt;
caddr_t create_module(const char *name, size_t size);
</code></pre>
<p> <i>Note</i>: No declaration of this system call is provided in glibc headers; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <i>Note</i>: This system call is present only in kernels before Linux 2.6. </p>
<p> <code>create_module</code>() attempts to create a loadable module entry and reserve the kernel memory that will be needed to hold the module. This system call requires privilege.</p>
<h2>RETURN VALUE</h2>
<p> On success, returns the kernel address at which the module will reside. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EEXIST</code></p>
<dd> A module by that name already exists.</p>
<dt><code>EFAULT</code></p>
<dd> <i>name</i> is outside the program&#8217;s accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> The requested size is too small even for the module header information.</p>
<dt><code>ENOMEM</code></p>
<dd> The kernel could not allocate a contiguous block of memory large enough for the module.</p>
<dt><code>ENOSYS</code></p>
<dd> <code>create_module</code>() is not supported in this version of the kernel (e.g., the kernel is version 2.6 or later).</p>
<dt><code>EPERM</code></p>
<dd> The caller was not privileged (did not have the <code>CAP_SYS_MODULE</code> capability).</dl>
<h2>VERSIONS</h2>
<p> This system call is present on Linux only up until kernel 2.4; it was removed in Linux 2.6.</p>
<h2>CONFORMING TO</h2>
<p> <code>create_module</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> This obsolete system call is not supported by glibc. No declaration is provided in glibc headers, but, through a quirk of history, glibc versions before 2.23 did export an ABI for this system call. Therefore, in order to employ this system call, it was sufficient to manually declare the interface in your code; alternatively, you could invoke the system call using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-delete_module/">delete_module</a></code>(2), <code><a href="/docs/linux/man/2-init_module/">init_module</a></code>(2), <code><a href="/docs/linux/man/2-query_module/">query_module</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
