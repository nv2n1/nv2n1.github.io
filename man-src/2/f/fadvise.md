---
title: "fadvise(2)"
name: "fadvise"
section: "2"
letter: "f"
url: "/docs/linux/man/2-fadvise/"
description: "fadvise64,fadvise64_64 – Give advice about file access"
---

<h2>NAME</h2>
<p> fadvise64,fadvise64_64 &#8211; Give advice about file access</p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>long&nbsp;<wbr><code>fadvise64_64</code> (int&nbsp;<wbr><i>fs</i>, loff_t&nbsp;<wbr><i>offset</i>, loff_t&nbsp;<wbr><i>len</i>, int&nbsp;<wbr><i>advice</i>, int&nbsp;<wbr><i>fs</i>, loff_t&nbsp;<wbr><i>offset</i>, loff_t&nbsp;<wbr><i>len</i>, int&nbsp;<wbr><i>advice</i>);</p>
<dt>
<dd>long&nbsp;<wbr><code>sys_fadvise64</code>&nbsp;<wbr> (int&nbsp;<wbr><i>fs</i>, loff_t&nbsp;<wbr><i>offset</i>, loff_t&nbsp;<wbr><i>len</i>, int&nbsp;<wbr><i>advice</i>, int&nbsp;<wbr><i>fs</i>, loff_t&nbsp;<wbr><i>offset</i>, loff_t&nbsp;<wbr><i>len</i>, int&nbsp;<wbr><i>advice</i>); </p>
</dl>
<h2>DESCRIPTION</h2>
<p> Allows an application to to tell the kernel how it expects to use a file handle, so that the kernel can choose appropriate read-ahead and caching techniques for access to the corresponding file. This is similar to the POSIX version of the <code>madvise</code> system call, but for file access instead of memory access. The sys_fadvise64() function is obsolete and corresponds to a broken glibc API, sys_fadvise64_64() is the fixed version. The following are the values for the <i>advice</i> parameter: </p>
<dl>
<dt>FADV_NORMAL</p>
<dd> No special treatment. </p>
<dt>FADV_RANDOM</p>
<dd> Expect page references in random order. </p>
<dt>FADV_SEQUENTIAL</p>
<dd> Expect page references in sequential order. </p>
<dt>FADV_WILLNEED</p>
<dd> Expect access in the near future. </p>
<dt>FADV_DONTNEED</p>
<dd> Do not expect access in the near future. Subsequent access of pages in this range will succeed, but will result either in reloading of the memory contents from the underlying mapped file or zero-fill-in-demand pages for mappings without an underlying file. </p>
<dt>FADV_NOREUSE</p>
<dd> Access data only once. </p>
</dl>
<h2>ERRORS</h2>
<dl>
<dt>-EBADF</p>
<dd> An invalid file descriptor was specified. to modify the modules. </p>
<dt>-EINVAL</p>
<dd> An invalid <i>f_mapping</i> of <i>file</i>, <i>len</i> value smaller than 0 or <i>advice</i> value unknown. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-madvise/">madvise</a>(2)</code> </p>
<h2>AUTHOR</h2>
<p> Niki Rahimi </p>
<h2>Index</h2>
