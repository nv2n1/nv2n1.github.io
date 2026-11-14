---
title: "llseek(2)"
name: "llseek"
section: "2"
letter: "l"
url: "/docs/linux/man/2-llseek/"
description: "_llseek – reposition read/write file offset"
---

<h2 class="name">NAME</h2>
<p> _llseek &#8211; reposition read/write file offset </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
int _llseek(unsigned int fd, unsigned long offset_high,
            unsigned long offset_low, loff_t *result,
            unsigned int whence);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> Note: for information about the <code><a href="/docs/linux/man/3-llseek/">llseek</a></code>(3) library function, see <code><a href="/docs/linux/man/3-lseek64/">lseek64</a></code>(3). </p>
<p> The <code>_llseek</code>() system call repositions the offset of the open file description associated with the file descriptor <i>fd</i> to the value</p>
<dl>
<dt>
<dd> (offset_high &lt;&lt; 32) | offset_low</dl>
<p> This new offset is a byte offset relative to the beginning of the file, the current file offset, or the end of the file, depending on whether <i>whence</i> is <code>SEEK_SET</code>, <code>SEEK_CUR</code>, or <code>SEEK_END</code>, respectively. </p>
<p> The new file offset is returned in the argument <i>result</i>. The type <i>loff_t</i> is a 64-bit signed type. </p>
<p> This system call exists on various 32-bit platforms to support seeking to large file offsets.</p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>_llseek</code>() returns 0. Otherwise, a value of -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not an open file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> Problem with copying results to user space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>whence</i> is invalid.</dl>
<h2>CONFORMING TO</h2>
<p> This function is Linux-specific, and should not be used in programs intended to be portable.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call. To invoke it directly, use <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). However, you probably want to use the <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) wrapper function instead.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/3-lseek64/">lseek64</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
