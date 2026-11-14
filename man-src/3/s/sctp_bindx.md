---
title: "sctp_bindx(3)"
name: "sctp_bindx"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sctp_bindx/"
description: "sctp_bindx – Add or remove bind addresses on a socket."
---

<p>sctp_bindx &#8211; Add or remove bind addresses on a socket.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netinet/sctp.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;

int sctp_bindx(int sd, struct sockaddr *addrs, int addrcnt,
               int flags);</code></pre>
<h2>Description</h2>
<p><code>sctp_bindx</code> adds or removes a set of bind addresses passed in the array <i>addrs</i> to/from the socket <i>sd.</i> <i>addrcnt</i> is the number of addresses in the array and the <i>flags</i> paramater indicates if the addresses need to be added or removed. </p>
<p> If <i>sd</i> is an IPv4 socket, the addresses passed must be IPv4 addresses. If <i>sd</i> is an IPv6 socket, the addresses passed can be either IPv4 or IPv6 addresses. </p>
<p> <i>addrs</i> is a pointer to an array of one or more socket addresses. Each address is contained in its appropriate structure(i.e. struct sockaddr_in or struct sockaddr_in6). The family of the address type must be used to distinguish the address length. The caller specifies the number of addresses in the array with <i>addrcnt. </i> </p>
<p> The <i>flags</i> parameter can be either <code>SCTP_BINDX_ADD_ADDR</code> or <code>SCTP_BINDX_REM_ADDR.</code> An application can use <code>SCTP_BINDX_ADD_ADDR</code> to associate additional addresses with an endpoint after calling <code><a href="/docs/linux/man/2-bind/">bind</a>(2).</code> <code>SCTP_BINDX_REM_ADDR</code> directs SCTP to remove the given addresses from the association. A caller may not remove all addresses from an association. It will fail with <code>EINVAL.</code></p>
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
<dd>Invalid port or address or trying to remove all addresses from an association.</p>
<dt><code>EACCES</code></p>
<dd>The address is protected, and the user is not the super-user.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sctp/">sctp</a></code>(7) <code><a href="/docs/linux/man/3-sctp_sendmsg/">sctp_sendmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_send/">sctp_send</a></code>(3), <code><a href="/docs/linux/man/3-sctp_recvmsg/">sctp_recvmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_peeloff/">sctp_peeloff</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getpaddrs/">sctp_getpaddrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getladdrs/">sctp_getladdrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_opt_info/">sctp_opt_info</a></code>(3), <code><a href="/docs/linux/man/3-sctp_connectx/">sctp_connectx</a></code>(3) </p>
