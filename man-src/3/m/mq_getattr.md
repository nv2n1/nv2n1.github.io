---
title: "mq_getattr(3)"
name: "mq_getattr"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mq_getattr/"
description: "mq_getattr, mq_setattr – get/set message queue attributes"
---

<p>mq_getattr, mq_setattr &#8211; get/set message queue attributes </p>
<h2>Synopsis</h2>
<pre><code>#include &lt;mqueue.h&gt;</code>
<code>int mq_getattr(mqd_t </code><i>mqdes</i><code>, struct mq_attr *</code><i>attr</i><code>);</code>
<code>int mq_setattr(mqd_t </code><i>mqdes</i><code>, const struct mq_attr *</code><i>newattr</i><code>,</code>
<code> struct mq_attr *</code><i>oldattr</i><code>);</code></pre>
<p>Link with <i>-lrt</i>.</p>
<h2>Description</h2>
<p><code>mq_getattr</code>() and <code>mq_setattr</code>() respectively retrieve and modify attributes of the message queue referred to by the message queue descriptor <i>mqdes</i>. </p>
<p> <code>mq_getattr</code>() returns an <i>mq_attr</i> structure in the buffer pointed by <i>attr</i>. This structure is defined as: </p>
<p> struct mq_attr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long mq_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags: 0 or O_NONBLOCK&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long mq_maxmsg;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Max.&nbsp;#&nbsp;of messages on queue&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long mq_msgsize;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Max. message size&nbsp;(bytes)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long mq_curmsgs;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;of messages currently in queue&nbsp;*/ }; </p>
<p> The <i>mq_flags</i> field contains flags associated with the open message queue description. This field is initialized when the queue is created by <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3). The only flag that can appear in this field is <code>O_NONBLOCK</code>. </p>
<p> The <i>mq_maxmsg</i> and <i>mq_msgsize</i> fields are set when the message queue is created by <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3). The <i>mq_maxmsg</i> field is an upper limit on the number of messages that may be placed on the queue using <code><a href="/docs/linux/man/3-mq_send/">mq_send</a></code>(3). The <i>mq_msgsize</i> field is an upper limit on the size of messages that may be placed on the queue. Both of these fields must have a value greater than zero. Two <i>/proc</i> files that place ceilings on the values for these fields are described in <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7). </p>
<p> The <i>mq_curmsgs</i> field returns the number of messages currently held in the queue. </p>
<p> <code>mq_setattr</code>() sets message queue attributes using information supplied in the <i>mq_attr</i> structure pointed to by <i>newattr</i>. The only attribute that can be modified is the setting of the <code>O_NONBLOCK</code> flag in <i>mq_flags</i>. The other fields in <i>newattr</i> are ignored. If the <i>oldattr</i> field is not NULL, then the buffer that it points to is used to return an <i>mq_attr</i> structure that contains the same information that is returned by <code>mq_getattr</code>().</p>
<h2>Return Value</h2>
<p>On success <code>mq_getattr</code>() and <code>mq_setattr</code>() return 0; on error, -1 is returned, with <i>errno</i> set to indicate the error.</p>
<h2>Errors</h2>
<dl COMPACT>
<dt><code>EBADF</code></p>
<dd>The message queue descriptor specified in <i>mqdes</i> is invalid.</p>
<dt><code>EINVAL</code></p>
<dd><i>newattr-&gt;mq_flags</i> contained set bits other than <code>O_NONBLOCK</code>.</dl>
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
<td> <code>mq_getattr</code>(), <code>mq_setattr</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
</table>
<h2>Conforming To</h2>
<p>POSIX.1-2001, POSIX.1-2008.</p>
<h2>Notes</h2>
<p>On Linux, <code>mq_getattr</code>() and <code>mq_setattr</code>() are library functions layered on top of the <code><a href="/docs/linux/man/2-mq_getsetattr/">mq_getsetattr</a></code>(2) system call.</p>
<h2>Examples</h2>
<p>The program below can be used to show the default <i>mq_maxmsg</i> and <i>mq_msgsize</i> values that are assigned to a message queue that is created with a call to <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3) in which the <i>attr</i> argument is NULL. Here is an example run of the program: </p>
<p> $ <code>./a.out /testq</code> Maximum # of messages on queue: 10 Maximum message size: 8192 </p>
<p> Since Linux 3.5, the following <i>/proc</i> files (described in <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7)) can be used to control the defaults: </p>
<p> $ <code>uname -sr</code> Linux 3.8.0 $ <code>cat /proc/sys/fs/mqueue/msg_default</code> 10 $ <code>cat /proc/sys/fs/mqueue/msgsize_default</code> 8192</p>
<h3>Program source</h3>
<p>#include &lt;mqueue.h&gt; #include &lt;sys/stat.h&gt; #include &lt;fcntl.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; </p>
<p> #define errExit(msg) do { perror(msg); exit(EXIT_FAILURE); \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;while&nbsp;(0) </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mqd_t mqd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct mq_attr attr; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;2)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s mq-name
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mqd&nbsp;=&nbsp;mq_open(argv[1], O_CREAT | O_EXCL, S_IRUSR | S_IWUSR, NULL);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mqd&nbsp;==&nbsp;(mqd_t)&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;mq_open&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mq_getattr(mqd,&nbsp;&amp;attr)&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;mq_getattr&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Maximum&nbsp;#&nbsp;of messages on queue:&nbsp;<wbr>&nbsp;<wbr>&nbsp;%ld
&quot;, attr.mq_maxmsg);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Maximum message size:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%ld
&quot;, attr.mq_msgsize); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(mq_unlink(argv[1])&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;errExit(&quot;mq_unlink&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-mq_close/">mq_close</a></code>(3), <code><a href="/docs/linux/man/3-mq_notify/">mq_notify</a></code>(3), <code><a href="/docs/linux/man/3-mq_open/">mq_open</a></code>(3), <code><a href="/docs/linux/man/3-mq_receive/">mq_receive</a></code>(3), <code><a href="/docs/linux/man/3-mq_send/">mq_send</a></code>(3), <code><a href="/docs/linux/man/3-mq_unlink/">mq_unlink</a></code>(3), <code><a href="/docs/linux/man/7-mq_overview/">mq_overview</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a></p>
