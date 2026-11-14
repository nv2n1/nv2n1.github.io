---
title: "pthread_self(3)"
name: "pthread_self"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_self/"
description: "pthread_self – obtain ID of the calling thread"
---

<p>pthread_self &#8211; obtain ID of the calling thread</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

pthread_t pthread_self(void);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_self</code>() function returns the ID of the calling thread. This is the same value that is returned in <i>*thread</i> in the <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3) call that created this thread.</p>
<h2>Return Value</h2>
<p>This function always succeeds, returning the calling thread&#8217;s ID.</p>
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
<td> <code>pthread_self</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>POSIX.1 allows an implementation wide freedom in choosing the type used to represent a thread ID; for example, representation using either an arithmetic type or a structure is permitted. Therefore, variables of type <i>pthread_t</i> can&#8217;t portably be compared using the C equality operator (<code>==</code>); use <code><a href="/docs/linux/man/3-pthread_equal/">pthread_equal</a></code>(3) instead. </p>
<p> Thread identifiers should be considered opaque: any attempt to use a thread ID other than in pthreads calls is nonportable and can lead to unspecified results. </p>
<p> Thread IDs are guaranteed to be unique only within a process. A thread ID may be reused after a terminated thread has been joined, or a detached thread has terminated. </p>
<p> The thread ID returned by <code>pthread_self</code>() is not the same thing as the kernel thread ID returned by a call to <code><a href="/docs/linux/man/2-gettid/">gettid</a></code>(2).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_equal/">pthread_equal</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
