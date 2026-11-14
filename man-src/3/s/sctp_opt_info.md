---
title: "sctp_opt_info(3)"
name: "sctp_opt_info"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sctp_opt_info/"
description: "sctp_optinfo – Get options on a SCTP socket."
---

<p>sctp_optinfo &#8211; Get options on a SCTP socket.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netinet/sctp.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;

int sctp_opt_info(int sd, sctp_assoc_t id, int opt,
                  void *arg, socklen_t *size);</code></pre>
<h2>Description</h2>
<p><code>sctp_opt_info</code> is a wrapper library function that can be used to get SCTP level options on a socket. <i>sd</i> is the socket descriptor for which the option is requested. For one-to-many style sockets, <i>id</i> specifies the association to query. For one-to-one style sockets, <i>id</i> is ignored. <i>opt</i> specifes the SCTP socket option to get. <i>arg</i> is an option-specific structure buffer provided by the caller. <i>size</i> is a value-result parameter, initially containing the size of the buffer pointed to by <i>arg</i> and modifed on return to indicate the actual size of the value returned.</p>
<h2>Return Value</h2>
<p>On success, <code>sctp_opt_info</code> returns 0 and on failure -1 is returned with errno set to the appropriate error code.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sctp/">sctp</a></code>(7) <code><a href="/docs/linux/man/3-sctp_bindx/">sctp_bindx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_connectx/">sctp_connectx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_sendmsg/">sctp_sendmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_send/">sctp_send</a></code>(3), <code><a href="/docs/linux/man/3-sctp_recvmsg/">sctp_recvmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_peeloff/">sctp_peeloff</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getpaddrs/">sctp_getpaddrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getladdrs/">sctp_getladdrs</a></code>(3), </p>
