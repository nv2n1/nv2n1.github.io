---
title: "get_kernel_syms(2)"
name: "get_kernel_syms"
section: "2"
letter: "g"
url: "/docs/linux/man/2-get_kernel_syms/"
description: "get_kernel_syms – retrieve exported kernel and module symbols"
---

<h2 class="name">NAME</h2>
<p> get_kernel_syms &#8211; retrieve exported kernel and module symbols </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/module.h&gt;
int get_kernel_syms(struct kernel_sym *table);
</code></pre>
<p> <i>Note</i>: No declaration of this system call is provided in glibc headers; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <code>Note</code>: This system call is present only in kernels before Linux 2.6. </p>
<p> If <i>table</i> is NULL, <code>get_kernel_syms</code>() returns the number of symbols available for query. Otherwise, it fills in a table of structures: </p>
<p> struct kernel_sym {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long value;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;name[60]; }; </p>
<p> The symbols are interspersed with magic symbols of the form <code>#</code><i>module-name</i> with the kernel having an empty name. The value associated with a symbol of this form is the address at which the module is loaded. </p>
<p> The symbols exported from each module follow their magic module tag and the modules are returned in the reverse of the order in which they were loaded.</p>
<h2>RETURN VALUE</h2>
<p> On success, returns the number of symbols copied to <i>table</i>. On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> There is only one possible error return:</p>
<dl>
<dt><code>ENOSYS</code></p>
<dd> <code>get_kernel_syms</code>() is not supported in this version of the kernel.</dl>
<h2>VERSIONS</h2>
<p> This system call is present on Linux only up until kernel 2.4; it was removed in Linux 2.6.</p>
<h2>CONFORMING TO</h2>
<p> <code>get_kernel_syms</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> This obsolete system call is not supported by glibc. No declaration is provided in glibc headers, but, through a quirk of history, glibc versions before 2.23 did export an ABI for this system call. Therefore, in order to employ this system call, it was sufficient to manually declare the interface in your code; alternatively, you could invoke the system call using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).</p>
<h2>BUGS</h2>
<p> There is no way to indicate the size of the buffer allocated for <i>table</i>. If symbols have been added to the kernel since the program queried for the symbol table size, memory will be corrupted. </p>
<p> The length of exported symbol names is limited to 59 characters. </p>
<p> Because of these limitations, this system call is deprecated in favor of <code><a href="/docs/linux/man/2-query_module/">query_module</a></code>(2) (which is itself nowadays deprecated in favor of other interfaces described on its manual page).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-create_module/">create_module</a></code>(2), <code><a href="/docs/linux/man/2-delete_module/">delete_module</a></code>(2), <code><a href="/docs/linux/man/2-init_module/">init_module</a></code>(2), <code><a href="/docs/linux/man/2-query_module/">query_module</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
