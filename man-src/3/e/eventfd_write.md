---
title: "eventfd_write(3)"
name: "eventfd_write"
section: "3"
letter: "e"
url: "/docs/linux/man/3-eventfd_write/"
description: "eventfd – create a file descriptor for event notification"
---

<h2 class="name">NAME</h2>
<p> eventfd &#8211; create a file descriptor for event notification </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/eventfd.h&gt;</code> </p>
<p> <code>int eventfd(unsigned int </code><i>initval</i><code>, int </code><i>flags</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>eventfd</code>() creates an &quot;eventfd object&quot; that can be used as an event wait/notify mechanism by user-space applications, and by the kernel to notify user-space applications of events. The object contains an unsigned 64-bit integer (<i>uint64_t</i>) counter that is maintained by the kernel. This counter is initialized with the value specified in the argument <i>initval</i>. </p>
<p> As its return value, <code>eventfd</code>() returns a new file descriptor that can be used to refer to the eventfd object. </p>
<p> The following values may be bitwise ORed in <i>flags</i> to change the behavior of <code>eventfd</code>():</p>
<dl>
<dt><code>EFD_CLOEXEC</code> (since Linux 2.6.27)</p>
<dd> Set the close-on-exec (<code>FD_CLOEXEC</code>) flag on the new file descriptor. See the description of the <code>O_CLOEXEC</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for reasons why this may be useful.</p>
<dt><code>EFD_NONBLOCK</code> (since Linux 2.6.27)</p>
<dd> Set the <code>O_NONBLOCK</code> file status flag on the open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) referred to by the new file descriptor. Using this flag saves extra calls to <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) to achieve the same result.</p>
<dt><code>EFD_SEMAPHORE</code> (since Linux 2.6.30)</p>
<dd> Provide semaphore-like semantics for reads from the new file descriptor. See below.</dl>
<p> In Linux up to version 2.6.26, the <i>flags</i> argument is unused, and must be specified as zero. </p>
<p> The following operations can be performed on the file descriptor returned by <code>eventfd</code>():</p>
<dl>
<dt><code><a href="/docs/linux/man/2-read/">read</a></code>(2)</p>
<dd> Each successful <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns an 8-byte integer. A <code><a href="/docs/linux/man/2-read/">read</a></code>(2) fails with the error <code>EINVAL</code> if the size of the supplied buffer is less than 8 bytes.</p>
<dt>
<dd> The value returned by <code><a href="/docs/linux/man/2-read/">read</a></code>(2) is in host byte order&#8212;that is, the native byte order for integers on the host machine.</p>
<dt>
<dd> The semantics of <code><a href="/docs/linux/man/2-read/">read</a></code>(2) depend on whether the eventfd counter currently has a nonzero value and whether the <code>EFD_SEMAPHORE</code> flag was specified when creating the eventfd file descriptor:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> If <code>EFD_SEMAPHORE</code> was not specified and the eventfd counter has a nonzero value, then a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns 8 bytes containing that value, and the counter&#8217;s value is reset to zero.</p>
<dt>*</p>
<dd> If <code>EFD_SEMAPHORE</code> was specified and the eventfd counter has a nonzero value, then a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns 8 bytes containing the value 1, and the counter&#8217;s value is decremented by 1.</p>
<dt>*</p>
<dd> If the eventfd counter is zero at the time of the call to <code><a href="/docs/linux/man/2-read/">read</a></code>(2), then the call either blocks until the counter becomes nonzero (at which time, the <code><a href="/docs/linux/man/2-read/">read</a></code>(2) proceeds as described above) or fails with the error <code>EAGAIN</code> if the file descriptor has been made nonblocking.</dl>
</dl>
<dt><code><a href="/docs/linux/man/2-write/">write</a></code>(2)</p>
<dd> A <code><a href="/docs/linux/man/2-write/">write</a></code>(2) call adds the 8-byte integer value supplied in its buffer to the counter. The maximum value that may be stored in the counter is the largest unsigned 64-bit value minus 1 (i.e., 0xfffffffffffffffe). If the addition would cause the counter&#8217;s value to exceed the maximum, then the <code><a href="/docs/linux/man/2-write/">write</a></code>(2) either blocks until a <code><a href="/docs/linux/man/2-read/">read</a></code>(2) is performed on the file descriptor, or fails with the error <code>EAGAIN</code> if the file descriptor has been made nonblocking.</p>
<dt>
<dd> A <code><a href="/docs/linux/man/2-write/">write</a></code>(2) fails with the error <code>EINVAL</code> if the size of the supplied buffer is less than 8 bytes, or if an attempt is made to write the value 0xffffffffffffffff.</p>
<dt><code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2) (and similar)</p>
<dd> The returned file descriptor supports <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) (and analogously <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7)) and <code><a href="/docs/linux/man/2-select/">select</a></code>(2), as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> The file descriptor is readable (the <code><a href="/docs/linux/man/2-select/">select</a></code>(2) <i>readfds</i> argument; the <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) <code>POLLIN</code> flag) if the counter has a value greater than 0.</p>
<dt>*</p>
<dd> The file descriptor is writable (the <code><a href="/docs/linux/man/2-select/">select</a></code>(2) <i>writefds</i> argument; the <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) <code>POLLOUT</code> flag) if it is possible to write a value of at least &quot;1&quot; without blocking.</p>
<dt>*</p>
<dd> If an overflow of the counter value was detected, then <code><a href="/docs/linux/man/2-select/">select</a></code>(2) indicates the file descriptor as being both readable and writable, and <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) returns a <code>POLLERR</code> event. As noted above, <code><a href="/docs/linux/man/2-write/">write</a></code>(2) can never overflow the counter. However an overflow can occur if 2^64 eventfd &quot;signal posts&quot; were performed by the KAIO subsystem (theoretically possible, but practically unlikely). If an overflow has occurred, then <code><a href="/docs/linux/man/2-read/">read</a></code>(2) will return that maximum <i>uint64_t</i> value (i.e., 0xffffffffffffffff).</dl>
</dl>
<dt>
<dd> The eventfd file descriptor also supports the other file-descriptor multiplexing APIs: <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2) and <code><a href="/docs/linux/man/2-ppoll/">ppoll</a></code>(2).</p>
<dt><code><a href="/docs/linux/man/2-close/">close</a></code>(2)</p>
<dd> When the file descriptor is no longer required it should be closed. When all file descriptors associated with the same eventfd object have been closed, the resources for object are freed by the kernel.</dl>
<p> A copy of the file descriptor created by <code>eventfd</code>() is inherited by the child produced by <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). The duplicate file descriptor is associated with the same eventfd object. File descriptors created by <code>eventfd</code>() are preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), unless the close-on-exec flag has been set.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>eventfd</code>() returns a new eventfd file descriptor. On error, -1 is returned and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> An unsupported value was specified in <i>flags</i>.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENODEV</code></p>
<dd> Could not mount (internal) anonymous inode device.</p>
<dt><code>ENOMEM</code></p>
<dd> There was insufficient memory to create a new eventfd file descriptor.</dl>
<h2>VERSIONS</h2>
<p> <code>eventfd</code>() is available on Linux since kernel 2.6.22. Working support is provided in glibc since version 2.8. The <code>eventfd2</code>() system call (see NOTES) is available on Linux since kernel 2.6.27. Since version 2.9, the glibc <code>eventfd</code>() wrapper will employ the <code>eventfd2</code>() system call, if it is supported by the kernel.</p>
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
<td> <code>eventfd</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> <code>eventfd</code>() and <code>eventfd2</code>() are Linux-specific.</p>
<h2>NOTES</h2>
<p> Applications can use an eventfd file descriptor instead of a pipe (see <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2)) in all cases where a pipe is used simply to signal events. The kernel overhead of an eventfd file descriptor is much lower than that of a pipe, and only one file descriptor is required (versus the two required for a pipe). </p>
<p> When used in the kernel, an eventfd file descriptor can provide a bridge from kernel to user space, allowing, for example, functionalities like KAIO (kernel AIO) to signal to a file descriptor that some operation is complete. </p>
<p> A key point about an eventfd file descriptor is that it can be monitored just like any other file descriptor using <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), or <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7). This means that an application can simultaneously monitor the readiness of &quot;traditional&quot; files and the readiness of other kernel mechanisms that support the eventfd interface. (Without the <code>eventfd</code>() interface, these mechanisms could not be multiplexed via <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), or <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7).) </p>
<p> The current value of an eventfd counter can be viewed via the entry for the corresponding file descriptor in the process&#8217;s <i>/proc/[pid]/fdinfo</i> directory. See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for further details.</p>
<h3>C library/kernel differences</h3>
<p> There are two underlying Linux system calls: <code>eventfd</code>() and the more recent <code>eventfd2</code>(). The former system call does not implement a <i>flags</i> argument. The latter system call implements the <i>flags</i> values described above. The glibc wrapper function will use <code>eventfd2</code>() where it is available.</p>
<h3>Additional glibc features</h3>
<p> The GNU C library defines an additional type, and two functions that attempt to abstract some of the details of reading and writing on an eventfd file descriptor: </p>
<p> typedef uint64_t eventfd_t; </p>
<p> int eventfd_read(int fd, eventfd_t *value); int eventfd_write(int fd, eventfd_t value); </p>
<p> The functions perform the read and write operations on an eventfd file descriptor, returning 0 if the correct number of bytes was transferred, or -1 otherwise.</p>
<h2>EXAMPLES</h2>
<p> The following program creates an eventfd file descriptor and then forks to create a child process. While the parent briefly sleeps, the child writes each of the integers supplied in the program&#8217;s command-line arguments to the eventfd file descriptor. When the parent has finished sleeping, it reads from the eventfd file descriptor. </p>
<p> The following shell session shows a sample run of the program: </p>
<p> $<code> ./a.out 1 2 4 7 14</code> Child writing 1 to efd Child writing 2 to efd Child writing 4 to efd Child writing 7 to efd Child writing 14 to efd Child completed write loop Parent about to read Parent read 28 (0x1c) from efd</p>
<h3>Program source</h3>
<p> #include &lt;sys/eventfd.h&gt; #include &lt;unistd.h&gt; #include &lt;inttypes.h&gt; /* Definition of PRIu64 &amp; PRIx64 */ #include &lt;stdlib.h&gt; #include &lt;stdio.h&gt; #include &lt;stdint.h&gt; /* Definition of uint64_t */ </p>
<p> #define handle_error(msg) \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{&nbsp;perror(msg);&nbsp;exit(EXIT_FAILURE);&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int efd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t u;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t s; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;num&gt;&#8230;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;efd&nbsp;=&nbsp;eventfd(0, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(efd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;eventfd&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switch&nbsp;(fork())&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case 0:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;1;&nbsp;j&nbsp;&lt;&nbsp;argc;&nbsp;j++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Child writing&nbsp;%s to efd
&quot;, argv[j]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u&nbsp;=&nbsp;strtoull(argv[j], NULL, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;strtoull()&nbsp;allows various bases&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;write(efd,&nbsp;&amp;u, sizeof(uint64_t));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;!=&nbsp;sizeof(uint64_t))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;write&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Child completed write loop
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<a href="/docs/linux/man/2-sleep/">sleep</a>(2); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Parent about to read
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s&nbsp;=&nbsp;read(efd,&nbsp;&amp;u, sizeof(uint64_t));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;!=&nbsp;sizeof(uint64_t))<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;read&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Parent read&nbsp;%&quot;PRIu64&quot;&nbsp;(%#&quot;PRIx64&quot;)&nbsp;from efd
&quot;, u, u);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case -1:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;fork&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-futex/">futex</a></code>(2), <code><a href="/docs/linux/man/2-pipe/">pipe</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-signalfd/">signalfd</a></code>(2), <code><a href="/docs/linux/man/2-timerfd_create/">timerfd_create</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7), <code><a href="/docs/linux/man/7-sem_overview/">sem_overview</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
