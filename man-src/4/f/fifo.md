---
title: "fifo(4)"
name: "fifo"
section: "4"
letter: "f"
url: "/docs/linux/man/4-fifo/"
description: "fifo – first-in first-out special file, named pipe"
---

<p>fifo &#8211; first-in first-out special file, named pipe</p>
<h2>Description</h2>
<p>A FIFO special file (a named pipe) is similar to a pipe, except that it is accessed as part of the file system. It can be opened by multiple processes for reading or writing. When processes are exchanging data via the FIFO, the kernel passes all data internally without writing it to the file system. Thus, the FIFO special file has no contents on the file system; the file system entry merely serves as a reference point so that processes can access the pipe using a name in the file system. </p>
<p> The kernel maintains exactly one pipe object for each FIFO special file that is opened by at least one process. The FIFO must be opened on both ends (reading and writing) before data can be passed. Normally, opening the FIFO blocks until the other end is opened also. </p>
<p> A process can open a FIFO in nonblocking mode. In this case, opening for read only will succeed even if no-one has opened on the write side yet, opening for write only will fail with <code>ENXIO</code> (no such device or address) unless the other end has already been opened. </p>
<p> Under Linux, opening a FIFO for read and write will succeed both in blocking and nonblocking mode. POSIX leaves this behavior undefined. This can be used to open a FIFO for writing while there are no readers available. A process that uses both ends of the connection in order to communicate with itself should be very careful to avoid deadlocks.</p>
<h2>Notes</h2>
<p>When a process tries to write to a FIFO that is not opened for read on the other side, the process is sent a <code>SIGPIPE</code> signal. </p>
<p> FIFO special files can be created by <code><a href="/docs/linux/man/3-mkfifo/">mkfifo</a></code>(3), and are indicated by <i>ls -l</i> with the file type &#8216;p&#8217;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-mkfifo/">mkfifo</a></code>(1), <code><a href="/docs/linux/man/2-open/">open</a></code>(2), <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-socketpair/">socketpair</a></code>(2), <code><a href="/docs/linux/man/3-mkfifo/">mkfifo</a></code>(3), <code><a href="/docs/linux/man/7-pipe/">pipe</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 3.35 of the Linux <i>man-pages</i> project. A description of the project, and information about reporting bugs, can be found at <a rel="nofollow" href="http://man7.org/linux/man-pages/.">http://man7.org/linux/man-pages/.</a> </p>
