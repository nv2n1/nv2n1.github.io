---
title: "inotify_add_watch(2)"
name: "inotify_add_watch"
section: "2"
letter: "i"
url: "/docs/linux/man/2-inotify_add_watch/"
description: "inotify_add_watch – add a watch to an initialized inotify instance"
---

<h2 class="name">NAME</h2>
<p> inotify_add_watch &#8211; add a watch to an initialized inotify instance </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;sys/inotify.h&gt;</code> </p>
<p> <code>int inotify_add_watch(int </code><i>fd</i><code>, const char *</code><i>pathname</i><code>, uint32_t </code><i>mask</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> <code>inotify_add_watch</code>() adds a new watch, or modifies an existing watch, for the file whose location is specified in <i>pathname</i>; the caller must have read permission for this file. The <i>fd</i> argument is a file descriptor referring to the inotify instance whose watch list is to be modified. The events to be monitored for <i>pathname</i> are specified in the <i>mask</i> bit-mask argument. See <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7) for a description of the bits that can be set in <i>mask</i>. </p>
<p> A successful call to <code>inotify_add_watch</code>() returns a unique watch descriptor for this inotify instance, for the filesystem object (inode) that corresponds to <i>pathname</i>. If the filesystem object was not previously being watched by this inotify instance, then the watch descriptor is newly allocated. If the filesystem object was already being watched (perhaps via a different link to the same object), then the descriptor for the existing watch is returned. </p>
<p> The watch descriptor is returned by later <code><a href="/docs/linux/man/2-read/">read</a></code>(2)s from the inotify file descriptor. These reads fetch <i>inotify_event</i> structures (see <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7)) indicating filesystem events; the watch descriptor inside this structure identifies the object for which the event occurred.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>inotify_add_watch</code>() returns a watch descriptor (a nonnegative integer). On error, -1 is returned and <i>errno</i> is set appropriately.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> Read access to the given file is not permitted.</p>
<dt><code>EBADF</code></p>
<dd> The given file descriptor is not valid.</p>
<dt><code>EEXIST</code></p>
<dd> <i>mask</i> contains <code>IN_MASK_CREATE</code> and <i>pathname</i> refers to a file already being watched by the same <i>fd</i>.</p>
<dt><code>EFAULT</code></p>
<dd> <i>pathname</i> points outside of the process&#8217;s accessible address space.</p>
<dt><code>EINVAL</code></p>
<dd> The given event mask contains no valid events; or <i>mask</i> contains both <code>IN_MASK_ADD</code> and <code>IN_MASK_CREATE</code>; or <i>fd</i> is not an inotify file descriptor.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>pathname</i> is too long.</p>
<dt><code>ENOENT</code></p>
<dd> A directory component in <i>pathname</i> does not exist or is a dangling symbolic link.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient kernel memory was available.</p>
<dt><code>ENOSPC</code></p>
<dd> The user limit on the total number of inotify watches was reached or the kernel failed to allocate a needed resource.</p>
<dt><code>ENOTDIR</code></p>
<dd> <i>mask</i> contains <code>IN_ONLYDIR</code> and <i>pathname</i> is not a directory.</dl>
<h2>VERSIONS</h2>
<p> Inotify was merged into the 2.6.13 Linux kernel.</p>
<h2>CONFORMING TO</h2>
<p> This system call is Linux-specific.</p>
<h2>EXAMPLES</h2>
<p> See <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-inotify_init/">inotify_init</a></code>(2), <code><a href="/docs/linux/man/2-inotify_rm_watch/">inotify_rm_watch</a></code>(2), <code><a href="/docs/linux/man/7-inotify/">inotify</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
