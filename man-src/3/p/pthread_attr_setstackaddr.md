---
title: "pthread_attr_setstackaddr(3)"
name: "pthread_attr_setstackaddr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_attr_setstackaddr/"
description: "pthread_attr_setstackaddr, pthread_attr_getstackaddr – set/get stack address attribute in thread attributes object"
---

<p>pthread_attr_setstackaddr, pthread_attr_getstackaddr &#8211; set/get stack address attribute in thread attributes object</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pthread.h&gt;

int pthread_attr_setstackaddr(pthread_attr_t *attr, void *stackaddr);
int pthread_attr_getstackaddr(const pthread_attr_t *attr,
                              void **stackaddr);

Compile and link with - pthread.</code></pre>
<h2>Description</h2>
<p>These functions are obsolete: <code>do not use them.</code> Use <code><a href="/docs/linux/man/3-pthread_attr_setstack/">pthread_attr_setstack</a></code>(3) and <code><a href="/docs/linux/man/3-pthread_attr_getstack/">pthread_attr_getstack</a></code>(3) instead. </p>
<p> The <code>pthread_attr_setstackaddr</code>() function sets the stack address attribute of the thread attributes object referred to by <i>attr</i> to the value specified in <i>stackaddr</i>. This attribute specifies the location of the stack that should be used by a thread that is created using the thread attributes object <i>attr</i>. </p>
<p> <i>stackaddr</i> should point to a buffer of at least <code>PTHREAD_STACK_MIN</code> bytes that was allocated by the caller. The pages of the allocated buffer should be both readable and writable. </p>
<p> The <code>pthread_attr_getstackaddr</code>() function returns the stack address attribute of the thread attributes object referred to by <i>attr</i> in the buffer pointed to by <i>stackaddr</i>.</p>
<h2>Return Value</h2>
<p>On success, these functions return 0; on error, they return a nonzero error number.</p>
<h2>Errors</h2>
<p>No errors are defined (but applications should nevertheless handle a possible error return).</p>
<h2>Versions</h2>
<p>These functions are provided by glibc since version 2.1.</p>
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
<td> <code>pthread_attr_setstackaddr</code>(), <code>pthread_attr_getstackaddr</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001 specifies these functions but marks them as obsolete. POSIX.1-2008 removes the specification of these functions.</p>
<h2>Notes</h2>
<p><i>Do not use these functions!</i> They cannot be portably used, since they provide no way of specifying the direction of growth or the range of the stack. For example, on architectures with a stack that grows downward, <i>stackaddr</i> specifies the next address past the <i>highest</i> address of the allocated stack area. However, on architectures with a stack that grows upward, <i>stackaddr</i> specifies the <i>lowest</i> address in the allocated stack area. By contrast, the <i>stackaddr</i> used by <code><a href="/docs/linux/man/3-pthread_attr_setstack/">pthread_attr_setstack</a></code>(3) and <code><a href="/docs/linux/man/3-pthread_attr_getstack/">pthread_attr_getstack</a></code>(3), is always a pointer to the lowest address in the allocated stack area (and the <i>stacksize</i> argument specifies the range of the stack).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-pthread_attr_init/">pthread_attr_init</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setstack/">pthread_attr_setstack</a></code>(3), <code><a href="/docs/linux/man/3-pthread_attr_setstacksize/">pthread_attr_setstacksize</a></code>(3), <code><a href="/docs/linux/man/3-pthread_create/">pthread_create</a></code>(3), <code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
