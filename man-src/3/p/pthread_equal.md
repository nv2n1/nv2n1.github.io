---
title: "pthread_equal(3)"
name: "pthread_equal"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_equal/"
description: "pthread_equal – compare thread IDs"
---

<p>pthread_equal &#8211; compare thread IDs</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_equal(pthread_t t1, pthread_t t2);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>The <code>pthread_equal</code>() function compares two thread identifiers.</p>
<h2>Return Value</h2>
<p>If the two thread IDs are equal, <code>pthread_equal</code>() returns a nonzero value; otherwise, it returns 0.</p>
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
<td> <code>pthread_equal</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>The <code>pthread_equal</code>() function is necessary because thread IDs should be considered opaque: there is no portable way for applications to directly compare two <i>pthread_t</i> values.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/3-pthread_self/">pthread_self</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
