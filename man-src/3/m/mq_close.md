---
title: "mq_close(3)"
name: "mq_close"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mq_close/"
description: "mq_close – close a message queue descriptor"
---

<p>mq_close &#8211; close a message queue descriptor </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;mqueue.h&gt;</code>
<code>int mq_close(mqd_t </code><i>mqdes</i><code>);</code></pre>
<p>Link with <i>-lrt</i>.</p>
<h2>Description</h2>
<p><code>mq_close</code>() closes the message queue descriptor <i>mqdes</i>. </p>
<p> If the calling process has attached a notification request (see (<code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3)) to this message queue via <i>mqdes</i>, then this request is removed, and another process can now attach a notification request.</p>
<h2>Return Value</h2>
<p>On success <code>mq_close</code>() returns 0; on error, -1 is returned, with <i>errno</i> set to indicate the error.</p>
<h2>Errors</h2>
<dl COMPACT>
<dt><code>EBADF</code></p>
<dd>The message queue descriptor specified in <i>mqdes</i> is invalid.</dl>
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
<td> <code>mq_close</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>All open message queues are automatically closed on process termination, or upon <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mq_getattr/">mq_getattr</a></code>(3), <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3), <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3), <code><a href="/docs/linux/man/3-mq_receive/">mq_receive</a></code>(3), <code><a href="/docs/linux/man/3-mq_send/">mq_send</a></code>(3), <code><a href="/docs/linux/man/3-mq_unlink/">mq_unlink</a></code>(3), <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
