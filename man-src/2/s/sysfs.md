---
title: "sysfs(2)"
name: "sysfs"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sysfs/"
description: "sysfs – get filesystem type information"
---

<h2 class="name">NAME</h2>
<p> sysfs &#8211; get filesystem type information </p>
<h2>SYNOPSIS</h2>
<p> <code>int sysfs(int </code><i>option</i><code>, const char *</code><i>fsname</i><code>);</code> </p>
<p> <code>int sysfs(int </code><i>option</i><code>, unsigned int </code><i>fs_index</i><code>, char *</code><i>buf</i><code>);</code> </p>
<p> <code>int sysfs(int </code><i>option</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>Note</code>: if you are looking for information about the <code>sysfs</code> filesystem that is normally mounted at <i>/sys</i>, see <code><a href="/docs/linux/man/5-sysfs/">sysfs</a></code>(5). </p>
<p> The (obsolete) <code>sysfs</code>() system call returns information about the filesystem types currently present in the kernel. The specific form of the <code>sysfs</code>() call and the information returned depends on the <i>option</i> in effect:</p>
<dl>
<dt><code>1</code></p>
<dd> Translate the filesystem identifier string <i>fsname</i> into a filesystem type index.</p>
<dt><code>2</code></p>
<dd> Translate the filesystem type index <i>fs_index</i> into a null-terminated filesystem identifier string. This string will be written to the buffer pointed to by <i>buf</i>. Make sure that <i>buf</i> has enough space to accept the string.</p>
<dt><code>3</code></p>
<dd> Return the total number of filesystem types currently present in the kernel.</dl>
<p> The numbering of the filesystem type indexes begins with zero.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>sysfs</code>() returns the filesystem index for option <code>1</code>, zero for option <code>2</code>, and the number of currently configured filesystems for option <code>3</code>. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> Either <i>fsname</i> or <i>buf</i> is outside your accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>fsname</i> is not a valid filesystem type identifier; <i>fs_index</i> is out-of-bounds; <i>option</i> is invalid.</dl>
<h2>CONFORMING TO</h2>
<p> SVr4.</p>
<h2>NOTES</h2>
<p> This System-V derived system call is obsolete; don&#8217;t use it. On systems with <i>/proc</i>, the same information can be obtained via <i>/proc</i>; use that interface instead.</p>
<h2>BUGS</h2>
<p> There is no libc or glibc support. There is no way to guess how large <i>buf</i> should be.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5), <code><a href="/docs/linux/man/5-sysfs/">sysfs</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
