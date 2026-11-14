---
title: "pthread_kill_other_threads_np(3)"
name: "pthread_kill_other_threads_np"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_kill_other_threads_np/"
description: "pthread_kill_other_threads_np – terminate all other threads in process"
---

<p>pthread_kill_other_threads_np &#8211; terminate all other threads in process</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

void pthread_kill_other_threads_np(void);</code></pre>
<h2>Description</h2>
<p><code>pthread_kill_other_threads_np</code>() has an effect only in the LinuxThreads threading implementation. On that implementation, calling this function causes the immediate termination of all threads in the application, except the calling thread. The cancellation state and cancellation type of the to-be-terminated threads are ignored, and the cleanup handlers are not called in those threads.</p>
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
<td> <code>pthread_kill_other_threads_np</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>This function is a nonstandard GNU extension; hence the suffix &quot;_np&quot; (nonportable) in the name.</p>
<h2>Notes</h2>
<p><code>pthread_kill_other_threads_np</code>() is intended to be called just before a thread calls <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) or a similar function. This function is designed to address a limitation in the obsolete LinuxThreads implementation whereby the other threads of an application are not automatically terminated (as POSIX.1-2001 requires) during <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2). </p>
<p> In the NPTL threading implementation, <code>pthread_kill_other_threads_np</code>() exists, but does nothing. (Nothing needs to be done, because the implementation does the right thing during an <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).)</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setcancelstate/">pthread_setcancelstate</a></code>(3), <code><a href="/docs/linux/man/3-pthread_setcanceltype/">pthread_setcanceltype</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
