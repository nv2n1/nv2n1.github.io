---
title: "sctp_getpaddrs(3)"
name: "sctp_getpaddrs"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sctp_getpaddrs/"
description: "sctp_getpaddrs – Returns all peer addresses in an association."
---

<p>sctp_getpaddrs &#8211; Returns all peer addresses in an association.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netinet/sctp.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;

int sctp_getpaddrs(int sd, sctp_assoc_t assoc_id,
                   struct sockaddr **addrs);

void sctp_freepaddrs(struct sockaddr *addrs);</code></pre>
<h2>Description</h2>
<p><code>sctp_getpaddrs</code> returns all peer addresses in an association. On return, <i>addrs</i> will point to a dynamically allocated packed array of <code>sockaddr</code> structures of the appropriate type for each address. The caller should use <code>sctp_freepaddrs</code> to free the memory. Note that the in/out parameter <i>addrs</i> must not be NULL. </p>
<p> If <i>sd</i> is an IPv4 socket, the addresses returned will be all IPv4 addresses. If <i>sd</i> is an IPv6 socket, the addresses returned can be a mix of IPv4 or IPv6 addresses. </p>
<p> For one-to-many style sockets, <i>id</i> specifies the association to query. For one-to-one style sockets, <i>id</i> is ignored. </p>
<p> <code>sctp_freepaddrs</code> frees all the resources allocated by <code>sctp_getpaddrs.</code></p>
<h2>Return Value</h2>
<p>On success, <code>sctp_getpaddrs</code> returns the number of peer addresses in the association. If there is no association on this socket, 0 is returned and the value of <i>*addrs</i> is undefined. On error, <code>sctp_getpaddrs</code> returns -1 and the value of <i>*addrs</i> is undefined.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sctp/">sctp</a></code>(7) <code><a href="/docs/linux/man/3-sctp_bindx/">sctp_bindx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_connectx/">sctp_connectx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_sendmsg/">sctp_sendmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_send/">sctp_send</a></code>(3), <code><a href="/docs/linux/man/3-sctp_recvmsg/">sctp_recvmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_peeloff/">sctp_peeloff</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getladdrs/">sctp_getladdrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_opt_info/">sctp_opt_info</a></code>(3), </p>
