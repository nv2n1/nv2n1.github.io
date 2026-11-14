---
title: "fexecve(3)"
name: "fexecve"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fexecve/"
description: "fexecve – execute program specified via file descriptor"
---

<h2 class="name">NAME</h2>
<p> fexecve &#8211; execute program specified via file descriptor </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
int fexecve(int fd, char *const argv[], char *const envp[]);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>fexecve</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.10:</p>
<dd> _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200809L</p>
<dt>Before glibc 2.10:</p>
<dd> _GNU_SOURCE</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> <code>fexecve</code>() performs the same task as <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), with the difference that the file to be executed is specified via a file descriptor, <i>fd</i>, rather than via a pathname. The file descriptor <i>fd</i> must be opened read-only (<code>O_RDONLY</code>) or with the <code>O_PATH</code> flag and the caller must have permission to execute the file that it refers to.</p>
<h2>RETURN VALUE</h2>
<p> A successful call to <code>fexecve</code>() never returns. On error, the function does return, with a result value of -1, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> Errors are as for <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), with the following additions:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>fd</i> is not a valid file descriptor, or <i>argv</i> is NULL, or <i>envp</i> is NULL.</p>
<dt><code>ENOENT</code></p>
<dd> The close-on-exec flag is set on <i>fd</i>, and <i>fd</i> refers to a script. See BUGS.</p>
<dt><code>ENOSYS</code></p>
<dd> The kernel does not provide the <code><a href="/docs/linux/man/2-execveat/">execveat</a></code>(2) system call, and the <i>/proc</i> filesystem could not be accessed.</dl>
<h2>VERSIONS</h2>
<p> <code>fexecve</code>() is implemented since glibc 2.3.2.</p>
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
<td> <code>fexecve</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2008. This function is not specified in POSIX.1-2001, and is not widely available on other systems. It is specified in POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> On Linux with glibc versions 2.26 and earlier, <code>fexecve</code>() is implemented using the <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) filesystem, so <i>/proc</i> needs to be mounted and available at the time of the call. Since glibc 2.27, if the underlying kernel supports the <code><a href="/docs/linux/man/2-execveat/">execveat</a></code>(2) system call, then <code>fexecve</code>() is implemented using that system call, with the benefit that <i>/proc</i> does not need to be mounted. </p>
<p> The idea behind <code>fexecve</code>() is to allow the caller to verify (checksum) the contents of an executable before executing it. Simply opening the file, checksumming the contents, and then doing an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) would not suffice, since, between the two steps, the filename, or a directory prefix of the pathname, could have been exchanged (by, for example, modifying the target of a symbolic link). <code>fexecve</code>() does not mitigate the problem that the <i>contents</i> of a file could be changed between the checksumming and the call to <code>fexecve</code>(); for that, the solution is to ensure that the permissions on the file prevent it from being modified by malicious users. </p>
<p> The natural idiom when using <code>fexecve</code>() is to set the close-on-exec flag on <i>fd</i>, so that the file descriptor does not leak through to the program that is executed. This approach is natural for two reasons. First, it prevents file descriptors being consumed unnecessarily. (The executed program normally has no need of a file descriptor that refers to the program itself.) Second, if <code>fexecve</code>() is used recursively, employing the close-on-exec flag prevents the file descriptor exhaustion that would result from the fact that each step in the recursion would cause one more file descriptor to be passed to the new program. (But see BUGS.)</p>
<h2>BUGS</h2>
<p> If <i>fd</i> refers to a script (i.e., it is an executable text file that names a script interpreter with a first line that begins with the characters <i>#!</i>) and the close-on-exec flag has been set for <i>fd</i>, then <code>fexecve</code>() fails with the error <code>ENOENT</code>. This error occurs because, by the time the script interpreter is executed, <i>fd</i> has already been closed because of the close-on-exec flag. Thus, the close-on-exec flag can&#8217;t be set on <i>fd</i> if it refers to a script, leading to the problems described in NOTES.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/2-execveat/">execveat</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
