---
title: "msgctl(2)"
name: "msgctl"
section: "2"
letter: "m"
url: "/docs/linux/man/2-msgctl/"
description: "msgctl – System V message control operations"
---

<h2 class="name">NAME</h2>
<p> msgctl &#8211; System V message control operations </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/ipc.h&gt;
#include &lt;sys/msg.h&gt;
#include &lt;sys/types.h&gt;
int msgctl(int msqid, int cmd, struct msqid_ds *buf);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>msgctl</code>() performs the control operation specified by <i>cmd</i> on the System V message queue with identifier <i>msqid</i>. </p>
<p> The <i>msqid_ds</i> data structure is defined in <i>&lt;sys/msg.h&gt;</i> as follows: </p>
<p> struct msqid_ds {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct ipc_perm msg_perm;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Ownership and permissions&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_stime;&nbsp;<wbr>&nbsp;/*&nbsp;Time of last&nbsp;<a href="/docs/linux/man/2-msgsnd/">msgsnd</a>(2)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_rtime;&nbsp;<wbr>&nbsp;/*&nbsp;Time of last&nbsp;<a href="/docs/linux/man/2-msgrcv/">msgrcv</a>(2)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_ctime;&nbsp;<wbr>&nbsp;/*&nbsp;Time of creation or last<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;modification by msgctl()&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned long&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_cbytes;&nbsp;/*&nbsp;#&nbsp;of bytes in queue&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msgqnum_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_qnum;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;number of messages in queue&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msglen_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_qbytes;&nbsp;/*&nbsp;Maximum&nbsp;#&nbsp;of bytes in queue&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_lspid;&nbsp;<wbr>&nbsp;/*&nbsp;PID of last&nbsp;<a href="/docs/linux/man/2-msgsnd/">msgsnd</a>(2)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_lrpid;&nbsp;<wbr>&nbsp;/*&nbsp;PID of last&nbsp;<a href="/docs/linux/man/2-msgrcv/">msgrcv</a>(2)&nbsp;*/ }; </p>
<p> The fields of the <i>msgid_ds</i> structure are as follows:</p>
<dl>
<dt><i>msg_perm</i></p>
<dd> This is an <i>ipc_perm</i> structure (see below) that specifies the access permissions on the message queue.</p>
<dt><i>msg_stime</i></p>
<dd> Time of the last <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2) system call.</p>
<dt><i>msg_rtime</i></p>
<dd> Time of the last <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2) system call.</p>
<dt><i>msg_ctime</i></p>
<dd> Time of creation of queue or time of last <code>msgctl</code>() <code>IPC_SET</code> operation.</p>
<dt><i>msg_cbytes</i></p>
<dd> Number of bytes in all messages currently on the message queue. This is a nonstandard Linux extension that is not specified in POSIX.</p>
<dt><i>msg_qnum</i></p>
<dd> Number of messages currently on the message queue.</p>
<dt><i>msg_qbytes</i></p>
<dd> Maximum number of bytes of message text allowed on the message queue.</p>
<dt><i>msg_lspid</i></p>
<dd> ID of the process that performed the last <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2) system call.</p>
<dt><i>msg_lrpid</i></p>
<dd> ID of the process that performed the last <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2) system call.</dl>
<p> The <i>ipc_perm</i> structure is defined as follows (the highlighted fields are settable using <code>IPC_SET</code>): </p>
<p> struct ipc_perm {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__key;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Key supplied to&nbsp;<a href="/docs/linux/man/2-msgget/">msgget</a>(2)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>uid</code>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Effective UID of owner&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>gid</code>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Effective GID of owner&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cuid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Effective UID of creator&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;cgid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Effective GID of creator&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short&nbsp;<code>mode</code>;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Permissions&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short&nbsp;__seq;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Sequence number&nbsp;*/ }; </p>
<p> The least significant 9 bits of the <i>mode</i> field of the <i>ipc_perm</i> structure define the access permissions for the message queue. The permission bits are as follows: </p>
<table>
<tr VALIGN=top>
<td>0400</td>
<td>Read by user
</td>
</tr>
<tr VALIGN=top>
<td>0200</td>
<td>Write by user
</td>
</tr>
<tr VALIGN=top>
<td>0040</td>
<td>Read by group
</td>
</tr>
<tr VALIGN=top>
<td>0020</td>
<td>Write by group
</td>
</tr>
<tr VALIGN=top>
<td>0004</td>
<td>Read by others
</td>
</tr>
<tr VALIGN=top>
<td>0002</td>
<td>Write by others
</td>
</tr>
</table>
<p> Bits 0100, 0010, and 0001 (the execute bits) are unused by the system. </p>
<p> Valid values for <i>cmd</i> are:</p>
<dl>
<dt><code>IPC_STAT</code></p>
<dd> Copy information from the kernel data structure associated with <i>msqid</i> into the <i>msqid_ds</i> structure pointed to by <i>buf</i>. The caller must have read permission on the message queue.</p>
<dt><code>IPC_SET</code></p>
<dd> Write the values of some members of the <i>msqid_ds</i> structure pointed to by <i>buf</i> to the kernel data structure associated with this message queue, updating also its <i>msg_ctime</i> member.</p>
<dt>
<dd> The following members of the structure are updated: <i>msg_qbytes</i>, <i>msg_perm.uid</i>, <i>msg_perm.gid</i>, and (the least significant 9 bits of) <i>msg_perm.mode</i>.</p>
<dt>
<dd> The effective UID of the calling process must match the owner (<i>msg_perm.uid</i>) or creator (<i>msg_perm.cuid</i>) of the message queue, or the caller must be privileged. Appropriate privilege (Linux: the <code>CAP_SYS_RESOURCE</code> capability) is required to raise the <i>msg_qbytes</i> value beyond the system parameter <code>MSGMNB</code>.</p>
<dt><code>IPC_RMID</code></p>
<dd> Immediately remove the message queue, awakening all waiting reader and writer processes (with an error return and <i>errno</i> set to <code>EIDRM</code>). The calling process must have appropriate privileges or its effective user ID must be either that of the creator or owner of the message queue. The third argument to <code>msgctl</code>() is ignored in this case.</p>
<dt><code>IPC_INFO</code> (Linux-specific)</p>
<dd> Return information about system-wide message queue limits and parameters in the structure pointed to by <i>buf</i>. This structure is of type <i>msginfo</i> (thus, a cast is required), defined in <i>&lt;sys/msg.h&gt;</i> if the <code>_GNU_SOURCE</code> feature test macro is defined:</p>
<dt>
<dd> struct msginfo {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int msgpool;&nbsp;/*&nbsp;Size in kibibytes of buffer pool<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;used to hold message data;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unused within kernel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int msgmap;&nbsp;<wbr>&nbsp;/*&nbsp;Maximum number of entries in message<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;map;&nbsp;unused within kernel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int msgmax;&nbsp;<wbr>&nbsp;/*&nbsp;Maximum number of bytes that can be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;written in a single message&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int msgmnb;&nbsp;<wbr>&nbsp;/*&nbsp;Maximum number of bytes that can be<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;written to queue;&nbsp;used to initialize<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg_qbytes during queue creation<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(<a href="/docs/linux/man/2-msgget/">msgget</a>(2))&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int msgmni;&nbsp;<wbr>&nbsp;/*&nbsp;Maximum number of message queues&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int msgssz;&nbsp;<wbr>&nbsp;/*&nbsp;Message segment size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unused within kernel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int msgtql;&nbsp;<wbr>&nbsp;/*&nbsp;Maximum number of messages on all queues<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;in system;&nbsp;unused within kernel&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short msgseg;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Maximum number of segments;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unused within kernel&nbsp;*/ };</p>
<dt>
<dd> The <i>msgmni</i>, <i>msgmax</i>, and <i>msgmnb</i> settings can be changed via <i>/proc</i> files of the same name; see <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5) for details.</p>
<dt><code>MSG_INFO</code> (Linux-specific)</p>
<dd> Return a <i>msginfo</i> structure containing the same information as for <code>IPC_INFO</code>, except that the following fields are returned with information about system resources consumed by message queues: the <i>msgpool</i> field returns the number of message queues that currently exist on the system; the <i>msgmap</i> field returns the total number of messages in all queues on the system; and the <i>msgtql</i> field returns the total number of bytes in all messages in all queues on the system.</p>
<dt><code>MSG_STAT</code> (Linux-specific)</p>
<dd> Return a <i>msqid_ds</i> structure as for <code>IPC_STAT</code>. However, the <i>msqid</i> argument is not a queue identifier, but instead an index into the kernel&#8217;s internal array that maintains information about all message queues on the system.</p>
<dt><code>MSG_STAT_ANY</code> (Linux-specific, since Linux 4.17)</p>
<dd> Return a <i>msqid_ds</i> structure as for <code>MSG_STAT</code>. However, <i>msg_perm.mode</i> is not checked for read access for <i>msqid</i> meaning that any user can employ this operation (just as any user may read <i>/proc/sysvipc/msg</i> to obtain the same information).</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>IPC_STAT</code>, <code>IPC_SET</code>, and <code>IPC_RMID</code> return 0. A successful <code>IPC_INFO</code> or <code>MSG_INFO</code> operation returns the index of the highest used entry in the kernel&#8217;s internal array recording information about all message queues. (This information can be used with repeated <code>MSG_STAT</code> or <code>MSG_STAT_ANY</code> operations to obtain information about all queues on the system.) A successful <code>MSG_STAT</code> or <code>MSG_STAT_ANY</code> operation returns the identifier of the queue whose index was given in <i>msqid</i>. </p>
<p> On error, -1 is returned with <i>errno</i> indicating the error.</p>
<h2>ERRORS</h2>
<p> On failure, <i>errno</i> is set to one of the following:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> The argument <i>cmd</i> is equal to <code>IPC_STAT</code> or <code>MSG_STAT</code>, but the calling process does not have read permission on the message queue <i>msqid</i>, and does not have the <code>CAP_IPC_OWNER</code> capability in the user namespace that governs its IPC namespace.</p>
<dt><code>EFAULT</code></p>
<dd> The argument <i>cmd</i> has the value <code>IPC_SET</code> or <code>IPC_STAT</code>, but the address pointed to by <i>buf</i> isn&#8217;t accessible.</p>
<dt><code>EIDRM</code></p>
<dd> The message queue was removed.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid value for <i>cmd</i> or <i>msqid</i>. Or: for a <code>MSG_STAT</code> operation, the index value specified in <i>msqid</i> referred to an array slot that is currently unused.</p>
<dt><code>EPERM</code></p>
<dd> The argument <i>cmd</i> has the value <code>IPC_SET</code> or <code>IPC_RMID</code>, but the effective user ID of the calling process is not the creator (as found in <i>msg_perm.cuid</i>) or the owner (as found in <i>msg_perm.uid</i>) of the message queue, and the caller is not privileged (Linux: does not have the <code>CAP_SYS_ADMIN</code> capability).</p>
<dt><code>EPERM</code></p>
<dd> An attempt (<code>IPC_SET</code>) was made to increase <i>msg_qbytes</i> beyond the system parameter <code>MSGMNB</code>, but the caller is not privileged (Linux: does not have the <code>CAP_SYS_RESOURCE</code> capability).</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4.</p>
<h2>NOTES</h2>
<p> The inclusion of <i>&lt;sys/types.h&gt;</i> and <i>&lt;sys/ipc.h&gt;</i> isn&#8217;t required on Linux or by any version of POSIX. However, some old implementations required the inclusion of these header files, and the SVID also documented their inclusion. Applications intended to be portable to such old systems may need to include these header files. </p>
<p> The <code>IPC_INFO</code>, <code>MSG_STAT</code>, and <code>MSG_INFO</code> operations are used by the <code><a href="/docs/linux/man/1-ipcs/">ipcs</a></code>(1) program to provide information on allocated resources. In the future these may modified or moved to a <i>/proc</i> filesystem interface. </p>
<p> Various fields in the <i>struct msqid_ds</i> were typed as <i>short</i> under Linux 2.2 and have become <i>long</i> under Linux 2.4. To take advantage of this, a recompilation under glibc-2.1.91 or later should suffice. (The kernel distinguishes old and new calls by an <code>IPC_64</code> flag in <i>cmd</i>.)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2), <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2), <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
