---
title: "msgsnd(2)"
name: "msgsnd"
section: "2"
letter: "m"
url: "/docs/linux/man/2-msgsnd/"
description: "msgrcv, msgsnd – System V message queue operations"
---

<h2 class="name">NAME</h2>
<p> msgrcv, msgsnd &#8211; System V message queue operations </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/ipc.h&gt;
#include &lt;sys/msg.h&gt;
#include &lt;sys/types.h&gt;
int msgsnd(int msqid, const void *msgp, size_t msgsz, int msgflg);
ssize_t msgrcv(int msqid, void *msgp, size_t msgsz, long msgtyp,
               int msgflg);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>msgsnd</code>() and <code>msgrcv</code>() system calls are used to send messages to, and receive messages from, a System V message queue. The calling process must have write permission on the message queue in order to send a message, and read permission to receive a message. </p>
<p> The <i>msgp</i> argument is a pointer to a caller-defined structure of the following general form: </p>
<p> struct msgbuf {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long mtype;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;message type, must be&nbsp;&gt;&nbsp;0&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char mtext[1];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;message data&nbsp;*/ }; </p>
<p> The <i>mtext</i> field is an array (or other structure) whose size is specified by <i>msgsz</i>, a nonnegative integer value. Messages of zero length (i.e., no <i>mtext</i> field) are permitted. The <i>mtype</i> field must have a strictly positive integer value. This value can be used by the receiving process for message selection (see the description of <code>msgrcv</code>() below).</p>
<h3>msgsnd()</h3>
<p> The <code>msgsnd</code>() system call appends a copy of the message pointed to by <i>msgp</i> to the message queue whose identifier is specified by <i>msqid</i>. </p>
<p> If sufficient space is available in the queue, <code>msgsnd</code>() succeeds immediately. The queue capacity is governed by the <i>msg_qbytes</i> field in the associated data structure for the message queue. During queue creation this field is initialized to <code>MSGMNB</code> bytes, but this limit can be modified using <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2). A message queue is considered to be full if either of the following conditions is true:</p>
<dl>
<dt>&bull;</p>
<dd> Adding a new message to the queue would cause the total number of bytes in the queue to exceed the queue&#8217;s maximum size (the <i>msg_qbytes</i> field).</p>
<dt>&bull;</p>
<dd> Adding another message to the queue would cause the total number of messages in the queue to exceed the queue&#8217;s maximum size (the <i>msg_qbytes</i> field). This check is necessary to prevent an unlimited number of zero-length messages being placed on the queue. Although such messages contain no data, they nevertheless consume (locked) kernel memory.</dl>
<p> If insufficient space is available in the queue, then the default behavior of <code>msgsnd</code>() is to block until space becomes available. If <code>IPC_NOWAIT</code> is specified in <i>msgflg</i>, then the call instead fails with the error <code>EAGAIN</code>. </p>
<p> A blocked <code>msgsnd</code>() call may also fail if:</p>
<dl>
<dt>&bull;</p>
<dd> the queue is removed, in which case the system call fails with <i>errno</i> set to <code>EIDRM</code>; or</p>
<dt>&bull;</p>
<dd> a signal is caught, in which case the system call fails with <i>errno</i> set to <code>EINTR</code>;<code>see</code> <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7). (<code>msgsnd</code>() is never automatically restarted after being interrupted by a signal handler, regardless of the setting of the <code>SA_RESTART</code> flag when establishing a signal handler.)</dl>
<p> Upon successful completion the message queue data structure is updated as follows:</p>
<dl>
<dt>&bull;</p>
<dd> <i>msg_lspid</i> is set to the process ID of the calling process.</p>
<dt>&bull;</p>
<dd> <i>msg_qnum</i> is incremented by 1.</p>
<dt>&bull;</p>
<dd> <i>msg_stime</i> is set to the current time.</dl>
<h3>msgrcv()</h3>
<p> The <code>msgrcv</code>() system call removes a message from the queue specified by <i>msqid</i> and places it in the buffer pointed to by <i>msgp</i>. </p>
<p> The argument <i>msgsz</i> specifies the maximum size in bytes for the member <i>mtext</i> of the structure pointed to by the <i>msgp</i> argument. If the message text has length greater than <i>msgsz</i>, then the behavior depends on whether <code>MSG_NOERROR</code> is specified in <i>msgflg</i>. If <code>MSG_NOERROR</code> is specified, then the message text will be truncated (and the truncated part will be lost); if <code>MSG_NOERROR</code> is not specified, then the message isn&#8217;t removed from the queue and the system call fails returning -1 with <i>errno</i> set to <code>E2BIG</code>. </p>
<p> Unless <code>MSG_COPY</code> is specified in <i>msgflg</i> (see below), the <i>msgtyp</i> argument specifies the type of message requested, as follows:</p>
<dl>
<dt>&bull;</p>
<dd> If <i>msgtyp</i> is 0, then the first message in the queue is read.</p>
<dt>&bull;</p>
<dd> If <i>msgtyp</i> is greater than 0, then the first message in the queue of type <i>msgtyp</i> is read, unless <code>MSG_EXCEPT</code> was specified in <i>msgflg</i>, in which case the first message in the queue of type not equal to <i>msgtyp</i> will be read.</p>
<dt>&bull;</p>
<dd> If <i>msgtyp</i> is less than 0, then the first message in the queue with the lowest type less than or equal to the absolute value of <i>msgtyp</i> will be read.</dl>
<p> The <i>msgflg</i> argument is a bit mask constructed by ORing together zero or more of the following flags:</p>
<dl>
<dt><code>IPC_NOWAIT</code></p>
<dd> Return immediately if no message of the requested type is in the queue. The system call fails with <i>errno</i> set to <code>ENOMSG</code>.</p>
<dt><code>MSG_COPY</code> (since Linux 3.8)</p>
<dd> Nondestructively fetch a copy of the message at the ordinal position in the queue specified by <i>msgtyp</i> (messages are considered to be numbered starting at 0).</p>
<dt>
<dd> This flag must be specified in conjunction with <code>IPC_NOWAIT</code>, with the result that, if there is no message available at the given position, the call fails immediately with the error <code>ENOMSG</code>. Because they alter the meaning of <i>msgtyp</i> in orthogonal ways, <code>MSG_COPY</code> and <code>MSG_EXCEPT</code> may not both be specified in <i>msgflg</i>.</p>
<dt>
<dd> The <code>MSG_COPY</code> flag was added for the implementation of the kernel checkpoint-restore facility and is available only if the kernel was built with the <code>CONFIG_CHECKPOINT_RESTORE</code> option.</p>
<dt><code>MSG_EXCEPT</code></p>
<dd> Used with <i>msgtyp</i> greater than 0 to read the first message in the queue with message type that differs from <i>msgtyp</i>.</p>
<dt><code>MSG_NOERROR</code></p>
<dd> To truncate the message text if longer than <i>msgsz</i> bytes.</dl>
<p> If no message of the requested type is available and <code>IPC_NOWAIT</code> isn&#8217;t specified in <i>msgflg</i>, the calling process is blocked until one of the following conditions occurs:</p>
<dl>
<dt>&bull;</p>
<dd> A message of the desired type is placed in the queue.</p>
<dt>&bull;</p>
<dd> The message queue is removed from the system. In this case, the system call fails with <i>errno</i> set to <code>EIDRM</code>.</p>
<dt>&bull;</p>
<dd> The calling process catches a signal. In this case, the system call fails with <i>errno</i> set to <code>EINTR</code>. (<code>msgrcv</code>() is never automatically restarted after being interrupted by a signal handler, regardless of the setting of the <code>SA_RESTART</code> flag when establishing a signal handler.)</dl>
<p> Upon successful completion the message queue data structure is updated as follows:</p>
<dl>
<dt>
<dd> <i>msg_lrpid</i> is set to the process ID of the calling process.</p>
<dt>
<dd> <i>msg_qnum</i> is decremented by 1.</p>
<dt>
<dd> <i>msg_rtime</i> is set to the current time.</dl>
<h2>RETURN VALUE</h2>
<p> On failure both functions return -1 with <i>errno</i> indicating the error, otherwise <code>msgsnd</code>() returns 0 and <code>msgrcv</code>() returns the number of bytes actually copied into the <i>mtext</i> array.</p>
<h2>ERRORS</h2>
<p> When <code>msgsnd</code>() fails, <i>errno</i> will be set to one among the following values:</p>
<dl>
<dt><code>EACCES</code></p>
<dd> The calling process does not have write permission on the message queue, and does not have the <code>CAP_IPC_OWNER</code> capability in the user namespace that governs its IPC namespace.</p>
<dt><code>EAGAIN</code></p>
<dd> The message can&#8217;t be sent due to the <i>msg_qbytes</i> limit for the queue and <code>IPC_NOWAIT</code> was specified in <i>msgflg</i>.</p>
<dt><code>EFAULT</code></p>
<dd> The address pointed to by <i>msgp</i> isn&#8217;t accessible.</p>
<dt><code>EIDRM</code></p>
<dd> The message queue was removed.</p>
<dt><code>EINTR</code></p>
<dd> Sleeping on a full message queue condition, the process caught a signal.</p>
<dt><code>EINVAL</code></p>
<dd> Invalid <i>msqid</i> value, or nonpositive <i>mtype</i> value, or invalid <i>msgsz</i> value (less than 0 or greater than the system value <code>MSGMAX</code>).</p>
<dt><code>ENOMEM</code></p>
<dd> The system does not have enough memory to make a copy of the message pointed to by <i>msgp</i>.</dl>
<p> When <code>msgrcv</code>() fails, <i>errno</i> will be set to one among the following values:</p>
<dl>
<dt><code>E2BIG</code></p>
<dd> The message text length is greater than <i>msgsz</i> and <code>MSG_NOERROR</code> isn&#8217;t specified in <i>msgflg</i>.</p>
<dt><code>EACCES</code></p>
<dd> The calling process does not have read permission on the message queue, and does not have the <code>CAP_IPC_OWNER</code> capability in the user namespace that governs its IPC namespace.</p>
<dt><code>EFAULT</code></p>
<dd> The address pointed to by <i>msgp</i> isn&#8217;t accessible.</p>
<dt><code>EIDRM</code></p>
<dd> While the process was sleeping to receive a message, the message queue was removed.</p>
<dt><code>EINTR</code></p>
<dd> While the process was sleeping to receive a message, the process caught a signal; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> <i>msqid</i> was invalid, or <i>msgsz</i> was less than 0.</p>
<dt><code>EINVAL</code> (since Linux 3.14)</p>
<dd> <i>msgflg</i> specified <code>MSG_COPY</code>, but not <code>IPC_NOWAIT</code>.</p>
<dt><code>EINVAL</code> (since Linux 3.14)</p>
<dd> <i>msgflg</i> specified both <code>MSG_COPY</code> and <code>MSG_EXCEPT</code>.</p>
<dt><code>ENOMSG</code></p>
<dd> <code>IPC_NOWAIT</code> was specified in <i>msgflg</i> and no message of the requested type existed on the message queue.</p>
<dt><code>ENOMSG</code></p>
<dd> <code>IPC_NOWAIT</code> and <code>MSG_COPY</code> were specified in <i>msgflg</i> and the queue contains less than <i>msgtyp</i> messages.</p>
<dt><code>ENOSYS</code> (since Linux 3.8)</p>
<dd> Both <code>MSG_COPY</code> and <code>IPC_NOWAIT</code> were specified in <i>msgflg</i>, and this kernel was configured without <code>CONFIG_CHECKPOINT_RESTORE</code>.</dl>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4. </p>
<p> The <code>MSG_EXCEPT</code> and <code>MSG_COPY</code> flags are Linux-specific; their definitions can be obtained by defining the <code>_GNU_SOURCE</code> feature test macro.</p>
<h2>NOTES</h2>
<p> The inclusion of <i>&lt;sys/types.h&gt;</i> and <i>&lt;sys/ipc.h&gt;</i> isn&#8217;t required on Linux or by any version of POSIX. However, some old implementations required the inclusion of these header files, and the SVID also documented their inclusion. Applications intended to be portable to such old systems may need to include these header files. </p>
<p> The <i>msgp</i> argument is declared as <i>struct msgbuf&nbsp;*</i> in glibc 2.0 and 2.1. It is declared as <i>void&nbsp;*</i> in glibc 2.2 and later, as required by SUSv2 and SUSv3. </p>
<p> The following limits on message queue resources affect the <code>msgsnd</code>() call:</p>
<dl>
<dt><code>MSGMAX</code></p>
<dd> Maximum size of a message text, in bytes (default value: 8192 bytes). On Linux, this limit can be read and modified via <i>/proc/sys/kernel/msgmax</i>.</p>
<dt><code>MSGMNB</code></p>
<dd> Maximum number of bytes that can be held in a message queue (default value: 16384 bytes). On Linux, this limit can be read and modified via <i>/proc/sys/kernel/msgmnb</i>. A privileged process (Linux: a process with the <code>CAP_SYS_RESOURCE</code> capability) can increase the size of a message queue beyond <code>MSGMNB</code> using the <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2) <code>IPC_SET</code> operation.</dl>
<p> The implementation has no intrinsic system-wide limits on the number of message headers (<code>MSGTQL</code>) and the number of bytes in the message pool (<code>MSGPOOL</code>).</p>
<h2>BUGS</h2>
<p> In Linux 3.13 and earlier, if <code>msgrcv</code>() was called with the <code>MSG_COPY</code> flag, but without <code>IPC_NOWAIT</code>, and the message queue contained less than <i>msgtyp</i> messages, then the call would block until the next message is written to the queue. At that point, the call would return a copy of the message, <i>regardless</i> of whether that message was at the ordinal position <i>msgtyp</i>. This bug is fixed in Linux 3.14. </p>
<p> Specifying both <code>MSG_COPY</code> and <code>MSC_EXCEPT</code> in <i>msgflg</i> is a logical error (since these flags impose different interpretations on <i>msgtyp</i>). In Linux 3.13 and earlier, this error was not diagnosed by <code>msgrcv</code>(). This bug is fixed in Linux 3.14.</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>msgsnd</code>() and <code>msgrcv</code>(). </p>
<p> The example program is first run with the <code>-s</code> option to send a message and then run again with the <code>-r</code> option to receive a message. </p>
<p> The following shell session shows a sample run of the program: </p>
<p> $<code> ./a.out -s</code> sent: a message at Wed Mar 4 16:25:45 2015 </p>
<p> $<code> ./a.out -r</code> message received: a message at Wed Mar 4 16:25:45 2015</p>
<h3>Program source</h3>
<p> #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; #include &lt;time.h&gt; #include &lt;unistd.h&gt; #include &lt;errno.h&gt; #include &lt;sys/types.h&gt; #include &lt;sys/ipc.h&gt; #include &lt;sys/msg.h&gt; </p>
<p> struct msgbuf {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long mtype;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char mtext[80]; }; </p>
<p> static void usage(char *prog_name, char *msg) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(msg&nbsp;!=&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fputs(msg, stderr); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;[options]
&quot;, prog_name);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Options are:
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;-s&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;send message using msgsnd()
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;-r&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;read message using msgrcv()
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;-t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;message type&nbsp;(default is 1)
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;-k&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;message queue key&nbsp;(default is 1234)
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); } </p>
<p> static void send_msg(int qid, int msgtype) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct msgbuf msg;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t t; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg.mtype&nbsp;=&nbsp;msgtype; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time(&amp;t);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;snprintf(msg.mtext, sizeof(msg.mtext),&nbsp;&quot;a message at&nbsp;%s&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ctime(&amp;t)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(msgsnd(qid,&nbsp;&amp;msg, sizeof(msg.mtext),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;IPC_NOWAIT)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;msgsnd error&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;sent:&nbsp;%s
&quot;, msg.mtext); } </p>
<p> static void get_msg(int qid, int msgtype) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct msgbuf msg; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(msgrcv(qid,&nbsp;&amp;msg, sizeof(msg.mtext), msgtype,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;MSG_NOERROR | IPC_NOWAIT)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(errno&nbsp;!=&nbsp;ENOMSG)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;msgrcv&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;No message available for msgrcv()
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;message received:&nbsp;%s
&quot;, msg.mtext); } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int qid, opt;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int mode&nbsp;=&nbsp;0;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;1&nbsp;=&nbsp;send, 2&nbsp;=&nbsp;receive&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int msgtype&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int msgkey&nbsp;=&nbsp;1234; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;while&nbsp;((opt&nbsp;=&nbsp;getopt(argc, argv,&nbsp;&quot;srt:k:&quot;))&nbsp;!=&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;switch&nbsp;(opt)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;s&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mode&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;r&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mode&nbsp;=&nbsp;2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;t&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msgtype&nbsp;=&nbsp;atoi(optarg);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(msgtype&nbsp;&lt;=&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;usage(argv[0],&nbsp;&quot;-t option must be greater than 0
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;case&nbsp;&#8216;k&#8217;:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msgkey&nbsp;=&nbsp;atoi(optarg);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;break;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;default:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;usage(argv[0],&nbsp;&quot;Unrecognized option
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mode&nbsp;==&nbsp;0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;usage(argv[0],&nbsp;&quot;must use either -s or -r option
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;qid&nbsp;=&nbsp;msgget(msgkey, IPC_CREAT | 0666); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(qid&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;msgget&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mode&nbsp;==&nbsp;2)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;get_msg(qid, msgtype);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;send_msg(qid, msgtype); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-msgctl/">msgctl</a></code>(2), <code><a href="/docs/linux/man/2-msgget/">msgget</a></code>(2), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
