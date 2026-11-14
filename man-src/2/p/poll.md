---
title: "poll(2)"
name: "poll"
section: "2"
letter: "p"
url: "/docs/linux/man/2-poll/"
description: "poll, ppoll – wait for some event on a file descriptor"
---

<h2 class="name">NAME</h2>
<p> poll, ppoll &#8211; wait for some event on a file descriptor </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;poll.h&gt;
int poll(struct pollfd *fds, nfds_t nfds, int timeout);
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;poll.h&gt;
#include &lt;signal.h&gt;
int ppoll(struct pollfd *fds, nfds_t nfds,
          const struct timespec *tmo_p, const sigset_t *sigmask);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>poll</code>() performs a similar task to <code><a href="/docs/linux/man/2-select/">select</a></code>(2): it waits for one of a set of file descriptors to become ready to perform I/O. The Linux-specific <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) API performs a similar task, but offers features beyond those found in <code>poll</code>(). </p>
<p> The set of file descriptors to be monitored is specified in the <i>fds</i> argument, which is an array of structures of the following form: </p>
<p> struct pollfd {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;file descriptor&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short events;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;requested events&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short revents;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;returned events&nbsp;*/ }; </p>
<p> The caller should specify the number of items in the <i>fds</i> array in <i>nfds</i>. </p>
<p> The field <i>fd</i> contains a file descriptor for an open file. If this field is negative, then the corresponding <i>events</i> field is ignored and the <i>revents</i> field returns zero. (This provides an easy way of ignoring a file descriptor for a single <code>poll</code>() call: simply negate the <i>fd</i> field. Note, however, that this technique can&#8217;t be used to ignore file descriptor 0.) </p>
<p> The field <i>events</i> is an input parameter, a bit mask specifying the events the application is interested in for the file descriptor <i>fd</i>. This field may be specified as zero, in which case the only events that can be returned in <i>revents</i> are <code>POLLHUP</code>, <code>POLLERR</code>, and <code>POLLNVAL</code> (see below). </p>
<p> The field <i>revents</i> is an output parameter, filled by the kernel with the events that actually occurred. The bits returned in <i>revents</i> can include any of those specified in <i>events</i>, or one of the values <code>POLLERR</code>, <code>POLLHUP</code>, or <code>POLLNVAL</code>. (These three bits are meaningless in the <i>events</i> field, and will be set in the <i>revents</i> field whenever the corresponding condition is true.) </p>
<p> If none of the events requested (and no error) has occurred for any of the file descriptors, then <code>poll</code>() blocks until one of the events occurs. </p>
<p> The <i>timeout</i> argument specifies the number of milliseconds that <code>poll</code>() should block waiting for a file descriptor to become ready. The call will block until either:</p>
<dl>
<dt>&bull;</p>
<dd> a file descriptor becomes ready;</p>
<dt>&bull;</p>
<dd> the call is interrupted by a signal handler; or</p>
<dt>&bull;</p>
<dd> the timeout expires.</dl>
<p> Note that the <i>timeout</i> interval will be rounded up to the system clock granularity, and kernel scheduling delays mean that the blocking interval may overrun by a small amount. Specifying a negative value in <i>timeout</i> means an infinite timeout. Specifying a <i>timeout</i> of zero causes <code>poll</code>() to return immediately, even if no file descriptors are ready. </p>
<p> The bits that may be set/returned in <i>events</i> and <i>revents</i> are defined in <i>&lt;poll.h&gt;</i>:</p>
<dl>
<dt><code>POLLIN</code></p>
<dd> There is data to read.</p>
<dt><code>POLLPRI</code></p>
<dd> There is some exceptional condition on the file descriptor. Possibilities include:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> There is out-of-band data on a TCP socket (see <code><a href="/docs/linux/man/7-tcp/">tcp</a></code>(7)).</p>
<dt>&bull;</p>
<dd> A pseudoterminal master in packet mode has seen a state change on the slave (see <code><a href="/docs/linux/man/2-ioctl_tty/">ioctl_tty</a></code>(2)).</p>
<dt>&bull;</p>
<dd> A <i>cgroup.events</i> file has been modified (see <code><a href="/docs/linux/man/7-cgroups/">cgroups</a></code>(7)).</dl>
</dl>
<dt><code>POLLOUT</code></p>
<dd> Writing is now possible, though a write larger than the available space in a socket or pipe will still block (unless <code>O_NONBLOCK</code> is set).</p>
<dt><code>POLLRDHUP</code> (since Linux 2.6.17)</p>
<dd> Stream socket peer closed connection, or shut down writing half of connection. The <code>_GNU_SOURCE</code> feature test macro must be defined (before including <i>any</i> header files) in order to obtain this definition.</p>
<dt><code>POLLERR</code></p>
<dd> Error condition (only returned in <i>revents</i>; ignored in <i>events</i>). This bit is also set for a file descriptor referring to the write end of a pipe when the read end has been closed.</p>
<dt><code>POLLHUP</code></p>
<dd> Hang up (only returned in <i>revents</i>; ignored in <i>events</i>). Note that when reading from a channel such as a pipe or a stream socket, this event merely indicates that the peer closed its end of the channel. Subsequent reads from the channel will return 0 (end of file) only after all outstanding data in the channel has been consumed.</p>
<dt><code>POLLNVAL</code></p>
<dd> Invalid request: <i>fd</i> not open (only returned in <i>revents</i>; ignored in <i>events</i>).</dl>
<p> When compiling with <code>_XOPEN_SOURCE</code> defined, one also has the following, which convey no further information beyond the bits listed above:</p>
<dl>
<dt><code>POLLRDNORM</code></p>
<dd> Equivalent to <code>POLLIN</code>.</p>
<dt><code>POLLRDBAND</code></p>
<dd> Priority band data can be read (generally unused on Linux).</p>
<dt><code>POLLWRNORM</code></p>
<dd> Equivalent to <code>POLLOUT</code>.</p>
<dt><code>POLLWRBAND</code></p>
<dd> Priority data may be written.</dl>
<p> Linux also knows about, but does not use <code>POLLMSG</code>.</p>
<h3>ppoll()</h3>
<p> The relationship between <code>poll</code>() and <code>ppoll</code>() is analogous to the relationship between <code><a href="/docs/linux/man/2-select/">select</a></code>(2) and <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2): like <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2), <code>ppoll</code>() allows an application to safely wait until either a file descriptor becomes ready or until a signal is caught. </p>
<p> Other than the difference in the precision of the <i>timeout</i> argument, the following <code>ppoll</code>() call: </p>
<p> ready = ppoll(&amp;fds, nfds, tmo_p, &amp;sigmask); </p>
<p> is nearly equivalent to <i>atomically</i> executing the following calls: </p>
<p> sigset_t origmask; int timeout; </p>
<p> timeout = (tmo_p == NULL) ? -1 :<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(tmo_p-&gt;tv_sec&nbsp;*&nbsp;1000&nbsp;+&nbsp;tmo_p-&gt;tv_nsec&nbsp;/&nbsp;1000000); pthread_sigmask(SIG_SETMASK, &amp;sigmask, &amp;origmask); ready = poll(&amp;fds, nfds, timeout); pthread_sigmask(SIG_SETMASK, &amp;origmask, NULL); </p>
<p> The above code segment is described as <i>nearly</i> equivalent because whereas a negative <i>timeout</i> value for <code>poll</code>() is interpreted as an infinite timeout, a negative value expressed in <i>*tmo_p</i> results in an error from <code>ppoll</code>(). </p>
<p> See the description of <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2) for an explanation of why <code>ppoll</code>() is necessary. </p>
<p> If the <i>sigmask</i> argument is specified as NULL, then no signal mask manipulation is performed (and thus <code>ppoll</code>() differs from <code>poll</code>() only in the precision of the <i>timeout</i> argument). </p>
<p> The <i>tmo_p</i> argument specifies an upper limit on the amount of time that <code>ppoll</code>() will block. This argument is a pointer to a structure of the following form: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;nanoseconds&nbsp;*/ }; </p>
<p> If <i>tmo_p</i> is specified as NULL, then <code>ppoll</code>() can block indefinitely.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>poll</code>() returns a nonnegative value which is the number of elements in the <i>pollfds</i> whose <i>revents</i> fields have been set to a nonzero value (indicating an event or an error). A return value of zero indicates that the system call timed out before any file descriptors became read. </p>
<p> On error, -1 is returned, and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EFAULT</code></p>
<dd> <i>fds</i> points outside the process&#8217;s accessible address space. The array given as argument was not contained in the calling program&#8217;s address space.</p>
<dt><code>EINTR</code></p>
<dd> A signal occurred before any requested event; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> The <i>nfds</i> value exceeds the <code>RLIMIT_NOFILE</code> value.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>ppoll</code>()) The timeout value expressed in <i>*ip</i> is invalid (negative).</p>
<dt><code>ENOMEM</code></p>
<dd> Unable to allocate memory for kernel data structures.</dl>
<h2>VERSIONS</h2>
<p> The <code>poll</code>() system call was introduced in Linux 2.1.23. On older kernels that lack this system call, the glibc <code>poll</code>() wrapper function provides emulation using <code><a href="/docs/linux/man/2-select/">select</a></code>(2). </p>
<p> The <code>ppoll</code>() system call was added to Linux in kernel 2.6.16. The <code>ppoll</code>() library call was added in glibc 2.4.</p>
<h2>CONFORMING TO</h2>
<p> <code>poll</code>() conforms to POSIX.1-2001 and POSIX.1-2008. <code>ppoll</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> The operation of <code>poll</code>() and <code>ppoll</code>() is not affected by the <code>O_NONBLOCK</code> flag. </p>
<p> On some other UNIX systems, <code>poll</code>() can fail with the error <code>EAGAIN</code> if the system fails to allocate kernel-internal resources, rather than <code>ENOMEM</code> as Linux does. POSIX permits this behavior. Portable programs may wish to check for <code>EAGAIN</code> and loop, just as with <code>EINTR</code>. </p>
<p> Some implementations define the nonstandard constant <code>INFTIM</code> with the value -1 for use as a <i>timeout</i> for <code>poll</code>(). This constant is not provided in glibc. </p>
<p> For a discussion of what may happen if a file descriptor being monitored by <code>poll</code>() is closed in another thread, see <code><a href="/docs/linux/man/2-select/">select</a></code>(2).</p>
<h3>C library/kernel differences</h3>
<p> The Linux <code>ppoll</code>() system call modifies its <i>tmo_p</i> argument. However, the glibc wrapper function hides this behavior by using a local variable for the timeout argument that is passed to the system call. Thus, the glibc <code>ppoll</code>() function does not modify its <i>tmo_p</i> argument. </p>
<p> The raw <code>ppoll</code>() system call has a fifth argument, <i>size_t sigsetsize</i>, which specifies the size in bytes of the <i>sigmask</i> argument. The glibc <code>ppoll</code>() wrapper function specifies this argument as a fixed value (equal to <i>sizeof(kernel_sigset_t)</i>). See <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2) for a discussion on the differences between the kernel and the libc notion of the sigset.</p>
<h2>BUGS</h2>
<p> See the discussion of spurious readiness notifications under the BUGS section of <code><a href="/docs/linux/man/2-select/">select</a></code>(2).</p>
<h2>EXAMPLES</h2>
<p> The program below opens each of the files named in its command-line arguments and monitors the resulting file descriptors for readiness to read (<code>POLLIN</code>). The program loops, repeatedly using <code>poll</code>() to monitor the file descriptors, printing the number of ready file descriptors on return. For each ready file descriptor, the program:</p>
<dl>
<dt>&bull;</p>
<dd> displays the returned <i>revents</i> field in a human-readable form;</p>
<dt>&bull;</p>
<dd> if the file descriptor is readable, reads some data from it, and displays that data on standard output; and</p>
<dt>&bull;</p>
<dd> if the file descriptors was not readable, but some other event occurred (presumably <code>POLLHUP</code>), closes the file descriptor.</dl>
<p> Suppose we run the program in one terminal, asking it to open a FIFO: </p>
<p> $ <code>mkfifo myfifo</code> $ <code>./poll_input myfifo</code> </p>
<p> In a second terminal window, we then open the FIFO for writing, write some data to it, and close the FIFO: </p>
<p> $ <code>echo aaaaabbbbbccccc &gt; myfifo</code> </p>
<p> In the terminal where we are running the program, we would then see: </p>
<p> Opened &quot;myfifo&quot; on fd 3 About to poll() Ready: 1<br />
&nbsp;<wbr>&nbsp;fd=3;&nbsp;events: POLLIN POLLHUP<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;read 10 bytes: aaaaabbbbb About to poll() Ready: 1<br />
&nbsp;<wbr>&nbsp;fd=3;&nbsp;events: POLLIN POLLHUP<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;read 6 bytes: ccccc </p>
<p> About to poll() Ready: 1<br />
&nbsp;<wbr>&nbsp;fd=3;&nbsp;events: POLLHUP<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;closing fd 3 All file descriptors closed; bye </p>
<p> In the above output, we see that <code>poll</code>() returned three times:</p>
<dl>
<dt>&bull;</p>
<dd> On the first return, the bits returned in the <i>revents</i> field were <code>POLLIN</code>, indicating that the file descriptor is readable, and <code>POLLHUP</code>, indicating that the other end of the FIFO has been closed. The program then consumed some of the available input.</p>
<dt>&bull;</p>
<dd> The second return from <code>poll</code>() also indicated <code>POLLIN</code> and <code>POLLHUP</code>; the program then consumed the last of the available input.</p>
<dt>&bull;</p>
<dd> On the final return, <code>poll</code>() indicated only <code>POLLHUP</code> on the FIFO, at which point the file descriptor was closed and the program terminated.</dl>
<h3>Program source</h3>
<p> /* poll_input.c </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Licensed under GNU General Public License v2 or later. */ #include &lt;poll.h&gt; #include &lt;fcntl.h&gt; #include &lt;sys/types.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int nfds, num_open_fds;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct pollfd&nbsp;*pfds; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;&lt;&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s file&#8230;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;num_open_fds&nbsp;=&nbsp;nfds&nbsp;=&nbsp;argc &#8211; 1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pfds&nbsp;=&nbsp;calloc(nfds, sizeof(struct pollfd));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pfds&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;malloc&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Open each file on command line, and add it&nbsp;&#8216;pfds&#8217;&nbsp;array&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;nfds;&nbsp;j++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pfds[j].fd&nbsp;=&nbsp;open(argv[j&nbsp;+&nbsp;1], O_RDONLY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pfds[j].fd&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;open&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Opened&nbsp;\&quot;%s\&quot;&nbsp;on fd&nbsp;%d
&quot;, argv[j&nbsp;+&nbsp;1], pfds[j].fd); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pfds[j].events&nbsp;=&nbsp;POLLIN;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Keep calling poll()&nbsp;as long as at least one file descriptor is<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;open&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;(num_open_fds&nbsp;&gt;&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int ready; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;About to poll()
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ready&nbsp;=&nbsp;poll(pfds, nfds, -1);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(ready&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;poll&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Ready:&nbsp;%d
&quot;, ready); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Deal with array returned by poll()&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int j&nbsp;=&nbsp;0;&nbsp;j&nbsp;&lt;&nbsp;nfds;&nbsp;j++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char buf[10]; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pfds[j].revents&nbsp;!=&nbsp;0)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;fd=%d;&nbsp;events:&nbsp;%s%s%s
&quot;, pfds[j].fd,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(pfds[j].revents&nbsp;&amp;&nbsp;POLLIN)&nbsp;<wbr>&nbsp;?&nbsp;&quot;POLLIN&nbsp;&quot;&nbsp;<wbr>&nbsp;:&nbsp;&quot;&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(pfds[j].revents&nbsp;&amp;&nbsp;POLLHUP)&nbsp;?&nbsp;&quot;POLLHUP&nbsp;&quot;&nbsp;:&nbsp;&quot;&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(pfds[j].revents&nbsp;&amp;&nbsp;POLLERR)&nbsp;?&nbsp;&quot;POLLERR&nbsp;&quot;&nbsp;:&nbsp;&quot;&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(pfds[j].revents&nbsp;&amp;&nbsp;POLLIN)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t s&nbsp;=&nbsp;read(pfds[j].fd, buf, sizeof(buf));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(s&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;read&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;read&nbsp;%zd bytes:&nbsp;%.*s
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;s,&nbsp;(int)&nbsp;s, buf);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else&nbsp;{&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;POLLERR | POLLHUP&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;closing fd&nbsp;%d
&quot;, pfds[j].fd);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(close(pfds[j].fd)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;close&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;num_open_fds&#8211;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;All file descriptors closed;&nbsp;bye
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-restart_syscall/">restart_syscall</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-select_tut/">select_tut</a></code>(2), <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
