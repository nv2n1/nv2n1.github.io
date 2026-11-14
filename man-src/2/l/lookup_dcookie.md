---
title: "lookup_dcookie(2)"
name: "lookup_dcookie"
section: "2"
letter: "l"
url: "/docs/linux/man/2-lookup_dcookie/"
description: "lookup_dcookie – return a directory entry’s path"
---

<h2 class="name">NAME</h2>
<p> lookup_dcookie &#8211; return a directory entry&#8217;s path </p>
<h2>SYNOPSIS</h2>
<p> <code>int lookup_dcookie(u64 </code><i>cookie</i><code>, char *</code><i>buffer</i><code>, size_t </code><i>len</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> Look up the full path of the directory entry specified by the value <i>cookie</i>. The cookie is an opaque identifier uniquely identifying a particular directory entry. The buffer given is filled in with the full path of the directory entry. </p>
<p> For <code>lookup_dcookie</code>() to return successfully, the kernel must still hold a cookie reference to the directory entry.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>lookup_dcookie</code>() returns the length of the path string copied into the buffer. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> The buffer was not valid.</p>
<dt><code>EINVAL</code></p>
<dd> The kernel has no registered cookie/directory entry mappings at the time of lookup, or the cookie does not refer to a valid directory entry.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> The name could not fit in the buffer.</p>
<dt><code>ENOMEM</code></p>
<dd> The kernel could not allocate memory for the temporary buffer holding the path.</p>
<dt><code>EPERM</code></p>
<dd> The process does not have the capability <code>CAP_SYS_ADMIN</code> required to look up cookie values.</p>
<dt><code>ERANGE</code></p>
<dd> The buffer was not large enough to hold the path of the directory entry.</dl>
<h2>VERSIONS</h2>
<p> Available since Linux 2.5.43. The <code>ENAMETOOLONG</code> error return was added in 2.5.70.</p>
<h2>CONFORMING TO</h2>
<p> <code>lookup_dcookie</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> <code>lookup_dcookie</code>() is a special-purpose system call, currently used only by the <code><a href="/docs/linux/man/1-oprofile/">oprofile</a></code>(1) profiler. It relies on a kernel driver to register cookies for directory entries. </p>
<p> The path returned may be suffixed by the string &quot; (deleted)&quot; if the directory entry has been removed.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-oprofile/">oprofile</a></code>(1)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
