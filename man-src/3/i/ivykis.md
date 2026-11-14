---
title: "ivykis(3)"
name: "ivykis"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ivykis/"
description: "ivykis – library for asynchronous I/O readiness notification"
---

<h2>NAME</h2>
<p> ivykis &#8211; library for asynchronous I/O readiness notification</p>
<h2>DESCRIPTION</h2>
<p> ivykis is a library for asynchronous I/O readiness notification. It is a thin, portable wrapper around OS-provided mechanisms such as <code><a href="/docs/linux/man/2-epoll_create/">epoll_create</a></code>(2), <code><a href="/docs/linux/man/2-kqueue/">kqueue</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="//www.systutorials.com/docs/linux/man/7d-poll/">poll</a></code>(7d) (/dev/poll) and <code><a href="//www.systutorials.com/docs/linux/man/3C-port_create/">port_create</a></code>(3C). </p>
<p> ivykis was mainly designed for building high-performance network applications, but can be used in any event-driven application that uses <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2)able file descriptors as its event sources. </p>
<p> While some programming models dictate using blocking I/O and starting a thread per event source, programs written to the ivykis API are generally single-threaded (or use only a small number of threads), and never block on I/O. All input and output is done in a nonblocking fashion, with I/O readiness notifications delivered via callback functions. </p>
<p> The two main event sources in ivykis are file descriptors and timers. File descriptors generate an event when they become readable or writable or trigger an error condition, while timers generate an event when the system time increments past a certain pre-set time. Events associated with file descriptors are level-triggered &#8212; a callback function set up to handle a certain file descriptor event will be called repeatedly until the condition generating the event has been cleared. </p>
<p> As mentioned, applications using ivykis are generally single-threaded. Event callbacks are strictly serialised within a thread, and non-preemptible. This mostly removes the need for locking of shared data, and generally simplifies writing applications. </p>
<p> Each thread that uses ivykis has its own file descriptors and timers, and runs a separate event loop. </p>
<p> In ivykis, all code that is not initialization code runs from callback functions. Callback functions are not allowed to block. If a particular piece of code wants to perform a certain operation that can block, it either has to schedule it to run in a separate thread, or it has to perform the operation in a nonblocking fashion instead. For example, registering an input callback function instead of blocking on a read, registering a timer instead of calling <code><a href="/docs/linux/man/2-sleep/">sleep</a></code>(2), etc. </p>
<p> In case of an internal error, ivykis will use <code><a href="/docs/linux/man/3-iv_fatal/">iv_fatal</a></code>(3) to report the error. The application can provide a custom fatal error handler by calling <code><a href="/docs/linux/man/3-iv_set_fatal_msg_handler/">iv_set_fatal_msg_handler</a></code>(3).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-iv_examples/">iv_examples</a></code>(3), <code><a href="/docs/linux/man/3-iv_fatal/">iv_fatal</a></code>(3), <code><a href="/docs/linux/man/3-iv_fd/">iv_fd</a></code>(3), <code><a href="/docs/linux/man/3-iv_timer/">iv_timer</a></code>(3), <code><a href="/docs/linux/man/3-iv_task/">iv_task</a></code>(3), <code><a href="/docs/linux/man/3-iv_init/">iv_init</a></code>(3), <code><a href="/docs/linux/man/3-iv_main/">iv_main</a></code>(3), <code><a href="/docs/linux/man/3-iv_time/">iv_time</a></code>(3) </p>
<h2>Index</h2>
