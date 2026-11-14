---
title: "removexattr(2)"
name: "removexattr"
section: "2"
letter: "r"
url: "/docs/linux/man/2-removexattr/"
description: "removexattr, lremovexattr, fremovexattr – remove an extended attribute"
---

<h2 class="name">NAME</h2>
<p> removexattr, lremovexattr, fremovexattr &#8211; remove an extended attribute </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/types.h&gt;
#include &lt;sys/xattr.h&gt;
int removexattr(const char &amp;nbsp; *path, const char &amp;nbsp; *name);
int lremovexattr(const char &amp;nbsp; *path, const char &amp;nbsp; *name);
int fremovexattr(int fd, const char &amp;nbsp; *name);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Extended attributes are <i>name</i>:<i>value</i> pairs associated with inodes (files, directories, symbolic links, etc.). They are extensions to the normal attributes which are associated with all inodes in the system (i.e., the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) data). A complete overview of extended attributes concepts can be found in <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7). </p>
<p> <code>removexattr</code>() removes the extended attribute identified by <i>name</i> and associated with the given <i>path</i> in the filesystem. </p>
<p> <code>lremovexattr</code>() is identical to <code>removexattr</code>(), except in the case of a symbolic link, where the extended attribute is removed from the link itself, not the file that it refers to. </p>
<p> <code>fremovexattr</code>() is identical to <code>removexattr</code>(), only the extended attribute is removed from the open file referred to by <i>fd</i> (as returned by <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) in place of <i>path</i>. </p>
<p> An extended attribute name is a null-terminated string. The <i>name</i> includes a namespace prefix; there may be several, disjoint namespaces associated with an individual inode.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On failure, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENODATA</code></p>
<dd> The named attribute does not exist.</p>
<dt><code>ENOTSUP</code></p>
<dd> Extended attributes are not supported by the filesystem, or are disabled.</dl>
<p> In addition, the errors documented in <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) can also occur.</p>
<h2>VERSIONS</h2>
<p> These system calls have been available on Linux since kernel 2.4; glibc support is provided since version 2.3.</p>
<h2>CONFORMING TO</h2>
<p> These system calls are Linux-specific.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-getfattr/">getfattr</a></code>(1), <code><a href="/docs/linux/man/1-setfattr/">setfattr</a></code>(1), <code><a href="/docs/linux/man/2-getxattr/">getxattr</a></code>(2), <code><a href="/docs/linux/man/2-listxattr/">listxattr</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-setxattr/">setxattr</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7), <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
