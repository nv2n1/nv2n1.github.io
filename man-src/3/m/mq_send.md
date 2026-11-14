---
title: "mq_send(3)"
name: "mq_send"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mq_send/"
description: "mq_send, mq_timedsend – send a message to a message queue"
---

<p>mq_send, mq_timedsend &#8211; send a message to a message queue </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;mqueue.h&gt;</code>
<code>int mq_send(mqd_t </code><i>mqdes</i><code>, const char *</code><i>msg_ptr</i><code>,</code>
<code> size_t </code><i>msg_len</i><code>, unsigned int </code><i>msg_prio</i><code>);</code>
<code>#include &lt;time.h&gt;</code>
<code>#include &lt;mqueue.h&gt;</code>
<code>int mq_timedsend(mqd_t </code><i>mqdes</i><code>, const char *</code><i>msg_ptr</i><code>,</code>
<code> size_t </code><i>msg_len</i><code>, unsigned int </code><i>msg_prio</i><code>,</code>
<code> const struct timespec *</code><i>abs_timeout</i><code>);</code></pre>
<p>Link with <i>-lrt</i>. </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>mq_timedsend</code>():</p>
<dl COMPACT>
<dd>_POSIX_C_SOURCE&nbsp;&gt;=&nbsp;200112L</dl>
<h2>Description</h2>
<p><code>mq_send</code>() adds the message pointed to by <i>msg_ptr</i> to the message queue referred to by the message queue descriptor <i>mqdes</i>. The <i>msg_len</i> argument specifies the length of the message pointed to by <i>msg_ptr</i>; this length must be less than or equal to the queue&#8217;s <i>mq_msgsize</i> attribute. Zero-length messages are allowed. </p>
<p> The <i>msg_prio</i> argument is a nonnegative integer that specifies the priority of this message. Messages are placed on the queue in decreasing order of priority, with newer messages of the same priority being placed after older messages with the same priority. See <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7) for details on the range for the message priority. </p>
<p> If the message queue is already full (i.e., the number of messages on the queue equals the queue&#8217;s <i>mq_maxmsg</i> attribute), then, by default, <code>mq_send</code>() blocks until sufficient space becomes available to allow the message to be queued, or until the call is interrupted by a signal handler. If the <code>O_NONBLOCK</code> flag is enabled for the message queue description, then the call instead fails immediately with the error <code>EAGAIN</code>. </p>
<p> <code>mq_timedsend</code>() behaves just like <code>mq_send</code>(), except that if the queue is full and the <code>O_NONBLOCK</code> flag is not enabled for the message queue description, then <i>abs_timeout</i> points to a structure which specifies how long the call will block. This value is an absolute timeout in seconds and nanoseconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC), specified in the following structure: </p>
<p> struct timespec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t tv_sec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;seconds&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;tv_nsec;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;nanoseconds&nbsp;*/ }; </p>
<p> If the message queue is full, and the timeout has already expired by the time of the call, <code>mq_timedsend</code>() returns immediately.</p>
<h2>Return Value</h2>
<p>On success, <code>mq_send</code>() and <code>mq_timedsend</code>() return zero; on error, -1 is returned, with <i>errno</i> set to indicate the error.</p>
<h2>Errors</h2>
<dl COMPACT>
<dt><code>EAGAIN</code></p>
<dd>The queue was full, and the <code>O_NONBLOCK</code> flag was set for the message queue description referred to by <i>mqdes</i>.</p>
<dt><code>EBADF</code></p>
<dd>The descriptor specified in <i>mqdes</i> was invalid or not opened for writing.</p>
<dt><code>EINTR</code></p>
<dd>The call was interrupted by a signal handler; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd>The call would have blocked, and <i>abs_timeout</i> was invalid, either because <i>tv_sec</i> was less than zero, or because <i>tv_nsec</i> was less than zero or greater than 1000 million.</p>
<dt><code>EMSGSIZE</code></p>
<dd><i>msg_len</i> was greater than the <i>mq_msgsize</i> attribute of the message queue.</p>
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
<td> <code>mq_send</code>(), <code>mq_timedsend</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>On Linux, <code>mq_timedsend</code>() is a system call, and <code>mq_send</code>() is a library function layered on top of that system call.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mq_close/">mq_close</a></code>(3), <code><a href="/docs/linux/man/3-mq_getattr/">mq_getattr</a></code>(3), <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3), <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3), <code><a href="/docs/linux/man/3-mq_receive/">mq_receive</a></code>(3), <code><a href="/docs/linux/man/3-mq_unlink/">mq_unlink</a></code>(3), <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
