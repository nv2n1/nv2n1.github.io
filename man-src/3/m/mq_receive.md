---
title: "mq_receive(3)"
name: "mq_receive"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mq_receive/"
description: "mq_receive, mq_timedreceive – receive a message from a message queue"
---

<p>mq_receive, mq_timedreceive &#8211; receive a message from a message queue </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;mqueue.h&gt;</code>
<code>ssize_t mq_receive(mqd_t </code><i>mqdes</i><code>, char *</code><i>msg_ptr</i><code>,</code>
<code> size_t </code><i>msg_len</i><code>, unsigned int *</code><i>msg_prio</i><code>);</code>
<code>#include &lt;time.h&gt;</code>
<code>#include &lt;mqueue.h&gt;</code>
<code>ssize_t mq_timedreceive(mqd_t </code><i>mqdes</i><code>, char *</code><i>msg_ptr</i><code>,</code>
<code> size_t </code><i>msg_len</i><code>, unsigned int *</code><i>msg_prio</i><code>,</code>
<code> const struct timespec *</code><i>abs_timeout</i><code>);</code></pre>
<p>Link with <i>-lrt</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>mq_timedreceive</code>():</p>
<dl COMPACT>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p><code>mq_receive</code>() removes the oldest message with the highest priority from the message queue referred to by the message queue descriptor <i>mqdes</i>, and places it in the buffer pointed to by <i>msg_ptr</i>. The <i>msg_len</i> argument specifies the size of the buffer pointed to by <i>msg_ptr</i>; this must be greater than or equal to the <i>mq_msgsize</i> attribute of the queue (see <code><a href="/docs/linux/man/3-mq_getattr/">mq_getattr</a></code>(3)). If <i>msg_prio</i> is not NULL, then the buffer to which it points is used to return the priority associated with the received message. </p>
<p> If the queue is empty, then, by default, <code>mq_receive</code>() blocks until a message becomes available, or the call is interrupted by a signal handler. If the <code>O_NONBLOCK</code> flag is enabled for the message queue description, then the call instead fails immediately with the error <code>EAGAIN</code>. </p>
<p> <code>mq_timedreceive</code>() behaves just like <code>mq_receive</code>(), except that if the queue is empty and the <code>O_NONBLOCK</code> flag is not enabled for the message queue description, then <i>abs_timeout</i> points to a structure which specifies how long the call will block. This value is an absolute timeout in seconds and nanoseconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC), specified in the following structure: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;nanoseconds&nbsp;*/ }; </p>
<p> If no message is available, and the timeout has already expired by the time of the call, <code>mq_timedreceive</code>() returns immediately.</p>
<h2>Return Value</h2>
<p>On success, <code>mq_receive</code>() and <code>mq_timedreceive</code>() return the number of bytes in the received message; on error, -1 is returned, with <i>errno</i> set to indicate the error.</p>
<h2>Errors</h2>
<dl COMPACT>
<dt><code>EAGAIN</code></p>
<dd>The queue was empty, and the <code>O_NONBLOCK</code> flag was set for the message queue description referred to by <i>mqdes</i>.</p>
<dt><code>EBADF</code></p>
<dd>The descriptor specified in <i>mqdes</i> was invalid or not opened for reading.</p>
<dt><code>EINTR</code></p>
<dd>The call was interrupted by a signal handler; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd>The call would have blocked, and <i>abs_timeout</i> was invalid, either because <i>tv_sec</i> was less than zero, or because <i>tv_nsec</i> was less than zero or greater than 1000 million.</p>
<dt><code>EMSGSIZE</code></p>
<dd><i>msg_len</i> was less than the <i>mq_msgsize</i> attribute of the message queue.</p>
<dt><code>ETIMEDOUT</code></p>
<dd>The call timed out before a message could be transferred.</dl>
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
<td> <code>mq_receive</code>(), <code>mq_timedreceive</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>On Linux, <code>mq_timedreceive</code>() is a system call, and <code>mq_receive</code>() is a library function layered on top of that system call.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mq_close/">mq_close</a></code>(3), <code><a href="/docs/linux/man/3-mq_getattr/">mq_getattr</a></code>(3), <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3), <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3), <code><a href="/docs/linux/man/3-mq_send/">mq_send</a></code>(3), <code><a href="/docs/linux/man/3-mq_unlink/">mq_unlink</a></code>(3), <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
