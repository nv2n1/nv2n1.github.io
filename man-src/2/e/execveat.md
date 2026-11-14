---
title: "execveat(2)"
name: "execveat"
section: "2"
letter: "e"
url: "/docs/linux/man/2-execveat/"
description: "execveat – execute program relative to a directory file descriptor"
---

<h2 class="name">NAME</h2>
<p> execveat &#8211; execute program relative to a directory file descriptor </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int execveat(int </code><i>dirfd</i><code>, const char *</code><i>pathname</i><code>,</code><br />
 <code> char *const </code><i>argv</i><code>[], char *const </code><i>envp</i><code>[],</code><br />
 <code> int </code><i>flags</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> The <code>execveat</code>() system call executes the program referred to by the combination of <i>dirfd</i> and <i>pathname</i>. It operates in exactly the same way as <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), except for the differences described in this manual page. </p>
<p> If the pathname given in <i>pathname</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) for a relative pathname). </p>
<p> If <i>pathname</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the calling process (like <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2)). </p>
<p> If <i>pathname</i> is absolute, then <i>dirfd</i> is ignored. </p>
<p> If <i>pathname</i> is an empty string and the <code>AT_EMPTY_PATH</code> flag is specified, then the file descriptor <i>dirfd</i> specifies the file to be executed (i.e., <i>dirfd</i> refers to an executable file, rather than a directory). </p>
<p> The <i>flags</i> argument is a bit mask that can include zero or more of the following flags:</p>
<dl>
<dt><code>AT_EMPTY_PATH</code></p>
<dd> If <i>pathname</i> is an empty string, operate on the file referred to by <i>dirfd</i> (which may have been obtained using the <code><a href="/docs/linux/man/2-open/">open</a></code>(2) <code>O_PATH</code> flag).</p>
<dt><code>AT_SYMLINK_NOFOLLOW</code></p>
<dd> If the file identified by <i>dirfd</i> and a non-NULL <i>pathname</i> is a symbolic link, then the call fails with the error <code>ELOOP</code>.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>execveat</code>() does not return. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> The same errors that occur for <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) can also occur for <code>execveat</code>(). The following additional errors can occur for <code>execveat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid flag specified in <i>flags</i>.</p>
<dt><code>ELOOP</code></p>
<dd> <i>flags</i> includes <code>AT_SYMLINK_NOFOLLOW</code> and the file identified by <i>dirfd</i> and a non-NULL <i>pathname</i> is a symbolic link.</p>
<dt><code>ENOENT</code></p>
<dd> The program identified by <i>dirfd</i> and <i>pathname</i> requires the use of an interpreter program (such as a script starting with &quot;#!&quot;), but the file descriptor <i>dirfd</i> was opened with the <code>O_CLOEXEC</code> flag, with the result that the program file is inaccessible to the launched interpreter. See BUGS.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>pathname</i> is relative and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>execveat</code>() was added to Linux in kernel 3.19. GNU C library support is pending.</p>
<h2>CONFORMING TO</h2>
<p> The <code>execveat</code>() system call is Linux-specific.</p>
<h2>NOTES</h2>
<p> In addition to the reasons explained in <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2), the <code>execveat</code>() system call is also needed to allow <code><a href="/docs/linux/man/3-fexecve/">fexecve</a></code>(3) to be implemented on systems that do not have the <i>/proc</i> filesystem mounted. </p>
<p> When asked to execute a script file, the <i>argv[0]</i> that is passed to the script interpreter is a string of the form <i>/dev/fd/N</i> or <i>/dev/fd/N/P</i>, where <i>N</i> is the number of the file descriptor passed via the <i>dirfd</i> argument. A string of the first form occurs when <code>AT_EMPTY_PATH</code> is employed. A string of the second form occurs when the script is specified via both <i>dirfd</i> and <i>pathname</i>; in this case, <i>P</i> is the value given in <i>pathname</i>. </p>
<p> For the same reasons described in <code><a href="/docs/linux/man/3-fexecve/">fexecve</a></code>(3), the natural idiom when using <code>execveat</code>() is to set the close-on-exec flag on <i>dirfd</i>. (But see BUGS.)</p>
<h2>BUGS</h2>
<p> The <code>ENOENT</code> error described above means that it is not possible to set the close-on-exec flag on the file descriptor given to a call of the form: </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;execveat(fd,&nbsp;&quot;&quot;, argv, envp, AT_EMPTY_PATH); </p>
<p> However, the inability to set the close-on-exec flag means that a file descriptor referring to the script leaks through to the script itself. As well as wasting a file descriptor, this leakage can lead to file-descriptor exhaustion in scenarios where scripts recursively employ <code>execveat</code>().</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2), <code><a href="/docs/linux/man/3-fexecve/">fexecve</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
