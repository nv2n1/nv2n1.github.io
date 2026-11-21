---
title: "ustat(2)"
name: "ustat"
section: "2"
letter: "u"
url: "/docs/linux/man/2-ustat/"
description: "ustat – get filesystem statistics"
---

<h2 class="name">NAME</h2>
<p> ustat &#8211; get filesystem statistics </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt; /* libc[45] */
#include &lt;ustat.h&gt;  /* glibc2 */
int ustat(dev_t dev, struct ustat *ubuf);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>ustat</code>() returns information about a mounted filesystem. <i>dev</i> is a device number identifying a device containing a mounted filesystem. <i>ubuf</i> is a pointer to a <i>ustat</i> structure that contains the following members: </p>
<p> daddr_t f_tfree; /* Total free blocks */ ino_t f_tinode; /* Number of free inodes */ char f_fname[6]; /* Filsys name */ char f_fpack[6]; /* Filsys pack name */ </p>
<p> The last two fields, <i>f_fname</i> and <i>f_fpack</i>, are not implemented and will always be filled with null bytes (&#8216;\0&#8217;).  </p>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned and the <i>ustat</i> structure pointed to by <i>ubuf</i> will be filled in. On error, -1 is returned, and <i>errno</i> is set appropriately.  </p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></dt>
<dd> <p> <i>ubuf</i> points outside of your accessible address space. </p>
 </dd>
<dt><code>EINVAL</code></dt>
<dd> <p> <i>dev</i> does not refer to a device containing a mounted filesystem. </p>
 </dd>
<dt><code>ENOSYS</code></dt>
<dd> <p> The mounted filesystem referenced by <i>dev</i> does not support this operation, or any version of Linux before 1.3.16. </p>
 </dd></dl>
<h2>VERSIONS</h2>
<p> Since version 2.28, glibc no longer provides a wrapper for this system call.  </p>
<h2>CONFORMING TO</h2>
<p> SVr4.  </p>
<h2>NOTES</h2>
<p> <code>ustat</code>() is deprecated and has been provided only for compatibility. All new programs should use <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2) instead.  </p>
<h3>HP-UX notes</h3>
<p> The HP-UX version of the <i>ustat</i> structure has an additional field, <i>f_blksize</i>, that is unknown elsewhere. HP-UX warns: For some filesystems, the number of free inodes does not change. Such filesystems will return -1 in the field <i>f_tinode</i>. For some filesystems, inodes are dynamically allocated. Such filesystems will return the current number of free inodes.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-statfs/">statfs</a></code>(2)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
