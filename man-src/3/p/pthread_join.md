---
title: "pthread_join(3)"
name: "pthread_join"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_join/"
description: "pthread_join – join with a terminated thread"
---

<p>pthread_join &#8211; join with a terminated thread</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_join(pthread_t thread, void **retval);</code></pre>
<p> Compile and link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p>The <code>pthread_join</code>() function waits for the thread specified by <i>thread</i> to terminate. If that thread has already terminated, then <code>pthread_join</code>() returns immediately. The thread specified by <i>thread</i> must be joinable. </p>
<p> If <i>retval</i> is not NULL, then <code>pthread_join</code>() copies the exit status of the target thread (i.e., the value that the target thread supplied to <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3)) into the location pointed to by <i>retval</i>. If the target thread was canceled, then <code>PTHREAD_CANCELED</code> is placed in the location pointed to by <i>retval</i>. </p>
<p> If multiple threads simultaneously try to join with the same thread, the results are undefined. If the thread calling <code>pthread_join</code>() is canceled, then the target thread will remain joinable (i.e., it will not be detached).</p>
<h2>Return Value</h2>
<p>On success, <code>pthread_join</code>() returns 0; on error, it returns an error number.</p>
<h2>Errors</h2>
<dl>
<dt><code>EDEADLK</code></p>
<dd>A deadlock was detected (e.g., two threads tried to join with each other); or <i>thread</i> specifies the calling thread.</p>
<dt><code>EINVAL</code></p>
<dd><i>thread</i> is not a joinable thread.</p>
<dt><code>EINVAL</code></p>
<dd>Another thread is already waiting to join with this thread.</p>
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
<td> <code>pthread_join</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>After a successful call to <code>pthread_join</code>(), the caller is guaranteed that the target thread has terminated. The caller may then choose to do any clean-up that is required after termination of the thread (e.g., freeing memory or other resources that were allocated to the target thread). </p>
<p> Joining with a thread that has previously been joined results in undefined behavior. </p>
<p> Failure to join with a thread that is joinable (i.e., one that is not detached), produces a &quot;zombie thread&quot;. Avoid doing this, since each zombie thread consumes some system resources, and when enough zombie threads have accumulated, it will no longer be possible to create new threads (or processes). </p>
<p> There is no pthreads analog of <i>waitpid(-1,&nbsp;&amp;status, 0)</i>, that is, &quot;join with any terminated thread&quot;. If you believe you need this functionality, you probably need to rethink your application design. </p>
<p> All of the threads in a process are peers: any thread can join with any other thread in the process.</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_cancel/">pthread_cancel</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_detach/">pthread_detach</a></code>(3), <code><a href="/docs/linux/man/3-pthread_exit/">pthread_exit</a></code>(3), <code><a href="/docs/linux/man/3-pthread_tryjoin_np/">pthread_tryjoin_np</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
