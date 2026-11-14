---
title: "pthread_detach(3)"
name: "pthread_detach"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_detach/"
description: "pthread_detach – detach a thread"
---

<p>pthread_detach &#8211; detach a thread</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_detach(pthread_t thread);</code></pre>
<p> Compile and link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p>The <code>pthread_detach</code>() function marks the thread identified by <i>thread</i> as detached. When a detached thread terminates, its resources are automatically released back to the system without the need for another thread to join with the terminated thread. </p>
<p> Attempting to detach an already detached thread results in unspecified behavior.</p>
<h2>Return Value</h2>
<p>On success, <code>pthread_detach</code>() returns 0; on error, it returns an error number.</p>
<h2>Errors</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd><i>thread</i> is not a joinable thread.</p>
<dt><code>ESRCH</code></p>
<dd>No thread with the ID <i>thread</i> could be found.</dl>
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
<td> <code>pthread_detach</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>Once a thread has been detached, it can&#8217;t be joined with <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3) or be made joinable again. </p>
<p> A new thread can be created in a detached state using <code><a href="/docs/linux/man/3-pthread_attr_setdetachstate/">pthread_attr_setdetachstate</a></code>(3) to set the detached attribute of the <i>attr</i> argument of <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3). </p>
<p> The detached attribute merely determines the behavior of the system when the thread terminates; it does not prevent the thread from being terminated if the process terminates using <code><a href="/docs/linux/man/3-exit/">exit</a></code>(3) (or equivalently, if the main thread returns). </p>
<p> Either <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3) or <code>pthread_detach</code>() should be called for each thread that an application creates, so that system resources for the thread can be released. (But note that the resources of any threads for which one of these actions has not been done will be freed when the process terminates.)</p>
<h2>Examples</h2>
<p>The following statement detaches the calling thread: </p>
<pre><code>pthread_detach(pthread_self());</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_attr_setdetachstate/">pthread_attr_setdetachstate</a></code>(3), <code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3), <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
