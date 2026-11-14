---
title: "epoll(7)"
name: "epoll"
section: "7"
letter: "e"
url: "/docs/linux/man/7-epoll/"
description: "epoll – I/O event notification facility"
---

<p>epoll &#8211; I/O event notification facility</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/epoll.h&gt;</code></pre>
<h2>Description</h2>
<p>The <code>epoll</code> API performs a similar task to <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2): monitoring multiple file descriptors to see if I/O is possible on any of them. The <code>epoll</code> API can be used either as an edge-triggered or a level-triggered interface and scales well to large numbers of watched file descriptors. The central concept of the <code>epoll</code> API is the <code>epoll</code> <i>instance</i>, an in-kernel data structure which, from a user-space perspective, can be considered as a container for two lists:</p>
<dl>
<dt>&bull;</p>
<dd>The <i>interest</i> list (sometimes also called the <code>epoll</code> set): the set of file descriptors that the process has registered an interest in monitoring.</p>
<dt>&bull;</p>
<dd>The <i>ready</i> list: the set of file descriptors that are &quot;ready&quot; for I/O. The ready list is a subset of (or, more precisely, a set of references to) the file descriptors in the interest list. The ready list is dynamically populated by the kernel as a result of I/O activity on those file descriptors.</dl>
<p> The following system calls are provided to create and manage an <code>epoll</code> instance:</p>
<dl>
<dt>&bull;</p>
<dd><code><a href="/docs/linux/man/2-epoll_create/">epoll_create</a></code>(2) creates a new <code>epoll</code> instance and returns a file descriptor referring to that instance. (The more recent <code><a href="/docs/linux/man/2-epoll_create1/">epoll_create1</a></code>(2) extends the functionality of <code><a href="/docs/linux/man/2-epoll_create/">epoll_create</a></code>(2).)</p>
<dt>&bull;</p>
<dd>Interest in particular file descriptors is then registered via <code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2), which adds items to the interest list of the <code>epoll</code> instance.</p>
<dt>&bull;</p>
<dd><code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) waits for I/O events, blocking the calling thread if no events are currently available. (This system call can be thought of as fetching items from the ready list of the <code>epoll</code> instance.)</dl>
<h3>Level-triggered and edge-triggered</h3>
<p>The <code>epoll</code> event distribution interface is able to behave both as edge-triggered (ET) and as level-triggered (LT). The difference between the two mechanisms can be described as follows. Suppose that this scenario happens:</p>
<dl>
<dt>1.</p>
<dd>The file descriptor that represents the read side of a pipe (<i>rfd</i>) is registered on the <code>epoll</code> instance.</p>
<dt>2.</p>
<dd>A pipe writer writes 2 kB of data on the write side of the pipe.</p>
<dt>3.</p>
<dd>A call to <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) is done that will return <i>rfd</i> as a ready file descriptor.</p>
<dt>4.</p>
<dd>The pipe reader reads 1 kB of data from <i>rfd</i>.</p>
<dt>5.</p>
<dd>A call to <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) is done.</dl>
<p> If the <i>rfd</i> file descriptor has been added to the <code>epoll</code> interface using the <code>EPOLLET</code> (edge-triggered) flag, the call to <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) done in step <code>5</code> will probably hang despite the available data still present in the file input buffer; meanwhile the remote peer might be expecting a response based on the data it already sent. The reason for this is that edge-triggered mode delivers events only when changes occur on the monitored file descriptor. So, in step <code>5</code> the caller might end up waiting for some data that is already present inside the input buffer. In the above example, an event on <i>rfd</i> will be generated because of the write done in <code>2</code> and the event is consumed in <code>3</code>. Since the read operation done in <code>4</code> does not consume the whole buffer data, the call to <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) done in step <code>5</code> might block indefinitely. An application that employs the <code>EPOLLET</code> flag should use nonblocking file descriptors to avoid having a blocking read or write starve a task that is handling multiple file descriptors. The suggested way to use <code>epoll</code> as an edge-triggered (<code>EPOLLET</code>) interface is as follows:</p>
<dl>
<dt>a)</p>
<dd>with nonblocking file descriptors; and</p>
<dt>b)</p>
<dd>by waiting for an event only after <code><a href="/docs/linux/man/2-read/">read</a></code>(2) or <code><a href="/docs/linux/man/2-write/">write</a></code>(2) return <code>EAGAIN</code>.</dl>
<p> By contrast, when used as a level-triggered interface (the default, when <code>EPOLLET</code> is not specified), <code>epoll</code> is simply a faster <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), and can be used wherever the latter is used since it shares the same semantics. Since even with edge-triggered <code>epoll</code>, multiple events can be generated upon receipt of multiple chunks of data, the caller has the option to specify the <code>EPOLLONESHOT</code> flag, to tell <code>epoll</code> to disable the associated file descriptor after the receipt of an event with <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2). When the <code>EPOLLONESHOT</code> flag is specified, it is the caller&#8217;s responsibility to rearm the file descriptor using <code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2) with <code>EPOLL_CTL_MOD</code>. If multiple threads (or processes, if child processes have inherited the <code>epoll</code> file descriptor across <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)) are blocked in <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) waiting on the same epoll file descriptor and a file descriptor in the interest list that is marked for edge-triggered (<code>EPOLLET</code>) notification becomes ready, just one of the threads (or processes) is awoken from <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2). This provides a useful optimization for avoiding &quot;thundering herd&quot; wake-ups in some scenarios.</p>
<h3>Interaction with autosleep</h3>
<p>If the system is in <code>autosleep</code> mode via <i>/sys/power/autosleep</i> and an event happens which wakes the device from sleep, the device driver will keep the device awake only until that event is queued. To keep the device awake until the event has been processed, it is necessary to use the <code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2) <code>EPOLLWAKEUP</code> flag. When the <code>EPOLLWAKEUP</code> flag is set in the <code>events</code> field for a <i>struct epoll_event</i>, the system will be kept awake from the moment the event is queued, through the <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) call which returns the event until the subsequent <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) call. If the event should keep the system awake beyond that time, then a separate <i>wake_lock</i> should be taken before the second <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) call.</p>
<h3>/proc interfaces</h3>
<p>The following interfaces can be used to limit the amount of kernel memory consumed by epoll:</p>
<dl>
<dt><i>/proc/sys/fs/epoll/max_user_watches</i> (since Linux 2.6.28)</p>
<dd>This specifies a limit on the total number of file descriptors that a user can register across all epoll instances on the system. The limit is per real user ID. Each registered file descriptor costs roughly 90 bytes on a 32-bit kernel, and roughly 160 bytes on a 64-bit kernel. Currently, the default value for <i>max_user_watches</i> is 1/25 (4%) of the available low memory, divided by the registration cost in bytes.</dl>
<h3>Example for suggested usage</h3>
<p>While the usage of <code>epoll</code> when employed as a level-triggered interface does have the same semantics as <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), the edge-triggered usage requires more clarification to avoid stalls in the application event loop. In this example, listener is a nonblocking socket on which <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2) has been called. The function <i>do_use_fd()</i> uses the new ready file descriptor until <code>EAGAIN</code> is returned by either <code><a href="/docs/linux/man/2-read/">read</a></code>(2) or <code><a href="/docs/linux/man/2-write/">write</a></code>(2). An event-driven state machine application should, after having received <code>EAGAIN</code>, record its current state so that at the next call to <i>do_use_fd()</i> it will continue to <code><a href="/docs/linux/man/2-read/">read</a></code>(2) or <code><a href="/docs/linux/man/2-write/">write</a></code>(2) from where it stopped before. epollfd = epoll_create1(0);<br />
if (epollfd == -1) {<br />
    perror(&quot;epoll_create1&quot;);<br />
    exit(EXIT_FAILURE);<br />
}<br />
ev.events = EPOLLIN;<br />
ev.data.fd = listen_sock;<br />
if (epoll_ctl(epollfd, EPOLL_CTL_ADD, listen_sock, &amp;ev) == -1) {<br />
    perror(&quot;epoll_ctl: listen_sock&quot;);<br />
    exit(EXIT_FAILURE);<br />
}<br />
for (;;) {<br />
    nfds = epoll_wait(epollfd, events, MAX_EVENTS, -1);<br />
    if (nfds == -1) {<br />
        perror(&quot;epoll_wait&quot;);<br />
        exit(EXIT_FAILURE);<br />
    }<br />
    for (n = 0; n &lt; nfds; ++n) {<br />
        if (events[n].data.fd == listen_sock) {<br />
            conn_sock = accept(listen_sock,<br />
                               (struct sockaddr *)&amp;addr, &amp;addrlen);<br />
            if (conn_sock == -1) {<br />
                perror(&quot;accept&quot;);<br />
                exit(EXIT_FAILURE);<br />
            }<br />
            setnonblocking(conn_sock);<br />
            ev.events = EPOLLIN | EPOLLET;<br />
            ev.data.fd = conn_sock;<br />
            if (epoll_ctl(epollfd, EPOLL_CTL_ADD, conn_sock,<br />
                          &amp;ev) == -1) {<br />
                perror(&quot;epoll_ctl: conn_sock&quot;);<br />
                exit(EXIT_FAILURE);<br />
            }<br />
        } else {<br />
            do_use_fd(events[n].data.fd);<br />
        }<br />
    }<br />
} /* Code to set up listening socket, &#8216;listen_sock&#8217;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;(socket(), bind(), listen())&nbsp;omitted&nbsp;*/ </p>
<pre><code>epollfd = epoll_create1(0);
if (epollfd == -1) {
    perror(&quot;epoll_create1&quot;);
    exit(EXIT_FAILURE);
}
ev.events = EPOLLIN;
ev.data.fd = listen_sock;
if (epoll_ctl(epollfd, EPOLL_CTL_ADD, listen_sock, &amp;ev) == -1) {
    perror(&quot;epoll_ctl: listen_sock&quot;);
    exit(EXIT_FAILURE);
}
for (;;) {
    nfds = epoll_wait(epollfd, events, MAX_EVENTS, -1);
    if (nfds == -1) {
        perror(&quot;epoll_wait&quot;);
        exit(EXIT_FAILURE);
    }
    for (n = 0; n &lt; nfds; ++n) {
        if (events[n].data.fd == listen_sock) {
            conn_sock = accept(listen_sock,
                               (struct sockaddr *)&amp;addr, &amp;addrlen);
            if (conn_sock == -1) {
                perror(&quot;accept&quot;);
                exit(EXIT_FAILURE);
            }
            setnonblocking(conn_sock);
            ev.events = EPOLLIN | EPOLLET;
            ev.data.fd = conn_sock;
            if (epoll_ctl(epollfd, EPOLL_CTL_ADD, conn_sock,
                          &amp;ev) == -1) {
                perror(&quot;epoll_ctl: conn_sock&quot;);
                exit(EXIT_FAILURE);
            }
        } else {
            do_use_fd(events[n].data.fd);
        }
    }
}</code></pre>
<p> When used as an edge-triggered interface, for performance reasons, it is possible to add the file descriptor inside the <code>epoll</code> interface (<code>EPOLL_CTL_ADD</code>) once by specifying (<code>EPOLLIN</code>|<code>EPOLLOUT</code>). This allows you to avoid continuously switching between <code>EPOLLIN</code> and <code>EPOLLOUT</code> calling <code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2) with <code>EPOLL_CTL_MOD</code>.</p>
<h3>Questions and answers</h3>
<dl>
<dt>0.</p>
<dd>What is the key used to distinguish the file descriptors registered in an interest list?</p>
<dd>The key is the combination of the file descriptor number and the open file description (also known as an &quot;open file handle&quot;, the kernel&#8217;s internal representation of an open file).</p>
<dt>1.</p>
<dd>What happens if you register the same file descriptor on an <code>epoll</code> instance twice?</p>
<dd>You will probably get <code>EEXIST</code>. However, it is possible to add a duplicate (<code><a href="/docs/linux/man/2-dup/">dup</a></code>(2), <code><a href="/docs/linux/man/2-dup2/">dup2</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_DUPFD</code>) file descriptor to the same <code>epoll</code> instance. This can be a useful technique for filtering events, if the duplicate file descriptors are registered with different <i>events</i> masks.</p>
<dt>2.</p>
<dd>Can two <code>epoll</code> instances wait for the same file descriptor? If so, are events reported to both <code>epoll</code> file descriptors?</p>
<dd>Yes, and events would be reported to both. However, careful programming may be needed to do this correctly.</p>
<dt>3.</p>
<dd>Is the <code>epoll</code> file descriptor itself poll/epoll/selectable?</p>
<dd>Yes. If an <code>epoll</code> file descriptor has events waiting, then it will indicate as being readable.</p>
<dt>4.</p>
<dd>What happens if one attempts to put an <code>epoll</code> file descriptor into its own file descriptor set?</p>
<dd>The <code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2) call fails (<code>EINVAL</code>). However, you can add an <code>epoll</code> file descriptor inside another <code>epoll</code> file descriptor set.</p>
<dt>5.</p>
<dd>Can I send an <code>epoll</code> file descriptor over a UNIX domain socket to another process?</p>
<dd>Yes, but it does not make sense to do this, since the receiving process would not have copies of the file descriptors in the interest list.</p>
<dt>6.</p>
<dd>Will closing a file descriptor cause it to be removed from all <code>epoll</code> interest lists?</p>
<dd>Yes, but be aware of the following point. A file descriptor is a reference to an open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)). Whenever a file descriptor is duplicated via <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2), <code><a href="/docs/linux/man/2-dup2/">dup2</a></code>(2), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) <code>F_DUPFD</code>, or <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), a new file descriptor referring to the same open file description is created. An open file description continues to exist until all file descriptors referring to it have been closed.</p>
<dd>A file descriptor is removed from an interest list only after all the file descriptors referring to the underlying open file description have been closed. This means that even after a file descriptor that is part of an interest list has been closed, events may be reported for that file descriptor if other file descriptors referring to the same underlying file description remain open. To prevent this happening, the file descriptor must be explicitly removed from the interest list (using <code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2) <code>EPOLL_CTL_DEL</code>) before it is duplicated. Alternatively, the application must ensure that all file descriptors are closed (which may be difficult if file descriptors were duplicated behind the scenes by library functions that used <code><a href="/docs/linux/man/2-dup/">dup</a></code>(2) or <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2)).</p>
<dt>7.</p>
<dd>If more than one event occurs between <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) calls, are they combined or reported separately?</p>
<dd>They will be combined.</p>
<dt>8.</p>
<dd>Does an operation on a file descriptor affect the already collected but not yet reported events?</p>
<dd>You can do two operations on an existing file descriptor. Remove would be meaningless for this case. Modify will reread available I/O.</p>
<dt>9.</p>
<dd>Do I need to continuously read/write a file descriptor until <code>EAGAIN</code> when using the <code>EPOLLET</code> flag (edge-triggered behavior)?</p>
<dd>Receiving an event from <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2) should suggest to you that such file descriptor is ready for the requested I/O operation. You must consider it ready until the next (nonblocking) read/write yields <code>EAGAIN</code>. When and how you will use the file descriptor is entirely up to you.</p>
<dd>For packet/token-oriented files (e.g., datagram socket, terminal in canonical mode), the only way to detect the end of the read/write I/O space is to continue to read/write until <code>EAGAIN</code>.</p>
<dd>For stream-oriented files (e.g., pipe, FIFO, stream socket), the condition that the read/write I/O space is exhausted can also be detected by checking the amount of data read from / written to the target file descriptor. For example, if you call <code><a href="/docs/linux/man/2-read/">read</a></code>(2) by asking to read a certain amount of data and <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns a lower number of bytes, you can be sure of having exhausted the read I/O space for the file descriptor. The same is true when writing using <code><a href="/docs/linux/man/2-write/">write</a></code>(2). (Avoid this latter technique if you cannot guarantee that the monitored file descriptor always refers to a stream-oriented file.)</dl>
<h3>Possible pitfalls and ways to avoid them</h3>
<dl>
<dt><code>o Starvation (edge-triggered)</code></p>
<dd></dl>
<p> If there is a large amount of I/O space, it is possible that by trying to drain it the other files will not get processed causing starvation. (This problem is not specific to <code>epoll</code>.) The solution is to maintain a ready list and mark the file descriptor as ready in its associated data structure, thereby allowing the application to remember which files need to be processed but still round robin amongst all the ready files. This also supports ignoring subsequent events you receive for file descriptors that are already ready.</p>
<dl>
<dt><code>o If using an event cache&#8230;</code></p>
<dd></dl>
<p> If you use an event cache or store all the file descriptors returned from <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2), then make sure to provide a way to mark its closure dynamically (i.e., caused by a previous event&#8217;s processing). Suppose you receive 100 events from <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2), and in event #47 a condition causes event #13 to be closed. If you remove the structure and <code><a href="/docs/linux/man/2-close/">close</a></code>(2) the file descriptor for event #13, then your event cache might still say there are events waiting for that file descriptor causing confusion. One solution for this is to call, during the processing of event 47, <code>epoll_ctl</code>(<code>EPOLL_CTL_DEL</code>) to delete file descriptor 13 and <code><a href="/docs/linux/man/2-close/">close</a></code>(2), then mark its associated data structure as removed and link it to a cleanup list. If you find another event for file descriptor 13 in your batch processing, you will discover the file descriptor had been previously removed and there will be no confusion.</p>
<h2>Versions</h2>
<p>The <code>epoll</code> API was introduced in Linux kernel 2.5.44. Support was added to glibc in version 2.3.2.</p>
<h2>Conforming To</h2>
<p>The <code>epoll</code> API is Linux-specific. Some other systems provide similar mechanisms, for example, FreeBSD has <i>kqueue</i>, and Solaris has <i>/dev/poll</i>.</p>
<h2>Notes</h2>
<p>The set of file descriptors that is being monitored via an epoll file descriptor can be viewed via the entry for the epoll file descriptor in the process&#8217;s <i>/proc/[pid]/fdinfo</i> directory. See <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for further details. </p>
<p> The <code><a href="/docs/linux/man/2-kcmp/">kcmp</a></code>(2) <code>KCMP_EPOLL_TFD</code> operation can be used to test whether a file descriptor is present in an epoll instance.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-epoll_create/">epoll_create</a></code>(2), <code><a href="/docs/linux/man/2-epoll_create1/">epoll_create1</a></code>(2), <code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2), <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
