---
title: "sctp_recvmsg(3)"
name: "sctp_recvmsg"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sctp_recvmsg/"
description: "sctp_recvmsg – Receive a message from a SCTP socket."
---

<p>sctp_recvmsg &#8211; Receive a message from a SCTP socket.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netinet/sctp.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;

int sctp_recvmsg(int sd, void *msg, size_t len,
                 struct sockaddr *from, socklen_t *fromlen,
                 struct sctp_sndrcvinfo *sinfo, int *msg_flags);</code></pre>
<h2>Description</h2>
<p><code>sctp_recvmsg</code> is a wrapper library function that can be used to receive a message from a socket while using the advanced features of SCTP. <i>sd</i> is the socket descriptor on which the message pointed to by <i>msg</i> of length <i>len</i> is received. </p>
<p> If <i>from</i> is not NULL, the source address of the message is filled in. The argument <i>fromlen</i> is a value-result parameter. initialized to the size of the buffer associated with <i>from ,</i> and modified on return to indicate the actual size of the address stored. </p>
<p> <i>sinfo</i> is a pointer to a sctp_sndrcvinfo structure to be filled upon receipt of the message. <i>msg_flags</i> is a pointer to a integer that is filled with any message flags like <code>MSG_NOTIFICATION or</code> <code>MSG_EOR.</code></p>
<h2>Return Value</h2>
<p>On success, <code>sctp_recvmsg</code> returns the number of bytes received or -1 if an error occurred.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sctp/">sctp</a></code>(7) <code><a href="/docs/linux/man/3-sctp_bindx/">sctp_bindx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_connectx/">sctp_connectx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_sendmsg/">sctp_sendmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_send/">sctp_send</a></code>(3), <code><a href="/docs/linux/man/3-sctp_peeloff/">sctp_peeloff</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getpaddrs/">sctp_getpaddrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getladdrs/">sctp_getladdrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_opt_info/">sctp_opt_info</a></code>(3) </p>
