---
title: "lsetxattr(2)"
name: "lsetxattr"
section: "2"
letter: "l"
url: "/docs/linux/man/2-lsetxattr/"
description: "setxattr, lsetxattr, fsetxattr – set an extended attribute value"
---

<h2 class="name">NAME</h2>
<p> setxattr, lsetxattr, fsetxattr &#8211; set an extended attribute value </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/types.h&gt;
#include &lt;sys/xattr.h&gt;
int setxattr(const char &amp;nbsp; *path, const char &amp;nbsp; *name,
                                                        const void &amp;nbsp;
             *value, size_t size, int flags);
int lsetxattr(const char &amp;nbsp; *path, const char &amp;nbsp; *name,
                                                         const void &amp;nbsp;
              *value, size_t size, int flags);
int fsetxattr(int fd, const char &amp;nbsp; *name,
                                        const void &amp;nbsp;
              *value, size_t size, int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Extended attributes are <i>name</i>:<i>value</i> pairs associated with inodes (files, directories, symbolic links, etc.). They are extensions to the normal attributes which are associated with all inodes in the system (i.e., the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) data). A complete overview of extended attributes concepts can be found in <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7). </p>
<p> <code>setxattr</code>() sets the <i>value</i> of the extended attribute identified by <i>name</i> and associated with the given <i>path</i> in the filesystem. The <i>size</i> argument specifies the size (in bytes) of <i>value</i>; a zero-length value is permitted. </p>
<p> <code>lsetxattr</code>() is identical to <code>setxattr</code>(), except in the case of a symbolic link, where the extended attribute is set on the link itself, not the file that it refers to. </p>
<p> <code>fsetxattr</code>() is identical to <code>setxattr</code>(), only the extended attribute is set on the open file referred to by <i>fd</i> (as returned by <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) in place of <i>path</i>. </p>
<p> An extended attribute name is a null-terminated string. The <i>name</i> includes a namespace prefix; there may be several, disjoint namespaces associated with an individual inode. The <i>value</i> of an extended attribute is a chunk of arbitrary textual or binary data of specified length. </p>
<p> By default (i.e., <i>flags</i> is zero), the extended attribute will be created if it does not exist, or the value will be replaced if the attribute already exists. To modify these semantics, one of the following values can be specified in <i>flags</i>:</p>
<dl>
<dt><code>XATTR_CREATE</code></p>
<dd> Perform a pure create, which fails if the named attribute exists already.</p>
<dt><code>XATTR_REPLACE</code></p>
<dd> Perform a pure replace operation, which fails if the named attribute does not already exist.</dl>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On failure, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EDQUOT</code></p>
<dd> Disk quota limits meant that there is insufficient space remaining to store the extended attribute.</p>
<dt><code>EEXIST</code></p>
<dd> <code>XATTR_CREATE</code> was specified, and the attribute exists already.</p>
<dt><code>ENODATA</code></p>
<dd> <code>XATTR_REPLACE</code> was specified, and the attribute does not exist.</p>
<dt><code>ENOSPC</code></p>
<dd> There is insufficient space remaining to store the extended attribute.</p>
<dt><code>ENOTSUP</code></p>
<dd> The namespace prefix of <i>name</i> is not valid.</p>
<dt><code>ENOTSUP</code></p>
<dd> Extended attributes are not supported by the filesystem, or are disabled,</p>
<dt><code>EPERM</code></p>
<dd> The file is marked immutable or append-only. (See <code><a href="/docs/linux/man/2-ioctl_iflags/">ioctl_iflags</a></code>(2).)</dl>
<p> In addition, the errors documented in <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) can also occur.</p>
<dl>
<dt><code>ERANGE</code></p>
<dd> The size of <i>name</i> or <i>value</i> exceeds a filesystem-specific limit.</dl>
<h2>VERSIONS</h2>
<p> These system calls have been available on Linux since kernel 2.4; glibc support is provided since version 2.3.</p>
<h2>CONFORMING TO</h2>
<p> These system calls are Linux-specific.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-getfattr/">getfattr</a></code>(1), <code><a href="/docs/linux/man/1-setfattr/">setfattr</a></code>(1), <code><a href="/docs/linux/man/2-getxattr/">getxattr</a></code>(2), <code><a href="/docs/linux/man/2-listxattr/">listxattr</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-removexattr/">removexattr</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7), <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
