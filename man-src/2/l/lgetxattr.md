---
title: "lgetxattr(2)"
name: "lgetxattr"
section: "2"
letter: "l"
url: "/docs/linux/man/2-lgetxattr/"
description: "getxattr, lgetxattr, fgetxattr – retrieve an extended attribute value"
---

<h2 class="name">NAME</h2>
<p> getxattr, lgetxattr, fgetxattr &#8211; retrieve an extended attribute value </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/types.h&gt;
#include &lt;sys/xattr.h&gt;
ssize_t getxattr(const char &amp;nbsp; *path, const char &amp;nbsp; *name,
                                                            void &amp;nbsp;
                 *value, size_t size);
ssize_t lgetxattr(const char &amp;nbsp; *path, const char &amp;nbsp; *name,
                                                             void &amp;nbsp;
                  *value, size_t size);
ssize_t fgetxattr(int fd, const char &amp;nbsp; *name,
                                            void &amp;nbsp;
                  *value, size_t size);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Extended attributes are <i>name</i>:<i>value</i> pairs associated with inodes (files, directories, symbolic links, etc.). They are extensions to the normal attributes which are associated with all inodes in the system (i.e., the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) data). A complete overview of extended attributes concepts can be found in <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7). </p>
<p> <code>getxattr</code>() retrieves the value of the extended attribute identified by <i>name</i> and associated with the given <i>path</i> in the filesystem. The attribute value is placed in the buffer pointed to by <i>value</i>; <i>size</i> specifies the size of that buffer. The return value of the call is the number of bytes placed in <i>value</i>. </p>
<p> <code>lgetxattr</code>() is identical to <code>getxattr</code>(), except in the case of a symbolic link, where the link itself is interrogated, not the file that it refers to. </p>
<p> <code>fgetxattr</code>() is identical to <code>getxattr</code>(), only the open file referred to by <i>fd</i> (as returned by <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) is interrogated in place of <i>path</i>. </p>
<p> An extended attribute <i>name</i> is a null-terminated string. The name includes a namespace prefix; there may be several, disjoint namespaces associated with an individual inode. The value of an extended attribute is a chunk of arbitrary textual or binary data that was assigned using <code><a href="/docs/linux/man/2-setxattr/">setxattr</a></code>(2). </p>
<p> If <i>size</i> is specified as zero, these calls return the current size of the named extended attribute (and leave <i>value</i> unchanged). This can be used to determine the size of the buffer that should be supplied in a subsequent call. (But, bear in mind that there is a possibility that the attribute value may change between the two calls, so that it is still necessary to check the return status from the second call.)</p>
<h2>RETURN VALUE</h2>
<p> On success, these calls return a nonnegative value which is the size (in bytes) of the extended attribute value. On failure, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>E2BIG</code></p>
<dd> The size of the attribute value is larger than the maximum size allowed; the attribute cannot be retrieved. This can happen on filesystems that support very large attribute values such as NFSv4, for example.</p>
<dt><code>ENODATA</code></p>
<dd> The named attribute does not exist, or the process has no access to this attribute.</p>
<dt><code>ENOTSUP</code></p>
<dd> Extended attributes are not supported by the filesystem, or are disabled.</p>
<dt><code>ERANGE</code></p>
<dd> The <i>size</i> of the <i>value</i> buffer is too small to hold the result.</dl>
<p> In addition, the errors documented in <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) can also occur.</p>
<h2>VERSIONS</h2>
<p> These system calls have been available on Linux since kernel 2.4; glibc support is provided since version 2.3.</p>
<h2>CONFORMING TO</h2>
<p> These system calls are Linux-specific.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/2-listxattr/">listxattr</a></code>(2).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-getfattr/">getfattr</a></code>(1), <code><a href="/docs/linux/man/1-setfattr/">setfattr</a></code>(1), <code><a href="/docs/linux/man/2-listxattr/">listxattr</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-removexattr/">removexattr</a></code>(2), <code><a href="/docs/linux/man/2-setxattr/">setxattr</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7), <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
