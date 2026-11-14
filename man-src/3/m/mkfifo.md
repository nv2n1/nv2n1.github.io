---
title: "mkfifo(3)"
name: "mkfifo"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mkfifo/"
description: "mkfifo, mkfifoat – make a FIFO special file (a named pipe)"
---

<h2 class="name">NAME</h2>
<p> mkfifo, mkfifoat &#8211; make a FIFO special file (a named pipe) </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/stat.h&gt;
#include &lt;sys/types.h&gt;
int mkfifo(const char *pathname, mode_t mode);
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;sys/stat.h&gt;
int mkfifoat(int dirfd, const char *pathname, mode_t mode);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>mkfifoat</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd> _ATFILE_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>mkfifo</code>() makes a FIFO special file with name <i>pathname</i>. <i>mode</i> specifies the FIFO&#8217;s permissions. It is modified by the process&#8217;s <code>umask</code> in the usual way: the permissions of the created file are <code>(</code><i>mode</i><code> &amp; ~umask)</code>. </p>
<p> A FIFO special file is similar to a pipe, except that it is created in a different way. Instead of being an anonymous communications channel, a FIFO special file is entered into the filesystem by calling <code>mkfifo</code>(). </p>
<p> Once you have created a FIFO special file in this way, any process can open it for reading or writing, in the same way as an ordinary file. However, it has to be open at both ends simultaneously before you can proceed to do any input or output operations on it. Opening a FIFO for reading normally blocks until some other process opens the same FIFO for writing, and vice versa. See <code><a href="/docs/linux/man/7-fifo/">fifo</a></code>(7) for nonblocking handling of FIFO special files.</p>
<h3>mkfifoat()</h3>
<p> The <code>mkfifoat</code>() function operates in exactly the same way as <code>mkfifo</code>(), except for the differences described here. </p>
<p> If the pathname given in <i>pathname</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>mkfifo</code>() for a relative pathname). </p>
<p> If <i>pathname</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the calling process (like <code>mkfifo</code>()). </p>
<p> If <i>pathname</i> is absolute, then <i>dirfd</i> is ignored.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>mkfifo</code>() and <code>mkfifoat</code>() return 0. In the case of an error, -1 is returned (in which case, <i>errno</i> is set appropriately).</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> One of the directories in <i>pathname</i> did not allow search (execute) permission.</p>
<dt><code>EDQUOT</code></p>
<dd> The user&#8217;s quota of disk blocks or inodes on the filesystem has been exhausted.</p>
<dt><code>EEXIST</code></p>
<dd> <i>pathname</i> already exists. This includes the case where <i>pathname</i> is a symbolic link, dangling or not.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> Either the total length of <i>pathname</i> is greater than <code>PATH_MAX</code>, or an individual filename component has a length greater than <code>NAME_MAX</code>. In the GNU system, there is no imposed limit on overall filename length, but some filesystems may place limits on the length of a component.</p>
<dt><code>ENOENT</code></p>
<dd> A directory component in <i>pathname</i> does not exist or is a dangling symbolic link.</p>
<dt><code>ENOSPC</code></p>
<dd> The directory or filesystem has no room for the new file.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component used as a directory in <i>pathname</i> is not, in fact, a directory.</p>
<dt><code>EROFS</code></p>
<dd> <i>pathname</i> refers to a read-only filesystem.</dl>
<p> The following additional errors can occur for <code>mkfifoat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid file descriptor.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>pathname</i> is a relative path and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>mkfifoat</code>() was added to glibc in version 2.4. It is implemented using <code><a href="/docs/linux/man/2-mknodat/">mknodat</a></code>(2), available on Linux since kernel 2.6.16.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mkfifo</code>(), <code>mkfifoat</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>mkfifo</code>(): POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>mkfifoat</code>(): POSIX.1-2008.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mkfifo/">mkfifo</a></code>(1), <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-umask/">umask</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/7-fifo/">fifo</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
