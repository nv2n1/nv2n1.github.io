---
title: "epoll_pwait(2)"
name: "epoll_pwait"
section: "2"
letter: "e"
url: "/docs/linux/man/2-epoll_pwait/"
description: "epoll_wait, epoll_pwait – wait for an I/O event on an epoll file descriptor"
---

<h2 class="name">NAME</h2>
<p> epoll_wait, epoll_pwait &#8211; wait for an I/O event on an epoll file descriptor </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/epoll.h&gt;
int epoll_wait(int epfd, struct epoll_event *events,
               int maxevents, int timeout);
int epoll_pwait(int epfd, struct epoll_event *events,
                int maxevents, int timeout,
                const sigset_t *sigmask);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>epoll_wait</code>() system call waits for events on the <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) instance referred to by the file descriptor <i>epfd</i>. The buffer pointed to by <i>events</i> is used to return information from the ready list about file descriptors in the interest list that have some events available. Up to <i>maxevents</i> are returned by <code>epoll_wait</code>(). The <i>maxevents</i> argument must be greater than zero. </p>
<p> The <i>timeout</i> argument specifies the number of milliseconds that <code>epoll_wait</code>() will block. Time is measured against the <code>CLOCK_MONOTONIC</code> clock. </p>
<p> A call to <code>epoll_wait</code>() will block until either:</p>
<dl>
<dt>&bull;</p>
<dd> a file descriptor delivers an event;</p>
<dt>&bull;</p>
<dd> the call is interrupted by a signal handler; or</p>
<dt>&bull;</p>
<dd> the timeout expires.</dl>
<p> Note that the <i>timeout</i> interval will be rounded up to the system clock granularity, and kernel scheduling delays mean that the blocking interval may overrun by a small amount. Specifying a <i>timeout</i> of -1 causes <code>epoll_wait</code>() to block indefinitely, while specifying a <i>timeout</i> equal to zero cause <code>epoll_wait</code>() to return immediately, even if no events are available. </p>
<p> The <i>struct epoll_event</i> is defined as: </p>
<p> typedef union epoll_data {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*ptr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t u32;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t u64; } epoll_data_t; </p>
<p> struct epoll_event {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;events;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Epoll events&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;epoll_data_t data;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;User data variable&nbsp;*/ }; </p>
<p> The <i>data</i> field of each returned <i>epoll_event</i> structure contains the same data as was specified in the most recent call to <code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2) (<code>EPOLL_CTL_ADD</code>, <code>EPOLL_CTL_MOD</code>) for the corresponding open file descriptor. </p>
<p> The <i>events</i> field is a bit mask that indicates the events that have occurred for the corresponding open file description. See <code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2) for a list of the bits that may appear in this mask.</p>
<h3>epoll_pwait()</h3>
<p> The relationship between <code>epoll_wait</code>() and <code>epoll_pwait</code>() is analogous to the relationship between <code><a href="/docs/linux/man/2-select/">select</a></code>(2) and <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2): like <code><a href="/docs/linux/man/2-pselect/">pselect</a></code>(2), <code>epoll_pwait</code>() allows an application to safely wait until either a file descriptor becomes ready or until a signal is caught. </p>
<p> The following <code>epoll_pwait</code>() call: </p>
<p> ready = epoll_pwait(epfd, &amp;events, maxevents, timeout, &amp;sigmask); </p>
<p> is equivalent to <i>atomically</i> executing the following calls: </p>
<p> sigset_t origmask; </p>
<p> pthread_sigmask(SIG_SETMASK, &amp;sigmask, &amp;origmask); ready = epoll_wait(epfd, &amp;events, maxevents, timeout); pthread_sigmask(SIG_SETMASK, &amp;origmask, NULL); </p>
<p> The <i>sigmask</i> argument may be specified as NULL, in which case <code>epoll_pwait</code>() is equivalent to <code>epoll_wait</code>().</p>
<h2>RETURN VALUE</h2>
<p> When successful, <code>epoll_wait</code>() returns the number of file descriptors ready for the requested I/O, or zero if no file descriptor became ready during the requested <i>timeout</i> milliseconds. When an error occurs, <code>epoll_wait</code>() returns -1 and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>epfd</i> is not a valid file descriptor.</p>
<dt><code>EFAULT</code></p>
<dd> The memory area pointed to by <i>events</i> is not accessible with write permissions.</p>
<dt><code>EINTR</code></p>
<dd> The call was interrupted by a signal handler before either (1) any of the requested events occurred or (2) the <i>timeout</i> expired; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> <i>epfd</i> is not an <code>epoll</code> file descriptor, or <i>maxevents</i> is less than or equal to zero.</dl>
<h2>VERSIONS</h2>
<p> <code>epoll_wait</code>() was added to the kernel in version 2.6. Library support is provided in glibc starting with version 2.3.2. </p>
<p> <code>epoll_pwait</code>() was added to Linux in kernel 2.6.19. Library support is provided in glibc starting with version 2.6.</p>
<h2>CONFORMING TO</h2>
<p> <code>epoll_wait</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> While one thread is blocked in a call to <code>epoll_wait</code>(), it is possible for another thread to add a file descriptor to the waited-upon <code>epoll</code> instance. If the new file descriptor becomes ready, it will cause the <code>epoll_wait</code>() call to unblock. </p>
<p> If more than <i>maxevents</i> file descriptors are ready when <code>epoll_wait</code>() is called, then successive <code>epoll_wait</code>() calls will round robin through the set of ready file descriptors. This behavior helps avoid starvation scenarios, where a process fails to notice that additional file descriptors are ready because it focuses on a set of file descriptors that are already known to be ready. </p>
<p> Note that it is possible to call <code>epoll_wait</code>() on an <code>epoll</code> instance whose interest list is currently empty (or whose interest list becomes empty because file descriptors are closed or removed from the interest in another thread). The call will block until some file descriptor is later added to the interest list (in another thread) and that file descriptor becomes ready.</p>
<h2>BUGS</h2>
<p> In kernels before 2.6.37, a <i>timeout</i> value larger than approximately <i>LONG_MAX / HZ</i> milliseconds is treated as -1 (i.e., infinity). Thus, for example, on a system where <i>sizeof(long)</i> is 4 and the kernel <i>HZ</i> value is 1000, this means that timeouts greater than 35.79 minutes are treated as infinity.</p>
<h3>C library/kernel differences</h3>
<p> The raw <code>epoll_pwait</code>() system call has a sixth argument, <i>size_t sigsetsize</i>, which specifies the size in bytes of the <i>sigmask</i> argument. The glibc <code>epoll_pwait</code>() wrapper function specifies this argument as a fixed value (equal to <i>sizeof(sigset_t)</i>).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-epoll_create/">epoll_create</a></code>(2), <code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2), <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
