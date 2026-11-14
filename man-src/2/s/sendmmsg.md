---
title: "sendmmsg(2)"
name: "sendmmsg"
section: "2"
letter: "s"
url: "/docs/linux/man/2-sendmmsg/"
description: "sendmmsg – send multiple messages on a socket"
---

<h2 class="name">NAME</h2>
<p> sendmmsg &#8211; send multiple messages on a socket </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;sys/socket.h&gt;
int sendmmsg(int sockfd, struct mmsghdr *msgvec, unsigned int vlen,
             int flags);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>sendmmsg</code>() system call is an extension of <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) that allows the caller to transmit multiple messages on a socket using a single system call. (This has performance benefits for some applications.) </p>
<p> The <i>sockfd</i> argument is the file descriptor of the socket on which data is to be transmitted. </p>
<p> The <i>msgvec</i> argument is a pointer to an array of <i>mmsghdr</i> structures. The size of this array is specified in <i>vlen</i>. </p>
<p> The <i>mmsghdr</i> structure is defined in <i>&lt;sys/socket.h&gt;</i> as: </p>
<p> struct mmsghdr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct msghdr msg_hdr;&nbsp;<wbr>&nbsp;/*&nbsp;Message header&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;msg_len;&nbsp;<wbr>&nbsp;/*&nbsp;Number of bytes transmitted&nbsp;*/ }; </p>
<p> The <i>msg_hdr</i> field is a <i>msghdr</i> structure, as described in <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2). The <i>msg_len</i> field is used to return the number of bytes sent from the message in <i>msg_hdr</i> (i.e., the same as the return value from a single <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2) call). </p>
<p> The <i>flags</i> argument contains flags ORed together. The flags are the same as for <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2). </p>
<p> A blocking <code>sendmmsg</code>() call blocks until <i>vlen</i> messages have been sent. A nonblocking call sends as many messages as possible (up to the limit specified by <i>vlen</i>) and returns immediately. </p>
<p> On return from <code>sendmmsg</code>(), the <i>msg_len</i> fields of successive elements of <i>msgvec</i> are updated to contain the number of bytes transmitted from the corresponding <i>msg_hdr</i>. The return value of the call indicates the number of elements of <i>msgvec</i> that have been updated.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>sendmmsg</code>() returns the number of messages sent from <i>msgvec</i>; if this is less than <i>vlen</i>, the caller can retry with a further <code>sendmmsg</code>() call to send the remaining messages. </p>
<p> On error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> Errors are as for <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2). An error is returned only if no datagrams could be sent. See also BUGS.</p>
<h2>VERSIONS</h2>
<p> The <code>sendmmsg</code>() system call was added in Linux 3.0. Support in glibc was added in version 2.14.</p>
<h2>CONFORMING TO</h2>
<p> <code>sendmmsg</code>() is Linux-specific.</p>
<h2>NOTES</h2>
<p> The value specified in <i>vlen</i> is capped to <code>UIO_MAXIOV</code> (1024).</p>
<h2>BUGS</h2>
<p> If an error occurs after at least one message has been sent, the call succeeds, and returns the number of messages sent. The error code is lost. The caller can retry the transmission, starting at the first failed message, but there is no guarantee that, if an error is returned, it will be the same as the one that was lost on the previous call.</p>
<h2>EXAMPLES</h2>
<p> The example below uses <code>sendmmsg</code>() to send <i>onetwo</i> and <i>three</i> in two distinct UDP datagrams using one system call. The contents of the first datagram originates from a pair of buffers. </p>
<p> #define _GNU_SOURCE #include &lt;netinet/ip.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; #include &lt;sys/types.h&gt; #include &lt;sys/socket.h&gt; </p>
<p> int main(void) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int sockfd;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sockaddr_in addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct mmsghdr msg[2];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct iovec msg1[2], msg2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int retval; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sockfd&nbsp;=&nbsp;socket(AF_INET, SOCK_DGRAM, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sockfd&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;socket()&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr.sin_family&nbsp;=&nbsp;AF_INET;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr.sin_addr.s_addr&nbsp;=&nbsp;htonl(INADDR_LOOPBACK);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr.sin_port&nbsp;=&nbsp;htons(1234);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(connect(sockfd,&nbsp;(struct sockaddr&nbsp;*)&nbsp;&amp;addr, sizeof(addr))&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;connect()&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(msg1, 0, sizeof(msg1));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg1[0].iov_base&nbsp;=&nbsp;&quot;one&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg1[0].iov_len&nbsp;=&nbsp;3;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg1[1].iov_base&nbsp;=&nbsp;&quot;two&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg1[1].iov_len&nbsp;=&nbsp;3; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(&amp;msg2, 0, sizeof(msg2));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg2.iov_base&nbsp;=&nbsp;&quot;three&quot;;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg2.iov_len&nbsp;=&nbsp;5; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(msg, 0, sizeof(msg));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg[0].msg_hdr.msg_iov&nbsp;=&nbsp;msg1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg[0].msg_hdr.msg_iovlen&nbsp;=&nbsp;2; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg[1].msg_hdr.msg_iov&nbsp;=&nbsp;&amp;msg2;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msg[1].msg_hdr.msg_iovlen&nbsp;=&nbsp;1; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;retval&nbsp;=&nbsp;sendmmsg(sockfd, msg, 2, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(retval&nbsp;==&nbsp;-1)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;sendmmsg()&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;else<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%d messages sent
&quot;, retval); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(0); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-recvmmsg/">recvmmsg</a></code>(2), <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
