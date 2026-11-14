---
title: "pthread_exit(3)"
name: "pthread_exit"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_exit/"
description: "pthread_exit – terminate calling thread"
---

<p>pthread_exit &#8211; terminate calling thread</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

void pthread_exit(void *retval);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_exit</code>() function terminates the calling thread and returns a value via <i>retval</i> that (if the thread is joinable) is available to another thread in the same process that calls <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3). </p>
<p> Any clean-up handlers established by <code><a href="/docs/linux/man/3-pthread_cleanup_push/">pthread_cleanup_push</a></code>(3) that have not yet been popped, are popped (in the reverse of the order in which they were pushed) and executed. If the thread has any thread-specific data, then, after the clean-up handlers have been executed, the corresponding destructor functions are called, in an unspecified order. </p>
<p> When a thread terminates, process-shared resources (e.g., mutexes, condition variables, semaphores, and file descriptors) are not released, and functions registered using <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3) are not called. </p>
<p> After the last thread in a process terminates, the process terminates as by calling <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) with an exit status of zero; thus, process-shared resources are released and functions registered using <code><a href="/docs/linux/man/3-atexit/">atexit</a></code>(3) are called.</p>
<h2>Return Value</h2>
<p>This function does not return to the caller.</p>
<h2>Errors</h2>
<p>This function always succeeds.</p>
<h2>Attributes</h2>
<p>For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>pthread_exit</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>Performing a return from the start function of any thread other than the main thread results in an implicit call to <code>pthread_exit</code>(), using the function&#8217;s return value as the thread&#8217;s exit status. </p>
<p> To allow other threads to continue execution, the main thread should terminate by calling <code>pthread_exit</code>() rather than <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3). </p>
<p> The value pointed to by <i>retval</i> should not be located on the calling thread&#8217;s stack, since the contents of that stack are undefined after the thread terminates.</p>
<h2>Bugs</h2>
<p>Currently, there are limitations in the kernel implementation logic for <code><a href="/docs/linux/man/2-wait/">wait</a></code>(2)ing on a stopped thread group with a dead thread group leader. This can manifest in problems such as a locked terminal if a stop signal is sent to a foreground process whose thread group leader has already called <code>pthread_exit</code>().</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
