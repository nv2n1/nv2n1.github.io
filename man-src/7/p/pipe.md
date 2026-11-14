---
title: "pipe(7)"
name: "pipe"
section: "7"
letter: "p"
url: "/docs/linux/man/7-pipe/"
description: "pipe – overview of pipes and FIFOs"
---

<p>pipe &#8211; overview of pipes and FIFOs</p>
<h2>Description</h2>
<p>Pipes and FIFOs (also known as named pipes) provide a unidirectional interprocess communication channel. A pipe has a <i>read end</i> and a <i>write end</i>. Data written to the write end of a pipe can be read from the read end of the pipe. A pipe is created using <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2), which creates a new pipe and returns two file descriptors, one referring to the read end of the pipe, the other referring to the write end. Pipes can be used to create a communication channel between related processes; see <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2) for an example. A FIFO (short for First In First Out) has a name within the filesystem (created using <code><a href="/docs/linux/man/3-mkfifo/">mkfifo</a></code>(3)), and is opened using <code><a href="/docs/linux/man/2-open/">open</a></code>(2). Any process may open a FIFO, assuming the file permissions allow it. The read end is opened using the <code>O_RDONLY</code> flag; the write end is opened using the <code>O_WRONLY</code> flag. See <code><a href="/docs/linux/man/7-fifo/">fifo</a></code>(7) for further details. <i>Note</i>: although FIFOs have a pathname in the filesystem, I/O on FIFOs does not involve operations on the underlying device (if there is one).</p>
<h3>I/O on pipes and FIFOs</h3>
<p>The only difference between pipes and FIFOs is the manner in which they are created and opened. Once these tasks have been accomplished, I/O on pipes and FIFOs has exactly the same semantics. If a process attempts to read from an empty pipe, then <code><a href="/docs/linux/man/2-read/">read</a></code>(2) will block until data is available. If a process attempts to write to a full pipe (see below), then <code><a href="/docs/linux/man/2-write/">write</a></code>(2) blocks until sufficient data has been read from the pipe to allow the write to complete. Nonblocking I/O is possible by using the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_SETFL</code> operation to enable the <code>O_NONBLOCK</code> open file status flag. The communication channel provided by a pipe is a <i>byte stream</i>: there is no concept of message boundaries. If all file descriptors referring to the write end of a pipe have been closed, then an attempt to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) from the pipe will see end-of-file (<code><a href="/docs/linux/man/2-read/">read</a></code>(2) will return 0). If all file descriptors referring to the read end of a pipe have been closed, then a <code><a href="/docs/linux/man/2-write/">write</a></code>(2) will cause a <code>SIGPIPE</code> signal to be generated for the calling process. If the calling process is ignoring this signal, then <code><a href="/docs/linux/man/2-write/">write</a></code>(2) fails with the error <code>EPIPE</code>. An application that uses <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2) and <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) should use suitable <code><a href="/docs/linux/man/2-close/">close</a></code>(2) calls to close unnecessary duplicate file descriptors; this ensures that end-of-file and <code>SIGPIPE</code>/<code>EPIPE</code> are delivered when appropriate. It is not possible to apply <code><a href="/docs/linux/man/2-lseek/">lseek</a></code>(2) to a pipe.</p>
<h3>Pipe capacity</h3>
<p>A pipe has a limited capacity. If the pipe is full, then a <code><a href="/docs/linux/man/2-write/">write</a></code>(2) will block or fail, depending on whether the <code>O_NONBLOCK</code> flag is set (see below). Different implementations have different limits for the pipe capacity. Applications should not rely on a particular capacity: an application should be designed so that a reading process consumes data as soon as it is available, so that a writing process does not remain blocked. In Linux versions before 2.6.11, the capacity of a pipe was the same as the system page size (e.g., 4096 bytes on i386). Since Linux 2.6.11, the pipe capacity is 16 pages (i.e., 65,536 bytes in a system with a page size of 4096 bytes). Since Linux 2.6.35, the default pipe capacity is 16 pages, but the capacity can be queried and set using the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_GETPIPE_SZ</code> and <code>F_SETPIPE_SZ</code> operations. See <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) for more information. The following <code><a href="/docs/linux/man/2-ioctl/">ioctl</a></code>(2) operation, which can be applied to a file descriptor that refers to either end of a pipe, places a count of the number of unread bytes in the pipe in the <i>int</i> buffer pointed to by the final argument of the call: </p>
<pre><code>ioctl(fd, FIONREAD, &amp;nbytes);</code></pre>
<p> The <code>FIONREAD</code> operation is not specified in any standard, but is provided on many implementations.</p>
<h3>/proc files</h3>
<p>On Linux, the following files control how much memory can be used for pipes:</p>
<dl>
<dt><i>/proc/sys/fs/pipe-max-pages</i> (only in Linux 2.6.34)</p>
<dd>An upper limit, in pages, on the capacity that an unprivileged user (one without the <code>CAP_SYS_RESOURCE</code> capability) can set for a pipe.</p>
<dd>The default value for this limit is 16 times the default pipe capacity (see above); the lower limit is two pages.</p>
<dd>This interface was removed in Linux 2.6.35, in favor of <i>/proc/sys/fs/pipe-max-size</i>.</p>
<dt><i>/proc/sys/fs/pipe-max-size</i> (since Linux 2.6.35)</p>
<dd>The maximum size (in bytes) of individual pipes that can be set by users without the <code>CAP_SYS_RESOURCE</code> capability. The value assigned to this file may be rounded upward, to reflect the value actually employed for a convenient implementation. To determine the rounded-up value, display the contents of this file after assigning a value to it.</p>
<dd>The default value for this file is 1048576 (1 MiB). The minimum value that can be assigned to this file is the system page size. Attempts to set a limit less than the page size cause <code><a href="/docs/linux/man/2-write/">write</a></code>(2) to fail with the error <code>EINVAL</code>.</p>
<dd>Since Linux 4.9, the value on this file also acts as a ceiling on the default capacity of a new pipe or newly opened FIFO.</p>
<dt><i>/proc/sys/fs/pipe-user-pages-hard</i> (since Linux 4.5)</p>
<dd>The hard limit on the total size (in pages) of all pipes created or set by a single unprivileged user (i.e., one with neither the <code>CAP_SYS_RESOURCE</code> nor the <code>CAP_SYS_ADMIN</code> capability). So long as the total number of pages allocated to pipe buffers for this user is at this limit, attempts to create new pipes will be denied, and attempts to increase a pipe&#8217;s capacity will be denied.</p>
<dd>When the value of this limit is zero (which is the default), no hard limit is applied.</p>
<dt><i>/proc/sys/fs/pipe-user-pages-soft</i> (since Linux 4.5)</p>
<dd>The soft limit on the total size (in pages) of all pipes created or set by a single unprivileged user (i.e., one with neither the <code>CAP_SYS_RESOURCE</code> nor the <code>CAP_SYS_ADMIN</code> capability). So long as the total number of pages allocated to pipe buffers for this user is at this limit, individual pipes created by a user will be limited to one page, and attempts to increase a pipe&#8217;s capacity will be denied.</p>
<dd>When the value of this limit is zero, no soft limit is applied. The default value for this file is 16384, which permits creating up to 1024 pipes with the default capacity.</dl>
<p> Before Linux 4.9, some bugs affected the handling of the <i>pipe-user-pages-soft</i> and <i>pipe-user-pages-hard</i> limits; see BUGS.</p>
<h3>Pipe_Buf</h3>
<p>POSIX.1 says that <code><a href="/docs/linux/man/2-write/">write</a></code>(2)s of less than <code>PIPE_BUF</code> bytes must be atomic: the output data is written to the pipe as a contiguous sequence. Writes of more than <code>PIPE_BUF</code> bytes may be nonatomic: the kernel may interleave the data with data written by other processes. POSIX.1 requires <code>PIPE_BUF</code> to be at least 512 bytes. (On Linux, <code>PIPE_BUF</code> is 4096 bytes.) The precise semantics depend on whether the file descriptor is nonblocking (<code>O_NONBLOCK</code>), whether there are multiple writers to the pipe, and on <i>n</i>, the number of bytes to be written:</p>
<dl>
<dt><code>O_NONBLOCK</code> disabled, <i>n</i> &lt;= <code>PIPE_BUF</code></p>
<dd>All <i>n</i> bytes are written atomically; <code><a href="/docs/linux/man/2-write/">write</a></code>(2) may block if there is not room for <i>n</i> bytes to be written immediately</p>
<dt><code>O_NONBLOCK</code> enabled, <i>n</i> &lt;= <code>PIPE_BUF</code></p>
<dd>If there is room to write <i>n</i> bytes to the pipe, then <code><a href="/docs/linux/man/2-write/">write</a></code>(2) succeeds immediately, writing all <i>n</i> bytes; otherwise <code><a href="/docs/linux/man/2-write/">write</a></code>(2) fails, with <i>errno</i> set to <code>EAGAIN</code>.</p>
<dt><code>O_NONBLOCK</code> disabled, <i>n</i> &gt; <code>PIPE_BUF</code></p>
<dd>The write is nonatomic: the data given to <code><a href="/docs/linux/man/2-write/">write</a></code>(2) may be interleaved with <code><a href="/docs/linux/man/2-write/">write</a></code>(2)s by other process; the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) blocks until <i>n</i> bytes have been written.</p>
<dt><code>O_NONBLOCK</code> enabled, <i>n</i> &gt; <code>PIPE_BUF</code></p>
<dd>If the pipe is full, then <code><a href="/docs/linux/man/2-write/">write</a></code>(2) fails, with <i>errno</i> set to <code>EAGAIN</code>. Otherwise, from 1 to <i>n</i> bytes may be written (i.e., a &quot;partial write&quot; may occur; the caller should check the return value from <code><a href="/docs/linux/man/2-write/">write</a></code>(2) to see how many bytes were actually written), and these bytes may be interleaved with writes by other processes.</dl>
<h3>Open file status flags</h3>
<p>The only open file status flags that can be meaningfully applied to a pipe or FIFO are <code>O_NONBLOCK</code> and <code>O_ASYNC</code>. Setting the <code>O_ASYNC</code> flag for the read end of a pipe causes a signal (<code>SIGIO</code> by default) to be generated when new input becomes available on the pipe. The target for delivery of signals must be set using the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_SETOWN</code> command. On Linux, <code>O_ASYNC</code> is supported for pipes and FIFOs only since kernel 2.6.</p>
<h3>Portability notes</h3>
<p>On some systems (but not Linux), pipes are bidirectional: data can be transmitted in both directions between the pipe ends. POSIX.1 requires only unidirectional pipes. Portable applications should avoid reliance on bidirectional pipe semantics.</p>
<h3>Bugs</h3>
<p>Before Linux 4.9, some bugs affected the handling of the <i>pipe-user-pages-soft</i> and <i>pipe-user-pages-hard</i> limits when using the <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_SETPIPE_SZ</code> operation to change a pipe&#8217;s capacity:</p>
<dl>
<dt>(1)</p>
<dd>When increasing the pipe capacity, the checks against the soft and hard limits were made against existing consumption, and excluded the memory required for the increased pipe capacity. The new increase in pipe capacity could then push the total memory used by the user for pipes (possibly far) over a limit. (This could also trigger the problem described next.)</p>
<dd>Starting with Linux 4.9, the limit checking includes the memory required for the new pipe capacity.</p>
<dt>(2)</p>
<dd>The limit checks were performed even when the new pipe capacity was less than the existing pipe capacity. This could lead to problems if a user set a large pipe capacity, and then the limits were lowered, with the result that the user could no longer decrease the pipe capacity.</p>
<dd>Starting with Linux 4.9, checks against the limits are performed only when increasing a pipe&#8217;s capacity; an unprivileged user can always decrease a pipe&#8217;s capacity.</p>
<dt>(3)</p>
<dd>The accounting and checking against the limits were done as follows:</p>
<dd>
<dl>
<dd>
<dl>
<dt>(a)</p>
<dd>Test whether the user has exceeded the limit.</p>
<dt>(b)</p>
<dd>Make the new pipe buffer allocation.</p>
<dt>(c)</p>
<dd>Account new allocation against the limits.</dl>
</dl>
<dd>This was racey. Multiple processes could pass point (a) simultaneously, and then allocate pipe buffers that were accounted for only in step (c), with the result that the user&#8217;s pipe buffer allocation could be pushed over the limit.</p>
<dd>Starting with Linux 4.9, the accounting step is performed before doing the allocation, and the operation fails if the limit would be exceeded.</dl>
<p> Before Linux 4.9, bugs similar to points (1) and (3) could also occur when the kernel allocated memory for a new pipe buffer; that is, when calling <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2) and when opening a previously unopened FIFO.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mkfifo/">mkfifo</a></code>(1), <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2), <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/2-tee/">tee</a></code>(2), <code><a href="/docs/linux/man/2-vmsplice/">vmsplice</a></code>(2), <code><a href="/docs/linux/man/3-mkfifo/">mkfifo</a></code>(3), <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7), <code><a href="/docs/linux/man/7-fifo/">fifo</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
