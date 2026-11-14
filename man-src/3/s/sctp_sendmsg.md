---
title: "sctp_sendmsg(3)"
name: "sctp_sendmsg"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sctp_sendmsg/"
description: "sctp_sendmsg – Send a message from a SCTP socket."
---

<p>sctp_sendmsg &#8211; Send a message from a SCTP socket.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netinet/sctp.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;

int sctp_sendmsg(int sd, const void *msg, size_t len,
                 struct sockaddr *to, socklen_t tolen,
                 uint32_t ppid, uint32_t flags,
                 uint16_t stream_no, uint32_t timetolive,
                 uint32_t context);</code></pre>
<h2>Description</h2>
<p><code>sctp_sendmsg</code> is a wrapper library function that can be used to send a message from a socket while using the advanced features of SCTP. <i>sd</i> is the socket descriptor from which the message pointed to by <i>msg</i> of length <i>len</i> is sent. <i>to</i> is the destination address of the message and <i>tolen</i> is the length of the destination address. <i>stream_no</i> identifies the stream number that the application wishes to send this message to. <i>flags</i> parameter is composed of a bitwise OR of the following values.</p>
<dl>
<dt><code>SCTP_UNORDERED</code></p>
<dd>This flags requests the un-ordered delivery of the message.</p>
<dt><code>SCTP_ADDR_OVER</code></p>
<dd>This flag, in the one-to-many style, requests the SCTP stack to override the primary destination address with address specified in <i>to.</i></p>
<dt><code>SCTP_ABORT</code></p>
<dd>Setting this flag causes the specified association to abort by sending an ABORT message to the peer(one-to-many style only). The ABORT chunk will contain an error cause &#8216;User Initiated Abort&#8217; with cause code 12. The cause specific information of this error cause is provided in <i>msg.</i></p>
<dt><code>SCTP_EOF</code></p>
<dd>Setting this flag invokes the SCTP graceful shutdown procedure on the specific association(one-to-many style only).</dl>
<p> <i>timetolive</i> specifies the time duration in milliseconds. The sending side will expire the message if the message has not been sent to the peer within this time period. A value of 0 indicates that no timeout should occur on this message. <i>ppid</i> is an opaque unsigned value that is passed to the remote end along with the message. <i>context</i> is a 32 bit opaque value that is passed back to the upper layer along with the undelivered message if an error occurs on the send of the message.</p>
<h2>Return Value</h2>
<p>On success, <code>sctp_sendmsg</code> returns the number of bytes sent or -1 if an error occurred.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sctp/">sctp</a></code>(7) <code><a href="/docs/linux/man/3-sctp_bindx/">sctp_bindx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_connectx/">sctp_connectx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_send/">sctp_send</a></code>(3), <code><a href="/docs/linux/man/3-sctp_recvmsg/">sctp_recvmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_peeloff/">sctp_peeloff</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getpaddrs/">sctp_getpaddrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getladdrs/">sctp_getladdrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_opt_info/">sctp_opt_info</a></code>(3), </p>
