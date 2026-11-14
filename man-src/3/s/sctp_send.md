---
title: "sctp_send(3)"
name: "sctp_send"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sctp_send/"
description: "sctp_send – Send a message from a SCTP socket."
---

<p>sctp_send &#8211; Send a message from a SCTP socket.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netinet/sctp.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;

int sctp_send(int sd, const void *msg, size_t len,
              const struct sctp_sndrcvinfo *sinfo,
              uint32_t flags);</code></pre>
<h2>Description</h2>
<p><code>sctp_send</code> is a wrapper library function that can be used to send a message from a socket without the use of the CMSG header structures. <i>sd</i> is the socket descriptor from which the message pointed to by <i>msg</i> of length <i>len</i> is sent. <i>sinfo</i> is a pointer to a sctp_sndrcvinfo structure. <i>flags</i> parameter is composed of a bitwise OR of the flags that can be be passed as the 3rd argument of a standard sendmsg() call.</p>
<h2>Return Value</h2>
<p>On success, <code>sctp_sendmsg</code> returns the number of bytes sent or -1 if an error occurred.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sctp/">sctp</a></code>(7) <code><a href="/docs/linux/man/3-sctp_bindx/">sctp_bindx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_recvmsg/">sctp_recvmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_peeloff/">sctp_peeloff</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getpaddrs/">sctp_getpaddrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getladdrs/">sctp_getladdrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_opt_info/">sctp_opt_info</a></code>(3), <code><a href="/docs/linux/man/3-sctp_sendmsg/">sctp_sendmsg</a></code>(3) </p>
