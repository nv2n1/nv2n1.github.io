---
title: "rmdir(2)"
name: "rmdir"
section: "2"
letter: "r"
url: "/docs/linux/man/2-rmdir/"
description: "rmdir – delete a directory"
---

<h2 class="name">NAME</h2>
<p> rmdir &#8211; delete a directory </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int rmdir(const char *</code><i>pathname</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>rmdir</code>() deletes a directory, which must be empty.</p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Write access to the directory containing <i>pathname</i> was not allowed, or one of the directories in the path prefix of <i>pathname</i> did not allow search permission. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).</p>
<dt><code>EBUSY</code></p>
<dd> <i>pathname</i> is currently in use by the system or some process that prevents its removal. On Linux, this means <i>pathname</i> is currently used as a mount point or is the root directory of the calling process.</p>
<dt><code>EFAULT</code></p>
<dd> <i>pathname</i> points outside your accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>pathname</i> has <i>.</i> as last component.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in resolving <i>pathname</i>.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>pathname</i> was too long.</p>
<dt><code>ENOENT</code></p>
<dd> A directory component in <i>pathname</i> does not exist or is a dangling symbolic link.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>pathname</i>, or a component used as a directory in <i>pathname</i>, is not, in fact, a directory.</p>
<dt><code>ENOTEMPTY</code></p>
<dd> <i>pathname</i> contains entries other than <i>.</i> and <i>..</i> ; or, <i>pathname</i> has <i>..</i> as its final component. POSIX.1 also allows <code>EEXIST</code> for this condition.</p>
<dt><code>EPERM</code></p>
<dd> The directory containing <i>pathname</i> has the sticky bit (<code>S_ISVTX</code>) set and the process&#8217;s effective user ID is neither the user ID of the file to be deleted nor that of the directory containing it, and the process is not privileged (Linux: does not have the <code>CAP_FOWNER</code> capability).</p>
<dt><code>EPERM</code></p>
<dd> The filesystem containing <i>pathname</i> does not support the removal of directories.</p>
<dt><code>EROFS</code></p>
<dd> <i>pathname</i> refers to a directory on a read-only filesystem.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>BUGS</h2>
<p> Infelicities in the protocol underlying NFS can cause the unexpected disappearance of directories which are still being used.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rm/">rm</a></code>(1), <code><a href="/docs/linux/man/1-rmdir/">rmdir</a></code>(1), <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2), <code><a href="/docs/linux/man/2-chmod/">chmod</a></code>(2), <code><a href="/docs/linux/man/2-mkdir/">mkdir</a></code>(2), <code><a href="/docs/linux/man/2-rename/">rename</a></code>(2), <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2), <code><a href="/docs/linux/man/2-unlinkat/">unlinkat</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
