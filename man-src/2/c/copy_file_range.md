---
title: "copy_file_range(2)"
name: "copy_file_range"
section: "2"
letter: "c"
url: "/docs/linux/man/2-copy_file_range/"
description: "copy_file_range – Copy a range of data from one file to another"
---

<h2 class="name">NAME</h2>
<p> copy_file_range &#8211; Copy a range of data from one file to another </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE
#include &lt;unistd.h&gt;
ssize_t copy_file_range(int fd_in, loff_t *off_in,
                        int fd_out, loff_t *off_out,
                        size_t len, unsigned int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>copy_file_range</code>() system call performs an in-kernel copy between two file descriptors without the additional cost of transferring data from the kernel to user space and then back into the kernel. It copies up to <i>len</i> bytes of data from the source file descriptor <i>fd_in</i> to the target file descriptor <i>fd_out</i>, overwriting any data that exists within the requested range of the target file. </p>
<p> The following semantics apply for <i>off_in</i>, and similar statements apply to <i>off_out</i>:</p>
<dl>
<dt>*</p>
<dd> If <i>off_in</i> is NULL, then bytes are read from <i>fd_in</i> starting from the file offset, and the file offset is adjusted by the number of bytes copied.</p>
<dt>*</p>
<dd> If <i>off_in</i> is not NULL, then <i>off_in</i> must point to a buffer that specifies the starting offset where bytes from <i>fd_in</i> will be read. The file offset of <i>fd_in</i> is not changed, but <i>off_in</i> is adjusted appropriately.</dl>
<p> <i>fd_in</i> and <i>fd_out</i> can refer to the same file. If they refer to the same file, then the source and target ranges are not allowed to overlap. </p>
<p> The <i>flags</i> argument is provided to allow for future extensions and currently must be set to 0.</p>
<h2>RETURN VALUE</h2>
<p> Upon successful completion, <code>copy_file_range</code>() will return the number of bytes copied between files. This could be less than the length originally requested. If the file offset of <i>fd_in</i> is at or past the end of file, no bytes are copied, and <code>copy_file_range</code>() returns zero. </p>
<p> On error, <code>copy_file_range</code>() returns -1 and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> One or more file descriptors are not valid.</p>
<dt><code>EBADF</code></p>
<dd> <i>fd_in</i> is not open for reading; or <i>fd_out</i> is not open for writing.</p>
<dt><code>EBADF</code></p>
<dd> The <code>O_APPEND</code> flag is set for the open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) referred to by the file descriptor <i>fd_out</i>.</p>
<dt><code>EFBIG</code></p>
<dd> An attempt was made to write at a position past the maximum file offset the kernel supports.</p>
<dt><code>EFBIG</code></p>
<dd> An attempt was made to write a range that exceeds the allowed maximum file size. The maximum file size differs between filesystem implementations and can be different from the maximum allowed file offset.</p>
<dt><code>EFBIG</code></p>
<dd> An attempt was made to write beyond the process&#8217;s file size resource limit. This may also result in the process receiving a <code>SIGXFSZ</code> signal.</p>
<dt><code>EINVAL</code></p>
<dd> The <i>flags</i> argument is not 0.</p>
<dt><code>EINVAL</code></p>
<dd> <i>fd_in</i> and <i>fd_out</i> refer to the same file and the source and target ranges overlap.</p>
<dt><code>EINVAL</code></p>
<dd> Either <i>fd_in</i> or <i>fd_out</i> is not a regular file.</p>
<dt><code>EIO</code></p>
<dd> A low-level I/O error occurred while copying.</p>
<dt><code>EISDIR</code></p>
<dd> Either <i>fd_in</i> or <i>fd_out</i> refers to a directory.</p>
<dt><code>ENOMEM</code></p>
<dd> Out of memory.</p>
<dt><code>ENOSPC</code></p>
<dd> There is not enough space on the target filesystem to complete the copy.</p>
<dt><code>EOVERFLOW</code></p>
<dd> The requested source or destination range is too large to represent in the specified data types.</p>
<dt><code>EPERM</code></p>
<dd> <i>fd_out</i> refers to an immutable file.</p>
<dt><code>ETXTBSY</code></p>
<dd> Either <i>fd_in</i> or <i>fd_out</i> refers to an active swap file.</p>
<dt><code>EXDEV</code></p>
<dd> The files referred to by <i>fd_in</i> and <i>fd_out</i> are not on the same mounted filesystem (pre Linux 5.3).</dl>
<h2>VERSIONS</h2>
<p> The <code>copy_file_range</code>() system call first appeared in Linux 4.5, but glibc 2.27 provides a user-space emulation when it is not available. </p>
<p> A major rework of the kernel implementation occurred in 5.3. Areas of the API that weren&#8217;t clearly defined were clarified and the API bounds are much more strictly checked than on earlier kernels. Applications should target the behaviour and requirements of 5.3 kernels. </p>
<p> First support for cross-filesystem copies was introduced in Linux 5.3. Older kernels will return -EXDEV when cross-filesystem copies are attempted.</p>
<h2>CONFORMING TO</h2>
<p> The <code>copy_file_range</code>() system call is a nonstandard Linux and GNU extension.</p>
<h2>NOTES</h2>
<p> If <i>fd_in</i> is a sparse file, then <code>copy_file_range</code>() may expand any holes existing in the requested range. Users may benefit from calling <code>copy_file_range</code>() in a loop, and using the <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) <code>SEEK_DATA</code> and <code>SEEK_HOLE</code> operations to find the locations of data segments. </p>
<p> <code>copy_file_range</code>() gives filesystems an opportunity to implement &quot;copy acceleration&quot; techniques, such as the use of reflinks (i.e., two or more inodes that share pointers to the same copy-on-write disk blocks) or server-side-copy (in the case of NFS).</p>
<h2>EXAMPLES</h2>
<p> #define _GNU_SOURCE #include &lt;fcntl.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/stat.h&gt; #include &lt;sys/syscall.h&gt; #include &lt;unistd.h&gt; </p>
<p> /* On versions of glibc before 2.27, we must invoke copy_file_range()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;using&nbsp;<a href="/docs/linux/man/2-syscall/">syscall</a>(2)&nbsp;*/ </p>
<p> static loff_t copy_file_range(int fd_in, loff_t *off_in, int fd_out,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loff_t&nbsp;*off_out, size_t len, unsigned int flags) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;return syscall(__NR_copy_file_range, fd_in, off_in, fd_out,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;off_out, len, flags); } </p>
<p> int main(int argc, char **argv) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int fd_in, fd_out;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct stat stat;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;loff_t len, ret; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;3)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;source&gt;&nbsp;&lt;destination&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd_in&nbsp;=&nbsp;open(argv[1], O_RDONLY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd_in&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;open&nbsp;(argv[1])&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fstat(fd_in,&nbsp;&amp;stat)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;fstat&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;len&nbsp;=&nbsp;stat.st_size; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd_out&nbsp;=&nbsp;open(argv[2], O_CREAT | O_WRONLY | O_TRUNC, 0644);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fd_out&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;open&nbsp;(argv[2])&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ret&nbsp;=&nbsp;copy_file_range(fd_in, NULL, fd_out, NULL, len, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ret&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;copy_file_range&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;len -=&nbsp;ret;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(len&nbsp;&gt;&nbsp;0&nbsp;&amp;&amp;&nbsp;ret&nbsp;&gt;&nbsp;0); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(fd_in);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;close(fd_out);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2), <code><a href="/docs/linux/man/2-sendfile/">sendfile</a></code>(2), <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
