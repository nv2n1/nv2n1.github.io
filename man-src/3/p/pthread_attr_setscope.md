---
title: "pthread_attr_setscope(3)"
name: "pthread_attr_setscope"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_attr_setscope/"
description: "pthread_attr_setscope, pthread_attr_getscope – set/get contention scope attribute in thread attributes object"
---

<p>pthread_attr_setscope, pthread_attr_getscope &#8211; set/get contention scope attribute in thread attributes object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_attr_setscope(pthread_attr_t *attr, int scope);
int pthread_attr_getscope(const pthread_attr_t *attr, int *scope);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_attr_setscope</code>() function sets the contention scope attribute of the thread attributes object referred to by <i>attr</i> to the value specified in <i>scope</i>. The contention scope attribute defines the set of threads against which a thread competes for resources such as the CPU. POSIX.1 specifies two possible values for <i>scope</i>:</p>
<dl>
<dt><code>PTHREAD_SCOPE_SYSTEM</code></p>
<dd>The thread competes for resources with all other threads in all processes on the system that are in the same scheduling allocation domain (a group of one or more processors). <code>PTHREAD_SCOPE_SYSTEM</code> threads are scheduled relative to one another according to their scheduling policy and priority.</p>
<dt><code>PTHREAD_SCOPE_PROCESS</code></p>
<dd>The thread competes for resources with all other threads in the same process that were also created with the <code>PTHREAD_SCOPE_PROCESS</code> contention scope. <code>PTHREAD_SCOPE_PROCESS</code> threads are scheduled relative to other threads in the process according to their scheduling policy and priority. POSIX.1 leaves it unspecified how these threads contend with other threads in other process on the system or with other threads in the same process that were created with the <code>PTHREAD_SCOPE_SYSTEM</code> contention scope.</dl>
<p> POSIX.1 requires that an implementation support at least one of these contention scopes. Linux supports <code>PTHREAD_SCOPE_SYSTEM</code>, but not <code>PTHREAD_SCOPE_PROCESS</code>. </p>
<p> On systems that support multiple contention scopes, then, in order for the parameter setting made by <code>pthread_attr_setscope</code>() to have effect when calling <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), the caller must use <code><a href="/docs/linux/man/3-pthread_attr_setinheritsched/">pthread_attr_setinheritsched</a></code>(3) to set the inherit-scheduler attribute of the attributes object <i>attr</i> to <code>PTHREAD_EXPLICIT_SCHED</code>. </p>
<p> The <code>pthread_attr_getscope</code>() function returns the contention scope attribute of the thread attributes object referred to by <i>attr</i> in the buffer pointed to by <i>scope</i>.</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return a nonzero error number.</p>
<h2>Errors</h2>
<p><code>pthread_attr_setscope</code>() can fail with the following errors:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd>An invalid value was specified in <i>scope</i>.</p>
<dt><code>ENOTSUP</code></p>
<dd><i>scope</i> specified the value <code>PTHREAD_SCOPE_PROCESS</code>, which is not supported on Linux.</dl>
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
<td> <code>pthread_attr_setscope</code>(), <code>pthread_attr_getscope</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>The <code>PTHREAD_SCOPE_SYSTEM</code> contention scope typically indicates that a user-space thread is bound directly to a single kernel-scheduling entity. This is the case on Linux for the obsolete LinuxThreads implementation and the modern NPTL implementation, which are both 1:1 threading implementations. </p>
<p> POSIX.1 specifies that the default contention scope is implementation-defined.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setaffinity_np/">pthread_attr_setaffinity_np</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setinheritsched/">pthread_attr_setinheritsched</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setschedparam/">pthread_attr_setschedparam</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setschedpolicy/">pthread_attr_setschedpolicy</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
