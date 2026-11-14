---
title: "pselect6(2)"
name: "pselect6"
section: "2"
letter: "p"
url: "/docs/linux/man/2-pselect6/"
description: "select, pselect, FD_CLR, FD_ISSET, FD_SET, FD_ZERO – synchronous I/O multiplexing"
---

<h2 class="name">NAME</h2>
<p> select, pselect, FD_CLR, FD_ISSET, FD_SET, FD_ZERO &#8211; synchronous I/O multiplexing </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/select.h&gt;
int select(int nfds, fd_set *readfds, fd_set *writefds,
           fd_set *exceptfds, struct timeval *timeout);
void FD_CLR(int fd, fd_set *set);
int FD_ISSET(int fd, fd_set *set);
void FD_SET(int fd, fd_set *set);
void FD_ZERO(fd_set *set);
int pselect(int nfds, fd_set *readfds, fd_set *writefds,
            fd_set *exceptfds, const struct timespec *timeout,
            const sigset_t *sigmask);
</code></pre>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>pselect</code>(): _POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</p>
<h2>DESCRIPTION</h2>
<p> <code>select</code>() allows a program to monitor multiple file descriptors, waiting until one or more of the file descriptors become &quot;ready&quot; for some class of I/O operation (e.g., input possible). A file descriptor is considered ready if it is possible to perform a corresponding I/O operation (e.g., <code><a href="/docs/linux/man/2-read/">read</a></code>(2), or a sufficiently small <code><a href="/docs/linux/man/2-write/">write</a></code>(2)) without blocking. </p>
<p> <code>select</code>() can monitor only file descriptors numbers that are less than <code>FD_SETSIZE</code>; <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) do not have this limitation. See BUGS.</p>
<h3>File descriptor sets</h3>
<p> The principal arguments of <code>select</code>() are three &quot;sets&quot; of file descriptors (declared with the type <i>fd_set</i>), which allow the caller to wait for three classes of events on the specified set of file descriptors. Each of the <i>fd_set</i> arguments may be specified as NULL if no file descriptors are to be watched for the corresponding class of events. </p>
<p> <code>Note well</code>: Upon return, each of the file descriptor sets is modified in place to indicate which file descriptors are currently &quot;ready&quot;. Thus, if using <code>select</code>() within a loop, the sets <i>must be reinitialized</i> before each call. The implementation of the <i>fd_set</i> arguments as value-result arguments is a design error that is avoided in <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7). </p>
<p> The contents of a file descriptor set can be manipulated using the following macros:</p>
<dl>
<dt><code>FD_ZERO</code>()</p>
<dd> This macro clears (removes all file descriptors from) <i>set</i>. It should be employed as the first step in initializing a file descriptor set.</p>
<dt><code>FD_SET</code>()</p>
<dd> This macro adds the file descriptor <i>fd</i> to <i>set</i>. Adding a file descriptor that is already present in the set is a no-op, and does not produce an error.</p>
<dt><code>FD_CLR</code>()</p>
<dd> This macro removes the file descriptor <i>fd</i> from <i>set</i>. Removing a file descriptor that is not present in the set is a no-op, and does not produce an error.</p>
<dt><code>FD_ISSET</code>()</p>
<dd> <code>select</code>() modifies the contents of the sets according to the rules described below. After calling <code>select</code>(), the <code>FD_ISSET</code>() macro can be used to test if a file descriptor is still present in a set. <code>FD_ISSET</code>() returns nonzero if the file descriptor <i>fd</i> is present in <i>set</i>, and zero if it is not.</dl>
<h3>Arguments</h3>
<p> The arguments of <code>select</code>() are as follows:</p>
<dl>
<dt><i>readfds</i></p>
<dd> The file descriptors in this set are watched to see if they are ready for reading. A file descriptor is ready for reading if a read operation will not block; in particular, a file descriptor is also ready on end-of-file.</p>
<dt>
<dd> After <code>select</code>() has returned, <i>readfds</i> will be cleared of all file descriptors except for those that are ready for reading.</p>
<dt><i>writefds</i></p>
<dd> The file descriptors in this set are watched to see if they are ready for writing. A file descriptor is ready for writing if a write operation will not block. However, even if a file descriptor indicates as writable, a large write may still block.</p>
<dt>
<dd> After <code>select</code>() has returned, <i>writefds</i> will be cleared of all file descriptors except for those that are ready for writing.</p>
<dt><i>exceptfds</i></p>
<dd> The file descriptors in this set are watched for &quot;exceptional conditions&quot;. For examples of some exceptional conditions, see the discussion of <code>POLLPRI</code> in <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2).</p>
<dt>
<dd> After <code>select</code>() has returned, <i>exceptfds</i> will be cleared of all file descriptors except for those for which an exceptional condition has occurred.</p>
<dt><i>nfds</i></p>
<dd> This argument should be set to the highest-numbered file descriptor in any of the three sets, plus 1. The indicated file descriptors in each set are checked, up to this limit (but see BUGS).</p>
<dt><i>timeout</i></p>
<dd> The <i>timeout</i> argument is a <i>timeval</i> structure (shown below) that specifies the interval that <code>select</code>() should block waiting for a file descriptor to become ready. The call will block until either:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> a file descriptor becomes ready;</p>
<dt>&bull;</p>
<dd> the call is interrupted by a signal handler; or</p>
<dt>&bull;</p>
<dd> the timeout expires.</dl>
</dl>
<dt>
<dd> Note that the <i>timeout</i> interval will be rounded up to the system clock granularity, and kernel scheduling delays mean that the blocking interval may overrun by a small amount.</p>
<dt>
<dd> If both fields of the <i>timeval</i> structure are zero, then <code>select</code>() returns immediately. (This is useful for polling.)</p>
<dt>
<dd> If <i>timeout</i> is specified as NULL, <code>select</code>() blocks indefinitely waiting for a file descriptor to become ready.</dl>
<h3>pselect()</h3>
<p> The <code>pselect</code>() system call allows an application to safely wait until either a file descriptor becomes ready or until a signal is caught. </p>
<p> The operation of <code>select</code>() and <code>pselect</code>() is identical, other than these three differences:</p>
<dl>
<dt>&bull;</p>
<dd> <code>select</code>() uses a timeout that is a <i>struct timeval</i> (with seconds and microseconds), while <code>pselect</code>() uses a <i>struct timespec</i> (with seconds and nanoseconds).</p>
<dt>&bull;</p>
<dd> <code>select</code>() may update the <i>timeout</i> argument to indicate how much time was left. <code>pselect</code>() does not change this argument.</p>
<dt>&bull;</p>
<dd> <code>select</code>() has no <i>sigmask</i> argument, and behaves as <code>pselect</code>() called with NULL <i>sigmask</i>.</dl>
<p> <i>sigmask</i> is a pointer to a signal mask (see <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2)); if it is not NULL, then <code>pselect</code>() first replaces the current signal mask by the one pointed to by <i>sigmask</i>, then does the &quot;select&quot; function, and then restores the original signal mask. (If <i>sigmask</i> is NULL, the signal mask is not modified during the <code>pselect</code>() call.) </p>
<p> Other than the difference in the precision of the <i>timeout</i> argument, the following <code>pselect</code>() call: </p>
<p> ready = pselect(nfds, &amp;readfds, &amp;writefds, &amp;exceptfds,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;timeout,&nbsp;&amp;sigmask); </p>
<p> is equivalent to <i>atomically</i> executing the following calls: </p>
<p> sigset_t origmask; </p>
<p> pthread_sigmask(SIG_SETMASK, &amp;sigmask, &amp;origmask); ready = select(nfds, &amp;readfds, &amp;writefds, &amp;exceptfds, timeout); pthread_sigmask(SIG_SETMASK, &amp;origmask, NULL); </p>
<p> The reason that <code>pselect</code>() is needed is that if one wants to wait for either a signal or for a file descriptor to become ready, then an atomic test is needed to prevent race conditions. (Suppose the signal handler sets a global flag and returns. Then a test of this global flag followed by a call of <code>select</code>() could hang indefinitely if the signal arrived just after the test but just before the call. By contrast, <code>pselect</code>() allows one to first block signals, handle the signals that have come in, then call <code>pselect</code>() with the desired <i>sigmask</i>, avoiding the race.)</p>
<h3>The timeout</h3>
<p> The <i>timeout</i> argument for <code>select</code>() is a structure of the following type: </p>
<p> struct timeval {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;suseconds_t tv_usec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;microseconds&nbsp;*/ }; </p>
<p> The corresponding argument for <code>pselect</code>() has the following type: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;nanoseconds&nbsp;*/ }; </p>
<p> On Linux, <code>select</code>() modifies <i>timeout</i> to reflect the amount of time not slept; most other implementations do not do this. (POSIX.1 permits either behavior.) This causes problems both when Linux code which reads <i>timeout</i> is ported to other operating systems, and when code is ported to Linux that reuses a <i>struct timeval</i> for multiple <code>select</code>()s in a loop without reinitializing it. Consider <i>timeout</i> to be undefined after <code>select</code>() returns.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>select</code>() and <code>pselect</code>() return the number of file descriptors contained in the three returned descriptor sets (that is, the total number of bits that are set in <i>readfds</i>, <i>writefds</i>, <i>exceptfds</i>). The return value may be zero if the timeout expired before any file descriptors became ready. </p>
<p> On error, -1 is returned, and <i>errno</i> is set to indicate the error; the file descriptor sets are unmodified, and <i>timeout</i> becomes undefined.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> An invalid file descriptor was given in one of the sets. (Perhaps a file descriptor that was already closed, or one on which an error has occurred.) However, see BUGS.</p>
<dt><code>EINTR</code></p>
<dd> A signal was caught; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> <i>nfds</i> is negative or exceeds the <code>RLIMIT_NOFILE</code> resource limit (see <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)).</p>
<dt><code>EINVAL</code></p>
<dd> The value contained within <i>timeout</i> is invalid.</p>
<dt><code>ENOMEM</code></p>
<dd> Unable to allocate memory for internal tables.</dl>
<h2>VERSIONS</h2>
<p> <code>pselect</code>() was added to Linux in kernel 2.6.16. Prior to this, <code>pselect</code>() was emulated in glibc (but see BUGS).</p>
<h2>CONFORMING TO</h2>
<p> <code>select</code>() conforms to POSIX.1-2001, POSIX.1-2008, and 4.4BSD (<code>select</code>() first appeared in 4.2BSD). Generally portable to/from non-BSD systems supporting clones of the BSD socket layer (including System V variants). However, note that the System V variant typically sets the timeout variable before returning, but the BSD variant does not. </p>
<p> <code>pselect</code>() is defined in POSIX.1g, and in POSIX.1-2001 and POSIX.1-2008.</p>
<h2>NOTES</h2>
<p> An <i>fd_set</i> is a fixed size buffer. Executing <code>FD_CLR</code>() or <code>FD_SET</code>() with a value of <i>fd</i> that is negative or is equal to or larger than <code>FD_SETSIZE</code> will result in undefined behavior. Moreover, POSIX requires <i>fd</i> to be a valid file descriptor. </p>
<p> The operation of <code>select</code>() and <code>pselect</code>() is not affected by the <code>O_NONBLOCK</code> flag. </p>
<p> On some other UNIX systems, <code>select</code>() can fail with the error <code>EAGAIN</code> if the system fails to allocate kernel-internal resources, rather than <code>ENOMEM</code> as Linux does. POSIX specifies this error for <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), but not for <code>select</code>(). Portable programs may wish to check for <code>EAGAIN</code> and loop, just as with <code>EINTR</code>.</p>
<h3>The self-pipe trick</h3>
<p> On systems that lack <code>pselect</code>(), reliable (and more portable) signal trapping can be achieved using the self-pipe trick. In this technique, a signal handler writes a byte to a pipe whose other end is monitored by <code>select</code>() in the main program. (To avoid possibly blocking when writing to a pipe that may be full or reading from a pipe that may be empty, nonblocking I/O is used when reading from and writing to the pipe.)</p>
<h3>Emulating <a href="/docs/linux/man/3-usleep/">usleep</a>(3)</h3>
<p> Before the advent of <code><a href="/docs/linux/man/3-usleep/">usleep</a></code>(3), some code employed a call to <code>select</code>() with all three sets empty, <i>nfds</i> zero, and a non-NULL <i>timeout</i> as a fairly portable way to sleep with subsecond precision.</p>
<h3>Correspondence between select() and poll() notifications</h3>
<p> Within the Linux kernel source, we find the following definitions which show the correspondence between the readable, writable, and exceptional condition notifications of <code>select</code>() and the event notifications provided by <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) and <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7): </p>
<p> #define POLLIN_SET (EPOLLRDNORM | EPOLLRDBAND | EPOLLIN |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;EPOLLHUP | EPOLLERR)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ready for reading&nbsp;*/ #define POLLOUT_SET (EPOLLWRBAND | EPOLLWRNORM | EPOLLOUT |<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;EPOLLERR)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ready for writing&nbsp;*/ #define POLLEX_SET (EPOLLPRI)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Exceptional condition&nbsp;*/</p>
<h3>Multithreaded applications</h3>
<p> If a file descriptor being monitored by <code>select</code>() is closed in another thread, the result is unspecified. On some UNIX systems, <code>select</code>() unblocks and returns, with an indication that the file descriptor is ready (a subsequent I/O operation will likely fail with an error, unless another process reopens file descriptor between the time <code>select</code>() returned and the I/O operation is performed). On Linux (and some other systems), closing the file descriptor in another thread has no effect on <code>select</code>(). In summary, any application that relies on a particular behavior in this scenario must be considered buggy.</p>
<h3>C library/kernel differences</h3>
<p> The Linux kernel allows file descriptor sets of arbitrary size, determining the length of the sets to be checked from the value of <i>nfds</i>. However, in the glibc implementation, the <i>fd_set</i> type is fixed in size. See also BUGS. </p>
<p> The <code>pselect</code>() interface described in this page is implemented by glibc. The underlying Linux system call is named <code>pselect6</code>(). This system call has somewhat different behavior from the glibc wrapper function. </p>
<p> The Linux <code>pselect6</code>() system call modifies its <i>timeout</i> argument. However, the glibc wrapper function hides this behavior by using a local variable for the timeout argument that is passed to the system call. Thus, the glibc <code>pselect</code>() function does not modify its <i>timeout</i> argument; this is the behavior required by POSIX.1-2001. </p>
<p> The final argument of the <code>pselect6</code>() system call is not a <i>sigset_t&nbsp;*</i> pointer, but is instead a structure of the form: </p>
<p> struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;const kernel_sigset_t&nbsp;*ss;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Pointer to signal set&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t ss_len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size&nbsp;(in bytes)&nbsp;of object<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pointed to by&nbsp;&#8216;ss&#8217;&nbsp;*/ }; </p>
<p> This allows the system call to obtain both a pointer to the signal set and its size, while allowing for the fact that most architectures support a maximum of 6 arguments to a system call. See <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2) for a discussion of the difference between the kernel and libc notion of the signal set.</p>
<h3>Historical glibc details</h3>
<p> Glibc 2.0 provided an incorrect version of <code>pselect</code>() that did not take a <i>sigmask</i> argument. </p>
<p> In glibc versions 2.1 to 2.2.1, one must define <code>_GNU_SOURCE</code> in order to obtain the declaration of <code>pselect</code>() from <i>&lt;sys/select.h&gt;</i>.</p>
<h2>BUGS</h2>
<p> POSIX allows an implementation to define an upper limit, advertised via the constant <code>FD_SETSIZE</code>, on the range of file descriptors that can be specified in a file descriptor set. The Linux kernel imposes no fixed limit, but the glibc implementation makes <i>fd_set</i> a fixed-size type, with <code>FD_SETSIZE</code> defined as 1024, and the <code>FD_*</code>() macros operating according to that limit. To monitor file descriptors greater than 1023, use <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) or <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) instead. </p>
<p> According to POSIX, <code>select</code>() should check all specified file descriptors in the three file descriptor sets, up to the limit <i>nfds-1</i>. However, the current implementation ignores any file descriptor in these sets that is greater than the maximum file descriptor number that the process currently has open. According to POSIX, any such file descriptor that is specified in one of the sets should result in the error <code>EBADF</code>. </p>
<p> Starting with version 2.1, glibc provided an emulation of <code>pselect</code>() that was implemented using <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2) and <code>select</code>(). This implementation remained vulnerable to the very race condition that <code>pselect</code>() was designed to prevent. Modern versions of glibc use the (race-free) <code>pselect</code>() system call on kernels where it is provided. </p>
<p> On Linux, <code>select</code>() may report a socket file descriptor as &quot;ready for reading&quot;, while nevertheless a subsequent read blocks. This could for example happen when data has arrived but upon examination has the wrong checksum and is discarded. There may be other circumstances in which a file descriptor is spuriously reported as ready. Thus it may be safer to use <code>O_NONBLOCK</code> on sockets that should not block. </p>
<p> On Linux, <code>select</code>() also modifies <i>timeout</i> if the call is interrupted by a signal handler (i.e., the <code>EINTR</code> error return). This is not permitted by POSIX.1. The Linux <code>pselect</code>() system call has the same behavior, but the glibc wrapper hides this behavior by internally copying the <i>timeout</i> to a local variable and passing that variable to the system call.</p>
<h2>EXAMPLES</h2>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;sys/select.h&gt; </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd_set rfds;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timeval tv;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int retval; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Watch stdin&nbsp;(fd 0)&nbsp;to see when it has input.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FD_ZERO(&amp;rfds);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FD_SET(0,&nbsp;&amp;rfds); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Wait up to five seconds.&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv.tv_sec&nbsp;=&nbsp;5;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv.tv_usec&nbsp;=&nbsp;0; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;retval&nbsp;=&nbsp;select(1,&nbsp;&amp;rfds, NULL, NULL,&nbsp;&amp;tv);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Don&#8217;t rely on the value of tv now!&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(retval&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;select()&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else if&nbsp;(retval)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Data is available now.
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;FD_ISSET(0,&nbsp;&amp;rfds)&nbsp;will be true.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;No data within five seconds.
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-read/">read</a></code>(2), <code><a href="/docs/linux/man/2-recv/">recv</a></code>(2), <code><a href="/docs/linux/man/2-restart_syscall/">restart_syscall</a></code>(2), <code><a href="/docs/linux/man/2-send/">send</a></code>(2), <code><a href="/docs/linux/man/2-sigprocmask/">sigprocmask</a></code>(2), <code><a href="/docs/linux/man/2-write/">write</a></code>(2), <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7) </p>
<p> For a tutorial with discussion and examples, see <code><a href="/docs/linux/man/2-select_tut/">select_tut</a></code>(2).</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
