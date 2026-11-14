---
title: "mq_notify(3)"
name: "mq_notify"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mq_notify/"
description: "mq_notify – register for notification when a message is available"
---

<p>mq_notify &#8211; register for notification when a message is available </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;mqueue.h&gt;</code>
<code>int mq_notify(mqd_t </code><i>mqdes</i><code>, const struct sigevent *</code><i>sevp</i><code>);</code></pre>
<p>Link with <i>-lrt</i>.</p>
<h2>Description</h2>
<p><code>mq_notify</code>() allows the calling process to register or unregister for delivery of an asynchronous notification when a new message arrives on the empty message queue referred to by the message queue descriptor <i>mqdes</i>. </p>
<p> The <i>sevp</i> argument is a pointer to a <i>sigevent</i> structure. For the definition and general details of this structure, see <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7). </p>
<p> If <i>sevp</i> is a non-null pointer, then <code>mq_notify</code>() registers the calling process to receive message notification. The <i>sigev_notify</i> field of the <i>sigevent</i> structure to which <i>sevp</i> points specifies how notification is to be performed. This field has one of the following values:</p>
<dl COMPACT>
<dt><code>SIGEV_NONE</code></p>
<dd>A &quot;null&quot; notification: the calling process is registered as the target for notification, but when a message arrives, no notification is sent.</p>
<dt><code>SIGEV_SIGNAL</code></p>
<dd>Notify the process by sending the signal specified in <i>sigev_signo</i>. See <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7) for general details. The <i>si_code</i> field of the <i>siginfo_t</i> structure will be set to <code>SI_MESGQ</code>. In addition, <i>si_pid</i> will be set to the PID of the process that sent the message, and <i>si_uid</i> will be set to the real user ID of the sending process.</p>
<dt><code>SIGEV_THREAD</code></p>
<dd>Upon message delivery, invoke <i>sigev_notify_function</i> as if it were the start function of a new thread. See <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7) for details.</dl>
<p> Only one process can be registered to receive notification from a message queue. </p>
<p> If <i>sevp</i> is NULL, and the calling process is currently registered to receive notifications for this message queue, then the registration is removed; another process can then register to receive a message notification for this queue. </p>
<p> Message notification occurs only when a new message arrives and the queue was previously empty. If the queue was not empty at the time <code>mq_notify</code>() was called, then a notification will occur only after the queue is emptied and a new message arrives. </p>
<p> If another process or thread is waiting to read a message from an empty queue using <code><a href="/docs/linux/man/3-mq_receive/">mq_receive</a></code>(3), then any message notification registration is ignored: the message is delivered to the process or thread calling <code><a href="/docs/linux/man/3-mq_receive/">mq_receive</a></code>(3), and the message notification registration remains in effect. </p>
<p> Notification occurs once: after a notification is delivered, the notification registration is removed, and another process can register for message notification. If the notified process wishes to receive the next notification, it can use <code>mq_notify</code>() to request a further notification. This should be done before emptying all unread messages from the queue. (Placing the queue in nonblocking mode is useful for emptying the queue of messages without blocking once it is empty.)</p>
<h2>Return Value</h2>
<p>On success <code>mq_notify</code>() returns 0; on error, -1 is returned, with <i>errno</i> set to indicate the error.</p>
<h2>Errors</h2>
<dl COMPACT>
<dt><code>EBADF</code></p>
<dd>The message queue descriptor specified in <i>mqdes</i> is invalid.</p>
<dt><code>EBUSY</code></p>
<dd>Another process has already registered to receive notification for this message queue.</p>
<dt><code>EINVAL</code></p>
<dd><i>sevp-&gt;sigev_notify</i> is not one of the permitted values; or <i>sevp-&gt;sigev_notify</i> is <code>SIGEV_SIGNAL</code> and <i>sevp-&gt;sigev_signo</i> is not a valid signal number.</p>
<dt><code>ENOMEM</code></p>
<dd>Insufficient memory.</dl>
<p> POSIX.1-2008 says that an implementation <i>may</i> generate an <code>EINVAL</code> error if <i>sevp</i> is NULL, and the caller is not currently registered to receive notifications for the queue <i>mqdes</i>.</p>
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
<td> <code>mq_notify</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001.</p>
<h2>Notes</h2>
<h3>C library/kernel differences</h3>
<p>In the glibc implementation, the <code>mq_notify</code>() library function is implemented on top of the system call of the same name. When <i>sevp</i> is NULL, or specifies a notification mechanism other than <code>SIGEV_THREAD</code>, the library function directly invokes the system call. For <code>SIGEV_THREAD</code>, much of the implementation resides within the library, rather than the kernel. (This is necessarily so, since the thread involved in handling the notification is one that must be managed by the C library POSIX threads implementation.) The implementation involves the use of a raw <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7) socket and creates a new thread for each notification that is delivered to the process.</p>
<h2>Examples</h2>
<p>The following program registers a notification request for the message queue named in its command-line argument. Notification is performed by creating a thread. The thread executes a function which reads one message from the queue and then terminates the process.</p>
<h3>Program source</h3>
<p>#include &lt;pthread.h&gt; #include &lt;mqueue.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; </p>
<p> #define handle_error(msg) \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;do&nbsp;{&nbsp;perror(msg);&nbsp;exit(EXIT_FAILURE);&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> static void /* Thread start function */ tfunc(union sigval sv) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct mq_attr attr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ssize_t nr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;*buf;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mqd_t mqdes&nbsp;=&nbsp;*((mqd_t&nbsp;*)&nbsp;sv.sival_ptr); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Determine max. msg size;&nbsp;allocate buffer to receive msg&nbsp;*/ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mq_getattr(mqdes,&nbsp;&amp;attr)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;mq_getattr&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;buf&nbsp;=&nbsp;malloc(attr.mq_msgsize);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(buf&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;malloc&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;nr&nbsp;=&nbsp;mq_receive(mqdes, buf, attr.mq_msgsize, NULL);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(nr&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;mq_receive&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Read&nbsp;%zd bytes from MQ
&quot;, nr);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;free(buf);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS);&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Terminate the process&nbsp;*/ } </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mqd_t mqdes;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sigevent sev; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s&nbsp;&lt;mq-name&gt;
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mqdes&nbsp;=&nbsp;mq_open(argv[1], O_RDONLY);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mqdes&nbsp;==&nbsp;(mqd_t)&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;mq_open&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sev.sigev_notify&nbsp;=&nbsp;SIGEV_THREAD;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sev.sigev_notify_function&nbsp;=&nbsp;tfunc;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sev.sigev_notify_attributes&nbsp;=&nbsp;NULL;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sev.sigev_value.sival_ptr&nbsp;=&nbsp;&amp;mqdes;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Arg. to thread func.&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mq_notify(mqdes,&nbsp;&amp;sev)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;handle_error(&quot;mq_notify&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;pause();&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Process will be terminated by thread function&nbsp;*/ }</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mq_close/">mq_close</a></code>(3), <code><a href="/docs/linux/man/3-mq_getattr/">mq_getattr</a></code>(3), <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3), <code><a href="/docs/linux/man/3-mq_receive/">mq_receive</a></code>(3), <code><a href="/docs/linux/man/3-mq_send/">mq_send</a></code>(3), <code><a href="/docs/linux/man/3-mq_unlink/">mq_unlink</a></code>(3), <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7), <code><a href="/docs/linux/man/7-sigevent/">sigevent</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
