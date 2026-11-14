---
title: "readlink(2)"
name: "readlink"
section: "2"
letter: "r"
url: "/docs/linux/man/2-readlink/"
description: "readlink, readlinkat – read value of a symbolic link"
---

<h2 class="name">NAME</h2>
<p> readlink, readlinkat &#8211; read value of a symbolic link </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
ssize_t readlink(const char *pathname, char *buf, size_t bufsiz);
#include &lt;fcntl.h&gt; /* Definition of AT_* constants */
#include &lt;unistd.h&gt;
ssize_t readlinkat(int dirfd, const char *pathname,
                   char *buf, size_t bufsiz);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>readlink</code>():</p>
<dl>
<dt>
<dd> _XOPEN_SOURCE&nbsp;&gt;=&nbsp;500 || _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;||&nbsp;/*&nbsp;Glibc versions&nbsp;&lt;=&nbsp;2.19:&nbsp;*/&nbsp;_BSD_SOURCE</dl>
<p> <code>readlinkat</code>():</p>
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
<p> <code>readlink</code>() places the contents of the symbolic link <i>pathname</i> in the buffer <i>buf</i>, which has size <i>bufsiz</i>. <code>readlink</code>() does not append a null byte to <i>buf</i>. It will (silently) truncate the contents (to a length of <i>bufsiz</i> characters), in case the buffer is too small to hold all of the contents.</p>
<h3>readlinkat()</h3>
<p> The <code>readlinkat</code>() system call operates in exactly the same way as <code>readlink</code>(), except for the differences described here. </p>
<p> If the pathname given in <i>pathname</i> is relative, then it is interpreted relative to the directory referred to by the file descriptor <i>dirfd</i> (rather than relative to the current working directory of the calling process, as is done by <code>readlink</code>() for a relative pathname). </p>
<p> If <i>pathname</i> is relative and <i>dirfd</i> is the special value <code>AT_FDCWD</code>, then <i>pathname</i> is interpreted relative to the current working directory of the calling process (like <code>readlink</code>()). </p>
<p> If <i>pathname</i> is absolute, then <i>dirfd</i> is ignored. </p>
<p> Since Linux 2.6.39, <i>pathname</i> can be an empty string, in which case the call operates on the symbolic link referred to by <i>dirfd</i> (which should have been obtained using <code><a href="/docs/linux/man/2-open/">open</a></code>(2) with the <code>O_PATH</code> and <code>O_NOFOLLOW</code> flags). </p>
<p> See <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2) for an explanation of the need for <code>readlinkat</code>().</p>
<h2>RETURN VALUE</h2>
<p> On success, these calls return the number of bytes placed in <i>buf</i>. (If the returned value equals <i>bufsiz</i>, then truncation may have occurred.) On error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Search permission is denied for a component of the path prefix. (See also <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7).)</p>
<dt><code>EFAULT</code></p>
<dd> <i>buf</i> extends outside the process&#8217;s allocated address space.</p>
<dt><code>EINVAL</code></p>
<dd> <i>bufsiz</i> is not positive.</p>
<dt><code>EINVAL</code></p>
<dd> The named file (i.e., the final filename component of <i>pathname</i>) is not a symbolic link.</p>
<dt><code>EIO</code></p>
<dd> An I/O error occurred while reading from the filesystem.</p>
<dt><code>ELOOP</code></p>
<dd> Too many symbolic links were encountered in translating the pathname.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> A pathname, or a component of a pathname, was too long.</p>
<dt><code>ENOENT</code></p>
<dd> The named file does not exist.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOTDIR</code></p>
<dd> A component of the path prefix is not a directory.</dl>
<p> The following additional errors can occur for <code>readlinkat</code>():</p>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>dirfd</i> is not a valid file descriptor.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>pathname</i> is relative and <i>dirfd</i> is a file descriptor referring to a file other than a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>readlinkat</code>() was added to Linux in kernel 2.6.16; library support was added to glibc in version 2.4.</p>
<h2>CONFORMING TO</h2>
<p> <code>readlink</code>(): 4.4BSD (<code>readlink</code>() first appeared in 4.2BSD), POSIX.1-2001, POSIX.1-2008. </p>
<p> <code>readlinkat</code>(): POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> In versions of glibc up to and including glibc 2.4, the return type of <code>readlink</code>() was declared as <i>int</i>. Nowadays, the return type is declared as <i>ssize_t</i>, as (newly) required in POSIX.1-2001. </p>
<p> Using a statically sized buffer might not provide enough room for the symbolic link contents. The required size for the buffer can be obtained from the <i>stat.st_size</i> value returned by a call to <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2) on the link. However, the number of bytes written by <code>readlink</code>() and <code>readlinkat</code>() should be checked to make sure that the size of the symbolic link did not increase between the calls. Dynamically allocating the buffer for <code>readlink</code>() and <code>readlinkat</code>() also addresses a common portability problem when using <code>PATH_MAX</code> for the buffer size, as this constant is not guaranteed to be defined per POSIX if the system does not have such limit.</p>
<h3>Glibc notes</h3>
<p> On older kernels where <code>readlinkat</code>() is unavailable, the glibc wrapper function falls back to the use of <code>readlink</code>(). When <i>pathname</i> is a relative pathname, glibc constructs a pathname based on the symbolic link in <i>/proc/self/fd</i> that corresponds to the <i>dirfd</i> argument.</p>
<h2>EXAMPLES</h2>
<p> The following program allocates the buffer needed by <code>readlink</code>() dynamically from the information provided by <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2), falling back to a buffer of size <code>PATH_MAX</code> in cases where <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2) reports a size of zero. </p>
<p> #include &lt;sys/types.h&gt; #include &lt;sys/stat.h&gt; #include &lt;limits.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct stat sb;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*buf;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t nbytes, bufsiz; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;pathname&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(lstat(argv[1],&nbsp;&amp;sb)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;lstat&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Add one to the link size, so that we can determine whether<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the buffer returned by readlink()&nbsp;was truncated.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bufsiz&nbsp;=&nbsp;sb.st_size&nbsp;+&nbsp;1; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Some magic symlinks under&nbsp;(for example)&nbsp;/proc and&nbsp;/sys<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;report&nbsp;&#8216;st_size&#8217;&nbsp;as zero. In that case, take PATH_MAX as<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a&nbsp;&quot;good enough&quot;&nbsp;estimate.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sb.st_size&nbsp;==&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bufsiz&nbsp;=&nbsp;PATH_MAX; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buf&nbsp;=&nbsp;malloc(bufsiz);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(buf&nbsp;==&nbsp;NULL)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;malloc&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nbytes&nbsp;=&nbsp;readlink(argv[1], buf, bufsiz);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nbytes&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;readlink&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&#8217;%s&#8217;&nbsp;points to&nbsp;&#8216;%.*s&#8217;
&quot;, argv[1],&nbsp;(int)&nbsp;nbytes, buf); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;If the return value was equal to the buffer size, then the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the link target was larger than expected&nbsp;(perhaps because the<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;target was changed between the call to lstat()&nbsp;and the call to<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;readlink()). Warn the user that the returned target may have<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;been truncated.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nbytes&nbsp;==&nbsp;bufsiz)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;(Returned buffer may have been truncated)
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(buf);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-readlink/">readlink</a></code>(1), <code><a href="/docs/linux/man/2-lstat/">lstat</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-symlink/">symlink</a></code>(2), <code><a href="/docs/linux/man/3-realpath/">realpath</a></code>(3), <code><a href="/docs/linux/man/7-path_resolution/">path_resolution</a></code>(7), <code><a href="/docs/linux/man/7-symlink/">symlink</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
