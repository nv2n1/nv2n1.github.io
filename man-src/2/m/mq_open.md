---
title: "mq_open(2)"
name: "mq_open"
section: "2"
letter: "m"
url: "/docs/linux/man/2-mq_open/"
description: "mq_open – open a message queue"
---

<h2 class="name">NAME</h2>
<p> mq_open &#8211; open a message queue </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fcntl.h&gt; /* For O_* constants */
#include &lt;mqueue.h&gt;
#include &lt;sys/stat.h&gt; /* For mode constants */
mqd_t mq_open(const char *name, int oflag);
mqd_t mq_open(const char *name, int oflag, mode_t mode,
              struct mq_attr *attr);
</code></pre>
<p> Link with <i>-lrt</i>.</p>
<h2>DESCRIPTION</h2>
<p> <code>mq_open</code>() creates a new POSIX message queue or opens an existing queue. The queue is identified by <i>name</i>. For details of the construction of <i>name</i>, see <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7). </p>
<p> The <i>oflag</i> argument specifies flags that control the operation of the call. (Definitions of the flags values can be obtained by including <i>&lt;fcntl.h&gt;</i>.) Exactly one of the following must be specified in <i>oflag</i>:</p>
<dl>
<dt><code>O_RDONLY</code></p>
<dd> Open the queue to receive messages only.</p>
<dt><code>O_WRONLY</code></p>
<dd> Open the queue to send messages only.</p>
<dt><code>O_RDWR</code></p>
<dd> Open the queue to both send and receive messages.</dl>
<p> Zero or more of the following flags can additionally be <i>OR</i>ed in <i>oflag</i>:</p>
<dl>
<dt><code>O_CLOEXEC</code> (since Linux 2.6.26)</p>
<dd> Set the close-on-exec flag for the message queue descriptor. See <code><a href="/docs/linux/man/2-open/">open</a></code>(2) for a discussion of why this flag is useful.</p>
<dt><code>O_CREAT</code></p>
<dd> Create the message queue if it does not exist. The owner (user ID) of the message queue is set to the effective user ID of the calling process. The group ownership (group ID) is set to the effective group ID of the calling process.</p>
<dt><code>O_EXCL</code></p>
<dd> If <code>O_CREAT</code> was specified in <i>oflag</i>, and a queue with the given <i>name</i> already exists, then fail with the error <code>EEXIST</code>.</p>
<dt><code>O_NONBLOCK</code></p>
<dd> Open the queue in nonblocking mode. In circumstances where <code><a href="/docs/linux/man/3-mq_receive/">mq_receive</a></code>(3) and <code><a href="/docs/linux/man/3-mq_send/">mq_send</a></code>(3) would normally block, these functions instead fail with the error <code>EAGAIN</code>.</dl>
<p> If <code>O_CREAT</code> is specified in <i>oflag</i>, then two additional arguments must be supplied. The <i>mode</i> argument specifies the permissions to be placed on the new queue, as for <code><a href="/docs/linux/man/2-open/">open</a></code>(2). (Symbolic definitions for the permissions bits can be obtained by including <i>&lt;sys/stat.h&gt;</i>.) The permissions settings are masked against the process umask. </p>
<p> The fields of the <i>struct mq_attr</i> pointed to <i>attr</i> specify the maximum number of messages and the maximum size of messages that the queue will allow. This structure is defined as follows: </p>
<p> struct mq_attr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long mq_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags&nbsp;(ignored for mq_open())&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long mq_maxmsg;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Max.&nbsp;#&nbsp;of messages on queue&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long mq_msgsize;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Max. message size&nbsp;(bytes)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long mq_curmsgs;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;of messages currently in queue<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(ignored for mq_open())&nbsp;*/ }; </p>
<p> Only the <i>mq_maxmsg</i> and <i>mq_msgsize</i> fields are employed when calling <code>mq_open</code>(); the values in the remaining fields are ignored. </p>
<p> If <i>attr</i> is NULL, then the queue is created with implementation-defined default attributes. Since Linux 3.5, two <i>/proc</i> files can be used to control these defaults; see <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7) for details.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>mq_open</code>() returns a message queue descriptor for use by other message queue functions. On error, <code>mq_open</code>() returns <i>(mqd_t)&nbsp;-1,</i> with <i>errno</i> set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> The queue exists, but the caller does not have permission to open it in the specified mode.</p>
<dt><code>EACCES</code></p>
<dd> <i>name</i> contained more than one slash.</p>
<dt><code>EEXIST</code></p>
<dd> Both <code>O_CREAT</code> and <code>O_EXCL</code> were specified in <i>oflag</i>, but a queue with this <i>name</i> already exists.</p>
<dt><code>EINVAL</code></p>
<dd> <i>name</i> doesn&#8217;t follow the format in <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> <code>O_CREAT</code> was specified in <i>oflag</i>, and <i>attr</i> was not NULL, but <i>attr-&gt;mq_maxmsg</i> or <i>attr-&gt;mq_msqsize</i> was invalid. Both of these fields must be greater than zero. In a process that is unprivileged (does not have the <code>CAP_SYS_RESOURCE</code> capability), <i>attr-&gt;mq_maxmsg</i> must be less than or equal to the <i>msg_max</i> limit, and <i>attr-&gt;mq_msgsize</i> must be less than or equal to the <i>msgsize_max</i> limit. In addition, even in a privileged process, <i>attr-&gt;mq_maxmsg</i> cannot exceed the <code>HARD_MAX</code> limit. (See <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7) for details of these limits.)</p>
<dt><code>EMFILE</code></p>
<dd> The per-process limit on the number of open file and message queue descriptors has been reached (see the description of <code>RLIMIT_NOFILE</code> in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2)).</p>
<dt><code>ENAMETOOLONG</code></p>
<dd> <i>name</i> was too long.</p>
<dt><code>ENFILE</code></p>
<dd> The system-wide limit on the total number of open files and message queues has been reached.</p>
<dt><code>ENOENT</code></p>
<dd> The <code>O_CREAT</code> flag was not specified in <i>oflag</i>, and no queue with this <i>name</i> exists.</p>
<dt><code>ENOENT</code></p>
<dd> <i>name</i> was just &quot;/&quot; followed by no other characters.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory.</p>
<dt><code>ENOSPC</code></p>
<dd> Insufficient space for the creation of a new message queue. This probably occurred because the <i>queues_max</i> limit was encountered; see <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7).</dl>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>mq_open</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008.</p>
<h2>NOTES</h2>
<h3>C library/kernel differences</h3>
<p> The <code>mq_open</code>() library function is implemented on top of a system call of the same name. The library function performs the check that the <i>name</i> starts with a slash (/), giving the <code>EINVAL</code> error if it does not. The kernel system call expects <i>name</i> to contain no preceding slash, so the C library function passes <i>name</i> without the preceding slash (i.e., <i>name+1</i>) to the system call.</p>
<h2>BUGS</h2>
<p> In kernels before 2.6.14, the process umask was not applied to the permissions specified in <i>mode</i>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-mq_close/">mq_close</a></code>(3), <code><a href="/docs/linux/man/3-mq_getattr/">mq_getattr</a></code>(3), <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3), <code><a href="/docs/linux/man/3-mq_receive/">mq_receive</a></code>(3), <code><a href="/docs/linux/man/3-mq_send/">mq_send</a></code>(3), <code><a href="/docs/linux/man/3-mq_unlink/">mq_unlink</a></code>(3), <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
