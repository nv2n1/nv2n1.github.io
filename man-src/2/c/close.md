---
title: "close(2)"
name: "close"
section: "2"
letter: "c"
url: "/docs/linux/man/2-close/"
description: "close – close a file descriptor"
---

<h2 class="name">NAME</h2>
<p> close &#8211; close a file descriptor </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
int close(int fd);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>close</code>() closes a file descriptor, so that it no longer refers to any file and may be reused. Any record locks (see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)) held on the file it was associated with, and owned by the process, are removed (regardless of the file descriptor that was used to obtain the lock). </p>
<p> If <i>fd</i> is the last file descriptor referring to the underlying open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)), the resources associated with the open file description are freed; if the file descriptor was the last reference to a file which has been removed using <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2), the file is deleted.</p>
<h2>RETURN VALUE</h2>
<p> <code>close</code>() returns zero on success. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> isn&#8217;t a valid open file descriptor.</p>
<dt><code>EINTR</code></p>
<dd> The <code>close</code>() call was interrupted by a signal; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EIO</code></p>
<dd> An I/O error occurred.</p>
<dt><code>ENOSPC</code>, <code>EDQUOT</code></p>
<dd> On NFS, these errors are not normally reported against the first write which exceeds the available storage space, but instead against a subsequent <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), or <code>close</code>().</dl>
<p> See NOTES for a discussion of why <code>close</code>() should not be retried after an error.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> A successful close does not guarantee that the data has been successfully saved to disk, as the kernel uses the buffer cache to defer writes. Typically, filesystems do not flush buffers when a file is closed. If you need to be sure that the data is physically stored on the underlying disk, use <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2). (It will depend on the disk hardware at this point.) </p>
<p> The close-on-exec file descriptor flag can be used to ensure that a file descriptor is automatically closed upon a successful <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2); see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) for details.</p>
<h3>Multithreaded processes and close()</h3>
<p> It is probably unwise to close file descriptors while they may be in use by system calls in other threads in the same process. Since a file descriptor may be reused, there are some obscure race conditions that may cause unintended side effects. </p>
<p> Furthermore, consider the following scenario where two threads are performing operations on the same file descriptor:</p>
<dl>
<dt>1.</p>
<dd> One thread is blocked in an I/O system call on the file descriptor. For example, it is trying to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) to a pipe that is already full, or trying to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from a stream socket which currently has no available data.</p>
<dt>2.</p>
<dd> Another thread closes the file descriptor.</dl>
<p> The behavior in this situation varies across systems. On some systems, when the file descriptor is closed, the blocking system call returns immediately with an error. </p>
<p> On Linux (and possibly some other systems), the behavior is different. the blocking I/O system call holds a reference to the underlying open file description, and this reference keeps the description open until the I/O system call completes. (See <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for a discussion of open file descriptions.) Thus, the blocking system call in the first thread may successfully complete after the <code>close</code>() in the second thread.</p>
<h3>Dealing with error returns from close()</h3>
<p> A careful programmer will check the return value of <code>close</code>(), since it is quite possible that errors on a previous <code><a href="/docs/linux/man/2-write/">write</a></code>(2) operation are reported only on the final <code>close</code>() that releases the open file description. Failing to check the return value when closing a file may lead to <i>silent</i> loss of data. This can especially be observed with NFS and with disk quota. </p>
<p> Note, however, that a failure return should be used only for diagnostic purposes (i.e., a warning to the application that there may still be I/O pending or there may have been failed I/O) or remedial purposes (e.g., writing the file once more or creating a backup). </p>
<p> Retrying the <code>close</code>() after a failure return is the wrong thing to do, since this may cause a reused file descriptor from another thread to be closed. This can occur because the Linux kernel <i>always</i> releases the file descriptor early in the close operation, freeing it for reuse; the steps that may return an error, such as flushing data to the filesystem or device, occur only later in the close operation. </p>
<p> Many other implementations similarly always close the file descriptor (except in the case of <code>EBADF</code>, meaning that the file descriptor was invalid) even if they subsequently report an error on return from <code>close</code>(). POSIX.1 is currently silent on this point, but there are plans to mandate this behavior in the next major release of the standard. </p>
<p> A careful programmer who wants to know about I/O errors may precede <code>close</code>() with a call to <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2). </p>
<p> The <code>EINTR</code> error is a somewhat special case. Regarding the <code>EINTR</code> error, POSIX.1-2008 says: </p>
<dl>
<dt>
<dd> If <code>close</code>() is interrupted by a signal that is to be caught, it shall return -1 with <i>errno</i> set to <code>EINTR</code> and the state of <i>fildes</i> is unspecified.</dl>
<p> This permits the behavior that occurs on Linux and many other implementations, where, as with other errors that may be reported by <code>close</code>(), the file descriptor is guaranteed to be closed. However, it also permits another possibility: that the implementation returns an <code>EINTR</code> error and keeps the file descriptor open. (According to its documentation, HP-UX&#8217;s <code>close</code>() does this.) The caller must then once more use <code>close</code>() to close the file descriptor, to avoid file descriptor leaks. This divergence in implementation behaviors provides a difficult hurdle for portable applications, since on many implementations, <code>close</code>() must not be called again after an <code>EINTR</code> error, and on at least one, <code>close</code>() must be called again. There are plans to address this conundrum for the next major release of the POSIX.1 standard.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-fsync/">fsync</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-shutdown/">shutdown</a></code>(2), <code><a href="/docs/linux/man/2-unlink/">unlink</a></code>(2), <code><a href="/docs/linux/man/3-fclose/">fclose</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
<dt><a href="#lbAK">SEE ALSO</a></p>
<dd>
<dt><a href="#lbAL">COLOPHON</a></p>
<dd></dl>
