---
title: "sctp_connectx(3)"
name: "sctp_connectx"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sctp_connectx/"
description: "sctp_connectx – initiate a connection on an SCTP socket using multiple destination addresses."
---

<p>sctp_connectx &#8211; initiate a connection on an SCTP socket using multiple destination addresses.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netinet/sctp.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;

int sctp_connectx(int sd, struct sockaddr *addrs, int addrcnt,
                  sctp_assoc_t *id);</code></pre>
<h2>Description</h2>
<p><code>sctp_connectx</code> initiates a connection to a set of addresses passed in the array <i>addrs</i> to/from the socket <i>sd.</i> <i>addrcnt</i> is the number of addresses in the array. </p>
<p> If <i>sd</i> is an IPv4 socket, the addresses passed must be IPv4 addresses. If <i>sd</i> is an IPv6 socket, the addresses passed can be either IPv4 or IPv6 addresses. </p>
<p> <i>addrs</i> is a pointer to an array of one or more socket addresses. Each address is contained in its appropriate structure(i.e. struct sockaddr_in or struct sockaddr_in6). The family of the address type must be used to distinguish the address length. The caller specifies the number of addresses in the array with <i>addrcnt. </i> </p>
<p> <i>id</i> is a pointer to the association id and, if provided, will be set to the identifier of the newly created association.</p>
<h2>Return Value</h2>
<p>On success, 0 is returned. On failure, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>EBADF</code></p>
<dd><i>sd</i> is not a valid descriptor.</p>
<dt><code>ENOTSOCK</code></p>
<dd><i>sd</i> is a descriptor for a file, not a socket.</p>
<dt><code>EFAULT</code></p>
<dd>Error while copying in or out from the user address space.</p>
<dt><code>EINVAL</code></p>
<dd>Invalid port or address.</p>
<dt><code>EACCES</code></p>
<dd>The address is protected, and the user is not the super-user.</p>
<dt><code>EISCONN</code></p>
<dd>The socket is already connected.</p>
<dt><code>ECONNREFUSED</code></p>
<dd>No one listening on the remote address.</p>
<dt><code>ETIMEDOUT</code></p>
<dd>Timeout while attempting connection. The server may be too busy to accept new connections. Note that for IP sockets the timeout may be very long when syncookies are enabled on the server.</p>
<dt><code>ENETUNREACH</code></p>
<dd>Network is unreachable.</p>
<dt><code>EADDRINUSE</code></p>
<dd>Local address is already in use.</p>
<dt><code>EINPROGRESS</code></p>
<dd>The socket is non-blocking and the connection cannot be completed immediately. It is possible to <code><a href="/docs/linux/man/2-select/">select</a></code>(2) or <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2) for completion by selecting the socket for writing. After <code>select</code> indicates writability, use <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) to read the <code>SO_ERROR</code> option at level <code>SOL_SOCKET</code> to determine whether <code>connect</code> completed successfully (<code>SO_ERROR</code> is zero) or unsuccessfully (<code>SO_ERROR</code> is one of the usual error codes listed here, explaining the reason for the failure).</p>
<dt><code>EALREADY</code></p>
<dd>The socket is non-blocking and a previous connection attempt has not yet been completed.</p>
<dt><code>EAGAIN</code></p>
<dd>No more free local ports or insufficient entries in the routing cache. For <code>PF_INET</code> see the <code>net.ipv4.ip_local_port_range</code> sysctl in <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7) on how to increase the number of local ports.</p>
<dt><code>EAFNOSUPPORT</code></p>
<dd>The passed address didn&#8217;t have the correct address family in its <i>sa_family</i> field.</p>
<dt><code>EACCES, EPERM</code></p>
<dd>The user tried to connect to a broadcast address without having the socket broadcast flag enabled or the connection request failed because of a local firewall rule.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sctp/">sctp</a></code>(7) <code><a href="/docs/linux/man/3-sctp_bindx/">sctp_bindx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_sendmsg/">sctp_sendmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_send/">sctp_send</a></code>(3), <code><a href="/docs/linux/man/3-sctp_recvmsg/">sctp_recvmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_peeloff/">sctp_peeloff</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getpaddrs/">sctp_getpaddrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getladdrs/">sctp_getladdrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_opt_info/">sctp_opt_info</a></code>(3), </p>
