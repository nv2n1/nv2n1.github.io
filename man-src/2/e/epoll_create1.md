---
title: "epoll_create1(2)"
name: "epoll_create1"
section: "2"
letter: "e"
url: "/docs/linux/man/2-epoll_create1/"
description: "epoll_create, epoll_create1 – open an epoll file descriptor"
---

<h2 class="name">NAME</h2>
<p> epoll_create, epoll_create1 &#8211; open an epoll file descriptor </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/epoll.h&gt;
int epoll_create(int size);
int epoll_create1(int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>epoll_create</code>() creates a new <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) instance. Since Linux 2.6.8, the <i>size</i> argument is ignored, but must be greater than zero; see NOTES. </p>
<p> <code>epoll_create</code>() returns a file descriptor referring to the new epoll instance. This file descriptor is used for all the subsequent calls to the <code>epoll</code> interface. When no longer required, the file descriptor returned by <code>epoll_create</code>() should be closed by using <code><a href="/docs/linux/man/2-close/">close</a></code>(2). When all file descriptors referring to an epoll instance have been closed, the kernel destroys the instance and releases the associated resources for reuse.</p>
<h3>epoll_create1()</h3>
<p> If <i>flags</i> is 0, then, other than the fact that the obsolete <i>size</i> argument is dropped, <code>epoll_create1</code>() is the same as <code>epoll_create</code>(). The following value can be included in <i>flags</i> to obtain different behavior:</p>
<dl>
<dt><code>EPOLL_CLOEXEC</code></p>
<dd> Set the close-on-exec (<code>FD_CLOEXEC</code>) flag on the new file descriptor. See the description of the <code>O_CLOEXEC</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for reasons why this may be useful.</dl>
<h2>RETURN VALUE</h2>
<p> On success, these system calls return a file descriptor (a nonnegative integer). On error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>size</i> is not positive.</p>
<dt><code>EINVAL</code></p>
<dd> (<code>epoll_create1</code>()) Invalid value specified in <i>flags</i>.</p>
<dt><code>EMFILE</code></p>
<dd> The per-user limit on the number of epoll instances imposed by <i>/proc/sys/fs/epoll/max_user_instances</i> was encountered. See <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) for further details.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOMEM</code></p>
<dd> There was insufficient memory to create the kernel object.</dl>
<h2>VERSIONS</h2>
<p> <code>epoll_create</code>() was added to the kernel in version 2.6. Library support is provided in glibc starting with version 2.3.2. </p>
<p> <code>epoll_create1</code>() was added to the kernel in version 2.6.27. Library support is provided in glibc starting with version 2.9.</p>
<h2>CONFORMING TO</h2>
<p> <code>epoll_create</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> In the initial <code>epoll_create</code>() implementation, the <i>size</i> argument informed the kernel of the number of file descriptors that the caller expected to add to the <code>epoll</code> instance. The kernel used this information as a hint for the amount of space to initially allocate in internal data structures describing events. (If necessary, the kernel would allocate more space if the caller&#8217;s usage exceeded the hint given in <i>size</i>.) Nowadays, this hint is no longer required (the kernel dynamically sizes the required data structures without needing the hint), but <i>size</i> must still be greater than zero, in order to ensure backward compatibility when new <code>epoll</code> applications are run on older kernels.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-close/">close</a></code>(2), <code><a href="/docs/linux/man/2-epoll_ctl/">epoll_ctl</a></code>(2), <code><a href="/docs/linux/man/2-epoll_wait/">epoll_wait</a></code>(2), <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
