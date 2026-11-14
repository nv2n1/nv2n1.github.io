---
title: "query_module(2)"
name: "query_module"
section: "2"
letter: "q"
url: "/docs/linux/man/2-query_module/"
description: "query_module – query the kernel for various bits pertaining to modules"
---

<h2 class="name">NAME</h2>
<p> query_module &#8211; query the kernel for various bits pertaining to modules </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/module.h&gt;
int query_module(const char *name, int which, void *buf,
                 size_t bufsize, size_t *ret);
</code></pre>
<p> <i>Note</i>: No declaration of this system call is provided in glibc headers; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <i>Note</i>: This system call is present only in kernels before Linux 2.6. </p>
<p> <code>query_module</code>() requests information from the kernel about loadable modules. The returned information is placed in the buffer pointed to by <i>buf</i>. The caller must specify the size of <i>buf</i> in <i>bufsize</i>. The precise nature and format of the returned information depend on the operation specified by <i>which</i>. Some operations require <i>name</i> to identify a currently loaded module, some allow <i>name</i> to be NULL, indicating the kernel proper. </p>
<p> The following values can be specified for <i>which</i>:</p>
<dl>
<dt><code>0</code></p>
<dd> Returns success, if the kernel supports <code>query_module</code>(). Used to probe for availability of the system call.</p>
<dt><code>QM_MODULES</code></p>
<dd> Returns the names of all loaded modules. The returned buffer consists of a sequence of null-terminated strings; <i>ret</i> is set to the number of modules.</p>
<dt><code>QM_DEPS</code></p>
<dd> Returns the names of all modules used by the indicated module. The returned buffer consists of a sequence of null-terminated strings; <i>ret</i> is set to the number of modules.</p>
<dt><code>QM_REFS</code></p>
<dd> Returns the names of all modules using the indicated module. This is the inverse of <code>QM_DEPS</code>. The returned buffer consists of a sequence of null-terminated strings; <i>ret</i> is set to the number of modules.</p>
<dt><code>QM_SYMBOLS</code></p>
<dd> Returns the symbols and values exported by the kernel or the indicated module. The returned buffer is an array of structures of the following form</p>
<dt>
<dd> struct module_symbol {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long value;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long name; };</p>
<dt>
<dd> followed by null-terminated strings. The value of <i>name</i> is the character offset of the string relative to the start of <i>buf</i>; <i>ret</i> is set to the number of symbols.</p>
<dt><code>QM_INFO</code></p>
<dd> Returns miscellaneous information about the indicated module. The output buffer format is:</p>
<dt>
<dd> struct module_info {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long address;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long flags; };</p>
<dt>
<dd> where <i>address</i> is the kernel address at which the module resides, <i>size</i> is the size of the module in bytes, and <i>flags</i> is a mask of <code>MOD_RUNNING</code>, <code>MOD_AUTOCLEAN</code>, and so on, that indicates the current status of the module (see the Linux kernel source file <i>include/linux/module.h</i>). <i>ret</i> is set to the size of the <i>module_info</i> structure.</dl>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> At least one of <i>name</i>, <i>buf</i>, or <i>ret</i> was outside the program&#8217;s accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid <i>which</i>; or <i>name</i> is NULL (indicating &quot;the kernel&quot;), but this is not permitted with the specified value of <i>which</i>.</p>
<dt><code>ENOENT</code></p>
<dd> No module by that <i>name</i> exists.</p>
<dt><code>ENOSPC</code></p>
<dd> The buffer size provided was too small. <i>ret</i> is set to the minimum size needed.</p>
<dt><code>ENOSYS</code></p>
<dd> <code>query_module</code>() is not supported in this version of the kernel (e.g., the kernel is version 2.6 or later).</dl>
<h2>VERSIONS</h2>
<p> This system call is present on Linux only up until kernel 2.4; it was removed in Linux 2.6.</p>
<h2>CONFORMING TO</h2>
<p> <code>query_module</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> Some of the information that was formerly available via <code>query_module</code>() can be obtained from <i>/proc/modules</i>, <i>/proc/kallsyms</i>, and the files under the directory <i>/sys/module</i>. </p>
<p> The <code>query_module</code>() system call is not supported by glibc. No declaration is provided in glibc headers, but, through a quirk of history, glibc does export an ABI for this system call. Therefore, in order to employ this system call, it is sufficient to manually declare the interface in your code; alternatively, you can invoke the system call using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-create_module/">create_module</a></code>(2), <code><a href="/docs/linux/man/2-delete_module/">delete_module</a></code>(2), <code><a href="/docs/linux/man/2-get_kernel_syms/">get_kernel_syms</a></code>(2), <code><a href="/docs/linux/man/2-init_module/">init_module</a></code>(2), <code><a href="/docs/linux/man/8-lsmod/">lsmod</a></code>(8), <code><a href="/docs/linux/man/8-modinfo/">modinfo</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
