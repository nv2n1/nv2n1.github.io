---
title: "flistxattr(2)"
name: "flistxattr"
section: "2"
letter: "f"
url: "/docs/linux/man/2-flistxattr/"
description: "listxattr, llistxattr, flistxattr – list extended attribute names"
---

<h2 class="name">NAME</h2>
<p> listxattr, llistxattr, flistxattr &#8211; list extended attribute names </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/types.h&gt;
#include &lt;sys/xattr.h&gt;
ssize_t listxattr(const char &amp;nbsp; *path, char &amp;nbsp; *list, size_t size);
ssize_t llistxattr(const char &amp;nbsp; *path, char &amp;nbsp; *list, size_t size);
ssize_t flistxattr(int fd, char &amp;nbsp; *list, size_t size);
</code></pre>
<h2>DESCRIPTION</h2>
<p> Extended attributes are <i>name</i>:<i>value</i> pairs associated with inodes (files, directories, symbolic links, etc.). They are extensions to the normal attributes which are associated with all inodes in the system (i.e., the <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) data). A complete overview of extended attributes concepts can be found in <code><a href="/docs/linux/man/7-xattr/">xattr</a></code>(7). </p>
<p> <code>listxattr</code>() retrieves the list of extended attribute names associated with the given <i>path</i> in the filesystem. The retrieved list is placed in <i>list</i>, a caller-allocated buffer whose size (in bytes) is specified in the argument <i>size</i>. The list is the set of (null-terminated) names, one after the other. Names of extended attributes to which the calling process does not have access may be omitted from the list. The length of the attribute name <i>list</i> is returned. </p>
<p> <code>llistxattr</code>() is identical to <code>listxattr</code>(), except in the case of a symbolic link, where the list of names of extended attributes associated with the link itself is retrieved, not the file that it refers to. </p>
<p> <code>flistxattr</code>() is identical to <code>listxattr</code>(), only the open file referred to by <i>fd</i> (as returned by <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) is interrogated in place of <i>path</i>. </p>
<p> A single extended attribute <i>name</i> is a null-terminated string. The name includes a namespace prefix; there may be several, disjoint namespaces associated with an individual inode. </p>
<p> If <i>size</i> is specified as zero, these calls return the current size of the list of extended attribute names (and leave <i>list</i> unchanged). This can be used to determine the size of the buffer that should be supplied in a subsequent call. (But, bear in mind that there is a possibility that the set of extended attributes may change between the two calls, so that it is still necessary to check the return status from the second call.)</p>
<h3>Example</h3>
<p> The <i>list</i> of names is returned as an unordered array of null-terminated character strings (attribute names are separated by null bytes (&#8216;
