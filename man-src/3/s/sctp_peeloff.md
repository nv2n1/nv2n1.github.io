---
title: "sctp_peeloff(3)"
name: "sctp_peeloff"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sctp_peeloff/"
description: "sctp_peeloff – Branch off an association into a separate socket."
---

<p>sctp_peeloff &#8211; Branch off an association into a separate socket.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;netinet/sctp.h&gt;
#include &lt;sys/socket.h&gt;
#include &lt;sys/types.h&gt;

int sctp_peeloff(int sd, sctp_assoc_t assoc_id);</code></pre>
<h2>Description</h2>
<p><code>sctp_peeloff</code> branches off an existing association <i>assoc_id</i> on a one-to-many style socket <i>sd</i> into a separate socket. The new socket is a one-to-one style socket. </p>
<p> This is particularly desirable when, for instance, the application wishes to have a number of sporadic message senders/receivers remain under the original one-to-many style socket, but branch off those assocations carrying high volume data traffic into their own separate socket descriptors.</p>
<h2>Return Value</h2>
<p>On success, the new socket descriptor representing the branched-off asociation is returned. On error, -1 is returned, and <i>errno</i> is set appropriately.</p>
<h2>Errors</h2>
<dl>
<dt><code>EBADF</code></p>
<dd><i>sd</i> is not a valid descriptor.</p>
<dt><code>EINVAL</code></p>
<dd>The assoc id passed is invalid or if the socket is a one-to-one style socket.</p>
<dt><code>ENOTSOCK</code></p>
<dd>Argument is a descriptor for a file, not a socket.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sctp/">sctp</a></code>(7) <code><a href="/docs/linux/man/3-sctp_bindx/">sctp_bindx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_connectx/">sctp_connectx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_sendmsg/">sctp_sendmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_send/">sctp_send</a></code>(3), <code><a href="/docs/linux/man/3-sctp_recvmsg/">sctp_recvmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getpaddrs/">sctp_getpaddrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getladdrs/">sctp_getladdrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_opt_info/">sctp_opt_info</a></code>(3), </p>
