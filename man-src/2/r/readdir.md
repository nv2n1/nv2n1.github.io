---
title: "readdir(2)"
name: "readdir"
section: "2"
letter: "r"
url: "/docs/linux/man/2-readdir/"
description: "readdir – read directory entry"
---

<h2 class="name">NAME</h2>
<p> readdir &#8211; read directory entry </p>
<h2>SYNOPSIS</h2>
<pre><code>
int readdir(unsigned int fd, struct old_linux_dirent *dirp,
            unsigned int count);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> This is not the function you are interested in. Look at <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) for the POSIX conforming C library interface. This page documents the bare kernel system call interface, which is superseded by <code><a href="/docs/linux/man/2-getdents/">getdents</a></code>(2). </p>
<p> <code>readdir</code>() reads one <i>old_linux_dirent</i> structure from the directory referred to by the file descriptor <i>fd</i> into the buffer pointed to by <i>dirp</i>. The argument <i>count</i> is ignored; at most one <i>old_linux_dirent</i> structure is read. </p>
<p> The <i>old_linux_dirent</i> structure is declared (privately in Linux kernel file <code>fs/readdir.c</code>) as follows: </p>
<p> struct old_linux_dirent {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long d_ino;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;inode number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long d_offset;&nbsp;<wbr>&nbsp;/*&nbsp;offset to this&nbsp;<i>old_linux_dirent</i>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short d_namlen;&nbsp;/*&nbsp;length of this&nbsp;<i>d_name</i>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;d_name[1];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;filename&nbsp;(null-terminated)&nbsp;*/ } </p>
<p> <i>d_ino</i> is an inode number. <i>d_offset</i> is the distance from the start of the directory to this <i>old_linux_dirent</i>. <i>d_reclen</i> is the size of <i>d_name</i>, not counting the terminating null byte (&#8216;\0&#8217;). <i>d_name</i> is a null-terminated filename.  </p>
<h2>RETURN VALUE</h2>
<p> On success, 1 is returned. On end of directory, 0 is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.  </p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></dt>
<dd> <p> Invalid file descriptor <i>fd</i>. </p>
 </dd>
<dt><code>EFAULT</code></dt>
<dd> <p> Argument points outside the calling process&#8217;s address space. </p>
 </dd>
<dt><code>EINVAL</code></dt>
<dd> <p> Result buffer is too small. </p>
 </dd>
<dt><code>ENOENT</code></dt>
<dd> <p> No such directory. </p>
 </dd>
<dt><code>ENOTDIR</code></dt>
<dd> <p> File descriptor does not refer to a directory. </p>
 </dd></dl>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.  </p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). You will need to define the <i>old_linux_dirent</i> structure yourself. However, probably you should use <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3) instead. </p>
<p> This system call does not exist on x86-64.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getdents/">getdents</a></code>(2), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
