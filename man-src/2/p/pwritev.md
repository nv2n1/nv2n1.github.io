---
title: "pwritev(2)"
name: "pwritev"
section: "2"
letter: "p"
url: "/docs/linux/man/2-pwritev/"
description: "readv, writev, preadv, pwritev, preadv2, pwritev2 – read or write data into multiple buffers"
---

<h2 class="name">NAME</h2>
<p> readv, writev, preadv, pwritev, preadv2, pwritev2 &#8211; read or write data into multiple buffers </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/uio.h&gt;
ssize_t readv(int fd, const struct iovec *iov, int iovcnt);
ssize_t writev(int fd, const struct iovec *iov, int iovcnt);
ssize_t preadv(int fd, const struct iovec *iov, int iovcnt,
               off_t offset);
ssize_t pwritev(int fd, const struct iovec *iov, int iovcnt,
                off_t offset);
ssize_t preadv2(int fd, const struct iovec *iov, int iovcnt,
                off_t offset, int flags);
ssize_t pwritev2(int fd, const struct iovec *iov, int iovcnt,
                 off_t offset, int flags);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>preadv</code>(), <code>pwritev</code>():<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Since glibc 2.19:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_DEFAULT_SOURCE<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Glibc 2.19 and earlier:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;_BSD_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>readv</code>() system call reads <i>iovcnt</i> buffers from the file associated with the file descriptor <i>fd</i> into the buffers described by <i>iov</i> (&quot;scatter input&quot;). </p>
<p> The <code>writev</code>() system call writes <i>iovcnt</i> buffers of data described by <i>iov</i> to the file associated with the file descriptor <i>fd</i> (&quot;gather output&quot;). </p>
<p> The pointer <i>iov</i> points to an array of <i>iovec</i> structures, defined in <i>&lt;sys/uio.h&gt;</i> as: </p>
<p> struct iovec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;*iov_base;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Starting address&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t iov_len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of bytes to transfer&nbsp;*/ }; </p>
<p> The <code>readv</code>() system call works just like <code><a href="/docs/linux/man/2-read/">read</a></code>(2) except that multiple buffers are filled. </p>
<p> The <code>writev</code>() system call works just like <code><a href="/docs/linux/man/2-write/">write</a></code>(2) except that multiple buffers are written out. </p>
<p> Buffers are processed in array order. This means that <code>readv</code>() completely fills <i>iov[0]</i> before proceeding to <i>iov[1]</i>, and so on. (If there is insufficient data, then not all buffers pointed to by <i>iov</i> may be filled.) Similarly, <code>writev</code>() writes out the entire contents of <i>iov[0]</i> before proceeding to <i>iov[1]</i>, and so on. </p>
<p> The data transfers performed by <code>readv</code>() and <code>writev</code>() are atomic: the data written by <code>writev</code>() is written as a single block that is not intermingled with output from writes in other processes (but see <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7) for an exception); analogously, <code>readv</code>() is guaranteed to read a contiguous block of data from the file, regardless of read operations performed in other threads or processes that have file descriptors referring to the same open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)).</p>
<h3>preadv() and pwritev()</h3>
<p> The <code>preadv</code>() system call combines the functionality of <code>readv</code>() and <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2). It performs the same task as <code>readv</code>(), but adds a fourth argument, <i>offset</i>, which specifies the file offset at which the input operation is to be performed. </p>
<p> The <code>pwritev</code>() system call combines the functionality of <code>writev</code>() and <code><a href="/docs/linux/man/2-pwrite/">pwrite</a></code>(2). It performs the same task as <code>writev</code>(), but adds a fourth argument, <i>offset</i>, which specifies the file offset at which the output operation is to be performed. </p>
<p> The file offset is not changed by these system calls. The file referred to by <i>fd</i> must be capable of seeking.</p>
<h3>preadv2() and pwritev2()</h3>
<p> These system calls are similar to <code>preadv</code>() and <code>pwritev</code>() calls, but add a fifth argument, <i>flags</i>, which modifies the behavior on a per-call basis. </p>
<p> Unlike <code>preadv</code>() and <code>pwritev</code>(), if the <i>offset</i> argument is -1, then the current file offset is used and updated. </p>
<p> The <i>flags</i> argument contains a bitwise OR of zero or more of the following flags:</p>
<dl>
<dt><code>RWF_DSYNC</code> (since Linux 4.7)</p>
<dd> Provide a per-write equivalent of the <code>O_DSYNC</code> <code><a href="/docs/linux/man/2-open/">open</a></code>(2) flag. This flag is meaningful only for <code>pwritev2</code>(), and its effect applies only to the data range written by the system call.</p>
<dt><code>RWF_HIPRI</code> (since Linux 4.6)</p>
<dd> High priority read/write. Allows block-based filesystems to use polling of the device, which provides lower latency, but may use additional resources. (Currently, this feature is usable only on a file descriptor opened using the <code>O_DIRECT</code> flag.)</p>
<dt><code>RWF_SYNC</code> (since Linux 4.7)</p>
<dd> Provide a per-write equivalent of the <code>O_SYNC</code> <code><a href="/docs/linux/man/2-open/">open</a></code>(2) flag. This flag is meaningful only for <code>pwritev2</code>(), and its effect applies only to the data range written by the system call.</p>
<dt><code>RWF_NOWAIT</code> (since Linux 4.14)</p>
<dd> Do not wait for data which is not immediately available. If this flag is specified, the <code>preadv2</code>() system call will return instantly if it would have to read data from the backing storage or wait for a lock. If some data was successfully read, it will return the number of bytes read. If no bytes were read, it will return -1 and set <i>errno</i> to <code>EAGAIN</code>. Currently, this flag is meaningful only for <code>preadv2</code>().</p>
<dt><code>RWF_APPEND</code> (since Linux 4.16)</p>
<dd> Provide a per-write equivalent of the <code>O_APPEND</code> <code><a href="/docs/linux/man/2-open/">open</a></code>(2) flag. This flag is meaningful only for <code>pwritev2</code>(), and its effect applies only to the data range written by the system call. The <i>offset</i> argument does not affect the write operation; the data is always appended to the end of the file. However, if the <i>offset</i> argument is -1, the current file offset is updated.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>readv</code>(), <code>preadv</code>(), and <code>preadv2</code>() return the number of bytes read; <code>writev</code>(), <code>pwritev</code>(), and <code>pwritev2</code>() return the number of bytes written. </p>
<p> Note that it is not an error for a successful call to transfer fewer bytes than requested (see <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2)). </p>
<p> On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<p> The errors are as given for <code><a href="/docs/linux/man/2-read/">read</a></code>(2) and <code><a href="/docs/linux/man/2-write/">write</a></code>(2). Furthermore, <code>preadv</code>(), <code>preadv2</code>(), <code>pwritev</code>(), and <code>pwritev2</code>() can also fail for the same reasons as <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2). Additionally, the following errors are defined:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> The sum of the <i>iov_len</i> values overflows an <i>ssize_t</i> value.</p>
<dt><code>EINVAL</code></p>
<dd> The vector count, <i>iovcnt</i>, is less than zero or greater than the permitted maximum.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> An unknown flag is specified in <i>flags</i>.</dl>
<h2>VERSIONS</h2>
<p> <code>preadv</code>() and <code>pwritev</code>() first appeared in Linux 2.6.30; library support was added in glibc 2.10. </p>
<p> <code>preadv2</code>() and <code>pwritev2</code>() first appeared in Linux 4.6. Library support was added in glibc 2.26.</p>
<h2>CONFORMING TO</h2>
<p> <code>readv</code>(), <code>writev</code>(): POSIX.1-2001, POSIX.1-2008, 4.4BSD (these system calls first appeared in 4.2BSD). </p>
<p> <code>preadv</code>(), <code>pwritev</code>(): nonstandard, but present also on the modern BSDs. </p>
<p> <code>preadv2</code>(), <code>pwritev2</code>(): nonstandard Linux extension.</p>
<h2>NOTES</h2>
<p> POSIX.1 allows an implementation to place a limit on the number of items that can be passed in <i>iov</i>. An implementation can advertise its limit by defining <code>IOV_MAX</code> in <i>&lt;limits.h&gt;</i> or at run time via the return value from <i>sysconf(_SC_IOV_MAX)</i>. On modern Linux systems, the limit is 1024. Back in Linux 2.0 days, this limit was 16.</p>
<h3>C library/kernel differences</h3>
<p> The raw <code>preadv</code>() and <code>pwritev</code>() system calls have call signatures that differ slightly from that of the corresponding GNU C library wrapper functions shown in the SYNOPSIS. The final argument, <i>offset</i>, is unpacked by the wrapper functions into two arguments in the system calls: </p>
<p> <code> unsigned long </code><i>pos_l</i><code>, unsigned long </code><i>pos</i> </p>
<p> These arguments contain, respectively, the low order and high order 32 bits of <i>offset</i>.</p>
<h3>Historical C library/kernel differences</h3>
<p> To deal with the fact that <code>IOV_MAX</code> was so low on early versions of Linux, the glibc wrapper functions for <code>readv</code>() and <code>writev</code>() did some extra work if they detected that the underlying kernel system call failed because this limit was exceeded. In the case of <code>readv</code>(), the wrapper function allocated a temporary buffer large enough for all of the items specified by <i>iov</i>, passed that buffer in a call to <code><a href="/docs/linux/man/2-read/">read</a></code>(2), copied data from the buffer to the locations specified by the <i>iov_base</i> fields of the elements of <i>iov</i>, and then freed the buffer. The wrapper function for <code>writev</code>() performed the analogous task using a temporary buffer and a call to <code><a href="/docs/linux/man/2-write/">write</a></code>(2). </p>
<p> The need for this extra effort in the glibc wrapper functions went away with Linux 2.2 and later. However, glibc continued to provide this behavior until version 2.10. Starting with glibc version 2.9, the wrapper functions provide this behavior only if the library detects that the system is running a Linux kernel older than version 2.6.18 (an arbitrarily selected kernel version). And since glibc 2.20 (which requires a minimum Linux kernel version of 2.6.32), the glibc wrapper functions always just directly invoke the system calls.</p>
<h2>EXAMPLES</h2>
<p> The following code sample demonstrates the use of <code>writev</code>(): </p>
<p> char *str0 = &quot;hello &quot;; char *str1 = &quot;world
&quot;; struct iovec iov[2]; ssize_t nwritten; </p>
<p> iov[0].iov_base = str0; iov[0].iov_len = strlen(str0); iov[1].iov_base = str1; iov[1].iov_len = strlen(str1); </p>
<p> nwritten = writev(STDOUT_FILENO, iov, 2);</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-pread/">pread</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
