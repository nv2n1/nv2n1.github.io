---
title: "inotify_init(2)"
name: "inotify_init"
section: "2"
letter: "i"
url: "/docs/linux/man/2-inotify_init/"
description: "inotify_init, inotify_init1 – initialize an inotify instance"
---

<h2 class="name">NAME</h2>
<p> inotify_init, inotify_init1 &#8211; initialize an inotify instance </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/inotify.h&gt;
int inotify_init(void);
int inotify_init1(int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> For an overview of the inotify API, see <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7). </p>
<p> <code>inotify_init</code>() initializes a new inotify instance and returns a file descriptor associated with a new inotify event queue. </p>
<p> If <i>flags</i> is 0, then <code>inotify_init1</code>() is the same as <code>inotify_init</code>(). The following values can be bitwise ORed in <i>flags</i> to obtain different behavior:</p>
<dl>
<dt><code>IN_NONBLOCK</code></p>
<dd> Set the <code>O_NONBLOCK</code> file status flag on the open file description (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) referred to by the new file descriptor. Using this flag saves extra calls to <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) to achieve the same result.</p>
<dt><code>IN_CLOEXEC</code></p>
<dd> Set the close-on-exec (<code>FD_CLOEXEC</code>) flag on the new file descriptor. See the description of the <code>O_CLOEXEC</code> flag in <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for reasons why this may be useful.</dl>
<h2>RETURN VALUE</h2>
<p> On success, these system calls return a new file descriptor. On error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EINVAL</code></p>
<dd> (<code>inotify_init1</code>()) An invalid value was specified in <i>flags</i>.</p>
<dt><code>EMFILE</code></p>
<dd> The user limit on the total number of inotify instances has been reached.</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file descriptors has been reached.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files has been reached.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory is available.</dl>
<h2>VERSIONS</h2>
<p> <code>inotify_init</code>() first appeared in Linux 2.6.13; library support was added to glibc in version 2.4. <code>inotify_init1</code>() was added in Linux 2.6.27; library support was added to glibc in version 2.9.</p>
<h2>CONFORMING TO</h2>
<p> These system calls are Linux-specific.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2), <code><a href="/docs/linux/man/2-inotify_rm_watch/">inotify_rm_watch</a></code>(2), <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
