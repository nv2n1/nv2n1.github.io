---
title: "pthread_attr_getdetachstate(3)"
name: "pthread_attr_getdetachstate"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_attr_getdetachstate/"
description: "pthread_attr_setdetachstate, pthread_attr_getdetachstate – set/get detach state attribute in thread attributes object"
---

<p>pthread_attr_setdetachstate, pthread_attr_getdetachstate &#8211; set/get detach state attribute in thread attributes object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_attr_setdetachstate(pthread_attr_t *attr, int detachstate);
int pthread_attr_getdetachstate(const pthread_attr_t *attr,
                                int *detachstate);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_attr_setdetachstate</code>() function sets the detach state attribute of the thread attributes object referred to by <i>attr</i> to the value specified in <i>detachstate</i>. The detach state attribute determines whether a thread created using the thread attributes object <i>attr</i> will be created in a joinable or a detached state. </p>
<p> The following values may be specified in <i>detachstate</i>:</p>
<dl>
<dt><code>PTHREAD_CREATE_DETACHED</code></p>
<dd>Threads that are created using <i>attr</i> will be created in a detached state.</p>
<dt><code>PTHREAD_CREATE_JOINABLE</code></p>
<dd>Threads that are created using <i>attr</i> will be created in a joinable state.</dl>
<p> The default setting of the detach state attribute in a newly initialized thread attributes object is <code>PTHREAD_CREATE_JOINABLE</code>. </p>
<p> The <code>pthread_attr_getdetachstate</code>() returns the detach state attribute of the thread attributes object <i>attr</i> in the buffer pointed to by <i>detachstate</i>.</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return a nonzero error number.</p>
<h2>Errors</h2>
<p><code>pthread_attr_setdetachstate</code>() can fail with the following error:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd>An invalid value was specified in <i>detachstate</i>.</dl>
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
<td> <code>pthread_attr_setdetachstate</code>(), <code>pthread_attr_getdetachstate</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>See <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3) for more details on detached and joinable threads. </p>
<p> A thread that is created in a joinable state should eventually either be joined using <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3) or detached using <code><a href="/docs/linux/man/3-pthread_detach/">pthread_detach</a></code>(3); see <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3). </p>
<p> It is an error to specify the thread ID of a thread that was created in a detached state in a later call to <code><a href="/docs/linux/man/3-pthread_detach/">pthread_detach</a></code>(3) or <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3).</p>
<h2>Examples</h2>
<p>See <code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_detach/">pthread_detach</a></code>(3), <code><a href="/docs/linux/man/3-pthread_join/">pthread_join</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
