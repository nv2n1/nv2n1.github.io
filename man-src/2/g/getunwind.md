---
title: "getunwind(2)"
name: "getunwind"
section: "2"
letter: "g"
url: "/docs/linux/man/2-getunwind/"
description: "getunwind – copy the unwind data to caller’s buffer"
---

<h2 class="name">NAME</h2>
<p> getunwind &#8211; copy the unwind data to caller&#8217;s buffer </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;linux/unwind.h&gt;
#include &lt;syscall.h&gt;
long getunwind(void *buf, size_t buf_size);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <i>Note: this function is obsolete.</i> </p>
<p> The IA-64-specific <code>getunwind</code>() system call copies the kernel&#8217;s call frame unwind data into the buffer pointed to by <i>buf</i> and returns the size of the unwind data; this data describes the gate page (kernel code that is mapped into user space). </p>
<p> The size of the buffer <i>buf</i> is specified in <i>buf_size</i>. The data is copied only if <i>buf_size</i> is greater than or equal to the size of the unwind data and <i>buf</i> is not NULL; otherwise, no data is copied, and the call succeeds, returning the size that would be needed to store the unwind data. </p>
<p> The first part of the unwind data contains an unwind table. The rest contains the associated unwind information, in no particular order. The unwind table contains entries of the following form: </p>
<p> u64 start; (64-bit address of start of function) u64 end; (64-bit address of end of function) u64 info; (BUF-relative offset to unwind info) </p>
<p> An entry whose <i>start</i> value is zero indicates the end of the table. For more information about the format, see the <i>IA-64 Software Conventions and Runtime Architecture</i> manual.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>getunwind</code>() returns the size of the unwind data. On error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> <code>getunwind</code>() fails with the error <code>EFAULT</code> if the unwind info can&#8217;t be stored in the space specified by <i>buf</i>.</p>
<h2>VERSIONS</h2>
<p> This system call is available since Linux 2.4.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific, and is available only on the IA-64 architecture.</p>
<h2>NOTES</h2>
<p> This system call has been deprecated. The modern way to obtain the kernel&#8217;s unwind data is via the <code><a href="/docs/linux/man/7-vdso/">vdso</a></code>(7). </p>
<p> Glibc does not provide a wrapper for this system call; in the unlikely event that you want to call it, use <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-getauxval/">getauxval</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
