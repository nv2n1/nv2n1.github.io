---
title: "mq_overview(7)"
name: "mq_overview"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mq_overview/"
description: "mq_overview – overview of POSIX message queues"
---

<p>mq_overview &#8211; overview of POSIX message queues</p>
<h2>Description</h2>
<p>POSIX message queues allow processes to exchange data in the form of messages. This API is distinct from that provided by System V message queues (<code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2), <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2), <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2), etc.), but provides similar functionality. </p>
<p> Message queues are created and opened using <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3); this function returns a <i>message queue descriptor</i> (<i>mqd_t</i>), which is used to refer to the open message queue in later calls. Each message queue is identified by a name of the form <i>/somename</i>; that is, a null-terminated string of up to <code>NAME_MAX</code> (i.e., 255) characters consisting of an initial slash, followed by one or more characters, none of which are slashes. Two processes can operate on the same queue by passing the same name to <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3). </p>
<p> Messages are transferred to and from a queue using <code><a href="/docs/linux/man/3-mq_send/">mq_send</a></code>(3) and <code><a href="/docs/linux/man/3-mq_receive/">mq_receive</a></code>(3). When a process has finished using the queue, it closes it using <code><a href="/docs/linux/man/3-mq_close/">mq_close</a></code>(3), and when the queue is no longer required, it can be deleted using <code><a href="/docs/linux/man/3-mq_unlink/">mq_unlink</a></code>(3). Queue attributes can be retrieved and (in some cases) modified using <code><a href="/docs/linux/man/3-mq_getattr/">mq_getattr</a></code>(3) and <code><a href="/docs/linux/man/3-mq_setattr/">mq_setattr</a></code>(3). A process can request asynchronous notification of the arrival of a message on a previously empty queue using <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3). </p>
<p> A message queue descriptor is a reference to an <i>open message queue description</i> (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)). After a <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2), a child inherits copies of its parent&#8217;s message queue descriptors, and these descriptors refer to the same open message queue descriptions as the corresponding message queue descriptors in the parent. Corresponding message queue descriptors in the two processes share the flags (<i>mq_flags</i>) that are associated with the open message queue description. </p>
<p> Each message has an associated <i>priority</i>, and messages are always delivered to the receiving process highest priority first. Message priorities range from 0 (low) to <i>sysconf(_SC_MQ_PRIO_MAX)&nbsp;&#8211; 1</i> (high). On Linux, <i>sysconf(_SC_MQ_PRIO_MAX)</i> returns 32768, but POSIX.1 requires only that an implementation support at least priorities in the range 0 to 31; some implementations provide only this range. </p>
<p> The remainder of this section describes some specific details of the Linux implementation of POSIX message queues.</p>
<h3>Library interfaces and system calls</h3>
<p>In most cases the <code>mq_*</code>() library interfaces listed above are implemented on top of underlying system calls of the same name. Deviations from this scheme are indicated in the following table:</p>
<dl>
<dd>
<table>
<tr VALIGN=top>
<td><code>Library interface</code></td>
<td><code>System call</code>
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/3-mq_close/">mq_close</a>(3)</td>
<td><a href="/docs/linux/man/2-close/">close</a>(2)
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/3-mq_getattr/">mq_getattr</a>(3)</td>
<td><a href="/docs/linux/man/2-mq_getsetattr/">mq_getsetattr</a>(2)
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/3-mq_notify/">mq_notify</a>(3)</td>
<td><a href="/docs/linux/man/2-mq_notify/">mq_notify</a>(2)
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/3-mq_open/">mq_open</a>(3)</td>
<td><a href="/docs/linux/man/2-mq_open/">mq_open</a>(2)
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/3-mq_receive/">mq_receive</a>(3)</td>
<td><a href="/docs/linux/man/2-mq_timedreceive/">mq_timedreceive</a>(2)
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/3-mq_send/">mq_send</a>(3)</td>
<td><a href="/docs/linux/man/2-mq_timedsend/">mq_timedsend</a>(2)
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/3-mq_setattr/">mq_setattr</a>(3)</td>
<td><a href="/docs/linux/man/2-mq_getsetattr/">mq_getsetattr</a>(2)
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/3-mq_timedreceive/">mq_timedreceive</a>(3)</td>
<td><a href="/docs/linux/man/2-mq_timedreceive/">mq_timedreceive</a>(2)
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/3-mq_timedsend/">mq_timedsend</a>(3)</td>
<td><a href="/docs/linux/man/2-mq_timedsend/">mq_timedsend</a>(2)
</td>
</tr>
<tr VALIGN=top>
<td><a href="/docs/linux/man/3-mq_unlink/">mq_unlink</a>(3)</td>
<td><a href="/docs/linux/man/2-mq_unlink/">mq_unlink</a>(2)
</td>
</tr>
</table>
</dl>
<h3>Versions</h3>
<p>POSIX message queues have been supported on Linux since kernel 2.6.6. Glibc support has been provided since version 2.3.4.</p>
<h3>Kernel configuration</h3>
<p>Support for POSIX message queues is configurable via the <code>CONFIG_POSIX_MQUEUE</code> kernel configuration option. This option is enabled by default.</p>
<h3>Persistence</h3>
<p>POSIX message queues have kernel persistence: if not removed by <code><a href="/docs/linux/man/3-mq_unlink/">mq_unlink</a></code>(3), a message queue will exist until the system is shut down.</p>
<h3>Linking</h3>
<p>Programs using the POSIX message queue API must be compiled with <i>cc -lrt</i> to link against the real-time library, <i>librt</i>.</p>
<h3>/proc interfaces</h3>
<p>The following interfaces can be used to limit the amount of kernel memory consumed by POSIX message queues and to set the default attributes for new message queues:</p>
<dl>
<dt><i>/proc/sys/fs/mqueue/msg_default</i> (since Linux 3.5)</p>
<dd>This file defines the value used for a new queue&#8217;s <i>mq_maxmsg</i> setting when the queue is created with a call to <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3) where <i>attr</i> is specified as NULL. The default value for this file is 10. The minimum and maximum are as for <i>/proc/sys/fs/mqueue/msg_max</i>. A new queue&#8217;s default <i>mq_maxmsg</i> value will be the smaller of <i>msg_default</i> and <i>msg_max</i>. Up until Linux 2.6.28, the default <i>mq_maxmsg</i> was 10; from Linux 2.6.28 to Linux 3.4, the default was the value defined for the <i>msg_max</i> limit.</p>
<dt><i>/proc/sys/fs/mqueue/msg_max</i></p>
<dd>This file can be used to view and change the ceiling value for the maximum number of messages in a queue. This value acts as a ceiling on the <i>attr-&gt;mq_maxmsg</i> argument given to <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3). The default value for <i>msg_max</i> is 10. The minimum value is 1 (10 in kernels before 2.6.28). The upper limit is <code>HARD_MSGMAX</code>. The <i>msg_max</i> limit is ignored for privileged processes (<code>CAP_SYS_RESOURCE</code>), but the <code>HARD_MSGMAX</code> ceiling is nevertheless imposed.</p>
<dd>The definition of <code>HARD_MSGMAX</code> has changed across kernel versions:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Up to Linux 2.6.32: <i>131072&nbsp;/&nbsp;sizeof(void&nbsp;*)</i></p>
<dt>*</p>
<dd>Linux 2.6.33 to 3.4: <i>(32768&nbsp;*&nbsp;sizeof(void&nbsp;*) / 4)</i></p>
<dt>*</p>
<dd>Since Linux 3.5: 65,536</dl>
</dl>
<dt><i>/proc/sys/fs/mqueue/msgsize_default</i> (since Linux 3.5)</p>
<dd>This file defines the value used for a new queue&#8217;s <i>mq_msgsize</i> setting when the queue is created with a call to <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3) where <i>attr</i> is specified as NULL. The default value for this file is 8192 (bytes). The minimum and maximum are as for <i>/proc/sys/fs/mqueue/msgsize_max</i>. If <i>msgsize_default</i> exceeds <i>msgsize_max</i>, a new queue&#8217;s default <i>mq_msgsize</i> value is capped to the <i>msgsize_max</i> limit. Up until Linux 2.6.28, the default <i>mq_msgsize</i> was 8192; from Linux 2.6.28 to Linux 3.4, the default was the value defined for the <i>msgsize_max</i> limit.</p>
<dt><i>/proc/sys/fs/mqueue/msgsize_max</i></p>
<dd>This file can be used to view and change the ceiling on the maximum message size. This value acts as a ceiling on the <i>attr-&gt;mq_msgsize</i> argument given to <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3). The default value for <i>msgsize_max</i> is 8192 bytes. The minimum value is 128 (8192 in kernels before 2.6.28). The upper limit for <i>msgsize_max</i> has varied across kernel versions:</p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>Before Linux 2.6.28, the upper limit is <code>INT_MAX</code>.</p>
<dt>*</p>
<dd>From Linux 2.6.28 to 3.4, the limit is 1,048,576.</p>
<dt>*</p>
<dd>Since Linux 3.5, the limit is 16,777,216 (<code>HARD_MSGSIZEMAX</code>).</dl>
</dl>
<dd>The <i>msgsize_max</i> limit is ignored for privileged process (<code>CAP_SYS_RESOURCE</code>), but, since Linux 3.5, the <code>HARD_MSGSIZEMAX</code> ceiling is enforced for privileged processes.</p>
<dt><i>/proc/sys/fs/mqueue/queues_max</i></p>
<dd>This file can be used to view and change the system-wide limit on the number of message queues that can be created. The default value for <i>queues_max</i> is 256. No ceiling is imposed on the <i>queues_max</i> limit; privileged processes (<code>CAP_SYS_RESOURCE</code>) can exceed the limit (but see BUGS).</dl>
<h3>Resource limit</h3>
<p>The <code>RLIMIT_MSGQUEUE</code> resource limit, which places a limit on the amount of space that can be consumed by all of the message queues belonging to a process&#8217;s real user ID, is described in <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2).</p>
<h3>Mounting the message queue filesystem</h3>
<p>On Linux, message queues are created in a virtual filesystem. (Other implementations may also provide such a feature, but the details are likely to differ.) This filesystem can be mounted (by the superuser) using the following commands: </p>
<p> #<code> mkdir /dev/mqueue</code> #<code> mount -t mqueue none /dev/mqueue</code> </p>
<p> The sticky bit is automatically enabled on the mount directory. </p>
<p> After the filesystem has been mounted, the message queues on the system can be viewed and manipulated using the commands usually used for files (e.g., <code><a href="/docs/linux/man/1-ls/">ls</a></code>(1) and <code><a href="/docs/linux/man/1-rm/">rm</a></code>(1)). </p>
<p> The contents of each file in the directory consist of a single line containing information about the queue: </p>
<p> $<code> cat /dev/mqueue/mymq</code> QSIZE:129 NOTIFY:2 SIGNO:0 NOTIFY_PID:8260 </p>
<p> These fields are as follows:</p>
<dl>
<dt><code>QSIZE</code></p>
<dd>Number of bytes of data in all messages in the queue (but see BUGS).</p>
<dt><code>NOTIFY_PID</code></p>
<dd>If this is nonzero, then the process with this PID has used <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3) to register for asynchronous message notification, and the remaining fields describe how notification occurs.</p>
<dt><code>NOTIFY</code></p>
<dd>Notification method: 0 is <code>SIGEV_SIGNAL</code>; 1 is <code>SIGEV_NONE</code>; and 2 is <code>SIGEV_THREAD</code>.</p>
<dt><code>SIGNO</code></p>
<dd>Signal number to be used for <code>SIGEV_SIGNAL</code>.</dl>
<h3>Linux implementation of message queue descriptors</h3>
<p>On Linux, a message queue descriptor is actually a file descriptor. (POSIX does not require such an implementation.) This means that a message queue descriptor can be monitored using <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), or <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7). This is not portable. </p>
<p> The close-on-exec flag (see <code><a href="/docs/linux/man/2-open/">open</a></code>(2)) is automatically set on the file descriptor returned by <code><a href="/docs/linux/man/2-mq_open/">mq_open</a></code>(2).</p>
<h3>IPC namespaces</h3>
<p>For a discussion of the interaction of POSIX message queue objects and IPC namespaces, see <code><a href="/docs/linux/man/7-ipc_namespaces/">ipc_namespaces</a></code>(7).</p>
<h2>Notes</h2>
<p>System V message queues (<code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2), <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2), <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2), etc.) are an older API for exchanging messages between processes. POSIX message queues provide a better designed interface than System V message queues; on the other hand POSIX message queues are less widely available (especially on older systems) than System V message queues. </p>
<p> Linux does not currently (2.6.26) support the use of access control lists (ACLs) for POSIX message queues.</p>
<h2>Bugs</h2>
<p>In Linux versions 3.5 to 3.14, the kernel imposed a ceiling of 1024 (<code>HARD_QUEUESMAX</code>) on the value to which the <i>queues_max</i> limit could be raised, and the ceiling was enforced even for privileged processes. This ceiling value was removed in Linux 3.14, and patches to stable kernels 3.5.x to 3.13.x also removed the ceiling. </p>
<p> As originally implemented (and documented), the QSIZE field displayed the total number of (user-supplied) bytes in all messages in the message queue. Some changes in Linux 3.5 inadvertently changed the behavior, so that this field also included a count of kernel overhead bytes used to store the messages in the queue. This behavioral regression was rectified in Linux 4.2 (and earlier stable kernel series), so that the count once more included just the bytes of user data in messages in the queue.</p>
<h2>Examples</h2>
<p>An example of the use of various message queue functions is shown in <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/2-mq_getsetattr/">mq_getsetattr</a></code>(2), <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/3-mq_close/">mq_close</a></code>(3), <code><a href="/docs/linux/man/3-mq_getattr/">mq_getattr</a></code>(3), <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3), <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3), <code><a href="/docs/linux/man/3-mq_receive/">mq_receive</a></code>(3), <code><a href="/docs/linux/man/3-mq_send/">mq_send</a></code>(3), <code><a href="/docs/linux/man/3-mq_unlink/">mq_unlink</a></code>(3), <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7), <code><a href="/docs/linux/man/7-namespaces/">namespaces</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
