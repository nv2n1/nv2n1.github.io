---
title: "epoll_ctl(2)"
name: "epoll_ctl"
section: "2"
letter: "e"
url: "/docs/linux/man/2-epoll_ctl/"
description: "epoll_ctl – control interface for an epoll file descriptor"
---

<h2 class="name">NAME</h2>
<p> epoll_ctl &#8211; control interface for an epoll file descriptor </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/epoll.h&gt;</code> </p>
<p> <code>int epoll_ctl(int </code><i>epfd</i><code>, int </code><i>op</i><code>, int </code><i>fd</i><code>, struct epoll_event *</code><i>event</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> This system call is used to add, modify, or remove entries in the interest list of the <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) instance referred to by the file descriptor <i>epfd</i>. It requests that the operation <i>op</i> be performed for the target file descriptor, <i>fd</i>. </p>
<p> Valid values for the <i>op</i> argument are:</p>
<dl>
<dt><code>EPOLL_CTL_ADD</code></p>
<dd> Add an entry to the interest list of the epoll file descriptor, <i>epfd</i>. The entry includes the file descriptor, <i>fd</i>, a reference to the corresponding open file description (see <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) and <code><a href="/docs/linux/man/2-open/">open</a></code>(2)), and the settings specified in <i>event</i>.</p>
<dt><code>EPOLL_CTL_MOD</code></p>
<dd> Change the settings associated with <i>fd</i> in the interest list to the new settings specified in <i>event</i>.</p>
<dt><code>EPOLL_CTL_DEL</code></p>
<dd> Remove (deregister) the target file descriptor <i>fd</i> from the interest list. The <i>event</i> argument is ignored and can be NULL (but see BUGS below).</dl>
<p> The <i>event</i> argument describes the object linked to the file descriptor <i>fd</i>. The <i>struct epoll_event</i> is defined as: </p>
<p> typedef union epoll_data {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*ptr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u64; } epoll_data_t; </p>
<p> struct epoll_event {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;events;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Epoll events&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;epoll_data_t data;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;User data variable&nbsp;*/ }; </p>
<p> The <i>data</i> member of the <i>epoll_event</i> structure specifies data that the kernel should save and then return (via <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2)) when this file descriptor becomes ready. </p>
<p> The <i>events</i> member of the <i>epoll_event</i> structure is a bit mask composed by ORing together zero or more of the following available event types:</p>
<dl>
<dt><code>EPOLLIN</code></p>
<dd> The associated file is available for <code><a href="/docs/linux/man/2-read/">read</a></code>(2) operations.</p>
<dt><code>EPOLLOUT</code></p>
<dd> The associated file is available for <code><a href="/docs/linux/man/2-write/">write</a></code>(2) operations.</p>
<dt><code>EPOLLRDHUP</code> (since Linux 2.6.17)</p>
<dd> Stream socket peer closed connection, or shut down writing half of connection. (This flag is especially useful for writing simple code to detect peer shutdown when using edge-triggered monitoring.)</p>
<dt><code>EPOLLPRI</code></p>
<dd> There is an exceptional condition on the file descriptor. See the discussion of <code>POLLPRI</code> in <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2).</p>
<dt><code>EPOLLERR</code></p>
<dd> Error condition happened on the associated file descriptor. This event is also reported for the write end of a pipe when the read end has been closed.</p>
<dt>
<dd> <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) will always report for this event; it is not necessary to set it in <i>events</i> when calling <code>epoll_ctl</code>().</p>
<dt><code>EPOLLHUP</code></p>
<dd> Hang up happened on the associated file descriptor.</p>
<dt>
<dd> <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) will always wait for this event; it is not necessary to set it in <i>events</i> when calling <code>epoll_ctl</code>().</p>
<dt>
<dd> Note that when reading from a channel such as a pipe or a stream socket, this event merely indicates that the peer closed its end of the channel. Subsequent reads from the channel will return 0 (end of file) only after all outstanding data in the channel has been consumed.</p>
<dt><code>EPOLLET</code></p>
<dd> Requests edge-triggered notification for the associated file descriptor. The default behavior for <code>epoll</code> is level-triggered. See <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) for more detailed information about edge-triggered and level-triggered notification.</p>
<dt>
<dd> This flag is an input flag for the <i>event.events</i> field when calling <code>epoll_ctl</code>(); it is never returned by <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2).</p>
<dt><code>EPOLLONESHOT</code> (since Linux 2.6.2)</p>
<dd> Requests one-shot notification for the associated file descriptor. This means that after an event notified for the file descriptor by <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2), the file descriptor is disabled in the interest list and no other events will be reported by the <code>epoll</code> interface. The user must call <code>epoll_ctl</code>() with <code>EPOLL_CTL_MOD</code> to rearm the file descriptor with a new event mask.</p>
<dt>
<dd> This flag is an input flag for the <i>event.events</i> field when calling <code>epoll_ctl</code>(); it is never returned by <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2).</p>
<dt><code>EPOLLWAKEUP</code> (since Linux 3.5)</p>
<dd> If <code>EPOLLONESHOT</code> and <code>EPOLLET</code> are clear and the process has the <code>CAP_BLOCK_SUSPEND</code> capability, ensure that the system does not enter &quot;suspend&quot; or &quot;hibernate&quot; while this event is pending or being processed. The event is considered as being &quot;processed&quot; from the time when it is returned by a call to <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) until the next call to <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) on the same <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) file descriptor, the closure of that file descriptor, the removal of the event file descriptor with <code>EPOLL_CTL_DEL</code>, or the clearing of <code>EPOLLWAKEUP</code> for the event file descriptor with <code>EPOLL_CTL_MOD</code>. See also BUGS.</p>
<dt>
<dd> This flag is an input flag for the <i>event.events</i> field when calling <code>epoll_ctl</code>(); it is never returned by <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2).</p>
<dt><code>EPOLLEXCLUSIVE</code> (since Linux 4.5)</p>
<dd> Sets an exclusive wakeup mode for the epoll file descriptor that is being attached to the target file descriptor, <i>fd</i>. When a wakeup event occurs and multiple epoll file descriptors are attached to the same target file using <code>EPOLLEXCLUSIVE</code>, one or more of the epoll file descriptors will receive an event with <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2). The default in this scenario (when <code>EPOLLEXCLUSIVE</code> is not set) is for all epoll file descriptors to receive an event. <code>EPOLLEXCLUSIVE</code> is thus useful for avoiding thundering herd problems in certain scenarios.</p>
<dt>
<dd> If the same file descriptor is in multiple epoll instances, some with the <code>EPOLLEXCLUSIVE</code> flag, and others without, then events will be provided to all epoll instances that did not specify <code>EPOLLEXCLUSIVE</code>, and at least one of the epoll instances that did specify <code>EPOLLEXCLUSIVE</code>.</p>
<dt>
<dd> The following values may be specified in conjunction with <code>EPOLLEXCLUSIVE</code>: <code>EPOLLIN</code>, <code>EPOLLOUT</code>, <code>EPOLLWAKEUP</code>, and <code>EPOLLET</code>. <code>EPOLLHUP</code> and <code>EPOLLERR</code> can also be specified, but this is not required: as usual, these events are always reported if they occur, regardless of whether they are specified in <i>events</i>. Attempts to specify other values in <i>events</i> yield the error <code>EINVAL</code>.</p>
<dt>
<dd> <code>EPOLLEXCLUSIVE</code> may be used only in an <code>EPOLL_CTL_ADD</code> operation; attempts to employ it with <code>EPOLL_CTL_MOD</code> yield an error. If <code>EPOLLEXCLUSIVE</code> has been set using <code>epoll_ctl</code>(), then a subsequent <code>EPOLL_CTL_MOD</code> on the same <i>epfd</i>,&nbsp;<i>fd</i> pair yields an error. A call to <code>epoll_ctl</code>() that specifies <code>EPOLLEXCLUSIVE</code> in <i>events</i> and specifies the target file descriptor <i>fd</i> as an epoll instance will likewise fail. The error in all of these cases is <code>EINVAL</code>.</p>
<dt>
<dd> The <code>EPOLLEXCLUSIVE</code> flag is an input flag for the <i>event.events</i> field when calling <code>epoll_ctl</code>(); it is never returned by <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2).</dl>
<h2>RETURN VALUE</h2>
<p> When successful, <code>epoll_ctl</code>() returns zero. When an error occurs, <code>epoll_ctl</code>() returns -1 and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>epfd</i> or <i>fd</i> is not a valid file descriptor.</p>
<dt><code>EEXIST</code></p>
<dd> <i>op</i> was <code>EPOLL_CTL_ADD</code>, and the supplied file descriptor <i>fd</i> is already registered with this epoll instance.</p>
<dt><code>EINVAL</code></p>
<dd> <i>epfd</i> is not an <code>epoll</code> file descriptor, or <i>fd</i> is the same as <i>epfd</i>, or the requested operation <i>op</i> is not supported by this interface.</p>
<dt><code>EINVAL</code></p>
<dd> An invalid event type was specified along with <code>EPOLLEXCLUSIVE</code> in <i>events</i>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>op</i> was <code>EPOLL_CTL_MOD</code> and <i>events</i> included <code>EPOLLEXCLUSIVE</code>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>op</i> was <code>EPOLL_CTL_MOD</code> and the <code>EPOLLEXCLUSIVE</code> flag has previously been applied to this <i>epfd</i>,&nbsp;<i>fd</i> pair.</p>
<dt><code>EINVAL</code></p>
<dd> <code>EPOLLEXCLUSIVE</code> was specified in <i>event</i> and <i>fd</i> refers to an epoll instance.</p>
<dt><code>ELOOP</code></p>
<dd> <i>fd</i> refers to an epoll instance and this <code>EPOLL_CTL_ADD</code> operation would result in a circular loop of epoll instances monitoring one another or a nesting depth of epoll instances greater than 5.</p>
<dt><code>ENOENT</code></p>
<dd> <i>op</i> was <code>EPOLL_CTL_MOD</code> or <code>EPOLL_CTL_DEL</code>, and <i>fd</i> is not registered with this epoll instance.</p>
<dt><code>ENOMEM</code></p>
<dd> There was insufficient memory to handle the requested <i>op</i> control operation.</p>
<dt><code>ENOSPC</code></p>
<dd> The limit imposed by <i>/proc/sys/fs/epoll/max_user_watches</i> was encountered while trying to register (<code>EPOLL_CTL_ADD</code>) a new file descriptor on an epoll instance. See <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) for further details.</p>
<dt><code>EPERM</code></p>
<dd> The target file <i>fd</i> does not support <code>epoll</code>. This error can occur if <i>fd</i> refers to, for example, a regular file or a directory.</dl>
<h2>VERSIONS</h2>
<p> <code>epoll_ctl</code>() was added to the kernel in version 2.6. Library support is provided in glibc starting with version 2.3.2.</p>
<h2>CONFORMING TO</h2>
<p> <code>epoll_ctl</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> The <code>epoll</code> interface supports all file descriptors that support <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2).</p>
<h2>BUGS</h2>
<p> In kernel versions before 2.6.9, the <code>EPOLL_CTL_DEL</code> operation required a non-null pointer in <i>event</i>, even though this argument is ignored. Since Linux 2.6.9, <i>event</i> can be specified as NULL when using <code>EPOLL_CTL_DEL</code>. Applications that need to be portable to kernels before 2.6.9 should specify a non-null pointer in <i>event</i>. </p>
<p> If <code>EPOLLWAKEUP</code> is specified in <i>flags</i>, but the caller does not have the <code>CAP_BLOCK_SUSPEND</code> capability, then the <code>EPOLLWAKEUP</code> flag is <i>silently ignored</i>. This unfortunate behavior is necessary because no validity checks were performed on the <i>flags</i> argument in the original implementation, and the addition of the <code>EPOLLWAKEUP</code> with a check that caused the call to fail if the caller did not have the <code>CAP_BLOCK_SUSPEND</code> capability caused a breakage in at least one existing user-space application that happened to randomly (and uselessly) specify this bit. A robust application should therefore double check that it has the <code>CAP_BLOCK_SUSPEND</code> capability if attempting to use the <code>EPOLLWAKEUP</code> flag.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-epoll_create/">epoll_create</a></code>(2), <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
