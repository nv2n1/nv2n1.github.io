---
title: "getwd(3)"
name: "getwd"
section: "3"
letter: "g"
url: "/docs/linux/man/3-getwd/"
description: "getcwd, getwd, get_current_dir_name – get current working directory"
---

<h2 class="name">NAME</h2>
<p> getcwd, getwd, get_current_dir_name &#8211; get current working directory </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
char *getcwd(char *buf, size_t size);
char *getwd(char *buf);
char *get_current_dir_name(void);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>get_current_dir_name</code>():</p>
<dl>
<dt>
<dd> _GNU_SOURCE</dl>
<p> <code>getwd</code>():</p>
<dl>
<dt>
<dd>
<dl>
<dt>Since glibc 2.12:</p>
<dd>
<pre><code>
(_XOPEN_SOURCE &amp;nbsp; &gt;= &amp;nbsp; 500) &amp;&amp; !(_POSIX_C_SOURCE &amp; nbsp; &gt;= &amp;nbsp; 200809L) || /* Glibc since 2.19: */ _DEFAULT_SOURCE
    || /* Glibc versions &lt;= 2.19: */ _BSD_SOURCE
</code></pre>
<dt>Before glibc 2.12:</p>
<dd> _BSD_SOURCE || _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500</dl>
</dl>
<h2>DESCRIPTION</h2>
<p> These functions return a null-terminated string containing an absolute pathname that is the current working directory of the calling process. The pathname is returned as the function result and via the argument <i>buf</i>, if present. </p>
<p> The <code>getcwd</code>() function copies an absolute pathname of the current working directory to the array pointed to by <i>buf</i>, which is of length <i>size</i>. </p>
<p> If the length of the absolute pathname of the current working directory, including the terminating null byte, exceeds <i>size</i> bytes, NULL is returned, and <i>errno</i> is set to <code>ERANGE</code>; an application should check for this error, and allocate a larger buffer if necessary. </p>
<p> As an extension to the POSIX.1-2001 standard, glibc&#8217;s <code>getcwd</code>() allocates the buffer dynamically using <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) if <i>buf</i> is NULL. In this case, the allocated buffer has the length <i>size</i> unless <i>size</i> is zero, when <i>buf</i> is allocated as big as necessary. The caller should <code><a href="/docs/linux/man/3-free/">free</a></code>(3) the returned buffer. </p>
<p> <code>get_current_dir_name</code>() will <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) an array big enough to hold the absolute pathname of the current working directory. If the environment variable <code>PWD</code> is set, and its value is correct, then that value will be returned. The caller should <code><a href="/docs/linux/man/3-free/">free</a></code>(3) the returned buffer. </p>
<p> <code>getwd</code>() does not <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3) any memory. The <i>buf</i> argument should be a pointer to an array at least <code>PATH_MAX</code> bytes long. If the length of the absolute pathname of the current working directory, including the terminating null byte, exceeds <code>PATH_MAX</code> bytes, NULL is returned, and <i>errno</i> is set to <code>ENAMETOOLONG</code>. (Note that on some systems, <code>PATH_MAX</code> may not be a compile-time constant; furthermore, its value may depend on the filesystem, see <code><a href="/docs/linux/man/3-pathconf/">pathconf</a></code>(3).) For portability and security reasons, use of <code>getwd</code>() is deprecated.</p>
<h2>RETURN VALUE</h2>
<p> On success, these functions return a pointer to a string containing the pathname of the current working directory. In the case of <code>getcwd</code>() and <code>getwd</code>() this is the same value as <i>buf</i>. </p>
<p> On failure, these functions return NULL, and <i>errno</i> is set to indicate the error. The contents of the array pointed to by <i>buf</i> are undefined on error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Permission to read or search a component of the filename was denied.</p>
<dt><code>EFAULT</code></p>
<dd> <i>buf</i> points to a bad address.</p>
<dt><code>EINVAL</code></p>
<dd> The <i>size</i> argument is zero and <i>buf</i> is not a null pointer.</p>
<dt><code>EINVAL</code></p>
<dd> <code>getwd</code>(): <i>buf</i> is NULL.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <code>getwd</code>(): The size of the null-terminated absolute pathname string exceeds <code>PATH_MAX</code> bytes.</p>
<dt><code>ENOENT</code></p>
<dd> The current working directory has been unlinked.</p>
<dt><code>ENOMEM</code></p>
<dd> Out of memory.</p>
<dt><code>ERANGE</code></p>
<dd> The <i>size</i> argument is less than the length of the absolute pathname of the working directory, including the terminating null byte. You need to allocate a bigger array and try again.</dl>
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
<td> <code>getcwd</code>(), <code>getwd</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>get_current_dir_name</code>() </td>
<td>Thread safety</td>
<td>MT-Safe env
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>getcwd</code>() conforms to POSIX.1-2001. Note however that POSIX.1-2001 leaves the behavior of <code>getcwd</code>() unspecified if <i>buf</i> is NULL. </p>
<p> <code>getwd</code>() is present in POSIX.1-2001, but marked LEGACY. POSIX.1-2008 removes the specification of <code>getwd</code>(). Use <code>getcwd</code>() instead. POSIX.1-2001 does not define any errors for <code>getwd</code>(). </p>
<p> <code>get_current_dir_name</code>() is a GNU extension.</p>
<h2>NOTES</h2>
<p> Under Linux, these functions make use of the <code>getcwd</code>() system call (available since Linux 2.1.92). On older systems they would query <i>/proc/self/cwd</i>. If both system call and proc filesystem are missing, a generic implementation is called. Only in that case can these calls fail under Linux with <code>EACCES</code>. </p>
<p> These functions are often used to save the location of the current working directory for the purpose of returning to it later. Opening the current directory (&quot;.&quot;) and calling <code><a href="/docs/linux/man/2-fchdir/">fchdir</a></code>(2) to return is usually a faster and more reliable alternative when sufficiently many file descriptors are available, especially on platforms other than Linux.</p>
<h3>C library/kernel differences</h3>
<p> On Linux, the kernel provides a <code>getcwd</code>() system call, which the functions described in this page will use if possible. The system call takes the same arguments as the library function of the same name, but is limited to returning at most <code>PATH_MAX</code> bytes. (Before Linux 3.12, the limit on the size of the returned pathname was the system page size. On many architectures, <code>PATH_MAX</code> and the system page size are both 4096 bytes, but a few architectures have a larger page size.) If the length of the pathname of the current working directory exceeds this limit, then the system call fails with the error <code>ENAMETOOLONG</code>. In this case, the library functions fall back to a (slower) alternative implementation that returns the full pathname. </p>
<p> Following a change in Linux 2.6.36, the pathname returned by the <code>getcwd</code>() system call will be prefixed with the string &quot;(unreachable)&quot; if the current directory is not below the root directory of the current process (e.g., because the process set a new filesystem root using <code><a href="/docs/linux/man/2-chroot/">chroot</a></code>(2) without changing its current directory into the new root). Such behavior can also be caused by an unprivileged user by changing the current directory into another mount namespace. When dealing with pathname from untrusted sources, callers of the functions described in this page should consider checking whether the returned pathname starts with &#8216;/&#8217; or &#8216;(&#8216; to avoid misinterpreting an unreachable path as a relative pathname.</p>
<h2>BUGS</h2>
<p> Since the Linux 2.6.36 change that added &quot;(unreachable)&quot; in the circumstances described above, the glibc implementation of <code>getcwd</code>() has failed to conform to POSIX and returned a relative pathname when the API contract requires an absolute pathname. With glibc 2.27 onwards this is corrected; calling <code>getcwd</code>() from such a pathname will now result in failure with <code>ENOENT</code>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pwd/">pwd</a></code>(1), <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2), <code><a href="/docs/linux/man/2-fchdir/">fchdir</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2), <code><a href="/docs/linux/man/3-free/">free</a></code>(3), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
