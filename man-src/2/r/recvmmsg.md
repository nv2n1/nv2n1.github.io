---
title: "recvmmsg(2)"
name: "recvmmsg"
section: "2"
letter: "r"
url: "/docs/linux/man/2-recvmmsg/"
description: "recvmmsg – receive multiple messages on a socket"
---

<h2 class="name">NAME</h2>
<p> recvmmsg &#8211; receive multiple messages on a socket </p>
<h2>SYNOPSIS</h2>
<pre><code>
#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;sys/socket.h&gt;
int recvmmsg(int sockfd, struct mmsghdr *msgvec, unsigned int vlen,
             int flags, struct timespec *timeout);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>recvmmsg</code>() system call is an extension of <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2) that allows the caller to receive multiple messages from a socket using a single system call. (This has performance benefits for some applications.) A further extension over <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2) is support for a timeout on the receive operation. </p>
<p> The <i>sockfd</i> argument is the file descriptor of the socket to receive data from. </p>
<p> The <i>msgvec</i> argument is a pointer to an array of <i>mmsghdr</i> structures. The size of this array is specified in <i>vlen</i>. </p>
<p> The <i>mmsghdr</i> structure is defined in <i>&lt;sys/socket.h&gt;</i> as: </p>
<p> struct mmsghdr {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct msghdr msg_hdr;&nbsp;<wbr>&nbsp;/*&nbsp;Message header&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned int&nbsp;<wbr>&nbsp;msg_len;&nbsp;<wbr>&nbsp;/*&nbsp;Number of received bytes for header&nbsp;*/ }; </p>
<p> The <i>msg_hdr</i> field is a <i>msghdr</i> structure, as described in <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2). The <i>msg_len</i> field is the number of bytes returned for the message in the entry. This field has the same value as the return value of a single <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2) on the header. </p>
<p> The <i>flags</i> argument contains flags ORed together. The flags are the same as documented for <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), with the following addition:</p>
<dl>
<dt><code>MSG_WAITFORONE</code> (since Linux 2.6.34)</p>
<dd> Turns on <code>MSG_DONTWAIT</code> after the first message has been received.</dl>
<p> The <i>timeout</i> argument points to a <i>struct timespec</i> (see <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2)) defining a timeout (seconds plus nanoseconds) for the receive operation (<i>but see BUGS!</i>). (This interval will be rounded up to the system clock granularity, and kernel scheduling delays mean that the blocking interval may overrun by a small amount.) If <i>timeout</i> is NULL, then the operation blocks indefinitely. </p>
<p> A blocking <code>recvmmsg</code>() call blocks until <i>vlen</i> messages have been received or until the timeout expires. A nonblocking call reads as many messages as are available (up to the limit specified by <i>vlen</i>) and returns immediately. </p>
<p> On return from <code>recvmmsg</code>(), successive elements of <i>msgvec</i> are updated to contain information about each received message: <i>msg_len</i> contains the size of the received message; the subfields of <i>msg_hdr</i> are updated as described in <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2). The return value of the call indicates the number of elements of <i>msgvec</i> that have been updated.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>recvmmsg</code>() returns the number of messages received in <i>msgvec</i>; on error, -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<p> Errors are as for <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2). In addition, the following error can occur:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>timeout</i> is invalid.</dl>
<p> See also BUGS.</p>
<h2>VERSIONS</h2>
<p> The <code>recvmmsg</code>() system call was added in Linux 2.6.33. Support in glibc was added in version 2.12.</p>
<h2>CONFORMING TO</h2>
<p> <code>recvmmsg</code>() is Linux-specific.</p>
<h2>BUGS</h2>
<p> The <i>timeout</i> argument does not work as intended. The timeout is checked only after the receipt of each datagram, so that if up to <i>vlen-1</i> datagrams are received before the timeout expires, but then no further datagrams are received, the call will block forever. </p>
<p> If an error occurs after at least one message has been received, the call succeeds, and returns the number of messages received. The error code is expected to be returned on a subsequent call to <code>recvmmsg</code>(). In the current implementation, however, the error code can be overwritten in the meantime by an unrelated network event on a socket, for example an incoming ICMP packet.</p>
<h2>EXAMPLES</h2>
<p> The following program uses <code>recvmmsg</code>() to receive multiple messages on a socket and stores them in multiple buffers. The call returns if all buffers are filled or if the timeout specified has expired. </p>
<p> The following snippet periodically generates UDP datagrams containing a random number: </p>
<p> $<code> while true; do echo $RANDOM &gt; /dev/udp/127.0.0.1/1234;</code> <code> sleep 0.25; done</code> </p>
<p> These datagrams are read by the example application, which can give the following output: </p>
<p> $<code> ./a.out</code> 5 messages received 1 11782 2 11345 3 304 4 13514 5 28421</p>
<h3>Program source</h3>
<p> #define _GNU_SOURCE #include &lt;netinet/ip.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; #include &lt;sys/socket.h&gt; </p>
<p> int main(void) { #define VLEN 10 #define BUFSIZE 200 #define TIMEOUT 1<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int sockfd, retval;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct sockaddr_in addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct mmsghdr msgs[VLEN];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct iovec iovecs[VLEN];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char bufs[VLEN][BUFSIZE+1];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct timespec timeout; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;sockfd&nbsp;=&nbsp;socket(AF_INET, SOCK_DGRAM, 0);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(sockfd&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;socket()&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr.sin_family&nbsp;=&nbsp;AF_INET;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr.sin_addr.s_addr&nbsp;=&nbsp;htonl(INADDR_LOOPBACK);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;addr.sin_port&nbsp;=&nbsp;htons(1234);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(bind(sockfd,&nbsp;(struct sockaddr&nbsp;*)&nbsp;&amp;addr, sizeof(addr))&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;bind()&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memset(msgs, 0, sizeof(msgs));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;0;&nbsp;i&nbsp;&lt;&nbsp;VLEN;&nbsp;i++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;iovecs[i].iov_base&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;bufs[i];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;iovecs[i].iov_len&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;BUFSIZE;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msgs[i].msg_hdr.msg_iov&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;=&nbsp;&amp;iovecs[i];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;msgs[i].msg_hdr.msg_iovlen&nbsp;=&nbsp;1;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;timeout.tv_sec&nbsp;=&nbsp;TIMEOUT;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;timeout.tv_nsec&nbsp;=&nbsp;0; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;retval&nbsp;=&nbsp;recvmmsg(sockfd, msgs, VLEN, 0,&nbsp;&amp;timeout);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(retval&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;recvmmsg()&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%d messages received
&quot;, retval);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;for&nbsp;(int i&nbsp;=&nbsp;0;&nbsp;i&nbsp;&lt;&nbsp;retval;&nbsp;i++)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;bufs[i][msgs[i].msg_len]&nbsp;=&nbsp;0;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;%d&nbsp;%s&quot;, i+1, bufs[i]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-clock_gettime/">clock_gettime</a></code>(2), <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), <code><a href="/docs/linux/man/2-sendmmsg/">sendmmsg</a></code>(2), <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
