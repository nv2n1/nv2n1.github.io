---
title: "inotify_rm_watch(2)"
name: "inotify_rm_watch"
section: "2"
letter: "i"
url: "/docs/linux/man/2-inotify_rm_watch/"
description: "inotify_rm_watch – remove an existing watch from an inotify instance"
---

<h2 class="name">NAME</h2>
<p> inotify_rm_watch &#8211; remove an existing watch from an inotify instance </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/inotify.h&gt;</code> </p>
<p> <code>int inotify_rm_watch(int </code><i>fd</i><code>, int </code><i>wd</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>inotify_rm_watch</code>() removes the watch associated with the watch descriptor <i>wd</i> from the inotify instance associated with the file descriptor <i>fd</i>. </p>
<p> Removing a watch causes an <code>IN_IGNORED</code> event to be generated for this watch descriptor. (See <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7).)</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>inotify_rm_watch</code>() returns zero. On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EBADF</code></p>
<dd> <i>fd</i> is not a valid file descriptor.</p>
<dt><code>EINVAL</code></p>
<dd> The watch descriptor <i>wd</i> is not valid; or <i>fd</i> is not an inotify file descriptor.</dl>
<h2>VERSIONS</h2>
<p> Inotify was merged into the 2.6.13 Linux kernel.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-inotify_add_watch/">inotify_add_watch</a></code>(2), <code><a href="/docs/linux/man/2-inotify_init/">inotify_init</a></code>(2), <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
