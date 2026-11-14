---
title: "mq_getsetattr(2)"
name: "mq_getsetattr"
section: "2"
letter: "m"
url: "/docs/linux/man/2-mq_getsetattr/"
description: "mq_getsetattr – get/set message queue attributes"
---

<h2 class="name">NAME</h2>
<p> mq_getsetattr &#8211; get/set message queue attributes </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;mqueue.h&gt;
#include &lt;sys/types.h&gt;
int mq_getsetattr(mqd_t mqdes, const struct mq_attr *newattr,
                  struct mq_attr *oldattr);
</code></pre>
<p> <i>Note</i>: There is no glibc wrapper for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> Do not use this system call. </p>
<p> This is the low-level system call used to implement <code><a href="/docs/linux/man/3-mq_getattr/">mq_getattr</a></code>(3) and <code><a href="/docs/linux/man/3-mq_setattr/">mq_setattr</a></code>(3). For an explanation of how this system call operates, see the description of <code><a href="/docs/linux/man/3-mq_setattr/">mq_setattr</a></code>(3).</p>
<h2>CONFORMING TO</h2>
<p> This interface is nonstandard; avoid its use.</p>
<h2>NOTES</h2>
<p> Glibc does not provide a wrapper for this system call; call it using <code><a href="/docs/linux/man/2-syscall/">syscall</a></code>(2). (Actually, never call it unless you are writing a C library!)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mq_getattr/">mq_getattr</a></code>(3), <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
