---
title: "mq_unlink(3)"
name: "mq_unlink"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mq_unlink/"
description: "mq_unlink – remove a message queue"
---

<p>mq_unlink &#8211; remove a message queue </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;mqueue.h&gt;</code>
<code>int mq_unlink(const char *</code><i>name</i><code>);</code></pre>
<p>Link with <i>-lrt</i>.</p>
<h2>Description</h2>
<p><code>mq_unlink</code>() removes the specified message queue <i>name</i>. The message queue name is removed immediately. The queue itself is destroyed once any other processes that have the queue open close their descriptors referring to the queue.</p>
<h2>Return Value</h2>
<p>On success <code>mq_unlink</code>() returns 0; on error, -1 is returned, with <i>errno</i> set to indicate the error.</p>
<h2>Errors</h2>
<dl COMPACT>
<dt><code>EACCES</code></p>
<dd>The caller does not have permission to unlink this message queue.</p>
<dt><code>ENAMETOOLONG</code></p>
<dd><i>name</i> was too long.</p>
<dt><code>ENOENT</code></p>
<dd>There is no message queue with the given <i>name</i>.</dl>
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
<td> <code>mq_unlink</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mq_close/">mq_close</a></code>(3), <code><a href="/docs/linux/man/3-mq_getattr/">mq_getattr</a></code>(3), <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3), <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3), <code><a href="/docs/linux/man/3-mq_receive/">mq_receive</a></code>(3), <code><a href="/docs/linux/man/3-mq_send/">mq_send</a></code>(3), <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
